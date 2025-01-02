---
title: FBA Inventory report
url: https://sellercentral.amazon.com/help/hub/reference/GKT9YKCHXMSDVJKB
section: General Documentation
---

The FBA Inventory page and report enables you to manage your restock, excess,
aged and unfulfillable inventory and maintain healthy inventory levels from a
single location. Additionally, they allow you to assess fees, monitor critical
factors such as your ASIN sales performance, optimize pricing, and maintain
healthy IPI score by utilizing your capacity at Amazon's fulfillment centers
more efficiently. Below is a list of metrics included in the FBA Inventory
report to help you plan your inventory.  
  
  * Seven-day, 30-day, 60-day, and 90-day sales and units shipped
  * Your list prices
  * Shipment quantities: working, shipped, and receiving

Field name | Description | Example  
---|---|---  
snapshot-date | The date the report was generated | 2011-06-26T07:00:00+00:00  
sku | Unique blocks of letters and numbers that you assign to the products that you are selling | MSKU-12345-prod1  
fnsku | Unique blocks of letters and numbers that Amazon assigns to products that are stored in and fulfilled from an Amazon fulfillment center | X003459202  
asin | Unique blocks of 10 letters or numbers that Amazon assigns to the products that are sold through Amazon | B0159KFV53  
product-name | The name of your product | ACME Gifts for Girls  
condition | The condition of the unit (for example, new or used) | New  
available | Available (sellable inventory) quantity | 24  
pending-removal-quantity | The number of units that you have asked to be returned to you or disposed of | 14  
inventory-age-0-to-90-days | The number of sellable units that have been in the fulfillment center for the last 0-90 days | 0  
inventory-age-91-to-180-days | The number of sellable units that have been in the fulfillment center for the last 91-180 days | 10  
inventory-age-181-to-270-days | The number of sellable units that have been in the fulfillment center for the last 181-270 days | 6  
inventory-age-271-to-365-days | The number of sellable units that have been in the fulfillment center for the last 271-365 days | 96  
inventory-age-365-plus-days | The number of sellable units that have been in the fulfillment center for the last 365+ days | 123  
currency | The currency for the estimated aged inventory surcharge | USD  
quantity-to-be-charged-ais-181-210-days | The number of available units that will have been in the fulfillment center for 181 to 210 days and would be subject to the 181-day aged inventory surcharge as of the next charge date. | 10  
estimated-ais-181-210-days | The estimated aged inventory surcharge amount for units that have been in fulfillment centers for 181 to 210 days on the next charge date. | 0.15  
quantity-to-be-charged-ais-211-240-days | The number of available units that will have been in the fulfillment center for 211 to 240 days and would be subject to the 211-day aged inventory surcharge as of the next charge date. | 10  
estimated-ais-211-240-days | The estimated aged inventory surcharge amount for units that have been in fulfillment centers for 211 to 240 days on the next charge date. | 0.3  
quantity-to-be-charged-ais-241-270-days | The number of available units that will have been in the fulfillment center for 241 to 270 days and would be subject to the 241-day aged inventory surcharge as of the next charge date. | 10  
estimated-ais-241-270-days | The estimated aged inventory surcharge amount for units that have been in fulfillment centers for 241 to 270 days on the next charge date. | 0.45  
quantity-to-be-charged-ais-271-300-days | The number of available units that will have been in the fulfillment center for 271 to 300 days and would be subject to the 271-day aged inventory surcharge as of the next charge date. | 10  
estimated-ais-271-300-days | The estimated aged inventory surcharge amount for units that have been in fulfillment centers for 271 to 300 days on the next charge date. | 1.14  
quantity-to-be-charged-ais-301-330-days | The number of available units that will have been in the fulfillment center for 301 to 330 days and would be subject to the 301-day aged inventory surcharge as of the next charge date. | 10  
estimated-ais-301-330-days | The estimated aged inventory surcharge amount for units that have been in fulfillment centers for 301 to 330 days on the next charge date. | 1.2  
quantity-to-be-charged-ais-331-365-days | The number of available units that will have been in the fulfillment center for 331 to 365 days and would be subject to the 331-day aged inventory surcharge as of the next charge date. | 10  
estimated-ais-331-365-days | The estimated aged inventory surcharge amount for units that have been in fulfillment centers for 331 to 365 days on the next charge date. | 1.26  
quantity-to-be-charged-ais-365-plus-days | The number of available units that will have been in the fulfillment center for 365+ days and would be subject to the 365-day aged inventory surcharge as of the next charge date. | 10  
estimated-ais-365-plus-days | The estimated aged inventory surcharge amount for units that have been in fulfillment centers for 365+ days on the next charge date. | 2.07  
units-shipped-t7 | Units shipped in the last 7 days | 12  
units-shipped-t30 | Units shipped in the last 30 days | 15  
units-shipped-t60 | Units shipped in the last 60 days | 67  
units-shipped-t90 | Units shipped in the last 90 days | 156  
alert |  This is displayed when an item has a low-traffic or low-conversion alert.

  * **Low traffic** indicates that a low number of potential buyers have seen the listing.
  * **Low conversion** indicates that potential buyers are viewing the listing but aren’t following through to buy the product. 

