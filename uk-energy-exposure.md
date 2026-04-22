# UK Supply Chains and Energy Price Exposure

An evidence-based scan of which UK industries (identified by SIC 2007 code) are most
exposed to wholesale energy prices, and — drawing on ONS data and the academic
literature on cost pass-through and price/quantity elasticities — which of them are
more likely to respond by raising prices versus cutting output.

The UK is a useful case. Between 2021 Q1 and 2024 Q4 the index of production for the
energy-intensive manufacturing industries fell by **33.6%**, reaching its lowest level
since the series began in 1990; over the same period food & beverage manufacturing,
which has stronger pricing power, largely passed costs on and kept producing (ONS,
2025). The cross-sector asymmetry is the core of the story below.

---

## 1. How we measure "energy exposure"

Three variables together determine how a firm absorbs an energy shock:

1. **Energy cost share** — electricity + gas spend as a share of GVA (or of total
   costs). The UK's Energy & Trade Intensive Industries (ETII) definition uses the
   **80th percentile of electricity and gas cost as a share of sector GVA** as its
   cutoff, based on ONS data (DESNZ, 2023).
2. **Trade intensity / import penetration** — how easily foreign competitors
   undercut a domestic price rise. ETII uses the **60th percentile of goods trade
   intensity**. UK steelmakers, for instance, export 45% of production and face
   imports covering over 60% of direct UK steel requirements (UK Parliament
   evidence; Commons Library CBP-7317).
3. **Fuel mix** — gas-dependent processes (ammonia, glass, ceramics, cement clinker)
   behave differently from electro-intensive processes (primary aluminium, electric-
   arc steel, chlor-alkali). UK electricity prices are elevated because the marginal
   generator is usually gas, so the two shocks travel together (ONS, 2025).

The combination of high energy share **and** high trade exposure is what makes a
firm structurally unable to pass costs through; it has to adjust on the quantity
margin instead.

---

## 2. UK sectors with the highest energy exposure (SIC 2007)

The ETII list, underpinned by ONS electricity-and-gas-to-GVA ratios, is the best
UK-specific ranking of energy-and-trade exposure. The following are the standout
SIC 2007 classes (2-digit division / 4-digit class):

| SIC 2007 | Sector | Primary energy driver | Why it's exposed |
|---|---|---|---|
| **24.10** | Manufacture of basic iron & steel, ferro-alloys | Electricity (EAF) + coke/gas (BOF) | Electro-intensive, highly tradable; UK prices among highest in Europe |
| **24.42** | Aluminium production | Electricity | Primary smelting ~15 MWh/t Al; globally traded LME commodity |
| **24.43–24.45** | Lead, zinc, tin, copper | Electricity | Electrometallurgy; LME-priced outputs |
| **20.13 / 20.15** | Basic inorganic chemicals; fertilisers and nitrogen compounds | Gas (feedstock + heat) | Gas is both fuel and feedstock for ammonia/urea — c.80% of variable cost |
| **20.14 / 20.16** | Basic organic chemicals; plastics in primary forms | Gas + electricity | Steam-cracker energy; globally traded |
| **20.11** | Industrial gases | Electricity | Air separation is ~essentially electricity-to-product |
| **23.51 / 23.52** | Cement; lime and plaster | Gas / coal / petcoke | Clinker kiln heat; 30–40% of cash cost is energy |
| **23.11 / 23.13 / 23.14** | Flat glass; hollow glass; glass fibres | Gas | Continuous melting furnaces cannot cycle down |
| **23.31 / 23.32 / 23.41–23.44** | Ceramic tiles, bricks, refractories, tableware, sanitaryware | Gas | Tunnel kilns; UK ceramics especially exposed per EIUG |
| **17.11 / 17.12** | Pulp and paper manufacturing | Gas + electricity (steam + drying) | Continuous process, trade-exposed |
| **17.21–17.23** | Corrugated paper, packaging | Electricity | Downstream paper converters |
| **13.10 / 13.20 / 13.30** | Textile preparation, weaving, finishing | Gas (drying/finishing) + electricity | High-temperature finishing processes |
| **10.xx** | Food and beverage manufacturing (various) | Gas (process heat) + electricity (refrigeration) | Large in absolute terms but moderate energy share |
| **16.10 / 16.21** | Sawmilling; veneer & plywood | Electricity + biomass | Kilns and dryers |
| **19.20** | Petroleum refining | Refinery fuel gas + electricity | Own energy is ~8–10% of throughput |

