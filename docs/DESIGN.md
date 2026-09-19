# d2c-mis — design

## Who it is for
A founder of a small Indian D2C brand (₹1–5 lakh a month in ad spend, no finance team) who wants an
investor-grade monthly MIS: a P&L with standard subtotals (Net Sales → GM → CM1 → CM2 → CM3 → EBITDA),
one P&L per channel that rolls up, and a lightweight working-capital and cash view.

## What it is not
Not an accounting system. Founder inputs are the source of truth: they read revenue, returns, ad spend
from Shopify, Amazon, Meta and type the monthly figure. No ledgers, no bank reconciliation, no audit tie-out.

## The three gaps it closes
1. **Which line goes where.** Every input cell carries a note: definition, where to find the number in the
   founder's dashboards, and the classic mistake. A Definitions tab holds the long form.
2. **Channel scorekeeping.** One tab per channel with the same waterfall in that channel's vocabulary
   (Amazon "referral fee", Myntra "commission", offline "distributor margin"). The Consolidated tab is
   formulas only and sums the channel tabs, so channel P&Ls always tie to the total.
3. **Where lines fall at margin level.** Placement decisions (Qcom consumer promos, marketplace commission
   netted vs billed, shipping fee recovered, exchanges, store staff, one-time costs) are set to investor-standard
   defaults, recorded on the Start Here tab with the reason, and baked into the formulas.

## How it runs
1. **Setup interview** (three questions): category archetype (BPC / F&B / Apparel / other), channels live
   today, brand name. Unit is INR lakh; first month is April of the current financial year.
2. **Placement decisions**: applied as defaults, never asked; recorded on Start Here with the reason so the
   founder can change any of them.
3. **Generate**: `scripts/build_mis.py config.json out.xlsx`. Empty blue input cells, black formulas,
   ratios and MoM growth prefilled, cell notes on every input, Definitions and Checks tabs.
4. **Fill**: founder drops the file into Google Drive (converts to Sheets, formulas intact) or uses Excel.
5. **Monthly close**: founder fills a column; skill runs `scripts/check_mis.py` on the downloaded file and
   reports anomalies (GST rate out of band, returns spike, GM outside archetype band, cash not rolling).
6. **Extend**: "add Blinkit", "add Amazon", "we started selling offline". Config is updated and the workbook
   regenerated with existing inputs preserved by (tab, line, month). Cohorts and category-level P&L are not
   yet supported.

## Workbook layout
| Tab | Contents | Who edits |
|---|---|---|
| Start Here | Legend, brand, unit, month header, GST rate per channel, placement decisions, how-to | Founder (yellow cells) |
| One per channel | GMV → CM2 waterfall in channel vocabulary, memo (orders, AOV, RoAS), ratios | Founder (blue cells) |
| Consolidated P&L | Sum of channels to CM2; brand marketing; fixed costs; EBITDA; below-EBITDA; ratios, MoM, mix | Founder fills only brand and fixed-cost lines |
| Cash & Working Capital | Inventory, receivables, payables, NWC, days, CCC; cash roll-forward and burn | Founder (blue cells) |
| Checks | Rule results per month, green/red | Nobody |
| Definitions | Every line: definition, where to find, mistake, placement note | Nobody |

## Archetype awareness
The archetype changes defaults and note text, never structure: GST rate default, returns lines (apparel gets
RTO / refund / exchange split), COGS guidance (contract manufacturing vs trading), expected bands used by
Checks, and which channels are suggested first. See `references/archetypes.md`.

## Source material
Frameworks and industry norms only. No company's data, names or figures are part of this repository.
