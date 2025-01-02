---
title: Low-inventory-level fee
url: https://sellercentral.amazon.com/help/hub/reference/GV43F6S76Y9DHYRH
section: General Documentation
---

Starting May 15, the low-inventory-level fee will not apply to products that
have sold less than 20 units in the past 7 days.

**Note:** For an overview of all 2024 US selling fee changes, go to
[amazon.com/selling-fee-changes](https://amazon.com/selling-fee-changes).

Effective April 1, 2024, a low-inventory-level fee will apply to standard-size
products with consistently low inventory relative to customer demand. When
sellers carry low inventory relative to unit sales, it inhibits our ability to
distribute products across our network, degrading delivery speed and
increasing our shipping costs.

A low-inventory-level fee will only apply if a product’s inventory level
relative to historical demand (known as "historical days of supply") is below
28 days. We will only charge a low-inventory-level fee when both the long-term
historical days of supply (last 90 days) and short-term historical days of
supply (last 30 days) are below 28 days (4 weeks). For example, if a product’s
short-term historical days of supply is above 28 days but long-term historical
days of supply is below 28 days, the low-inventory-level fee won’t apply.

For each seller, we will calculate the historical days of supply metric at the
parent-product level, and we will add the low-inventory-level fee to the FBA
fulfillment fee for all shipped units of eligible products. Note that some
products are not eligible for the low-inventory-level fee. For more
information on fee eligibility, review the FAQ below.

## Fee details

Time of charge | The time when the customer’s order is shipped.  
---|---  
Fee structure | Per unit fulfilled. Rate is based on size tier, shipping weight, and historical days of supply.  
  
## Rates

April 1, 2024 and after  
---  
2024 size tier | Shipping weight | Low-inventory-level fee  
0 ≤ historical days of supply < 14  | 14 ≤ historical days of supply < 21 | 21 ≤ historical days of supply < 28  
Small standard | Up to 16 oz | $0.89 | $0.63 | $0.32  
Large standard | Up to 3 lb | $0.97 | $0.70 | $0.36  
Large standard | 3+ lb to 20 lb | $1.11 | $0.87 | $0.47  
  
To determine fees, first determine a product’s size tier and then its shipping
weight. For small standard products, the shipping weight for calculating fees
is based on unit weight. For large standard products, the shipping weight is
the greater of unit or dimensional weight. For detailed definitions of each
size tier, go to [product size tiers](/help/hub/reference/GG5KW835AHDJCH8W).

## Tools

**Historical days of supply metric** | [FBA Inventory](/inventoryplanning/manageinventoryhealth) (view the **Low-inventory-level fee** column)  
---|---  
**Estimating fees** |  [Revenue Calculator](/fba/revenuecalculator/index) [FBA Inventory](/inventoryplanning/manageinventoryhealth) (view the **Estimated fee per unit sold** column)  
**Reporting fees** |  [Payments - Transaction View](https://sellercentral.amazon.com/payments/event/view) [SKU Economics report](/sereport)  
  
## Frequently asked questions

#### How can I view my historical days of supply metric to determine if I have
products that are subject to this fee?

To view your historical days of supply, go to [FBA
Inventory](/inventoryplanning/manageinventoryhealth). Monitor your historical
days of supply regularly to identify products that may incur the low-
inventory-level fee.

The historical days of supply metric is calculated at the parent-product
level, so all child products related to the same parent product will have the
same historical days of supply.

####  Which products are subject to the low-inventory-level fee?

The low-inventory-level fee only applies to standard-sized products if the
historical days of supply is less than 28 days.

The low-inventory-level fee won’t apply to the following:

  * New Professional sellers, for the first 365 days after the first inventory-received date.
  * New-to-FBA parent products for the first 180 days after the first inventory-received date. You must be enrolled in FBA New Selection to get this benefit. For more information, including seller and product eligibility, go to [FBA New Selection program](/help/hub/reference/GWHQRT98SAZC29VQ).
  * SKUs for which 70% or more of the inventory was auto-replenished through Amazon Warehousing and Distribution over the prior 90 days, because this program has managed that product’s replenishment into FBA on your behalf.
  * Products that have sold less than 20 units in the past 7 days.

#### How can I check if I have been charged low-inventory-level fee on an ASIN
or on an order?

To determine the low-inventory-level fee is charged on an ASIN:  

  1. Go to [SKU Economics report page](https://sellercentral.amazon.com/sereport)
  2. Follow the steps on the SKU Economics report page to select the Amazon Store, Data aggregation level, Date range, and data types you would like to include in your report.
  3. Refer to low-inventory-level fee column to see how much the fee has been charged for each ASIN.

To determine if the low-inventory-level fee is charged on an order:

a. Go to Seller Central Payments > Payments > Transaction View.

b. Input the order ID in the Find a transaction field and click Search.

c. Click **quicklink** in Total and enter the Transaction Details page.

d. Click **fees quicklink** in FBA Pick & Pack Fee and go to **Fee explainer -
FBA fulfillment fee** (Calculation Tab) to confirm that the low-inventory-
level fee has been charged.

#### How will the low-inventory-level fee be assessed?

The low-inventory-level fee only applies to a product when both its long-term
(the last 90 days) and short-term (the last 30 days) historical days of supply
are below 28 days. We will use the greater of the long- and short-term
historical days to determine the fee tier.

Below are examples of how the low-inventory-level fee will be assessed.

Example 1: This product incurs the low-inventory-level fee because both long-
term and short-term historical days of supply are below 28 days.

Sample product |  Size tier: Large standard Shipping weight: 4+ to 8 oz  
---|---  
Historical days of supply |  Historical days of supply: 24 (greater of below) _Long-term historical days of supply: 18_ _Short-term historical days of supply: 24_  
Total fulfillment fees |  Standard FBA fulfillment fee: $4.08 per unit (standard rate for the size tier and shipping weight) Low-inventory-level fee: $0.36 per units (rate for 21-28 historical days of supply) Total new FBA fulfillment fees: $4.08 per unit + $0.36 per unit = $4.44 per unit  
  
Example 2: This product does not incur the low-inventory-level fee because
long-term historical days of supply is at or above 28 days, while short-term
historical days of supply is below 28 days.

Sample product |  Size tier: Small standard Shipping weight: 6+ to 8 oz  
---|---  
Historical days of supply |  Historical days of supply: 40 (greater of below) _Long-term historical days of supply: 40_ _Short-term historical days of supply: 20_  
Total fulfillment fees |  Standard FBA fulfillment fee: $3.49 per unit (standard rate for the size tier and shipping weight) Low-inventory-level fee: $0.00 (no fee because historical days of supply is at or above 28) Total new FBA fulfillment fees: $3.49 per unit + $0.00 per unit = $3.49 per unit  
  
Example 3: This product does not incur the low-inventory-level fee because
short-term historical days of supply is at or above 28 days, while long-term
historical days of supply is below 28 days.

Sample product |  Size tier: Large standard Shipping weight: 2+ to 2.25 lb  
---|---  
Historical days of supply |  Historical days of supply: 35 (greater of below) _Long-term historical days of supply: 12_ _Short-term historical days of supply: 35_  
Total fulfillment fees |  Standard FBA fulfillment fee: $6.10 per unit (standard rate for the size tier and shipping weight) Low-inventory-level fee: $0.00 (no fee because historical days of supply is at or above 28) Total new FBA fulfillment fees: $6.10 per unit + $0.00 per unit = $6.10 per unit  
  
#### What metric is used as the basis for the low-inventory-level fee?

We will use a metric called historical days of supply, which is calculated
based on average daily inventory units on hand divided by average daily
shipped units, over both the long term (last 90 days) and short term (last 30
days). The following are the definitions for the metric components:

  * **Average daily inventory units** is sellable FBA inventory units in our US fulfillment network only. It is calculated by adding up inventory units available for sales, units that are being transferred between fulfillment centers, and units in fulfillment center processing. It does not include unsellable units, such as units that are pending removal, disposal, or liquidation, as well as units that are currently being inbounded to the Amazon fulfillment network.
  * **Average daily shipped units** is all units that are shipped from our US fulfillment network, including through FBA, Multi-Channel Fulfillment, Remote Fulfillment with FBA, and any other program that ships units from our US fulfillment network.

The formulas and examples below provide details on how we calculate historical
days of supply. Note that the average daily inventory units and shipped units
can be decimal, as your inventory levels and shipped units may change daily.

| Formula | Example  
---|---|---  
**Long-term historical days of supply (past 90 days)** |  Over past 90 days: (Average daily inventory units / average daily shipped units) |  Average daily inventory units: 243.6 units Average daily shipped units: 5.8 units Long-term historical days of supply = (243.6 units/ 5.8 units) Long-term historical days of supply = **42.0**  
**Short-term historical days of supply (past 30 days)** |  Over past 30 days: (Average daily inventory units / average daily shipped units) |  Average daily inventory units: 220.5 units Average daily shipped units: 12.6 units Short-term historical days of supply = (220.5 units/ 12.6 units)  Short-term historical days of supply = **17.5**  
  
On the [FBA Inventory](/inventoryplanning/manageinventoryhealth) page, we will
show one historical days of supply metric, which represents the greater of
long-term and short-term historical days of supply, and which we will use to
determine the low-inventory-level fee tier. We will also show details of long-
term and short-term historical days of supply on the page for your reference.
In the example above, the historical days of supply will be 42.0, which is the
greater of long-term historical days of supply (42.0) and short-term
historical days of supply (17.5).

For each seller, the historical days of supply metric is calculated at the
parent-product level, so all child products related to the same parent product
will have the same historical days of supply. The historical days of supply is
a seller-specific metric, which means that we only consider the seller’s
inventory units and shipped units in the metric calculation. The metric will
be updated weekly, and the latest available historical days of supply will
determine the fee rate for units shipped that week.

####  How will the low-inventory-level-fee affect different product types (for
example, seasonal products)?

Different products with different sales volume may be affected differently by
the fee. However, you can minimize or avoid the fee by sending in additional
units such that the product’s short-term (last 30 days) historical days of
supply exceeds 28 days, or by managing your product’s long-term (last 90 days)
historical days of supply.

See below examples of how specific product types may be affected by the low-
inventory-level fee.

**1\. Standard products**

Below is an example of a car accessory with sales that range from 25 to 30
units per day. This product does not incur the low-inventory-level fee as the
product’s historical days of supply is consistently above 28 days. In this
case, the seller opts to maintain 45 to 55 historical days of supply (or ~6 to
8 weeks of supply) to avoid the fee.

Week | Inventory units | Weekly sales units |  | Trailing 90 days |  | Trailing 30 days |  | Historical days of supply (greater of trailing 30 and 90 days) | Is historical days of supply below 28?  
---|---|---|---|---|---|---|---|---|---  
Average daily inventory units | Average daily shipped units | Historical days of supply (trailing 90 days) | Average daily inventory units | Average daily shipped units | Historical days of supply (trailing 30 days)  
(a) | (b) | (c)  | (d) | (e)  | (f = d/e) | (g) | (h) | (i = g/h) | (j) | (k)  
3/4 | 1,311  | 144 |  | 1007.2 | 28.1 | 35.8 |  | 1379.7 | 25.6 | 53.8 |  | 53.8 | No  
3/11 | 1,457  | 214 | 1052.9 | 29.4 | 35.8 | 1379.3 | 25.9 | 53.2 | 53.2 | No  
3/18 | 1,479  | 207 | 1099.9 | 29.8 | 36.9 | 1413.3 | 26.5 | 53.3 | 53.3 | No  
3/25 | 1,336  | 201 | 1149.9 | 29.0 | 39.7 | 1395.8 | 27.4 | 51.0 | 51.0 | No  
4/1 | 1,371  | 204 | 1205.9 | 28.5 | 42.3 | 1410.8 | 29.5 | 47.8 | 47.8 | No  
4/8 | 1,236 | 202 | 1261.6 | 28.5 | 44.2 | 1355.5 | 29.1 | 46.6 | 46.6 | No  
4/15 | 1,105 | 199 | 1299.4 | 28.4 | 45.7 | 1262.0 | 28.8 | 43.8 | 45.7 | No  
4/22 | 1,148  | 204 | 1312.9 | 28.2 | 46.5 | 1215.0 | 28.9 | 42.1 | 46.5 | No  
4/29 | 1,081  | 227 | 1298.8 | 28.4 | 45.7 | 1142.7 | 29.7 | 38.5 | 45.7 | No  
5/6 | 966  | 197 | 1284.5 | 28.3 | 45.4 | 1075.2 | 29.5 | 36.4 | 45.4 | No  
5/13 | 1,400  | 162 | 1280.0 | 27.8 | 46.1 | 1148.8 | 28.2 | 40.7 | 46.1 | No  
5/20 | 1,293  | 162 | 1276.1 | 27.5 | 46.5 | 1185.0 | 26.7 | 44.4 | 46.5 | No  
5/27 | 1,181  | 173 | 1258.8 | 27.4 | 45.9 | 1210.0 | 24.8 | 48.8 | 48.8 | No  
  
**2\. Seasonal products**

Below is an example of a winter boot where sales are highest in December and
January before tapering off in February and March. The product's historical
days of supply is above 28 days before and during the holiday season months
when considering the product's trailing 90 days performance. In mid-February,
the product’s historical days of supply falls below 28 days given low
inventory levels, but sales also dropped significantly (below 20 units per
week). In this case, the seller sells 730 units annually, with 19 units
incurring the low-inventory-level fee (or 2.6% of units sold) for a total
estimated fee of $8.93 (or $0.01 per annual unit sold).

Week | Inventory units | Weekly sales units |  | Trailing 90 days |  | Trailing 30 days |  | Historical days of supply (greater of trailing 30 and 90 days) | Is historical days of supply below 28?  
---|---|---|---|---|---|---|---|---|---  
Average daily inventory units | Average daily shipped units | Historical days of supply (trailing 90 days) | Average daily inventory units | Average daily shipped units | Historical days of supply (trailing 30 days)  
(a) | (b) | (c)  | (d) | (e)  | (f = d/e) | (g) | (h) | (i = g/h) | (j) | (k)  
11/5 | 322 | 5 |  | 83.2 | 0.9 | 94.7 |  | 228.3 | 1.5 | 148.6 |  | 148.6 | No  
11/12 | 457 | 13 | 118.4 | 1.0 | 115.8 | 304.5 | 1.4 | 218.6 | 218.6 | No  
11/19 | 440 | 28 | 152.2 | 1.3 | 114.5 | 377.0 | 2.1 | 178.9 | 178.9 | No  
11/26 | 432 | 42 | 185.5 | 1.8 | 103.5 | 412.8 | 3.1 | 131.3 | 131.3 | No  
12/3 | 430 | 32 | 218.5 | 2.1 | 102.0 | 439.8 | 4.1 | 107.1 | 107.1 | No  
12/10 | 348 | 88 | 245.3 | 3.1 | 78.9 | 412.5 | 6.8 | 60.8 | 78.9 | No  
12/17 | 173 | 189 | 257.0 | 5.1 | 50.0 | 345.8 | 12.5 | 27.6 | 50.0 | No  
12/24 | 133 | 55 | 264.5 | 5.6 | 46.8 | 271.0 | 13.0 | 20.8 | 46.8 | No  
12/31 | 139 | 7 | 273.4 | 5.5 | 49.3 | 198.3 | 12.1 | 16.4 | 49.3 | No  
1/7 | 142 | 5 | 277.5 | 5.5 | 50.3 | 146.8 | 9.1 | 16.1 | 50.3 | No  
1/14 | 142 | 11 | 276.7 | 5.5 | 50.8 | 139.0 | 2.8 | 49.9 | 50.8 | No  
1/21 | 112 | 37 | 273.8 | 5.8 | 47.5 | 133.8 | 2.1 | 62.4 | 62.4 | No  
1/28 | 70 | 44 | 256.9 | 6.1 | 42.1 | 116.5 | 3.5 | 33.6 | 42.1 | No  
2/4 | 45 | 27 | 235.6 | 6.4 | 37.1 | 92.3 | 4.3 | 21.7 | 37.1 | No  
2/11 | 32 | 20 | 202.9 | 6.4 | 31.6 | 64.8 | 4.6 | 14.2 | 31.6 | No  
2/18 | 16 | 19 | 170.3 | 6.3 | 26.9 | 40.8 | 3.9 | 10.4 | **26.9** | **Yes**  
2/25 | 12 | 8 | 138.0 | 6.0 | 23.2 | 26.3 | 2.6 | 9.9 | 23.2 | No  
3/4 | 8 | 6 | 105.5 | 5.7 | 18.6 | 17.0 | 1.9 | 9.0 | 18.6 | No  
3/11 | 3 | 7 | 79.0 | 4.8 | 16.5 | 9.8 | 1.4 | 6.8 | 16.5 | No  
3/18 | 2 | 3 | 65.8 | 2.7 | 24.1 | 6.3 | 0.9 | 7.3 | 24.1 | No  
3/25 | 1 | 0 | 55.7 | 2.1 | 26.1 | 3.5 | 0.6 | 6.1 | 26.1 | No  
4/1 | 1 | 1 | 45.1 | 2.1 | 21.8 | 1.8 | 0.4 | 4.5 | 21.8 | No  
4/8 | 1 | 0 | 34.2 | 2.0 | 17.0 | 1.3 | 0.1 | 8.8 | 17.0 | No  
4/15 | 1 | 0 | 23.4 | 1.9 | 12.4 | 1.0 | 0.0 | 28.0 | 28.0 | No  
  
**3\. Products with promotions**

Below is an example of an electronic product with a Prime Day deal. Although
sales are higher during Prime Day, the seller does not incur the low-
inventory-level fee because the historical days of supply is above 28 days
given the trailing 90 days performance of the product. The trailing 90-day
metric ensures that the seller does not incur the low-inventory-level fees
based on sudden increases in demand. The metric accounts for a seller’s long-
term inventory performance.

Week | Inventory units | Weekly sales units |  | Trailing 90 days |  | Trailing 30 days |  | Historical days of supply (greater of trailing 30 and 90 days) | Is historical days of supply below 28?  
---|---|---|---|---|---|---|---|---|---  
Average daily inventory units | Average daily shipped units | Historical days of supply (trailing 90 days) | Average daily inventory units | Average daily shipped units | Historical days of supply (trailing 30 days)  
(a) | (b) | (c)  | (d) | (e)  | (f = d/e) | (g) | (h) | (i = g/h) | (j) | (k)  
6/3 | 460 | 44 |  | 405.8 | 7.1 | 57.4 |  | 488.0 | 9.7 | 50.5 |  | 57.4 | No  
6/10 | 351 | 110 | 406.4 | 8.1 | 50.3 | 457.6 | 11.4 | 40.2 | 50.3 | No  
6/17 | 318 | 37 | 406.6 | 8.2 | 49.3 | 399.8 | 10.0 | 39.8 | 49.3 | No  
6/24 | 280 | 101 | 389.9 | 9.1 | 43.1 | 352.1 | 10.4 | 33.7 | 43.1 | No  
7/1 | 352 | 50 | 387.7 | 8.3 | 47.0 | 325.2 | 10.7 | 30.5 | 47.0 | No  
7/8 | 393 | 54 | 390.9 | 8.5 | 45.9 | 335.5 | 8.7 | 38.8 | 45.9 | No  
**7/15** | **223** | **363** | **383.1** | **12.2** | **31.4** | **311.9** | **20.3** | **15.4** | **31.4** | **No**  
7/22 | 170 | 57 | 374.9 | 12.3 | 30.5 | 284.5 | 18.7 | 15.2 | 30.5 | No  
7/29 | 219 | 38 | 367.9 | 12.2 | 30.1 | 251.1 | 18.3 | 13.7 | 30.1 | No  
8/5 | 244 | 41 | 346.2 | 12.3 | 28.1 | 213.9 | 17.8 | 12.0 | 28.1 | No  
8/12 | 205 | 40 | 316.4 | 12.1 | 26.2 | 209.4 | 6.3 | 33.3 | 33.3 | No  
8/19 | 221 | 33 | 300.4 | 11.6 | 25.8 | 222.2 | 5.4 | 41.0 | 41.0 | No  
8/26 | 200 | 31 | 279.6 | 11.0 | 25.5 | 217.4 | 5.2 | 42.0 | 42.0 | No  
  
**4\. Products with low sales volume**

Below is an example of a book with sales that range from 0 to 3 units per
week. This seller does not incur the low-inventory-level fee because the
product’s sales are consistently below 20 units per week.

Week | Inventory units | Weekly sales units |  | Trailing 90 days |  | Trailing 30 days |  | Historical days of supply (greater of trailing 30 and 90 days) | Is historical days of supply below 28?  
---|---|---|---|---|---|---|---|---|---  
Average daily inventory units | Average daily shipped units | Historical days of supply (trailing 90 days) | Average daily inventory units | Average daily shipped units | Historical days of supply (trailing 30 days)  
(a) | (b) | (c)  | (d) | (e)  | (f = d/e) | (g) | (h) | (i = g/h) | (j) | (k)  
4/29 | 4 | 0 |  | 2.62 | 0.04 | 59.5 |  | 4.00 | 0.00 | \-- |  | \-- | No  
5/6 | 4 | 0 | 2.69 | 0.04 | 61.3 | 4.00 | 0.00 | \-- | \-- | No  
5/13 | 4 | 0 | 2.85 | 0.03 | 86.3 | 4.00 | 0.00 | \-- | \-- | No  
5/20 | 4 | 0 | 3.00 | 0.03 | 91.0 | 4.00 | 0.00 | \-- | \-- | No  
5/27 | 3 | 1 | 3.08 | 0.04 | 70.0 | 3.75 | 0.04 | 105.0 | 105.0 | No  
6/3 | 3 | 0 | 3.31 | 0.02 | 150.5 | 3.50 | 0.04 | 98.0 | 150.5 | No  
6/10 | 3 | 0 | 3.31 | 0.02 | 150.5 | 3.25 | 0.04 | 91.0 | 150.5 | No  
6/17 | 0 | 3 | 3.15 | 0.04 | 71.8 | 2.25 | 0.14 | 15.8 | 71.8 | No  
6/24 | 3 | 0 | 3.23 | 0.04 | 73.5 | 2.25 | 0.11 | 21.0 | 73.5 | No  
7/1 | 3 | 0 | 3.31 | 0.04 | 75.3 | 2.25 | 0.11 | 21.0 | 75.3 | No  
7/8 | 1 | 2 | 3.23 | 0.07 | 49.0 | 1.75 | 0.18 | 9.8 | 49.0 | No  
7/15 | 0 | 1 | 2.85 | 0.08 | 37.0 | 1.75 | 0.11 | 16.3 | 37.0 | No  
7/22 | 3 | 0 | 2.69 | 0.08 | 35.0 | 1.75 | 0.11 | 16.3 | 35.0 | No  
  
#### What happens when my product has no sales for the past 30 or 90 days?

If your product has had no sales in the past 30 or 90 days (that is, your
average daily shipped units is 0), then your historical days of supply will be
above 28 days, and the product will not be charged the low-inventory-level
fee. On [FBA Inventory](/inventoryplanning/manageinventoryhealth?), the
historical days of supply metric will be displayed with the symbol “--.”

#### Why does the greater of short-term and long-term historical days of
supply determine the low-inventory-level fee?

Using the greater of historical days of supply to determine the fee considers
a product’s long-term inventory performance. These metrics can help you
minimize the fee by making improvements to a product’s inventory levels. As a
result, the fee will only apply to products with a consistently low level of
inventory.

#### Why is the historical days of supply metric calculated on the parent-
product level?

Some variations of a product have uncertain demand, making it difficult for
you to optimize your inventory. By calculating the metric on the parent-
product level, we only charge the low-inventory-level fee when most child
products under the parent product have consistently low inventory.

#### Is seller-fulfilled inventory considered in calculating historical days
of supply and determining the low-inventory-level fee eligibility?

No. The historical days of supply metric only considers FBA inventory stored
in the Amazon fulfillment network.

#### How is the low-inventory-level fee affected by inbound delay?

For normal receive and processing time, you’re less likely to incur the low-
inventory-level fee as the fee considers long-term (past 90 days) inventory
performance. For excessive inbound delays caused by Amazon or Amazon-managed
services, such as the Amazon Partnered Carrier program and Amazon Global
Logistics, Amazon will automatically reimburse you if the low-inventory-level
fees are charged.

To qualify for the reimbursement, you must prepare your shipments for on-time
pickup for Amazon-managed transportation services, and provide accurate
shipment tracking information for non-Amazon managed transportation services.
The reimbursement will occur by the 15th of the following month from when the
fee was incurred. For example, May charges with excessive inbound delays will
be credited back by June 30th.

To check if you received a reimbursement for an order, follow the below steps:

a. Go to Seller Central Payments > **Payments** > **Transaction View**.

b. Input the order ID in the **Find a transaction** field and click
**Search.**

#### How can I minimize or avoid the low-inventory-level fee?

For products where inventory is manually replenished by sellers, you will have
the opportunity to minimize or avoid the low-inventory-level fee by making
improvements in inventory levels. You can do so by sending in additional units
such that the product’s short-term (last 30 days) historical days of supply
exceeds 28 days. Otherwise, you can also avoid the fee by managing your
product’s long-term (last 90 days) historical days of supply. Go to [FBA
Inventory](/inventoryplanning/manageinventoryhealth) to identify products with
low inventory and recommended number of units to send to Amazon.

Alternatively, you may enroll your products in auto-replenishment by Amazon
Warehousing and Distribution. With this auto-replenishment service, Amazon
Warehousing and Distribution manages inventory replenishment into FBA on your
behalf. Therefore, the low-inventory-level fee does not apply at a SKU level
when you auto-replenish 70% or more of that SKU to FBA through Amazon
Warehousing and Distribution over the prior 90 days.

#### How do the FBA Minimum Inventory Level metric, historical days of supply,
and the low-inventory-level fee relate to each other?

Minimum Inventory Level is a forward-looking metric measured in units, that
helps you to plan your future FBA inventory replenishment. We leverage
Amazon’s inventory management and machine learning models to tailor Minimum
Inventory Levels to each product, considering factors like demand forecast and
replenishment settings. Keeping your inventory above this minimum level helps
increase delivery speed and reduces your risk of low-inventory-fee. Go to [FBA
inventory overview](/gp/help/GTMXYZN64UJL7TT6) to learn more

Historical days of supply is a backward-looking metric measured in days. It is
used as the basis for low-inventory-level fee. Products with low historical
days of supply metric have consistently low inventory levels in the past, and
will be subject to the fee.

#### What if I have a capacity limit that prevents me from inbounding products
with low inventory?

Efficient inventory management requires balancing how much inventory you are
holding; not too much (excess) or too little (low or out of stock). If you
have a capacity limit that prevents you from inbounding products with low
inventory, we recommend that you reduce excess inventory by improving [sell-
through rate](/gp/help/GZJF4DY2W6MERBAL#wjz_cjc_jcb-12), requesting a
[liquidation order](/gp/help/GYVCG5Q3BEJ6MLMF), or requesting a return or
disposal order through a [removal order](/gp/help/G200280650).  Go to [FBA
inventory](/inventoryplanning/manageinventoryhealth?) to identify products
with excess inventory.