This set is consistent with the ETII eligibility list published by DESNZ
(January 2023) and with the sectors foundationally covered by the EII Compensation
Scheme and the forthcoming British Industrial Competitiveness Scheme. In the ONS
environmental accounts (energy use reallocated to final consumer, SIC group level,
1990–2023), **iron & steel (24) and chemicals (20) alone have historically driven
the majority of changes in UK industrial energy use** (Hardt et al., 2018).

Economy-wide context: ONS estimates that the **direct** energy intensity of the CPI
is 6.6% but with big dispersion — housing services (20.5%) and transport (17.5%) at
the top, with indirect energy intensity for liquid fuels up to 69%. This maps into
which downstream industries themselves absorb the largest indirect hit (ONS 2022).

---

## 3. Academic evidence on cost pass-through

Two headline results from the literature tell us how energy shocks travel from
costs into prices.

**Ganapati, Shapiro & Walker (AEJ: Applied Economics, 2020)** — the reference
point for US manufacturing. Using Census micro-data and exogenous energy-price
variation across plants, they estimate that on average **~70% of energy-cost
changes are passed through to output prices in the short-to-medium run**, with
substantial heterogeneity: pass-through **exceeds 100% in some concentrated
industries** (consistent with Cournot/monopolistic-competition models where
markups scale with marginal cost) and is materially below 70% in more competitive,
trade-exposed segments. They show that incomplete pass-through shifts **25–75%
more of the welfare incidence onto producers** than a frictionless competitive
model would imply — important for carbon-price incidence too.

**Lafrogne-Joussier, Martin & Méjean (CEPII WP 2023-16 / INSEE DT 2023-13)** —
uses French firm-level data covering the 2020–22 energy shock. Headline findings:

- When firms reset prices, they pass through **~100% of the change in energy
  costs on average** (vs only ~30% of imported intermediate-input shocks).
- In the **least competitive sectors**, pass-through is **~115%** — i.e. margins
  expand in the shock, consistent with "excess pass-through" under imperfect
  competition.
- Export prices also rise roughly one-for-one with energy costs, so the volume
  response shows up as **lost export demand** rather than absorbed margins.

**Firm-level elasticity of energy demand** (Marin & Vona, *Energy Economics* and
related work; CEPR columns by Lafrogne-Joussier et al.):

- French manufacturing firm-level price elasticity of energy demand ≈ **−0.4 for
  electricity, −0.9 for gas**.
- For the largest shocks (≥36% YoY for electricity, ≥53% YoY for gas), elasticities
  **shrink in absolute value** (−0.2, −0.7) — short-run substitution is limited.
- Adjustment channels used ranked by importance: (a) cut the energy input,
  (b) raise prices, (c) substitute toward imported intermediate inputs, (d) shift
  production across plants, (e) invest in efficiency. Profit compression in the
  2022 shock was small on average and concentrated among the most energy-intensive
  firms.

**OECD / industry-level estimates** (Adeyemi-Hunt-style panel regressions; MDPI
*Sustainability* 2019 and Empirical Economics 2021):

- Industrial electricity **short-run price elasticity ≈ −0.11 to −0.24**,
  **long-run ≈ −0.11 to −0.28**, output elasticity ≈ 0.5.
- Meta-analysis of 428 studies (Labandeira et al., *Energy Policy* 2017):
  short-run price elasticity of energy demand ≈ **−0.21**, long-run ≈ **−0.61**.
- OECD (2023) *Rising Energy Prices and Productivity* confirms short-run pain /
  long-run reallocation, with the energy-intensive tail of firms most exposed.

