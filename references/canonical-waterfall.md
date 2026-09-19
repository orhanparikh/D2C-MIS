# Canonical D2C P&L waterfall (v1.0)

The line taxonomy this skill uses, with the other names each line commonly goes by in Indian D2C MIS
files, and the placement decisions that move margins. "Base" is the denominator for a line's ratio.
Category-level ranges live in `archetypes.md`; nothing here is attributed to any company.

## A. Orders → Net Sales

| # | Canonical line | Contents | Also called |
|---|---|---|---|
| A0 | Gross Orders (incl. GST) | Orders placed, before cancellation | Gross orders received |
| A0a | Cancellations | Cancelled before dispatch | Cancellations |
| **A1** | **Gross Revenue / GMV (incl. GST)** | Invoice value at list, before deductions | Gross sales · GMV · Gross revenue |
| A2 | Consumer Discounts | Coupons, promo codes, price-offs on own site and marketplaces | Discounts · Coupons |
| A3 | Trade / Channel Margin | Partner's cut when the partner invoices or buys stock: distributor and retailer margin, B2B marketplace commission, quick-commerce partner margin | Trade margins · Channel margins · B2B commission |
| A4 | Returns, RTO, Exchanges | Split when possible: RTO (undelivered) · customer return refunded · return to gift card · exchange | RTO/Cancellations · Sales returns · Returns, RTO & Exchange |
| A5 | Other revenue add-ons | COD handling fee, shipping fee charged to shopper, if booked as revenue | COD income · Shipping income |
| **A6** | **Pre-tax Net Revenue** | A1 − A2 − A3 − A4 + A5 | Net revenue · Pre-tax NSR · Gross revenue less margins |
| A7 | GST (output) | 5–18% by category; blended | GST · Taxes |
| **A8** | **Net Sales Revenue (NSR / NMV)** | A6 − A7. **Base for every % unless stated.** | Net sales · NSR · NMV · Post-tax NSR · Net revenue post GST |
| A9 | Consumer Promotions (if treated as revenue deduction) | Brand-funded price-offs on quick commerce and marketplaces | Consumer promo · Brand-funded discount |
| **A10** | **NSR post promo** | A8 − A9 (= A8 when promos are marketing) | Net sales after promotions |

## B. COGS → Gross Margin

| # | Line | Contents | Also called |
|---|---|---|---|
| B1 | Product Cost | Purchased or manufactured product | COGS · Product cost · Material cost |
| B2 | Conversion / Processing | Job-work, plant labour, power | Processing cost · Conversion cost |
| B3 | Primary Packaging | Touches the product | Primary packaging · (often inside "product + packaging") |
| B4 | Marketing / sampling COGS | Product given away; some brands deduct it from stock separately | Marketing COGS · Samples at cost |
| **B5** | **Gross Margin** | A10 − B1 − B2 − B3 | Gross margin · Gross profit · GM |

## C. Fulfilment and channel costs → CM1

| # | Line | Contents | Base | Also called |
|---|---|---|---|---|
| C1 | Logistics & Distribution | Forward + reverse courier, 3PL, freight to channel, marketplace fulfilment fees | NSR (and GMV in high-return categories) | Logistics · L&D · Shipping · Fulfilment |
| C1a | Shipping / COD fee recovered | Negative cost | | Shipping + COD fee from customer |
| C2 | Warehousing & Operations | Warehouse rent, staff, packing labour | NSR | Warehousing · Ops cost |
| C3 | Secondary Packaging | Shippers, fillers | NSR | Secondary packaging · Packing material |
| C4 | Payment Gateway | | Website NSR | PG charges · Payment processing |
| C5 | Marketplace Commission (billed) | When the platform bills commission and the brand invoices the shopper | Marketplace NSR | Referral fee · Commission · Channel margins (billed) |
| C6 | Platform Referral / Listing Fees | Fixed-ish platform fees, shared costs | Marketplace NSR | Listing fees · Fixed closing fees · Shared costs |
| **C7** | **CM1** | B5 − C1…C6 | | CM1 · Contribution margin 1 |

## D. Marketing → CM2, CM3

