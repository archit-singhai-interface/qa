---
title: SKU economics report
url: https://sellercentral.amazon.com/help/hub/reference/GZ8Y22NL2FSRY8M5
section: General Documentation
---

The SKU economics report provides aggregated historical data to help you
understand the economics of your products over time at the parent-ASIN, child-
ASIN, MSKU, or FNSKU level for a selected time period and Amazon store. This
includes data for Sales, Fees, Ads, Per-Unit costs, and Net Proceeds. Data in
this report can be up to 24 hours old.

Follow the steps on the [SKU Economics report page](/sereport) to select the
Amazon Store, data aggregation level, date range, and data types you would
like to include in your report.

**Accessing and downloading the report**

The downloadable file for this report is provided in a CSV format. If excel
does not automatically detect this format and asks you what format the file is
when opening, select Comma Separated Values or CSV.

**Note:** Sales data for seller-fulfilled listings are not available at the
FNSKU grain because Sales for those listings are tracked by MSKU. If you have
seller-fulfilled listings and think sales data may be missing try running the
report at the MSKU data aggregation level.

To include **storage fees** in your SKU economics report output ensure the
time period you have specified includes the date range between the 7 and 15 of
the month when storage fees are charged:

  * Select **Fee Data** and **Storage fees and surcharges** option in Step 2
  * Click **Generate report**

To include **Low Inventory level fees** in your SKU economics report output:

  * Select **Fee Data** and **Fulfillment base rate and surcharges** option in Step 2
  * Click **Generate report**

**User permissions**

