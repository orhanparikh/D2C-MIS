# Q&A knowledge base — how to think about each line

Definitions, reasoning and category-level ranges for how Indian D2C brands and their investors structure a monthly MIS. Nothing here describes or is attributed to any specific company, and no answer should be either. When a founder asks something this file does not cover,
reason from `canonical-waterfall.md` and say that it is a judgement call.

Answer style: two to five sentences. Say the default, the alternative if there is one, what moves if they
switch, and which tab and line it touches in their workbook. Use the archetype bands from `archetypes.md`
when they ask "is this normal".

## A. The waterfall and its words

**GMV, gross revenue, net revenue, net sales, NSR, NMV: which is which?**
GMV (or gross sales) is what shoppers paid before anything is taken off, including GST. Net revenue before
GST is GMV less discounts, partner margins and returns. Net sales (also NSR, NMV, "post-tax NSR") is that
number with GST backed out. Every ratio in the workbook is on net sales unless the label says otherwise.
Investors mean net sales when they say "revenue".

**Why divide by 1.18 to remove GST instead of multiplying by 0.18?**
Because the GST is inside the price. A ₹118 sale contains ₹18 of GST and ₹100 of revenue; 118 × 0.18 is
₹21.24, which overstates the tax and understates revenue by 3 points. The workbook does this for you from
the rate on Start Here. If your GSTR-1 gives a different number, overwrite the GST line.

**What is the difference between a discount, a trade margin, and a commission?**
A discount is money the shopper did not pay you: coupon, sale price, promo code. A trade margin is what a
partner keeps when they buy your stock or raise a purchase order (distributor, retailer, quick-commerce
partner, a marketplace on B2B terms); you never see that money, so it is a revenue deduction. A commission
is a fee a platform bills you after you invoiced the shopper (Amazon referral fee, Myntra commission); you
did receive the gross, so it is a cost below gross margin, inside CM1. The test is: who invoiced the end
customer? If you did, it is a cost. If the partner did, it is a margin.

**Why is Amazon's fee a cost but my Nykaa B2B margin a revenue deduction? They feel the same.**
They are the same economically and different in accounting, and the difference matters for gross margin.
A beauty brand often runs both models at once: a B2B partner's margin comes off revenue while Amazon's referral fee sits in CM1, so the two channels' GM% are not comparable even though the products are identical. The workbook handles this by channel type. When you compare channels, compare CM1, not GM.

**CM1, CM2, CM3: why does every deck define them differently?**
There is no standard, only conventions. This workbook uses: CM1 = gross margin less fulfilment and channel
costs (logistics, warehousing, payment gateway, billed commissions, platform fees); CM2 = CM1 less
channel-level marketing and selling; CM3 = CM2 less brand marketing. It is common to see CM1 alone defined three different ways across three decks. State the definition whenever you share a number, or point to the
Start Here tab, which records it.

**Which margin should I quote to an investor?**
Net sales, gross margin %, CM2 % (or CM3 % if you spend on brand), and operating EBITDA %, all on the same
month or trailing three months. GM% tells them your product economics, CM2 tells them whether channels pay
for their own growth, EBITDA tells them burn. Quoting only GM% invites the question "and after marketing?"

## B. Returns, RTO, cancellations, exchanges

**What is the difference between a cancellation, an RTO, a return and an exchange?**
Cancellation: the order never shipped; it is not in gross sales in some reports and is in others, so check
which your dashboard shows. RTO (return to origin): shipped but never delivered, usually a COD refusal; you
pay forward and reverse shipping and get the product back. Return: delivered, then sent back for a refund
or store credit. Exchange: delivered, sent back, and a replacement shipped. Each has a different cause and a
different fix, which is why apparel brands split them.

**Why are returns a revenue deduction and not a cost?**
Because the sale did not happen. Booking a return as a cost would leave the original sale in revenue and
inflate net sales, AOV, and every ratio. The cost of the return (reverse shipping, repackaging, write-off
if damaged) is real and sits in logistics and write-offs.

**Do exchanges double count?**
They can. If your marketplace report shows an exchange as a return plus a new order, and you also enter the
replacement's shipping in logistics, you have counted the logistics twice. The default in this workbook is
to record the exchange at full value as a deduction and count the replacement's shipping once. Investors notice this when logistics jumps in the month exchanges are launched.

**Where do refunds issued as gift cards or store credit go?**
As a return, on the returns-refund line. No cash left, but the sale reversed and you now owe the customer.
Track the outstanding gift-card balance separately; it is a liability that becomes revenue when redeemed.

