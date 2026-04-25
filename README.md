# UK supply-chain energy exposures

Two-page dashboard built from the **ONS 2023 Input-Output Analytical Tables**.
Maps every UK industry's exposure to energy-price shocks — both the structural
embedded-energy footprint and a price-side impulse response — with imports of
energy products folded in and DESNZ ETII status flagged.

## Live pages

- **Exposures table** — direct + indirect energy cost shares per SIC industry, with
  a fuel-totals / direct-indirect breakdown toggle, ETII filter, and an
  upstream-supply-chain-gap flag (`Imp%`):
  [emily-coding.github.io/supply-chain/](https://emily-coding.github.io/supply-chain/)
- **IRF + observed PPI** — Leontief price-side impulse response (unit shock and
  oil-led stress scenario) with a chart of realised UK PPI 2021 → early 2026:
  [emily-coding.github.io/supply-chain/irf.html](https://emily-coding.github.io/supply-chain/irf.html)

## What it does

### Exposures page (`index.html`)

Per-industry table covering all 101 non-energy IOAT industries. Columns:

- **Total gas / elec / oil** — embedded energy share per £1 of gross output, computed
  as `e_fuel · L_dom`. Each industry's energy intensity at every domestic node uses
  the **imports-corrected** vector `e_fuel[i] = A_dom[fuel,i] + A_imp[fuel,i]`, so
  imported jet kerosene, marine bunker, diesel, gas and electricity are captured as
  direct cost-share inputs. The Leontief inverse itself is strictly UK-domestic.
- **Toggle for direct + indirect breakdown** — splits each fuel total into the
  direct purchase (UK + imports) and the UK-domestic supply-chain indirect.
- **Gas+Elec / GVA** — direct gas + electricity rebased to value added; matches the
  **DESNZ ETII** formula. The 80th-percentile threshold is ~8.3% in this dataset.
- **Imp%** — share of an industry's intermediate spending that is imported. Acts as
  a flag for the residual MRIO gap (foreign embedded energy in imported non-energy
  intermediates is not captured by the domestic Leontief).
- **DESNZ ETII** — three-tier flag: `ETII` (whole bucket on the Jan 2023 list),
  `Partial` (some 4-digit sub-codes on the list), `—` (none). Filterable from the
  column header.
- **Adjustment margin** — Quantity-led / Mixed / Price-led derived from a
  sector-specific pass-through ρ calibrated to Ganapati/Shapiro/Walker (2020) and
  Lafrogne-Joussier/Martin/Méjean (2023). Hover the badge for the assigned ρ.
  Filterable from the column header.

### IRF page (`irf.html`)

Two complementary views.

**Leontief price-side IRF** (top): treats the three energy industries (refined
petroleum, electricity, gas) as exogenous price-setters. The energy → non-energy
block of A uses the same imports-corrected `e_fuel` vector as the exposures page;
the non-energy block stays domestic-A. Two scenarios:

- **Unit** — +10% on each energy product simultaneously; outputs scale linearly.
- **Oil-led stress** — refined oil +100%, electricity +50%, gas +50%. A
  forward-looking disturbance sized like a Strait of Hormuz / OPEC+ severe-cut
  episode, comparable in magnitude to 2022 but oil-led.

Two pass-through regimes (full ρ=1, realistic sector-specific ρⱼ); dynamic IRF
built by Neumann series (one round = one quarter, horizon shown to Q8). Results
visualised as:
- A line chart of price-response trajectory for the top-affected industries.
- A bar snapshot of the top 20 industries at the selected quarter, coloured by
  category (ETII / ETII partial / Food / Transport / Other).

**Observed PPI** (below): the realised counterpart. Monthly ONS Output PPI for
~78 industries from 2019 to early 2026, rebased to 2021-01 = 100. Energy lines
shown bold; the output-weighted headline shown dashed. The 2022 wholesale shock
is visible; 2024 onwards shows partial reversion plus a renewed oil-led move in
early 2026.

## Data sources

| File | What's in it |
|---|---|
| `data/iot2023industry.xlsx` | ONS 2023 IxI Input-Output table (domestic use, basic prices) |
| `data/iot2023product.xlsx` | ONS 2023 product-by-industry tables, including **`Imports use pxi`** for the imports correction |
| `data/ppi.xlsx` | ONS Output PPI (goods, monthly) |
| `data/sppi.xlsx` | ONS SPPI (services, quarterly — held flat across months) |
| `data/mm23.xlsx` | ONS CPI (used in the CPI-bridge work in `summary.html`) |
| `data/coicopconverterforhouseholdconsumption19972020.xlsx` | ONS CPA → COICOP household-expenditure converter |
| `data/gas-price-ofgem.xls` | Ofgem NBP day-ahead gas (external wholesale benchmark) |

Generated artefacts (rebuilt by the scripts):
- `data/irf.json` — per-industry direct + indirect energy shares, IRF trajectories, GVA, import intensity, ETII status
- `data/observed.json` — observed PPI / SPPI / CPI series, output-weighted headline, CPI bridge

## Running locally

```bash
# Regenerate model output (a few seconds)
python3 build_irf.py            # writes data/irf.json
python3 build_observed.py       # writes data/observed.json (slower; large PPI workbook)

# Serve
python3 -m http.server 8000
# Then open http://localhost:8000/index.html
```

The HTML pages fetch the JSON files directly with cache-busting query strings, so
a rebuild is picked up on the next page load.

## Methodology highlights

- **Imports correction** is applied only to the energy → non-energy block of A.
  The non-energy → non-energy block stays domestic, so foreign energy embedded
  in imported non-energy intermediates (Chinese steel, German chemicals, Asian
  electronics) is not captured. Hardt et al. (2018) put the average UK industrial
  uplift from a full multi-region IO treatment at 20–30% — concentrated in the
  high-`Imp%` tail.
- **`Total / GVA` is deliberately not shown** on the exposures page. Multiplying
  Leontief total embedded energy (which scales with gross output across the whole
  supply chain) by GVA gives values that can exceed 100% and aren't economically
  interpretable as "energy as share of value added". `Direct / GVA` (the ETII
  metric) is what's reported instead.
- **The IRF long-run is not equal to (Total energy share × shock).** That naive
  multiplication double-counts every chain that physically flows through an
  energy industry — once at the relevant fuel's shock and again at the energy
  industry's own shock. The IRF formula `Δp_R = (I − A_RR')⁻¹ · A_ER' · Δp_E`
  partitions A into energy and non-energy blocks specifically to avoid this.
  Detailed in the methodology block on the IRF page.

## File map

```
build_irf.py          # builds data/irf.json (IRF + exposures fields)
build_observed.py     # builds data/observed.json (PPI, SPPI, CPI series + bridge)
index.html            # exposures table page (default landing)
irf.html              # IRF + observed PPI page
summary.html          # earlier CPA → COICOP CPI bridge dashboard (separate analysis)
uk-energy-exposure.md # background document on the policy literature
data/                 # input spreadsheets + generated JSON
```

## References

- ONS (2023) Input-Output Analytical Tables, Industry × Industry; Blue Book 2025
  vintage.
- DESNZ (Jan 2023) Energy Bills Discount Scheme — ETII assessment methodology and
  eligible sectors list.
- Ganapati, Shapiro & Walker (2020) "Energy Cost Pass-Through in US
  Manufacturing", *AEJ Applied Economics* 12(2).
- Lafrogne-Joussier, Martin & Méjean (CEPII 2023) "Energy, Inflation and Market
  Power".
- Marin & Vona (2021) on French manufacturing energy demand elasticities;
  Labandeira et al. (2017) meta-analysis; Hardt et al. (2018) on UK MRIO uplift.
- Bank Underground (2023) on UK pass-through.

See [`uk-energy-exposure.md`](uk-energy-exposure.md) for the full reference list
and a narrative scan of UK industries by exposure type.