| # | Line | Contents | Base | Also called |
|---|---|---|---|---|
| D1 | Performance Marketing (own site) | Meta, Google, affiliates | Website NSR; RoAS = website NSR ÷ D1 | Digital marketing · Performance marketing · Paid media |
| D2 | Marketplace Advertising | Sponsored listings, banners, on-platform display | Marketplace NSR | Marketing on marketplaces · Banner expenses · Sponsored ads |
| D3 | Consumer Promotions (if treated as marketing) | See A9 | | Customer promo / discount |
| D4 | Selling Staff | Beauty advisors, sales officers, store staff paid per outlet | Offline NSR | BA salaries · Sales team · Promoters |
| D5 | Trade Visibility & Schemes | Shelf fees, testers, GWPs, extra margin | Offline NSR | Visibility · Testers · Schemes · Extra margin |
| **D6** | **CM2** | C7 − D1…D5 | | CM2 · Contribution margin 2 |
| D7 | Brand Marketing & Content | Brand campaigns, photoshoots, influencer retainers, gifting, events, billboards, PR | NSR | Brand building · Branding costs · Brand & other spends |
| **D8** | **CM3** | D6 − D7 | | CM3 · Contribution margin 3 |

## E. Fixed costs → EBITDA

| # | Line | Contents | Also called |
|---|---|---|---|
| E1 | People | Salaries, employee benefits, contractors (excluding D4) | Salaries · Salaries & EE · Payment & benefit to employees |
| E2 | Technology | SaaS, Shopify apps, dev | Tech expenses · Software |
| E3 | Rent & Admin | Rent, utilities, travel, office | Other overhead · G&A · Rentals · Admin & other |
| E4 | Legal & Professional | Audit, legal, consultants | Legal & professional charges |
| E5 | Agency Retainers | Web, design, packaging, NPD | Agency costs · Consultancy |
| E6 | Sampling (non-campaign) | | Sampling · Free product |
| E7 | Write-offs & Liquidation Loss | Inventory expiry/damage, bad debts, liquidation below cost | Write off · Liquidation loss |
| **E8** | **Operating EBITDA** | D8 − E1…E7 | Operating EBITDA · EBITDA · EBIT (when depreciation is nil) |
| E9 | One-time / Exceptional | Fund-raise costs, restructuring, one-off legal | One-time expenses · Exceptional items |
| **E10** | **Reported EBITDA** | E8 − E9 | Reported EBITDA |

## F. Below EBITDA (report, don't optimise)
Depreciation · Interest & finance charges · Interest income on deposits · Tax → PBT / PAT. Net interest
income below EBITDA; never let it lift operating performance.

## G. Memo block (always shown alongside)
AOV incl. GST by channel · Orders · Channel mix % of GMV and of NSR · Category mix and GM% by category ·
RoAS by channel · CAC, 12-month LTV, LTV/CAC when cohort data exists · Returns split · Inventory days and
ageing · Receivable/payable days, CCC · Opening/closing cash, monthly burn · MIS-to-books reconciliation flag.

## Placement decisions and their defaults

| Decision | Options | Default | Why |
|---|---|---|---|
| Consumer promos on Qcom/marketplaces | A9 revenue deduction · D3 marketing | A9 | Moves GM% by several points; investors expect the deduction view; EBITDA unchanged |
| Marketplace commission | A3 netted (partner invoices/buys) · C5 cost (platform bills) | Follow the paperwork: netted if payout arrives net | The same brand can have both models across two marketplaces; channel GM% then is not comparable, CM1 is |
| Shipping/COD fee from shopper | A5 revenue · C1a negative cost | C1a | Keeps GMV and AOV comparable with marketplaces |
| Exchanges | A4 deduction at full value · net only the margin/logistics | A4, and count replacement logistics once | Marketplace reports show exchanges as return + new order |
| Gift-card refunds | A4 deduction, tracked separately | Yes | Non-cash, creates a liability |
| Payment gateway | C4 · E3 overhead | C4 | Variable with website sales |
| Store staff / BAs | D4 selling cost · E1 people | D4 if paid per outlet | Scales with doors, not head office |
| Brand content (photoshoots) | D7 brand · D1 performance | D7 | Keeps channel CM2 honest |
| One-time expenses | E9 below operating EBITDA | Only genuinely non-recurring | Shows operating and reported EBITDA side by side |
| Interest income | F | Never above EBITDA | Flatters operating performance otherwise |
| Ratio denominators | Total NSR for everything · channel NSR for channel costs | Channel NSR for D1, D2, C4, C5; GMV as second view for logistics in apparel | Returns inflate NSR-based ratios |

## Benchmarks
See `archetypes.md` for category-level ranges (gross margin, returns, logistics, marketing, inventory and
receivable days). Ranges are industry norms for early-stage Indian D2C brands, not any company's figures.
