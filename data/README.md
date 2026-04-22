# /data/ — ONS SUT drop zone

Drop the latest ONS **Input-Output Analytical Tables, Industry by Industry**
(preferred) or **Supply and Use Tables** xlsx here. Source:

https://www.ons.gov.uk/economy/nationalaccounts/supplyandusetables/datasets/inputoutputsupplyandusetables
https://www.ons.gov.uk/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesindustrybyindustry

Any of these filenames will be picked up automatically by the parser:

- `ons_iot_iixi.xlsx` (industry-by-industry analytical table — best)
- `ons_iot_pxpa.xlsx` (product-by-product analytical table — also fine)
- `ons_sut.xlsx`      (supply and use tables — works, parser will derive A)

Just keep the original ONS filename if easier — the parser will glob `*.xlsx`
in this folder and pick the most recent.
