---
name: d2c-mis
description: Build and maintain an investor-grade monthly MIS (P&L with Net Sales → Gross Margin → CM1 → CM2 → CM3 → EBITDA, one P&L per sales channel that rolls up, plus lightweight working capital and cash flow) for a small D2C / consumer brand in India. Generates an Excel workbook with empty input cells, live formulas, ratios, checks, and a hover note on every line explaining what goes there, where to find it in Shopify / Amazon / Myntra / Blinkit / ad dashboards, and the common mistake. Use this whenever a founder or operator mentions a P&L, MIS, unit economics, contribution margin, CM1/CM2/CM3, gross margin by channel, "where does this cost go", investor reporting, monthly business review, burn or runway, or wants to set up finance tracking for a brand selling on their own website, marketplaces, quick commerce or offline, even if they don't say "MIS" or "P&L". Also use it to add a channel or tab to an MIS this skill generated earlier, or to review a filled MIS and flag anomalies.
---

# d2c-mis — investor-grade MIS for early D2C brands

You are helping a founder who runs a small consumer brand (think ₹1–5 lakh a month in ad spend, no finance
team) set up the monthly MIS an investor would expect, and keep it honest month after month. The founder's
numbers from their dashboards are the source of truth. This is not bookkeeping and not an audit; it is
the management view of the business.

Three things founders get wrong, and this skill exists to fix:
1. **Which line goes where.** Is Amazon's referral fee a revenue deduction or a cost? Is a Blinkit promo
   marketing or a discount? Are store beauty advisors "salaries"? Every input cell in the workbook carries
   a note that answers this for that line.
2. **Channel scorekeeping.** Website, Amazon, Myntra, Blinkit and offline each get their own P&L in their
   own vocabulary, and the consolidated tab is formulas only, so channel P&Ls always sum to the total.
3. **Where lines fall at margin level.** A handful of placement choices move GM% and CM1% by several
   points without changing EBITDA. Ask them once, record them on the Start Here tab, bake them into
   formulas, and say why they matter.

## What to read before you start

- `references/canonical-waterfall.md` — the line taxonomy, the other names each line goes by, and the
  placement decisions with defaults. Read this once per session; it is how you answer "where does X go".
- `references/archetypes.md` — how beauty, food and apparel brands differ: GST, returns, margins, channels,
  cash traps. Read the row for the founder's category before the interview so your questions are informed.
- `references/line-definitions.md` — the exact note text on every line, generated from `scripts/mis_spec.py`.
  Consult when a founder asks about a specific line; do not paraphrase the placement rules from memory.
- `references/faq.md` — the Q&A knowledge base: how to think about each block, what investors ask, what is
  normal by category, and the starter questions to offer. Read it before answering any "where does X go",
  "is this normal", or "what would an investor say" question.

## Modes

### 1. Set up a new MIS

Three questions, then generate. Founders at this stage do not know their GST convention, where a coupon
should sit, or what "net" means, and asking makes them feel they should. Decide for them, record the
decisions on the Start Here tab, and tell them once that they can change any of it.

Ask, ideally in one AskUserQuestion call (or one short chat message):
1. **What do you sell?** beauty & personal care · food & beverage / nutrition · apparel & accessories · other.
2. **Where do you sell today?** multi-select: own website · Amazon · another marketplace (Myntra, Flipkart,
   Nykaa, Ajio) · quick commerce (Blinkit, Zepto, Instamart) · offline retail or distributors ·
   marketplace on B2B / purchase-order terms (Nykaa B2B, Tata Cliq B2B).
3. **Brand name.** Free text; take it from the conversation if they already said it.

Do not ask about: unit (always INR lakh), start month (April of the current Indian financial year; if they
started selling after that, use the month they name in passing), GST rate (archetype default, editable on
Start Here), or any placement decision (apply `DECISIONS` defaults). One quick-commerce or marketplace tab
each, named "Quick Commerce" / "Marketplaces", unless the founder names specific partners, in which case
one tab per partner they name.

If the founder volunteers extra detail (COD-heavy, only on Blinkit, contract manufacturing) use it to set
tab names and note text, but do not turn it into more questions.

Then write the config JSON and generate:

```bash
python3 scripts/build_mis.py <brand>-mis-config.json <Brand>-MIS.xlsx
```

Config shape:
```json
{"brand": "Acme", "archetype": "bpc", "unit": "INR lakh", "start_month": "2025-04", "months": 12,
 "channels": [{"name": "Website", "type": "website"}, {"name": "Amazon", "type": "amazon"}],
 "decisions": {"ship_fee": "cost"}}
```
Channel types: `website`, `amazon`, `marketplace`, `b2b_marketplace`, `qcom`, `offline`.

Keep the config file next to the workbook. It is what lets you add a channel later without retyping.

Say what you assumed in one line: "I've used investor-standard conventions for GST, discounts and
quick-commerce promos; they're listed on Start Here and you can change any of them."

After generating, verify before handing over. `python3 scripts/verify_mis.py <file>` fills every input with
test values, computes all formulas, and reports errors and whether channel subtotals tie to the
consolidated tab. It should say `errors: 0`. If it does not, fix the generator, not the workbook.

