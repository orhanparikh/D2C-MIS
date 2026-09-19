# Line definitions (generated from scripts/mis_spec.py — do not edit by hand)

Each input line in the workbook carries this text as a hover note. WHAT it is, WHERE to find it, and the COMMON MISTAKE.

## Channel tabs

Lines marked with channel types appear only on those tabs. Labels and 'where' text adapt to the channel's vocabulary; the generic version is shown, with channel-specific variants below it.


### REVENUE

**Gross sales (GMV) incl. GST** — input

- What: Everything customers ordered and you shipped this month, valued at the price they paid before any discount, including GST.
- Where (Own website): Shopify › Analytics › Gross sales (before discounts, returns and shipping). Woo/Magento: sum of order value incl. GST.
- Where (Amazon): Seller Central › Business Reports › Ordered product sales (incl. GST).
- Where (Marketplace (billed commission)): Seller panel › Sales report › Gross sales incl. GST (Myntra: Partner Portal; Flipkart: Seller Hub; Nykaa marketplace: Seller Portal).
- Where (Marketplace on B2B terms (netted margin)): Partner's sell-through report at MRP incl. GST. If unavailable, use your invoice value grossed up by the agreed margin.
- Where (Quick commerce): Partner dashboard › GMV at MRP incl. GST for the month.
- Where (Offline retail / distribution): Sell-in to distributors or retailers valued at MRP incl. GST. If you only know your invoice value, gross it up by the trade margin.
- Common mistake: Entering Shopify 'Total sales' (already net of discounts and returns) or entering values excluding GST. Enter the gross, GST-inclusive number and let the sheet deduct.

**Consumer discounts & coupons** — input

- What: Discounts the shopper saw at checkout: coupon codes, automatic discounts, sale price-offs. Funded by you.
- Where (Own website): Shopify › Analytics › Discounts.
- Where (Amazon): Coupons, Lightning Deals and promo codes you funded: Seller Central › Payments › Transaction view › Promotion rebates.
- Where (Marketplace (billed commission)): Seller-funded discounts and coupon share from the settlement or promotions report.
- Where (Marketplace on B2B terms (netted margin)): Consumer discounts you funded per the partner's debit note.
- Where (Quick commerce): Leave blank here if you enter brand-funded promos on the Consumer promotions line.
- Where (Offline retail / distribution): Consumer schemes you funded (price-offs, GWPs) per debit notes.
- Common mistake: Mixing platform commission in here. Commission is what the platform keeps; discounts are what the customer did not pay.

**Channel / partner margin** — input  *(only: b2b_marketplace, offline, qcom)*

- What: The partner's margin when they buy your stock or raise a purchase order: MRP less what you invoice them.
- Where (Marketplace on B2B terms (netted margin)): Difference between MRP and your invoice price to the partner, per the trade agreement.
- Where (Quick commerce): MRP less your invoice price to the partner, per the trade agreement (typically 25–40%).
- Where (Offline retail / distribution): MRP less your invoice price, per the trade agreement (typically 25–40% of MRP).
- Common mistake: Forgetting this line makes GM% look like a website channel. If your invoice already excludes it, GMV must be grossed up to MRP or the line stays zero.

**Returns, RTO & cancellations after dispatch** — input

- What: Value (at selling price incl. GST) of orders that came back: undelivered COD (RTO), customer returns, cancellations after dispatch.
- Where (Own website): Shopify › Analytics › Returns, plus RTO value from your courier or Shiprocket RTO report.
- Where (Amazon): Seller Central › Reports › Returns; value of refunded orders.
- Where (Marketplace (billed commission)): Seller panel › Returns / RTO report. Apparel marketplaces run heavy exchanges; enter them on the exchanges line.
- Where (Marketplace on B2B terms (netted margin)): Stock returned or reversed under the PO, at MRP. Usually small.
- Where (Quick commerce): Expiry or damage returns reversed on the PO. Usually near zero.
- Where (Offline retail / distribution): Damaged or expired stock taken back, at MRP.
- Common mistake: Counting only refunds. RTO on COD orders is the bigger number for most website channels and never shows as a refund.

**RTO (undelivered / refused, returned to origin)** — input