**Bank of England / UK evidence** (Bank Underground, Aug 2023): UK pass-through
of input-cost shocks is gradual, incomplete and asymmetric; the energy
contribution to UK headline inflation peaked around mid-2022 and decayed
persistently through services (transport, hospitality), implying longer lags in
sectors where energy is one input among many.

---

## 4. Price vs quantity adjustment: the deciding variables

Combining the above, three axes determine which margin a firm uses:

| Axis | Implication |
|---|---|
| **Tradability / import penetration** | High → quantity adjustment (firms lose market share rather than raise price). UK steel, aluminium, basic chemicals, ceramics fit here. |
| **Market concentration / market power** | High → price adjustment or even *excess* pass-through (LMM, Ganapati et al.). UK examples: industrial gases (oligopoly), cement (concentrated), some specialty chemicals. |
| **Process flexibility** | Continuous high-temperature processes (glass furnaces, ammonia plants, blast furnaces) cannot cycle down cheaply → they **shut** (binary quantity response) rather than smoothly reduce output. CF Industries' Ince plant closure in 2022 is the textbook case. |

Short-run demand elasticity of energy is small (−0.1 to −0.4), so the first-order
adjustment for an energy-intensive firm is **not** to substitute away from energy;
it is to decide whether the market will pay the higher price or whether volume has
to fall.

---

## 5. Synthesis: UK sectors ranked by likely adjustment margin

| Likely margin | UK sectors (SIC 2007) | Reasoning |
|---|---|---|
| **Quantity-led (output/capacity cuts, closures)** | Basic iron & steel (24.10), Aluminium (24.42), Nitrogen fertilisers & basic inorganic chemicals (20.15, 20.13), Pulp & paper (17.11–17.12), Flat/hollow/fibre glass (23.11–23.14), Ceramics (23.31–23.44), Refining (19.20) | High gas/electricity share **and** high trade exposure; globally priced outputs. ONS 2025: EII output down one-third since 2021 Q1; CF Industries Ince closure (fertilisers); multiple UK blast-furnace idlings. |
| **Mixed (partial pass-through, partial output loss)** | Cement & lime (23.51, 23.52), Basic organic chemicals (20.14), Plastics primary forms (20.16), Textile finishing (13.30), Sawmilling and wood products (16.10, 16.21) | Moderate trade exposure; weight/transport costs protect cement domestically; chemicals commodity-priced but some specialty protection. |
| **Price-led (strong pass-through, margins protected or expanded)** | Industrial gases (20.11), Cement locally (23.51), Food manufacturing (10.xx), Beverages (11.xx), Pharmaceuticals (21.xx), Downstream paper packaging (17.21) | Market power, differentiated output, weak foreign substitution. ONS (2025) explicitly notes food & beverage manufacturers "largely able to pass on higher energy costs and remain profitable"; LMM's ~115% result most likely to apply here. |
| **Indirect exposure (energy travels through supply chain)** | Transport & logistics (49–53), Hospitality (55–56), Construction materials downstream (41–43 via 23), Agriculture (01) | ONS CPI decomposition: transport indirect energy intensity 17.5%; hospitality and transport saw the most persistent pass-through in Bank Underground evidence. |

---

## 6. Caveats

- ETII eligibility is a **binary** policy threshold (80th percentile of energy
  share, 60th percentile of trade intensity); it is a very good proxy but not a
  continuous measure of exposure. Firms just below the threshold can still be
  highly exposed.
- ONS industrial energy data are reported at **SIC division (2-digit) or group
  (3-digit)**; the 4-digit class tags above are indicative of where the exposure
  sits but some classes within a division behave differently.
- The academic pass-through literature is overwhelmingly **US (Ganapati et al.)**
  or **French (LMM, Marin–Vona)**. UK-specific firm-level pass-through estimates
  are scarce; the Bank of England's aggregate evidence and ONS' sector-level
  output/price data are the best UK proxies.
- Elasticities rise with horizon: a sector that looks "quantity-led" in 2022–23
  may re-enter via substitution, efficiency investment or offshoring within 3–5
  years. The 2023 OECD finding of short-run pain / long-run reallocation applies.
- Pass-through depends on whether the shock is perceived as **transitory or
  persistent**. LMM find nearly full pass-through during the 2022 shock partly
  because firms treated the cost increase as permanent.

