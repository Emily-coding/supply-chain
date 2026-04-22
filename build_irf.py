"""
UK Supply-Chain Leontief Price Impulse Response

Loads the ONS 2023 Input-Output Analytical Tables (industry-by-industry) from
`data/iot2023industry.xlsx`, partitions energy industries (C19 refined
petroleum, D351 electricity, D352_3 gas) as exogenous, and computes how a
shock to their output prices propagates to the producer price of every other
UK industry at SIC 2-digit granularity.

Two scenarios:
  - UNIT: +10% shock to every energy product (scales linearly).
  - 2022: calibrated to 2021 Q1 -> 2022 Q3 wholesale moves — refined petroleum
    +50%, electricity +200%, gas +250%.

Two pass-through regimes:
  - FULL: p = A' p + v solved exactly; upper-bound Leontief limit.
  - REALISTIC: sector-specific rho_j applied at each propagation round, drawn
    from Ganapati/Shapiro/Walker (AEJ Applied 2020), Lafrogne-Joussier/Martin/
    Mejean (CEPII 2023), and qualitative trade/market-power judgements.

Dynamic IRF built by Neumann series: one expansion round = one quarter.
Output: data/irf.json consumed by index.html.
"""
import json
from pathlib import Path
import numpy as np
import openpyxl

ROOT = Path(__file__).parent
XLSX = ROOT / "data" / "iot2023industry.xlsx"
OUT  = ROOT / "data" / "irf.json"

ENERGY_CODES = ["C19", "D351", "D352_3"]
HORIZON_QUARTERS = 12

# 2022-calibrated wholesale price shocks (decimal, not pp).
SHOCK_2022 = {"C19": 0.50, "D351": 2.00, "D352_3": 2.50}
SHOCK_UNIT = {"C19": 0.10, "D351": 0.10, "D352_3": 0.10}

# -----------------------------------------------------------------------------
# Load A matrix from ONS xlsx
# -----------------------------------------------------------------------------
def load_A():
    wb = openpyxl.load_workbook(XLSX, data_only=True, read_only=True)
    ws = wb["A"]
    # Row 5 (1-indexed) has column codes starting at col 3; col A code labels
    # start at row 8. We read until column/row label goes blank.
    col_codes, col_names = [], []
    for c in range(3, ws.max_column + 1):
        code = ws.cell(5, c).value
        name = ws.cell(6, c).value
        if code is None:
            break
        col_codes.append(str(code).strip())
        col_names.append(str(name).strip() if name else "")
    row_codes, row_names = [], []
    for r in range(8, ws.max_row + 1):
        code = ws.cell(r, 1).value
        name = ws.cell(r, 2).value
        if code is None:
            break
        row_codes.append(str(code).strip())
        row_names.append(str(name).strip() if name else "")
    # IxI tables are square
    n = min(len(row_codes), len(col_codes))
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            v = ws.cell(8 + i, 3 + j).value
            A[i, j] = float(v) if isinstance(v, (int, float)) else 0.0
    codes = row_codes[:n]
    names = row_names[:n]
    # Sanity: column codes should match row codes
    assert codes == col_codes[:n], "IxI rows and columns should align"
    return A, codes, names


# -----------------------------------------------------------------------------
# Sector-specific realistic pass-through coefficients
# Calibrated qualitatively to trade exposure + market power per the literature.
#   >=1.00 : concentrated, domestic-oriented, can expand margin (LMM 2023: ~115%
#            in least-competitive sectors)
#   0.90-1.00 : strong pricing power / differentiated output (food, pharma,
#               industrial gases)
#   0.60-0.80 : competitive but somewhat protected (cement, rubber & plastics)
#   0.30-0.50 : highly trade-exposed commodity manufacturing (steel, aluminium,
#               basic chemicals, paper, glass, ceramics) — Ganapati et al.
#               (2020) avg ~70%, tradeable commodity tail below that
# -----------------------------------------------------------------------------
RHO_OVERRIDES = {
    # Heavily trade-exposed EII commodity manufacturing
    "C241T243": 0.35,   # Basic iron & steel
    "C244_5":   0.35,   # Other basic metals (incl. aluminium)
    "C20A":     0.40,   # Industrial gases, inorganics, fertilisers
    "C20B":     0.50,   # Petrochemicals
    "C20C":     0.55,   # Dyestuffs, agrochemicals
    "C17":      0.55,   # Paper & paper products
    "C235_6":   0.80,   # Cement, lime, plaster (transport-protected domestically)
    "C23OTHER": 0.50,   # Glass, ceramics, refractories
    "C13":      0.55,   # Textiles
    "C14":      0.55,   # Wearing apparel
    "C15":      0.50,   # Leather
    "C16":      0.60,   # Wood & wood products
    "C22":      0.70,   # Rubber & plastics
    "C19":      0.90,   # Refined petroleum (duopoly-ish, pass-through high; NB
                        # shocked directly — rho only matters for own-inertia)
    # Concentrated / differentiated / strong pricing power
    "C101":     1.00, "C102_3": 1.00, "C104": 1.00, "C105": 1.00,
    "C106":     1.00, "C107": 1.00, "C108": 1.00, "C109": 1.00,
    "C1101T1106 & C12": 1.00, "C1107": 1.00,   # Food & beverages
    "C21":      0.95,  # Pharmaceuticals
    "D351":     1.00,  # Electricity (regulated pass-through)
    "D352_3":   1.00,
    # Utilities / non-tradeable
    "E36": 1.00, "E37": 1.00, "E38": 0.95, "E39": 0.95,
    "F41, F42  & F43": 0.90,  # Construction
    # Services — generally strong pass-through (LMM)
    # default handles these at 0.90 below
}
def rho_for(code: str) -> float:
    return RHO_OVERRIDES.get(code, 0.90)