- What: Orders the courier could not deliver, mostly COD refusals, valued at selling price incl. GST.
- Where (Own website): Shopify › Analytics › Returns, plus RTO value from your courier or Shiprocket RTO report.
- Where (Amazon): Seller Central › Reports › Returns; value of refunded orders.
- Where (Marketplace (billed commission)): Seller panel › Returns / RTO report. Apparel marketplaces run heavy exchanges; enter them on the exchanges line.
- Where (Marketplace on B2B terms (netted margin)): Stock returned or reversed under the PO, at MRP. Usually small.
- Where (Quick commerce): Expiry or damage returns reversed on the PO. Usually near zero.
- Where (Offline retail / distribution): Damaged or expired stock taken back, at MRP.
- Common mistake: Netting RTO into 'returns'. RTO is a delivery problem; returns are a product or fit problem. They need different fixes.

**Customer returns refunded** — input

- What: Delivered orders the customer sent back for a refund, at selling price incl. GST. Include refunds issued as store credit or gift cards.
- Where (Own website): Shopify › Analytics › Returns, plus RTO value from your courier or Shiprocket RTO report.
- Where (Amazon): Seller Central › Reports › Returns; value of refunded orders.
- Where (Marketplace (billed commission)): Seller panel › Returns / RTO report. Apparel marketplaces run heavy exchanges; enter them on the exchanges line.
- Where (Marketplace on B2B terms (netted margin)): Stock returned or reversed under the PO, at MRP. Usually small.
- Where (Quick commerce): Expiry or damage returns reversed on the PO. Usually near zero.
- Where (Offline retail / distribution): Damaged or expired stock taken back, at MRP.
- Common mistake: Ignoring gift-card refunds because no cash left. They still reverse revenue and create a liability.

**Exchanges (returned for another size / item)** — input

- What: Delivered orders returned and replaced. Enter the value of the returned unit at selling price incl. GST.
- Where (Own website): Shopify › Analytics › Returns, plus RTO value from your courier or Shiprocket RTO report.
- Where (Amazon): Seller Central › Reports › Returns; value of refunded orders.
- Where (Marketplace (billed commission)): Seller panel › Returns / RTO report. Apparel marketplaces run heavy exchanges; enter them on the exchanges line.
- Where (Marketplace on B2B terms (netted margin)): Stock returned or reversed under the PO, at MRP. Usually small.
- Where (Quick commerce): Expiry or damage returns reversed on the PO. Usually near zero.
- Where (Offline retail / distribution): Damaged or expired stock taken back, at MRP.
- Common mistake: Counting the replacement's shipping cost twice, once in forward logistics and once as an exchange cost. Count it once.

**Shipping & COD fees collected from customers** — input  *(only: website)*

- What: Fees the customer paid you for delivery or COD handling.
- Where: Shopify › Analytics › Shipping charges, plus COD handling fees charged to customers.
- Common mistake: Treating this as marketing or as a discount. It is money in, either as revenue (here) or as a reduction of logistics cost.

**Net revenue before GST** — formula

- What: What is left after discounts, partner margin and returns. Still includes GST.
- Formula: `{gmv}-{discounts}-{channel_margin}-{returns}-{rto}-{returns_refund}-{exchanges}+{ship_fee}`

**Less: GST (output tax)** — formula

- What: GST collected on your net revenue, at the rate set on Start Here for this channel. Overwrite with your GSTR-1 figure if you have it.
- Formula: `{pretax_net}-{pretax_net}/(1+{gst_rate})`

**NET SALES (post GST)** — formula

- What: The number every ratio below is measured against. Investors call it net sales, NSR or NMV.
- Formula: `{pretax_net}-{gst}`

**Consumer promotions funded by brand** — input  *(only: qcom)*

- What: Price-offs the shopper sees on the quick-commerce app that you fund, per the partner's debit note.
- Where (Quick commerce): Partner's debit note for brand-funded discounts, or dashboard › Promotions › brand share.
- Common mistake: Leaving it inside 'discounts' when the partner also funds part of the promo. Enter only your share.

**Net sales after brand-funded promotions** — formula  *(only: qcom)*