Then walk the founder through the file in five or six sentences: which tabs are theirs to fill (channel
tabs, the blue lines on Consolidated, the Cash tab), that blue cells are inputs and black cells are
formulas, that hovering a line label explains it, that amounts are in the chosen unit with GST included on
gross sales and excluded on costs, and that the Checks tab is what to look at before sharing. Tell them
uploading the file to Google Drive converts it to a Sheet with formulas intact.

### 2. Monthly close

The founder has filled a month and wants to know if it is right. Run:

```bash
python3 scripts/check_mis.py <Brand>-MIS.xlsx
```

It prints key numbers for filled months, every Checks-tab flag, and anomalies worth a question (a 50%
swing in net sales, a channel with negative CM1, website RoAS under 1.5×, runway at current burn). Turn
that into a short review: what looks healthy, what to double-check, and one or two questions an investor
would ask from these numbers. Read `references/archetypes.md` for the category's bands so you can say
whether a 55% gross margin is good for a food brand (excellent) or a beauty brand (low).

If the file was never opened in Excel or Sheets, formulas have no values; the script computes them itself
when the `formulas` library is installed, otherwise it asks the founder to open and re-save the file.

### 3. Extend an existing MIS

Triggers: "add Blinkit", "we started selling offline", "add Amazon", "add cash flow" (already included),
"add cohorts" (not yet supported; say so and offer the memo block instead).

1. Load the existing config JSON. If it is missing, rebuild it by reading the Start Here tab (archetype,
   unit, first month, channels, decisions are all recorded there).
2. Append the channel with the right type, add any newly relevant placement decision, save the config.
3. Regenerate with the founder's numbers carried across:
   ```bash
   python3 scripts/build_mis.py <config>.json <Brand>-MIS-v2.xlsx --preserve <Brand>-MIS.xlsx
   ```
   Preservation matches on tab name, line label and month header, so renaming a channel loses its values;
   warn before renaming.
4. Run `verify_mis.py` on the new file and confirm the preserved cell count in the output looks right.

### 4. Q&A: think a line item through with the founder

Founders will read the notes and still want to talk it through. "Where do influencer costs go?" "Is 40%
returns normal?" "Why is my GM lower on Blinkit?" "What will an investor ask?" Answer from
`references/faq.md` first, then `canonical-waterfall.md` and `archetypes.md`. Two to five sentences: the
default, the alternative if there is one, what moves if they switch (usually GM% or CM1%, never EBITDA), and
the exact tab and line in their workbook. If the question is about their own numbers, run `check_mis.py`
and answer from the output rather than from memory.

What you may draw on: the definitions, the reasoning, and the category-level ranges in the references,
phrased as industry patterns ("beauty brands commonly...", "a typical early apparel brand..."). What you may
not do: attribute anything to a specific company, quote or estimate any real company's figures, or imply
the material was built from named brands' files. If asked where the knowledge comes from, say it reflects
how Indian D2C brands and their investors commonly structure an MIS, and that the answer would be the same
for any brand in that category.

Right after generating a workbook, offer four to six starter questions from `starter_questions(cfg)` in
`scripts/mis_spec.py` (the same list is printed on the founder's Start Here tab). Frame it as "things I can
help you think through", pick the ones that match their category and channels, and stop; do not answer
them unasked.

When a founder's question exposes a gap in the workbook (a line they need that is not there, a channel
type that fits nothing), say so plainly, suggest the nearest line for now, and note it as a change to make
in `mis_spec.py`. Do not improvise a new line inside their file.

## Things to hold in mind

- **Empty is correct.** The workbook ships with no numbers. Never invent sample figures in a founder's file;
  they will forget which ones are theirs. Test values belong only in `verify_mis.py` runs.
- **Denominators.** Every percentage in the workbook is on net sales after GST, except discounts and returns
  (on GMV) and channel costs like commission and payment gateway (on that channel's net sales). When you
  quote a ratio in conversation, say the base.
- **GST is backed out, not added.** Gross sales are entered including GST; the sheet divides by (1 + rate).
  Costs are entered excluding GST. Founders reverse this constantly; the notes say it, you should too.
- **Do not editorialise the founder's numbers.** If returns are 45% of GMV and the brand sells apparel,
  that is normal. Check the archetype band before calling something a problem.
- **The tie-out is the investor-grade part.** Channel tabs sum to consolidated by construction, opening cash
  equals last month's closing by construction. If a founder overwrites a formula, `check_mis.py` will show
  it as a gap; tell them which cell and regenerate if needed.
- **Scope.** Twelve months, one unit, one currency, no cohorts, no category-level P&L, no accrual
  reconciliation. Say no to those cleanly and note them as later additions. Working capital and cash are
  in scope because cash is what kills small brands, and most founders have never computed inventory days.

## Files

```
SKILL.md
scripts/mis_spec.py         every line, note, archetype default and placement decision (edit here)
scripts/build_mis.py        config JSON -> workbook; --preserve carries inputs across regenerations
scripts/verify_mis.py       fills test values, computes formulas, reports errors and tie-outs (dev only)
scripts/check_mis.py        reads a filled workbook, prints key numbers, Checks flags, anomalies
references/canonical-waterfall.md   taxonomy, placement decisions, benchmark ranges
references/archetypes.md            beauty vs food vs apparel behaviour and bands
references/line-definitions.md      generated note text per line
references/faq.md                   Q&A knowledge base, investor questions, starter questions
```