**What return rate is normal?**
Returns plus RTO as a share of GMV: beauty and food typically under 10%, driven by COD refusals; apparel
35–55% including exchanges, with refunds 10–15%, RTO 8–13% and exchanges 20–30%. If you sell apparel and
see 45%, you are normal. If you sell skincare and see 20%, look at your COD share and pin-code serviceability.

## C. Discounts and promotions

**Where do the promotions I fund on Blinkit or Zepto go, and why does it matter?**
Two accepted answers. Investor standard: deduct them from net sales before gross margin, because the
shopper paid less and you funded it. Some brands and their auditors prefer to treat them as a marketing cost below CM1. Same numbers, and GM% read about six points lower one way than the other; CM3 and EBITDA were
identical. The workbook defaults to the deduction and records the choice on Start Here. Never compare your
GM% to a benchmark without knowing which treatment sits behind both numbers.

**Are my website coupon codes discounts or marketing?**
Discounts. The shopper saw a lower price. Influencer codes are still discounts; the influencer's fee is
marketing. If you cannot separate the two, the discount line is the less wrong home.

**Where do free gifts with purchase go?**
The cost of the gift is a cost, not a discount, because the shopper paid full price. Offline retailers
often bill GWPs as a scheme: put it on the testers-and-schemes line. On your own site, treat it as
sampling or as COGS if it is a regular part of the offer.

## D. COGS and gross margin

**What exactly goes into COGS?**
The landed cost of the units you sold this month: product or raw material, conversion (job-work, factory
labour, power), primary packaging (the jar, pouch, label). Not this month's purchases; purchases go to
inventory and become COGS when sold. Not shipper cartons or fillers; those are logistics. Not samples given
away; that is sampling. Not expired or damaged stock; that is write-offs.

**Why does my gross margin swing five points month to month?**
Usually one of three things. Product mix: product-level GM can range from the twenties to the fifties within one company. Channel mix: netted channels report lower GM% than billed
channels for identical products. Timing: a B2B or quick-commerce partner's sell-in is invoiced in one month
while the promo debit note lands the next. Look at channel GM% and product mix before assuming costs rose.

**My category-level GM% went negative one month. Is that possible?**
Yes, and it usually means liquidation below cost or a small-denominator effect on a low-volume line. An apparel brand discounting a seasonal category to clear more than six months of inventory will typically show negative GM on that category for a month or two. Report it, explain it, and fix the buying.

**What gross margin should I expect?**
Beauty 55–70%. Apparel 50–62%. Packaged food 30–45%, up to 50% for premium. So a food brand at 35% is healthy and a beauty brand at 45% needs a costing review.

## E. Logistics, warehousing, payment

**What belongs in logistics versus warehousing versus people?**
Logistics: anything that moves a parcel, including forward shipping, reverse shipping, RTO charges, COD
collection fees, courier surcharges, shipper cartons and fillers, and marketplace fulfilment fees like FBA.
Warehousing: storing and handling stock before it ships, including rent, warehouse staff and packing
consumables. People on the consolidated tab: everyone who is not in the warehouse or a store. Warehouse
staff scale with orders, so they are not overhead.

**Why is my logistics 20% of net sales when the courier quotes ₹80 a shipment?**
Because in a high-return business half of what you ship comes back and the returns are deducted from net
sales but the shipping is not. Apparel brands show logistics both as % of net sales and as % of GMV for
this reason; 20% of net sales can be 10% of GMV. The workbook shows the net-sales ratio on channel tabs;
compute the GMV version when you talk to investors about fashion.

**I charge shipping and COD fees to customers. Is that revenue?**
Either. The workbook's default nets it against logistics so GMV and AOV stay comparable with marketplaces,
where no such fee exists. Some MIS files book it as "COD income" above gross revenue; others net it. Both are accepted. Pick one and record it.

**Payment gateway charges: CM1 or overhead?**
CM1, because they scale with website sales. Some brands put them in overhead, which is defensible when they are tiny. At 1.8–2.2% of prepaid collections they are not tiny for a
website-led brand.

## F. Marketing and RoAS

**My Meta dashboard says RoAS 3.5 but the workbook says 2.1. Which is right?**
Both, for different questions. Platform RoAS divides attributed GMV including GST by spend, and attribution
is generous. The workbook divides net sales after GST, discounts and returns by spend, for the whole
channel. The second number is what an investor will compute. The gap between them is your discount, return
and GST leakage plus attribution optimism.