- What: Net sales after the promotions you fund. Gross margin is measured from here.
- Formula: `{nsr}-{promo_ded}`


### COST OF GOODS

**Cost of goods sold (product + conversion + primary packaging)** — input

- What: The cost of the units you actually sold: product, manufacturing or job-work, and the packaging that touches the product.
- Where: Units sold this month × landed cost per unit, from your costing sheet. Not purchases made this month.
- Common mistake: Entering this month's purchases or factory bills. Purchases go to inventory; COGS is only what left the warehouse as sales. Secondary packaging (shippers, fillers) goes in Logistics.

**GROSS MARGIN** — formula

- What: Net sales less cost of goods. The first number an investor looks at.
- Formula: `{nsr_base}-{cogs}`

**Gross margin %** — ratio



### FULFILMENT & CHANNEL COSTS

**Logistics: forward, reverse, RTO & COD charges, secondary packaging** — input

- What: Getting product to the customer and back: courier, 3PL pick-pack, RTO charges, COD collection fee, shipping cartons.
- Where: Shiprocket / Delhivery / Bluedart invoices for the month excl. GST, plus shipper cartons and fillers. Amazon: FBA fulfilment fee.
- Common mistake: Leaving out reverse and RTO charges, which can be 30–50% of forward cost in COD-heavy or apparel businesses.

**Less: shipping & COD fees collected from customers** — input  *(only: website)*

- What: Fees customers paid you for delivery or COD, netted against logistics.
- Where: Shopify › Analytics › Shipping charges, plus COD handling fees charged to customers. Enter as a positive number; the sheet subtracts it.
- Common mistake: Entering it as a negative. Enter positive; the formula subtracts.

**Warehousing & operations (rent, staff, packing labour)** — input

- What: Cost of storing and handling stock, before it ships.
- Where: Warehouse rent, warehouse staff, packing consumables for the month. If shared across channels, split by orders.
- Common mistake: Putting warehouse staff under Salaries. They scale with orders, so they belong here.

**Payment gateway charges** — input  *(only: website)*

- What: What the gateway kept from prepaid collections.
- Where: Razorpay / PayU / Cashfree statement › fees for the month excl. GST. Typically 1.8–2.2% of prepaid collections.
- Common mistake: Ignoring it because the payout arrives net. Gross up collections and show the fee.

**Marketplace commission** — input  *(only: amazon, marketplace)*

- What: What the platform charged you for the sale: referral or commission, collection fee, platform shipping fee.
- Where (Amazon): Seller Central › Payments › Transaction view › Amazon fees (referral fee only). FBA fees go in Logistics.
- Where (Marketplace (billed commission)): Settlement report › commission, fixed fee, collection fee, shipping fee charged by the platform.
- Common mistake: Netting it out of GMV so it disappears. When the platform bills commission and you invoice the shopper, it is a cost here, not a revenue deduction.

**Platform fixed / listing fees** — input  *(only: amazon, marketplace)*

- What: Fixed platform charges that do not scale with each order: subscription, closing fee, storage, cataloguing.
- Where (Amazon): Seller Central › Payments › FBA fulfilment fee, fixed closing fee, storage fee.
- Where (Marketplace (billed commission)): Monthly subscription, cataloguing, listing or 'shared cost' charges on the settlement.
- Common mistake: Mixing them into commission. Keep fixed fees separate so commission % stays comparable month to month.

**CONTRIBUTION MARGIN 1 (CM1)** — formula

- What: Margin after getting the product to the customer and paying the channel. What is left to pay for marketing.
- Formula: `{gm}-{logistics}+{ship_fee_cost}-{warehousing}-{pg}-{commission}-{platform_fees}`

**CM1 %** — ratio



### MARKETING & SELLING

**perf_mkt** — input