| Low traffic  
your-price | Your listed price | 34.99  
sales_price | Your sales price if you are running a sale on the product | 19.99  
lowest_price_new  | The lowest price (including shipping) for this item in new condition on Amazon | 19.99  
lowest_price_used | The lowest price (including shipping) for this item in used condition on Amazon | 15.99  
recommended-action | The action recommended for your inventory. Recommendations are based on your current customer demand and on whether it would cost you less to take an action than to do nothing.  | Create Outlet deal  
healthy-inventory-level | See “fba-minimum-inventory-level” and “fba-inventory-level-health-status” for inventory level recommendations. |   
fba-minimum-inventory-level | The minimum amount of FBA sellable inventory units that we recommend you maintain within the Amazon fulfillment network before your next incoming shipment arrives. | 100  
fba-inventory-level-health-status | Inventory-level category based on evaluating sellable on-hand quantity against the recommended minimum level and estimated excess units. | Healthy  
recommended-sales-price | Sales price recommended to help you sell through your inventory based on your current inventory settings. This value may be different from the lowest price or Featured Offer price. We recommend that you keep your product at this price until you have sold through your excess inventory. | 19.99  
recommended-sale-duration-days | If a sale is recommended, this is the estimated sale duration in days that would likely help you sell through your excess inventory. | 14  
recommended-removal-quantity | Estimated number of units that would likely benefit from removal instead of being charged storage fees | 4  
estimated-cost-savings-of-recommended-actions | Estimated cost savings between taking the recommended action versus the storage fees you would incur on that inventory by taking no action | 2   
sell-through | The rate at which your units sold and shipped over the past 90 days divided by the average inventory available at fulfillment centers during that time. Tracking your sell-through rate can help you determine whether you need to take action to improve traffic or conversion for your products. | 1.4  
item-volume | The volume of the item, which is calculated by multiplying the longest side, median side, and shortest side together. These measurements generally correspond to the length, width, and height of the item. | .23  
volume-unit-measurement | Unit of measurement for the volume of the item | Cubic feet  
storage-type |  Storage-type category of the product for which storage limits are set.  **Note:** Standard size includes small and standard types.  | Oversize  
storage-volume | Storage volume is the total usage for this product in our fulfillment centers minus inventory that is pending removal | 15.24  
marketplace  | The Amazon store where the product is located | IT  
product-group | Distinct product grouping distinguishing products like books, from watches or video games | gl_grocery  
sales-rank | The current rank for your product. The change in sales rank value is the plus or minus change in the past 7 days. | 15046  
days-of-supply | The estimated number of days that your current inventory supply will last based on the projected demand for your product | 45  
estimated-excess-quantity | Estimated excess units are overstocked units based on your current sales velocity and customer demand forecast. It’s costing you more to keep these units on hand and pay storage fees than to reduce the number of units through a price reduction or removal. | 100  
weeks-of-cover-t30 | Your historical trailing 30-day on-hand inventory average divided by your units sold over the same time period divided by 4 weeks. If you sold 400 units of a given item in the last 30 days (4 weeks) and had 100 sellable units in fulfillment centers, your weeks of cover last 30 days would be 1. | 4.1  
weeks-of-cover-t90 | Your historical trailing 90-day on-hand inventory average divided by your units sold over the same time period divided by 12 weeks. If you sold 400 units of a given item in the last 90 days (12 weeks) and had an average of 10 sellable units in fulfillment centers, your weeks of cover last 90 days would be 3.33. | 12.5  
featuredoffer-price | Offer displayed on a product detail page with an **Add to Cart** button | 24.99  
sales-shipped-last-7-days | Shipped-unit sales in the last 7 days | 1  
sales-shipped-last-30-days | Shipped-unit sales in the last 30 days | 5  
sales-shipped-last-60-days | Shipped-unit sales in the last 60 days | 20  
sales-shipped-last-90-days | Shipped-unit sales in the last 90 days | 45  
inventory-age-0-to-30-days | The number of sellable units that have been in the fulfillment center for the last 30 days | 0  
inventory-age-31-to-60-days | The number of sellable units that have been in the fulfillment center for the last 31-60 days | 10  
inventory-age-61-to-90-days | The number of sellable units that have been in the fulfillment center for the last 61-90 days | 20  
inventory-age-181-to-330-days | The number of sellable units that have been in the fulfillment center for the last 181-330 days | 0  
inventory-age-331-to-365-days | The number of sellable units that have been in the fulfillment center for the last 331-365 days | 34  
estimated-storage-cost-next-month |  Estimated storage fees (monthly storage + storage utilization surcharge + aged inventory surcharge) that you would incur 30 days from today, based on your current sales rate.  **Note:** Inventory costs are based on quantities in the latest daily snapshot and may differ from your actual inventory quantities. | 13.67  
inbound-quantity | Inbound quantity = inbound-working + inbound-shipped + inbound receiving | 14304  
inbound-working | Shipments in working status | 3400  
inbound-shipped | Shipments in shipped status | 1200  
inbound-received | Shipments in receiving status | 0  
no-sale-last-6-months | Inventory that has not sold in six or more consecutive months and that have been in fulfillment centers for more than 180 days. These units will be automatically removed during the next removal cycle if you are opted in to automated fulfillable inventory removals. | 0  
Total Reserved Quantity | Inventory in reserved status might be tied to a customer order in the process of being shipped between fulfillment centers, or set aside at a fulfillment center for additional processing |  10  
unfulfillable-quantity | The number of units you have in stock that are not available as inventory to sell or fulfill | 11  
recommended-order-quantity | The recommendation for the number of units to be restocked for FBA | 10  
recommended-order-date | The suggested date to ship the product to avoid running low or going out of stock, based on your estimated days of supply and lead time | 4/11/2021  
Last updated date for Historical Days of Supply | Updated date of Low inventory level fee | 4/22/2024  
Exempted from Low-Inventory-Level Fee? | Is Low inventory level fee exempted | No  
Exempted from Low-Inventory cost coverage Fee? | Is Low inventory cost coverage fee exempted | No  
Low-Inventory-Level Fee applied in current week? | Is Low inventory level fee applied | Yes  
Short term historical days of supply | short term historical days of supply (last 30 days) | 12  
Long term historical days of supply | long term historical days of supply (last 90 days) | 6  
Inventory age snapshot date | The exact date for inventory age and any associated surcharges for aged inventory is calculated | 4/10/2021  
Inventory Supply at FBA | The number of units you have for a SKU in fulfillment centers that can be picked, packed, and shipped | 10  
Reserved FC Transfer | The number of units being transferred from one fulfillment center to another | 1  
Reserved FC Processing | The number of units that have been sidelined at a fulfillment center for additional processing | 2  
Reserved Customer Order |  The number of units reserved for customer orders | 1  
Total Days of Supply (including units from open shipments)  | Total Days of Supply (including units from open shipments) | 23