**What RoAS is sustainable?**
Depends on gross margin. A rough test: RoAS times GM% should exceed 1 for CM2 to be positive after
logistics. At 60% GM you need RoAS above roughly 2.2×; at 35% GM above roughly 3.5×. Typical early-stage blended RoAS is a little over 2× in beauty and apparel, around 3× in multi-channel CPG, and much higher in food where quick commerce and offline carry most of the volume and paid media is a small share.

**Where do influencers, agencies, photoshoots and PR go?**
Influencer fees tied to a trackable sale (codes, affiliate links): performance marketing on the channel tab.
Influencer retainers, agency fees, photoshoots, PR, brand campaigns: brand marketing on the consolidated
tab, below CM2. The point of the split is that CM2 shows whether the channel pays for itself and CM3 shows
what the brand costs on top. Do not allocate brand spend across channels by guesswork.

**Should marketing be measured against total net sales or channel net sales?**
Channel. Meta spend drives website sales, Amazon Ads drive Amazon sales. Measuring Meta against total net
sales flatters it when marketplaces are growing. The workbook computes each channel's RoAS on its own net
sales and a blended RoAS on the consolidated tab.

**What about CAC and LTV?**
Not in this workbook, deliberately: they need order-level cohort data the dashboards do not summarise.
Rough version: CAC = performance marketing ÷ new customers this month; 12-month LTV = first-order net sales
× (1 + repeat revenue as a share of first-order revenue over twelve months). An early apparel brand typically runs LTV/CAC around 2× on a 12-month LTV, with cumulative repeat adding roughly a third on top of the first order. Above
2× is the usual bar. Ask for it when you have a year of cohorts.

## G. Channel P&Ls

**How do channel tabs roll up, and what about costs that are shared?**
Every line that appears on a channel tab is summed onto the consolidated tab by formula, so the channels
always tie. Costs that are genuinely shared (warehousing, brand marketing, people) either get split by a
stated rule or stay unallocated below CM2. The workbook keeps warehousing on the channel tab so you can
split it by orders, and keeps brand and fixed costs unallocated. Investor models usually allocate shared costs by a per-channel percentage and push the residual pro-rata so channels still sum to total; that is the right approach if you want a full channel EBITDA later.

**Why does quick commerce look great at gross margin and terrible at CM3?**
Because the promo, the partner margin and the ads all land between the two. A typical pattern in food brands: quick commerce grows to half of revenue at a CM3 near zero while the website runs comfortably positive, and quick-commerce receivables of 30–45 days stretch the cash cycle from about one month toward two as the mix shifts.
Growth there is real but cash-hungry. Watch channel CM3 and receivable days together.

**Is offline worth it at my stage?**
Look at the offline tab's CM2 after store staff, testers, visibility fees and schemes. Early beauty brands commonly show a healthy offline gross margin and a deeply negative CM2 once beauty advisors and visibility are counted. Offline is a brand investment until scale; the tab makes that visible.

**Should each marketplace get its own tab?**
If it is more than about 15% of net sales or has a different commercial model, yes. Amazon (billed fee)
and a beauty marketplace on B2B terms (netted margin) should never share a tab. Two small marketplaces on
the same terms can. Ask the skill to add a tab when one grows.

## H. Fixed costs and EBITDA

**Do I include my own salary if I do not pay myself?**
Yes, at what you would pay a replacement. Investors normalise for it anyway, and an EBITDA that improves
only because founders are unpaid is not a trend.

**Store staff and warehouse staff: salaries or not?**
Warehouse staff: warehousing, on the channel tab, because they scale with orders. Store staff or beauty
advisors: the offline channel's selling line by default, because they scale with doors. Everyone else:
people, on the consolidated tab. The rule is to put a cost where the decision that drives it is made.

**What counts as a one-time cost?**
Something that will not recur in the next twelve months: fund-raise costs, a legal settlement, an office
move. Not a bad marketing month, not a stock write-off (those recur), not annual fees. The workbook shows
operating EBITDA before one-offs and reported EBITDA after, so that both numbers are visible and neither hides the other.

**Where does interest earned on the money we raised go?**
Below EBITDA, netted against interest paid. Putting it above EBITDA flatters operating performance; even when it is netted into PBT correctly, investors ask for it to be shown separately.

**What EBITDA is normal at my stage?**
Negative. Early-stage brands commonly range from single-digit negative to around −50% of net sales while growing. What
investors look for is the trajectory: CM2 turning positive, then CM3, with fixed costs growing slower than
net sales. The workbook's fixed-costs-as-%-of-net-sales line is the one to watch.

## I. Working capital and cash