- What: Paid media and channel advertising that drives this channel's sales this month, excluding GST (you claim the input credit).
- Where (Own website): Meta Ads Manager and Google Ads billing for the month, excluding GST. Add affiliate and influencer payouts tied to sales.
- Where (Amazon): Amazon Advertising console › Campaign manager, spend for the month excluding GST.
- Where (Marketplace (billed commission)): Seller panel › Ads / Promotions › spend for the month excluding GST.
- Where (Marketplace on B2B terms (netted margin)): Debit notes or invoices from the partner for banners, campaigns, visibility.
- Where (Quick commerce): Blinkit / Zepto / Instamart brand dashboard › Ads › spend excluding GST.
- Where (Offline retail / distribution): Invoices or debit notes for shelf fees, displays, in-store activations.
- Common mistake: Entering the GST-inclusive invoice. Also: agency retainers and content production are brand costs on the Consolidated tab, not here.

**Consumer promotions funded by brand** — input  *(only: qcom)*

- What: Price-offs you fund on the quick-commerce app, treated here as a marketing cost.
- Where (Quick commerce): Partner's debit note for brand-funded discounts, or dashboard › Promotions › brand share.
- Common mistake: Also deducting them from net sales. Pick one place; you chose marketing.

**Store sales staff** — input  *(only: offline)*

- What: People placed in stores to sell: beauty advisors, promoters, sales officers.
- Where (Offline retail / distribution): Salaries and incentives of people placed in stores, if you treat them as a selling cost.
- Common mistake: Also including them under Salaries on the Consolidated tab. Once only.

**Testers, samples & retailer schemes** — input  *(only: offline)*

- What: Testers, gift-with-purchase, extra margin or scheme payouts the retailer bills you for.
- Where (Offline retail / distribution): Testers, GWPs, extra margin or scheme payouts billed by the retailer.
- Common mistake: Hiding these in discounts. They are the real cost of offline and should be visible.

**CONTRIBUTION MARGIN 2 (CM2)** — formula

- What: Margin after channel-level marketing and selling costs. Positive CM2 means the channel pays for its own growth.
- Formula: `{cm1}-{perf_mkt}-{promo_mkt}-{store_staff}-{schemes}`

**CM2 %** — ratio



### MEMO

**Orders shipped (count)** — input

- What: Number of orders that went out. Used for AOV.
- Where: Shopify › Orders (fulfilled) or marketplace › Orders shipped. Offline / Qcom: units or cases invoiced.
- Common mistake: Counting orders placed rather than shipped; cancellations inflate it.

**Average order value incl. GST** — formula

- What: GMV per shipped order.
- Formula: `{gmv}/{orders}`

**RoAS (net sales ÷ marketing)** — formula

- What: Net sales generated per rupee of marketing in this channel. Below 1.5× on a website channel is a red flag unless the brand is very new.
- Formula: `{nsr}/{perf_mkt}`

**Returns & RTO % of GMV** — ratio


**Discounts % of GMV** — ratio


**Marketing % of net sales** — ratio


**Logistics % of net sales** — ratio



## Consolidated P&L (lines below CM2)

**Brand marketing & content (campaigns, shoots, influencer retainers, PR, agency)** — input

- What: Marketing that builds the brand rather than a specific channel's sales this month.
- Where: Agency retainers, photoshoots, influencer fees not tied to a sale, PR, brand campaigns. Excl. GST.
- Common mistake: Splitting it into channels by guesswork. Keep it here so CM2 by channel stays honest.

**CONTRIBUTION MARGIN 3 (CM3)** — formula

- What: Margin after all marketing. This is the number that should turn positive first as you scale.
- Formula: `{cm2}-{brand_mkt}`

**CM3 %** — pct



### FIXED COSTS

**People: salaries, contractors, founder pay, employee benefits** — input

- What: Everyone on the team who is not in the warehouse or a store.
- Where: Payroll for the month incl. PF/ESI and contractors. Exclude warehouse staff (Logistics) and store staff if entered in the offline channel.
- Common mistake: Leaving out founder salary because it is unpaid. Enter what you would pay; investors add it back anyway.

**Technology: Shopify, apps, SaaS, domains** — input

- What: Software that runs the business.
- Where: Shopify bill, app subscriptions, Zoho/Notion/Slack, hosting. Excl. GST.
- Common mistake: Putting Shopify transaction fees here; those are payment gateway costs.

**Office rent, utilities, travel & admin** — input

- What: Running the office.
- Where: Office rent, electricity, internet, travel, meals, insurance, bank charges.
- Common mistake: Including warehouse rent, which belongs in Warehousing.