---

## 7. Suggested data to pull for a quantitative build-out

If this scan were to be turned into a live dashboard, the minimum data set is:

1. **ONS environmental accounts** — *Energy use by industry, source and fuel*
   (SIC 2007 group level, 1990–2023). Denominator: GVA from Blue Book.
2. **ONS Annual Business Survey / Annual Purchases Survey** — energy purchases by
   SIC (experimental series from 2022).
3. **DESNZ Energy Consumption in the UK (ECUK) 2025** — Tables C2/C3 for SIC
   2-digit industrial consumption.
4. **ONS Input-Output Analytical Tables** — to reallocate direct energy to final
   consumers and capture indirect exposure.
5. **HMRC overseas trade statistics by SITC / CN** — to compute trade intensity
   per SIC class.
6. **DESNZ ETII list (Jan 2023 PDF)** — authoritative 4-digit SIC eligibility.
7. **ONS producer prices (PPI by product)** + output volumes — to observe realised
   pass-through vs volume response per sector over 2021–24.

A simple composite score — `0.5 × (energy cost / GVA, percentile rank) + 0.5 ×
(imports+exports / output, percentile rank)` — reproduces the ETII logic on a
continuous scale and can be refreshed quarterly.

---

## 8. Sources

**UK official data and policy**

- ONS, *The impact of higher energy costs on UK businesses: 2021 to 2024* (2025).
- ONS, *Energy use: by industry reallocated to final consumer and energy intensity*
  (environmental accounts, SIC group level, 1990–2023).
- ONS, *Energy use: by industry, source and fuel*.
- ONS, *Business energy spending: experimental measures from ONS business surveys*
  (Sep 2022).
- ONS, *The energy intensity of the Consumer Prices Index: 2022*.
- DESNZ, *Energy Consumption in the UK (ECUK) 2025*.
- DESNZ, *Energy Bills Discount Scheme: ETII assessment methodology and eligible
  sectors list* (Jan 2023).
- DESNZ, *British Industrial Competitiveness Scheme: consultation on eligibility*
  (incl. Annex A SIC codes for frontier/foundational manufacturing).
- OBR, *Energy prices and potential output: a production function approach*.
- Commons Library CBP-7317, *UK steel industry: statistics and policy*.
- Energy Intensive Users Group (EIUG), *Energy Prices and Energy Intensive
  Industries*.

**Academic / think-tank literature on pass-through and elasticities**

- Ganapati, Shapiro & Walker (2020), "Energy Cost Pass-Through in US
  Manufacturing: Estimates and Implications for Carbon Taxes", *American Economic
  Journal: Applied Economics* 12(2): 303–42.
- Lafrogne-Joussier, Martin & Méjean (2023), "Energy, Inflation and Market Power:
  Excess Pass-Through in France", CEPII WP 2023-16 / INSEE DT 2023-13.
- Marin & Vona (2021), "The impact of energy prices on socioeconomic and
  environmental performance: evidence from French manufacturing establishments,
  1997–2015", *European Economic Review*.
- Bottasso, Conti, Ferrari & Tei (2015), "Do manufacturing firms react to energy
  prices? Evidence from Italy", *Energy Economics* 49: 168–181.
- Labandeira, Labeaga & López-Otero (2017), "A meta-analysis on the price
  elasticity of energy demand", *Energy Policy*.
- Adeyemi, Hunt and related work on industrial electricity elasticities in
  OECD/high-income countries (MDPI *Sustainability* 2019; *Empirical Economics*
  2021).
- OECD (2023), *Rising Energy Prices and Productivity: Short-run Pain, Long-term
  Gain?*
- Hardt et al. (2018), "Untangling the drivers of energy reduction in the UK
  productive sectors: efficiency or offshoring?", *Applied Energy*.
- Bank of England / Bank Underground (Aug 2023), "How do firms pass energy and
  food costs through the supply chain".
- CEPR VoxEU columns: *The many channels of firms' adjustments to energy shocks:
  evidence from France*; *The limited impact of the energy price hike on firms'
  profitability*.