**Why does my P&L say I lost 5 lakh but my bank went down 15?**
Because you bought inventory, your marketplace has not paid you yet, and you paid suppliers. That is the
change in working capital, and the Cash tab shows it. Growth usually eats cash before it shows profit.
A brand can go from positive to negative net working capital in a year by stretching payables past four months while inventory sits at three to four months; supplier-funded growth works until a supplier says no.

**What are inventory days, receivable days, payable days, and what is normal?**
Inventory days = inventory ÷ monthly COGS × 30: how long stock sits. Receivable days = receivables ÷ monthly
net sales × 30: how long you wait to be paid. Payable days = payables ÷ monthly COGS × 30: how long you take
to pay. Cash conversion cycle = inventory days + receivable days − payable days. Typical receivables by channel: website 2–5 days, Amazon 7–14, quick commerce 30–45, offline 45–60, B2B marketplaces
30–60. Inventory: food 30–60, beauty 60–120, apparel 90–200 and ageing matters more than the level.

**What is runway and which burn should I use?**
Operating burn is the cash the business consumed before equity and debt came in. Runway is closing cash
divided by average operating burn over the last three months. Net burn including financing is what your bank
statement shows and is not the number to plan on.

**How do I know the cash tab is right?**
Closing cash on the tab should equal your bank balance on the last day of the month. If it does not, a
number above is misclassified or missing; the "other cash movements" line exists so you can make it tie
while you find out, not so you can leave it there.

## J. What investors actually ask

The questions investors most often put to early D2C brands after reading an MIS:

1. Show me gross margin by product category, not just blended. Which lines are dragging it?
2. Split returns by channel and by type. What changed the month logistics jumped?
3. Show discounts as a percentage of gross, by channel, month by month.
4. Why did gross margin drop a point in the last two months?
5. Break down the fixed-cost block. Fifteen percent of revenue with no detail is a red flag.
6. What is the inventory ageing? How much stock is over 180 days and what is it worth at cost?
7. Where is the cash going: EBITDA, working capital or capex?
8. What is repeat behaviour by cohort, and is early repeat real or a return-and-reorder artefact?
9. Does the MIS tie to the books? Where are the differences and why?

Founders who can answer these from their MIS before the meeting are treated differently in the meeting.

**What makes an MIS "investor grade"?**
Five things, in order. It ties: channels sum to total, opening cash equals last month's closing, subtotals
are formulas not typed numbers. Definitions are consistent and written down. Ratios state their base.
Placement decisions are recorded, not implied. It reconciles to the bank at month end and, quarterly, to
the books. Polish and forty line items are not on the list.

**Mistakes that commonly appear in MIS files, so you can avoid them**
A month's GST copied from the previous month. A hard-coded net revenue that did not equal gross less
deductions. Broken cross-sheet references showing errors for six months. A placeholder warehousing cost
repeated for fifteen months. Two different figures for the same month in two tabs. A ratio labelled "ROAS"
that was actually spend divided by sales. None of these is a business problem; all of them cost credibility.

## K. Starter questions to offer after generating a workbook

Pick four or five that match the founder's archetype and channels. Offer them as "things I can help you
think through", not as homework. The same list lives in `scripts/mis_spec.py` as `STARTER_QUESTIONS` and is
printed on the Start Here tab.

Everyone
- Which margin should I quote when an investor asks "what are your margins?"
- My ad platform's RoAS and this sheet's RoAS don't match. Which one is right?
- What goes in COGS this month if I bought stock for the next three months?
- Why does the P&L show a loss but the bank balance dropped much more?
- What would an investor ask me from these numbers?

Beauty & personal care
- Should Nykaa be a revenue deduction or a cost, and why does it change my gross margin?
- Where do beauty advisors, testers and visibility fees go, and is offline paying for itself?
- Where do influencer codes, influencer retainers and shoots each go?

Food & beverage / nutrition
- Where do the promos I fund on Blinkit go, and why does GM% move when I change my mind?
- Why does quick commerce look profitable at gross margin and not at CM3?
- Where do expiry write-offs go, and how do I keep them out of COGS?

Apparel & accessories
- RTO, returns, exchanges: which is which, and am I double-counting exchange shipping?
- Is a 45% return rate normal, and which part of it can I actually reduce?
- Should I look at logistics as % of net sales or % of GMV?

Website-led
- What return rate and RoAS should I expect on COD-heavy orders?
- Shipping fees I charge customers: revenue or a reduction in logistics?

Marketplace-led
- Amazon referral fee, FBA fee, storage fee, closing fee: which line does each go to?
- Should Myntra and Ajio share a tab?

Offline
- How do I value sell-in to distributors when I only know my invoice price?
- Why is my offline gross margin high and CM2 negative?