**Legal, accounting & professional fees** — input

- What: Professional advisers.
- Where: CA, CS, lawyers, consultants.
- Common mistake: Including agency retainers, which are brand marketing.

**Sampling & free product (not campaign-led)** — input

- What: Product you did not sell and did not give as part of a specific campaign.
- Where: Cost of units given away outside a brand campaign: PR seeding, gifting, trade samples.
- Common mistake: Leaving this inside COGS, which understates true gross margin.

**Write-offs: expired, damaged, liquidated below cost** — input

- What: Inventory losses. Non-cash but real.
- Where: Stock written off or sold below cost this month, at cost.
- Common mistake: Ignoring them until year end; monthly visibility is the point.

**OPERATING EBITDA** — formula

- What: Profit before interest, depreciation, tax and one-offs. The bottom line an investor compares across brands.
- Formula: `{cm3}-{people}-{tech}-{rent_admin}-{legal_prof}-{sampling}-{writeoffs}`

**Operating EBITDA %** — pct


**One-time / exceptional costs** — input

- What: Costs that will not recur and should not be in the run-rate.
- Where: Fund-raise costs, legal settlements, relocation. Genuinely non-recurring only.
- Common mistake: Calling every bad month 'one-time'. If it happens twice a year, it is operating.

**REPORTED EBITDA** — formula

- What: Operating EBITDA less one-offs.
- Formula: `{op_ebitda}-{one_time}`


### BELOW EBITDA

**Depreciation & amortisation** — input

- What: Non-cash charge on equipment, moulds, software.
- Where: From your CA, or leave blank until year end.
- Common mistake: None; small brands can leave it blank.

**Interest & finance charges (net of interest earned)** — input

- What: Cost of borrowed money, net of what idle cash earned.
- Where: Loan and credit-line interest paid, less FD interest earned.
- Common mistake: Adding FD interest above EBITDA to flatter it. It belongs here.

**PROFIT BEFORE TAX** — formula

- What: What is left before income tax.
- Formula: `{rep_ebitda}-{dep}-{interest}`


### KEY RATIOS & MIX

**Net sales growth month on month** — pct


**Total marketing % of net sales** — pct


**Blended RoAS (net sales ÷ all marketing)** — formula

- Formula: `{nsr}/({perf_mkt}+{promo_mkt}+{brand_mkt})`

**People % of net sales** — pct


**Fixed costs % of net sales** — pct



## Cash & Working Capital


### WORKING CAPITAL (closing balances at month end)

**Inventory at cost (finished goods + raw & packing material + goods in transit)** — input

- What: Everything you own that has not been sold, at what it cost you.
- Where: Stock count or inventory system at month end, valued at cost. Include stock at 3PLs, Amazon FBA, Qcom dark stores that is still yours.
- Common mistake: Valuing at MRP, or forgetting stock sitting with Amazon and Qcom partners.

**Receivables (money owed to you by platforms, partners, retailers)** — input

- What: Sales you have made but not been paid for yet.
- Where: Unsettled marketplace payouts + Qcom / B2B / distributor invoices unpaid + COD remittances pending from couriers.
- Common mistake: Forgetting COD cash sitting with the courier for 7–10 days.

**Payables (money you owe suppliers, agencies, platforms)** — input

- What: Bills you have received but not paid.
- Where: Unpaid supplier, manufacturer, courier, agency and ad-platform invoices at month end.
- Common mistake: Excluding credit-card balances used for ads. They are payables.

**NET WORKING CAPITAL** — formula

- What: Cash tied up in running the business. Growth usually eats cash here before it shows profit.

**Inventory days (on COGS)** — formula

- What: How many days of sales your stock covers. Above your archetype band means cash is sitting on shelves.

**Receivable days (on net sales)** — formula

- What: How long customers and platforms take to pay you.

**Payable days (on COGS)** — formula

- What: How long you take to pay suppliers. Long is good for cash, bad for relationships.

**Cash conversion cycle (days)** — formula

- What: Days between paying for stock and getting paid for it. Lower is better; negative means suppliers fund your growth.


### CASH FLOW

**Opening cash (bank + wallets + FDs)** — input (first month only)

