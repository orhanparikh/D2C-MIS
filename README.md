# d2c-mis

A Claude Code skill that builds and maintains an investor-grade monthly MIS for a small D2C brand: a P&L
with the standard waterfall (Net Sales → Gross Margin → CM1 → CM2 → CM3 → EBITDA), one P&L per sales channel
that rolls up automatically, and a lightweight working-capital and cash view. The output is an Excel workbook
with empty input cells, live formulas, ratios, a Checks tab, and a hover note on every line saying what goes
there, where to find it in your dashboards, and the common mistake.

## Install

```bash
git clone https://github.com/orhanparikh/D2C-MIS.git ~/.claude/skills/d2c-mis
```
Then in Claude Code: "help me set up a P&L for my brand" or `/d2c-mis`.

## What it does
- **Set up**: three questions (what you sell, where you sell, brand name), then a generated workbook. Units, GST and placement conventions are set to investor-standard defaults and recorded on the Start Here tab, where you can change them.
- **Monthly close**: fill a month, run the check, get a short review with the flags an investor would raise.
- **Extend**: add a channel later; your numbers are carried across.
- **Answer placement questions**: "where do influencer costs go", "is Amazon's storage fee COGS".

## Layout
```
SKILL.md                          the skill: interview, generate, monthly close, extend, placement Q&A
scripts/mis_spec.py               every line, hover note, archetype default and placement decision
scripts/build_mis.py              config JSON -> workbook; --preserve carries inputs across regenerations
scripts/verify_mis.py             dev check: fills test values, computes formulas, reports errors and tie-outs
scripts/check_mis.py              founder check: reads a filled workbook, prints key numbers and flags
scripts/gen_line_definitions.py   regenerates references/line-definitions.md from the spec
references/canonical-waterfall.md unified line taxonomy, placement decisions and benchmark ranges
references/archetypes.md          beauty vs food vs apparel behaviour, defaults and bands
references/line-definitions.md    generated note text for every line
docs/DESIGN.md                    why it is built this way
evals/                            test configs and prompts
examples/                         a blank generated workbook and its config (beauty brand, website + quick commerce)
```

## How the knowledge was built
The line definitions, placement defaults, category ranges and Q&A reflect how Indian D2C brands and their
investors commonly structure a monthly MIS. They are frameworks and industry norms; no company's data is
included in this repository.
