#!/usr/bin/env python3
"""Generate references/line-definitions.md from mis_spec.py so the reference never drifts from the workbook."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from mis_spec import CHANNEL_LINES, CONSOLIDATED_LINES, CASH_LINES, CHANNEL_TYPES, DECISIONS, ARCHETYPES

def res(x, ct): return x(ct) if callable(x) else (x or "")

out = ["# Line definitions (generated from scripts/mis_spec.py — do not edit by hand)\n",
       "Each input line in the workbook carries this text as a hover note. WHAT it is, WHERE to find it, and the COMMON MISTAKE.\n"]
out.append("## Channel tabs\n")
out.append("Lines marked with channel types appear only on those tabs. Labels and 'where' text adapt to the channel's vocabulary; the generic version is shown, with channel-specific variants below it.\n")
for l in CHANNEL_LINES:
    if l["kind"] in ("header",): out.append(f"\n### {l['label']}\n"); continue
    if l["kind"] == "blank": continue
    generic = {}
    label = res(l.get("label"), generic) or l["key"]
    applies = l.get("applies", "all")
    tag = "" if applies == "all" else f"  *(only: {', '.join(sorted(applies))})*"
    kind = {"input": "input", "formula": "formula", "pct": "ratio"}[l["kind"]]
    out.append(f"**{label}** — {kind}{tag}\n")
    if l.get("what"): out.append(f"- What: {res(l['what'], generic)}")
    if l["kind"] == "input":
        where = res(l.get("where"), generic)
        if callable(l.get("where")):
            variants = {t: l["where"](ct) for t, ct in CHANNEL_TYPES.items() if (applies == "all" or t in applies) and l["where"](ct)}
            for t, w in variants.items(): out.append(f"- Where ({CHANNEL_TYPES[t]['label']}): {w}")
        elif where: out.append(f"- Where: {where}")
        if l.get("mistake"): out.append(f"- Common mistake: {res(l['mistake'], generic)}")
    if l.get("formula") and l["kind"] != "pct": out.append(f"- Formula: `{l['formula']}`")
    out.append("")
out.append("\n## Consolidated P&L (lines below CM2)\n")
for l in CONSOLIDATED_LINES:
    if l["kind"] == "header": out.append(f"\n### {l['label']}\n"); continue
    if l["kind"] == "blank": continue
    out.append(f"**{l['label']}** — {l['kind']}\n")
    for k, t in [("what", "What"), ("where", "Where"), ("mistake", "Common mistake")]:
        if l.get(k): out.append(f"- {t}: {l[k]}")
    if l.get("formula") and l["kind"] != "pct": out.append(f"- Formula: `{l['formula']}`")
    out.append("")
out.append("\n## Cash & Working Capital\n")
for l in CASH_LINES:
    if l["kind"] == "header": out.append(f"\n### {l['label']}\n"); continue
    if l["kind"] == "blank": continue
    out.append(f"**{l['label']}** — {l['kind'].replace('input_first','input (first month only)')}\n")
    for k, t in [("what", "What"), ("where", "Where"), ("mistake", "Common mistake")]:
        if l.get(k): out.append(f"- {t}: {l[k]}")
    out.append("")
out.append("\n## Placement decisions\n")
for k, d in DECISIONS.items():
    out.append(f"**{d['question']}**\n")
    for o, t in d["options"].items(): out.append(f"- `{o}`{' (default)' if o == d['default'] else ''}: {t}")
    out.append(f"- Why: {d['why']}\n")
out.append("\n## Archetype defaults\n")
out.append("| Archetype | GST default | Returns split | GM band | Returns % GMV band | Logistics band | Inventory days | Receivable days |")
out.append("|---|---|---|---|---|---|---|---|")
for k, a in ARCHETYPES.items():
    b = a["bands"]
    out.append(f"| {a['label']} | {a['gst']:.0%} | {'yes' if a['returns_split'] else 'no'} | {b['gm'][0]:.0%}–{b['gm'][1]:.0%} | {b['returns_pct_gmv'][0]:.0%}–{b['returns_pct_gmv'][1]:.0%} | {b['logistics_pct'][0]:.0%}–{b['logistics_pct'][1]:.0%} | {b['dio'][0]}–{b['dio'][1]} | {b['dso'][0]}–{b['dso'][1]} |")
open(os.path.join(os.path.dirname(__file__), "..", "references", "line-definitions.md"), "w").write("\n".join(out))
print("wrote references/line-definitions.md", len(out), "lines")