- What: Cash at the start of the month.
- Where: Bank balances on the 1st. Only the first month is typed; later months roll forward.
- Common mistake: Typing every month. Only month one is an input; the rest are formulas.

**Reported EBITDA (from Consolidated P&L)** — link


**Less: increase in working capital** — formula

- What: Cash absorbed (or released) by inventory, receivables and payables moving.

**Less: capex (equipment, moulds, fit-outs, software builds)** — input

- What: Money spent on things that last more than a year.
- Where: Asset purchases this month.
- Common mistake: Putting capex in the P&L as an expense.

**Less: interest & finance charges (from Consolidated P&L)** — link


**Less: taxes paid (income tax, net GST paid)** — input

- What: Tax actually paid in cash this month.
- Where: Advance tax, TDS deposited, net GST cash outflow.
- Common mistake: Confusing GST collected with GST paid; only the net cash outflow goes here.

**Add: equity raised** — input

- What: New equity money in.
- Where: Money received from investors or founders this month.
- Common mistake: Including convertible notes here and also under debt.

**Add: debt drawn less repaid** — input

- What: Net borrowing this month. Negative if you repaid more than you drew.
- Where: Loans, credit lines, venture debt drawn, net of principal repaid.
- Common mistake: Entering repayments as positive.

**Other cash movements** — input

- What: Catch-all so closing cash matches the bank.
- Where: Anything else: deposits paid, refunds received, corrections.
- Common mistake: Using it to hide a P&L gap. Explain any big number in a note.

**CLOSING CASH** — formula

- What: Should equal your bank balance on the last day. If it does not, something above is misclassified.

**Net burn (negative = cash consumed)** — formula

- What: Cash consumed this month, before financing is the honest view: add back equity and debt to see operating burn.

**Operating burn (before equity & debt)** — formula

- What: Cash the business itself consumed. The runway denominator.

**Runway (months, on last 3 months' operating burn)** — formula

- What: Closing cash divided by average operating burn over the last three months. Blank while burn is positive.


## Placement decisions

**Brand-funded consumer promotions on quick commerce: revenue deduction or marketing cost?**

- `deduction` (default): Deduct from net sales before gross margin (investor standard; GM% reads lower)
- `marketing`: Treat as a marketing cost below CM1 (GM% reads higher; CM2 and below unchanged)
- Why: Moves GM% by 5–6 points in food brands. Investors expect the deduction view; your auditor may prefer marketing. CM3 and EBITDA are identical either way.

**Shipping and COD fees you collect from website customers: add to revenue or net against logistics?**

- `cost` (default): Net against logistics cost (keeps GMV clean)
- `revenue`: Add to revenue above net sales
- Why: Both are accepted. Netting keeps AOV and GMV comparable with marketplaces that never show this fee.

**Salaries of sales staff or beauty advisors placed in stores: selling cost in the offline channel, or people cost below CM3?**

- `cm2` (default): Selling cost inside the offline channel P&L (shows true offline economics)
- `fixed`: People cost on the consolidated P&L
- Why: Store staff scale with doors, not with head office. Keeping them in the channel shows whether offline pays for itself.

**Exchanges in apparel: count the returned unit as a return and the replacement as new gross sales, or net them out?**

- `gross` (default): Return at full value; replacement counted as new gross sales (matches marketplace reports)
- `net`: Net: exclude both legs, record only the extra logistics
- Why: Marketplace reports show exchanges as returns plus new orders, so gross is easier to reconcile. Either way, do not count the replacement's logistics twice.


## Archetype defaults

| Archetype | GST default | Returns split | GM band | Returns % GMV band | Logistics band | Inventory days | Receivable days |
|---|---|---|---|---|---|---|---|
| Beauty & personal care | 18% | no | 45%–75% | 0%–15% | 5%–15% | 30–150 | 0–60 |
| Food & beverage / nutrition | 12% | no | 25%–55% | 0%–8% | 5%–15% | 20–90 | 0–60 |
| Apparel & accessories | 10% | yes | 40%–70% | 20%–60% | 8%–25% | 45–220 | 0–45 |
| Other | 18% | no | 20%–80% | 0%–30% | 3%–25% | 20–220 | 0–60 |