Primary users of a seller account have default access to the SKU Economics
report. However, if any additional users need to access the report, they must
be granted permissions. You can grant additional user permissions by going to
[Global User Permissions](/account/permissions#/overview/users/view) and
selecting **Manage rights** for the user you are updating permissions for.
From there, navigate to **Reporting Dashboards** and enable **SKU Economics**.
Seller Provided Costs and Net Proceeds outputs in the Fee and Economics
Preview report will only be enabled if a primary user has been granted seller
Provided Costs permissions.

**Sales data definitions:**

Field name | Definition  
---|---  
Sales | The amount of ordered product sales, calculated by multiplying the average selling price of products and the number of units ordered for the selected time period  
Units sold | The number of units ordered for the selected time period.  
Average sales price | The average price of the units sold in the selected time period, calculated by dividing the ordered Product Sales by units ordered for the selected time period.  
Units returned | The number of units refunded during a selected time period.   
Net sales | Net product sales, calculated by ordered Product Sales minus refunded Product Sales.  
Net units sold | The number of net units sold for the selected time period, calculated by units ordered minus units refunded.  
  
**Fees data definitions:**

For each fee type supported, the following data is in the report if applicable
to that fee type.

Field name | Definition  
---|---  
Fee quantity | Charged fee quantity for a given product in the seller's account. When the fee is not charged on a per unit basis, this value may be null or may not be an integer.  
Fee total | Final charge amount for this fee type after promotion and tax are considered. This value is calculated as amount - promotion Amount + tax Amount.  
Fee per unit | Final charge amount per unit after promotion and tax are considered. This value is calculated by dividing total Amount by charged quantity. This value will be null when quantity is null.  
Fee amount* | The fee amount as calculated by the rate card, not including promotions or tax.  
Promotion amount* | The promotion amount associated with this transaction type. This value is deducted from amount when computing total Amount.  
Tax amount* | The tax amount associated with this transaction type. This value is added to amount when computing total amount.  
  
**Note:** * denoted fields are not yet available in the downloadable report
but are available via the reports selling partner-API.

**Supported fee types:**

Field name | Definition  
---|---  
FBA fulfillment fee | The FBA fulfillment fee is charged per unit fulfilled. The rate is determined by the product category, size tier, and shipping weight of the item.  
Monthly inventory storage fee | The monthly inventory storage fee is based on the daily average volume of space your inventory occupies in our fulfillment centers1. The rate is determined by the product category, size tier, and the time of year stored. The fee is charged monthly.   
Low Inventory Level Fee | The low-inventory-level fee is charged per unit fulfilled. The rate is determined based on the historical days of supply, which is the ratio of average daily sellable inventory units to the average daily shipped units. For rate cards and information about this fee, go to [Low inventory level fee](/help/hub/reference/GV43F6S76Y9DHYRH).   
Referral fee | The referral fee is charged per unit sold. It is determined by the product category of the item. The fee is calculated on the total sales price, which is the total amount that the buyer pays, including the item price and any delivery or gift-wrapping charges.  
Long-term storage fee | Inventory that has been in a fulfillment center for an extended period of time is charged a monthly long-term storage fee as a surcharge on top of monthly inventory storage fees. Long-term storage fees are assessed using an inventory snapshot on the 15th of each month. For more information, go to [Long-term storage fees](/gp/help/GJQNPA23YWVA4SBD).  
FBA ship placement Service fee | The FBA ship placement service fee for standard and large bulky sized products reflects the cost of distributing inventory to fulfillment centers close to customers. For more information, go to [FBA ship Placement Service fee](/help/hub/reference/GC3Q44PBK8BXQW3Z).  
ship transportation charges | When sending inventory to fulfillment centers using an Amazon partnered carrier, the cost is billed to your account as an ship transportation charge. Billable weight is used to estimate the shipping cost. The billable weight will be either the dimensional weight or the shipment weight, whichever is greater. Dimensional weight is estimated based on the current dimensions of the product.  
Per-item selling fees | Subscribers to the Individual selling plan pay a fee for each item sold on Amazon, in addition to any other applicable fees.  
Closing fees | Closing fees are charged for each unit sold in the following categories: Books, DVD, Music, Software & Computer/Video Games, Video Game Consoles, and Video Game Accessories.  
Removal fee | Removal fees are charged per item removed from a fulfillment center.  
Disposal fee | Disposal fees are charged per item that you request we dispose of from a fulfillment center.  
Refund administration fee | If you refund a customer order for which you have already received payment, Amazon will refund you the amount of the referral fee you paid for the items, minus the applicable refund administration fee.  
FBA Prep fee | If you use the FBA Prep Service, Amazon will prepare your eligible products for a per-unit fee. The fee is charged on products for which Amazon performed the labeling, poly bagging, bubble wrapping, opaque poly bagging, or taping services.  
Returns Processing fee  | A fee charged per unit for each customer-returned unit in the Apparel and Shoes fee categories for returns exceeding the category-based return rate in some stores. For more information, go to [Returns processing fee](/help/hub/reference/G64LS955WNFT6EDP).  
  
**Note:** Not all fees are included in SKU Economics report at this time.
However, these represent the most common fees for the average seller. Leave
feedback to let us know what additional fees and features you would like to
see.

**Note:** SKU Economics, SKU Economics reports, and their net proceeds
calculations will not include FBA ship Placement service fees until May 1,
2024.

**Advertising:**

The following data types are in the report for advertising charges.

Field name | Definition  
---|---  
Total amount | Final charge amount for this fee type after promotion and tax are considered. This value is calculated as: amount–promotion amount + tax amount.  
Amount per unit | Final charge amount per unit after promotion and tax are considered. This value is calculated by dividing total amount by charged quantity. This value will be null when quantity is null.  
Quantity | Quantity charged for this advertising type.  
Promotion amount | The promotion amount associated with this transaction type. This value is deducted from amount when computing total amount.  
Tax amount | The tax amount associated with this transaction type. This value is added to amount when computing total Amount.  
  
The following advertising types are currently supported in SKU Economics
report:

Sponsored Products charges | Sponsored Products is a cost-per-click advertising solution that promotes your products using ads that can appear in highly visible locations across Amazon.  
---|---  
  
**Off Amazon costs:**

Off-Amazon cost provided by the seller at a per unit level for this product.

The following data types can be included in the report as per unit costs:

Field name | Definition  
---|---  
Cost of goods sold | Cost to manufacture or acquire the product. This value is provided by the seller and is applicable to both Fulfillment by Amazon (FBA) and Merchant Fulfilled Network (seller-fulfilled) products.  
Miscellaneous cost | Miscellaneous costs not related to this specific product, such as overhead, and so on. This value is provided by the seller and applicable to both Fulfillment by Amazon (FBA) and Merchant Fulfilled Network (seller-fulfilled) products.  
Fulfillment cost | Cost of fulfilling an order containing the product, including labor, packing material, shipping to customer, customer service and so on. This value is provided by the seller and applicable to Merchant Fulfilled Network (seller-fulfilled) products.  
Storage cost | Cost to store a single unit of the product per month. This value is provided by the seller and applicable to Merchant Fulfilled Network (seller-fulfilled) products.  
  
**Note:** The SKU Economics report can integrate your costs such as cost of
goods sold, miscellaneous costs, shipping cost, and seller-fulfilled costs to
calculate more accurate net proceeds per unit. It is voluntary to provide this
information, and you can use the SKU Economics Report without providing it.
The off-Amazon cost can be provided on [SKU Central](/skucentral?mSku=xxx) and
[Revenue Calculator](/revcal). User permissions for Seller Provided Costs must
enabled in order to include these costs in your report.

**Net proceeds:**

The net proceeds for a given product in the seller's account for a given time
range. These fields are calculated as Net Sales - sum of total fees charged -
sum of total ads charged - (per unit costs * Net units sold).

Net proceeds data types in the SKU Economics report:

Net proceeds total | Total net proceeds for a given product in the seller's account for a given time range.  
---|---  
Net proceeds per unit | Net proceeds per unit for a given product in the seller's account for a given time range. This value is calculated by dividing Total sales by net units sold.  
  
**Note:** Some jurisdictions may require Amazon to charge tax on the fees
above. We will use the information you supply in your seller account to
determine whether a particular fee is taxable and the appropriate VAT, GST,
sales tax, or other tax rate to charge. Tax rules and regulations are
jurisdiction-specific. Search for VAT, GST, sales tax, or your country name in
Seller Central help to find more information. Fees that are tax-inclusive will
be shown with the calculated taxes included on the Amazon fees card. For
information on which fees are tax-inclusive, consult your regional [Amazon
Services Business Solutions Agreement](/gp/help/1791).