# -----------------------------------------------------------------------------
# Build IRF
# -----------------------------------------------------------------------------
def build():
    A, codes, names = load_A()
    n = len(codes)
    idx = {c: i for i, c in enumerate(codes)}

    e_idx = [idx[c] for c in ENERGY_CODES if c in idx]
    r_idx = [i for i in range(n) if i not in e_idx]
    missing = [c for c in ENERGY_CODES if c not in idx]
    assert not missing, f"missing energy codes in IxI: {missing}"

    Arr = A[np.ix_(r_idx, r_idx)]   # R x R
    Aer = A[np.ix_(e_idx, r_idx)]   # E x R — each col j shows energy inputs to industry j

    # Long-run (full pass-through) closed-form:
    # dp_R = (I - Arr')^{-1} Aer' dp_E
    I = np.eye(len(r_idx))
    L_rr = np.linalg.inv(I - Arr.T)  # (R x R)

    def run(shock_dict, apply_rho=False):
        dp_E = np.array([shock_dict[ENERGY_CODES[k]] for k in range(len(e_idx))])
        # direct impulse to R: Aer' . dp_E (R-vector)
        direct = Aer.T @ dp_E
        # dynamic path
        quarters = np.zeros((HORIZON_QUARTERS + 1, len(r_idx)))
        quarters[0] = 0.0
        running = np.zeros(len(r_idx))
        for q in range(1, HORIZON_QUARTERS + 1):
            # p_R^{(q)} = direct + Arr' p_R^{(q-1)}
            new_running = direct + Arr.T @ running
            if apply_rho:
                rho_vec = np.array([rho_for(codes[r_idx[k]]) for k in range(len(r_idx))])
                # Apply rho at each round as a dampener on the running response
                # Equivalent to: effective pass-through = rho * full
                new_running = rho_vec * new_running
            quarters[q] = new_running
            running = new_running
        # Closed-form long-run (full path only — "realistic" stays at its q=12 value)
        lr = L_rr @ direct
        return direct, quarters, lr

    out_rows = []
    # Per-industry direct energy cost shares (per unit output, decimal)
    for i in range(n):
        if i in e_idx:
            continue
        code = codes[i]
        name = names[i]
        gas   = float(A[idx["D352_3"], i])
        elec  = float(A[idx["D351"],   i])
        oil   = float(A[idx["C19"],    i])
        direct_share = gas + elec + oil
        out_rows.append({
            "code": code,
            "name": name,
            "direct_gas":   gas,
            "direct_elec":  elec,
            "direct_oil":   oil,
            "direct_share": direct_share,
        })

    # Run scenarios
    scen_defs = [
        ("unit_full",      SHOCK_UNIT, False),
        ("unit_realistic", SHOCK_UNIT, True),
        ("s2022_full",     SHOCK_2022, False),
        ("s2022_realistic",SHOCK_2022, True),
    ]
    scenarios = {}
    for name_, shock, rho in scen_defs:
        direct, path, lr = run(shock, apply_rho=rho)
        scenarios[name_] = {"direct": direct, "path": path, "lr": lr}

    # Attach IRF per industry
    r_code_order = [codes[i] for i in r_idx]
    code_to_ridx = {c: k for k, c in enumerate(r_code_order)}
    for row in out_rows:
        k = code_to_ridx[row["code"]]
        row["rho"] = rho_for(row["code"])
        for sname in scenarios:
            sc = scenarios[sname]
            row[f"{sname}_irf"] = [float(x) for x in sc["path"][:, k]]
            row[f"{sname}_lr"]  = float(sc["lr"][k])
            row[f"{sname}_direct"] = float(sc["direct"][k])

    # Top-level metadata
    result = {
        "source": "ONS UK Input-Output Analytical Tables (Industry by Industry), reference year 2023; "
                  "Blue Book 2025 vintage; file data/iot2023industry.xlsx.",
        "energy_codes": ENERGY_CODES,
        "n_industries": n,
        "horizon_quarters": HORIZON_QUARTERS,
        "shock_unit": SHOCK_UNIT,
        "shock_2022": SHOCK_2022,
        "methodology": (
            "Leontief price-side IRF: treat energy industries (C19, D351, D352_3) "
            "as exogenous and compute dp_R = (I - A_RR')^-1 A_ER' dp_E for the "
            "full pass-through long-run limit. Dynamic path built by Neumann "
            "series with one round = one quarter. Realistic scenarios apply "
            "sector-specific rho_j pass-through coefficients (calibrated from "
            "Ganapati/Shapiro/Walker 2020 and Lafrogne-Joussier/Martin/Mejean 2023)."
        ),
        "industries": out_rows,
    }
    OUT.write_text(json.dumps(result, indent=1))
    print(f"wrote {OUT} — {len(out_rows)} industries")


if __name__ == "__main__":
    build()
