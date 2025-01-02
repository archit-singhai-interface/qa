---
title: Monthly storage fees report
url: https://sellercentral.amazon.com/help/hub/reference/G202086720
section: General Documentation
---

The [Monthly Storage Fees report](/reportcentral/STORAGE_FEE_CHARGES/1)
provides estimated monthly inventory storage fees incurred for each ASIN of
your inventory in Amazon fulfillment centers during the previous month. The
report is generated between the 10th and 18th of each month and is available
for download only.

Learn more about the [inventory storage fee](/gp/help/200612770).

## Field Definitions

Download header | Description | Example value  
---|---|---  
asin | Amazon standard identification numbers (ASINs) are unique blocks of 10 letters or numbers that identify items. Amazon assigns the ASIN, which you can find on the product-detail page. | 0991519108  
fnsku | Amazon's fulfillment network stock-keeping unit (SKU) identifier. | X000A8GG1A  
product-name | Description of the ASIN on the product-detail page. | Stylish hat for pets  
fulfillment-center | Fulfillment center in which the ASIN is stored. | FTW3  
country-code | Country in which the fulfillment center is located. | US  
longest-side | The dimensions of the longest side of a single unit of the item. The inventory storage fee is charged by volume in cubic feet, which equals the longest side x median side x shortest side. These often correspond to the length, width, and height of an item. | 8.43  
median-side | The dimensions of the side of a single unit of the item that is neither the longest nor the shortest. The inventory storage fee is charged by volume in cubic feet, which equals the longest side x median side x shortest side. These often correspond to the length, width, and height of an item. | 5.81  
shortest-side | The dimensions of the shortest side of a single unit of the item. The inventory storage fee is charged by volume in cubic feet, which equals the longest side x median side x shortest side. These often correspond to the length, width, and height of an item. | 0.73  
measurement-units | Unit of measurement for the longest, median, and shortest sides of the item for purposes of calculating the inventory storage fee. | inches  
weight | The item's weight used to identify its product-size tier. This can be the item's unit weight or dimensional weight, depending on the item. For more details, go to [Dimensional weight](/gp/help/G53Z9EKF8VVZVH29). | 0.79  
weight-units | Unit of measurement for the weight of the item. | pounds  
item-volume | The inventory storage fee is charged per volume in cubic feet, which equals the longest side x median side x shortest side. These often correspond to the length, width, and height of an item. | 0.0208  
volume-units | Unit of measurement for the volume of the item. | cubic feet  
product-size-tier | Classification of the item by its dimensions for purposes of calculating fees. For more details, go to [Product size tiers](/gp/help/GG5KW835AHDJCH8W). | Standard-sized or Oversize  
average-quantity-on-hand | Daily average quantity of the item in fulfillment centers. This is equal to the inventory for the trailing month divided by the number of days in that month.  | 2.0  
average-quantity-on-hand-above-30-days | Daily average quantity of the item in fulfillment centers that are aged above 30 days. This is equal to the inventory aged above 30 days for the trailing month divided by the number of days in that month. | 0.5  
average-quantity-pending-removal | Daily average quantity of items for which removal from the fulfillment center was requested. | 0.0  
estimated-total-item-volume | Average volume on hand, minus average volume pending removal, multiplied by the volume of the item. | 0.0148  
estimated-total-storage-utilization-surcharge-volume | Average volume for on hand inventory aged above 30 days, minus average volume pending removal, multiplied by the volume of the item. | 0.0104  
month-of-charge | Month of year in which storage-fee estimate applies; format is YEAR-MONTH. | 2024-04  
storage-utilization-ratio | Storage utilization ratio for the product size tier on the last day of the month. The ratio is calculated by dividing the average daily inventory volume stored in cubic feet divided by the average daily shipped volume in cubic feet over the trailing 13 weeks. | 26.5  
storage-utilization-ratio-units | Unit of measurement for the storage utilization ratio | weeks  
base-rate | Amount of the base monthly inventory storage fee rate that will apply to this ASIN. The rate is based on product size tier and time of the year. Base monthly storage fee is higher from October to November. | 0.78  
utilization-surcharge-rate | Amount of the storage utilization surcharge rate that will apply to this ASIN. The rate is based on product size tier and storage utilization ratio. | 0.44  
currency | Currency of the storage rate amount. | USD  
estimated-base-monthly-storage-fee | Estimated base monthly storage fee per ASIN, calculated based on the base rate multiplied by total volume of the item. | 0.012  
estimated-storage-utilization-surcharge | Estimated storage utilization surcharge per ASIN, calculated based on the storage utilization surcharge rate multiplied by volume of inventory aged above 30 days | 0.004  
estimated-monthly-storage-fee | Estimated monthly storage fee per ASIN, calculated based on the sum of base rate and utilization surcharge rate, multiplied by total volume of the item. | 0.016  
dangerous-goods-storage-type | Identify if an ASIN is classified as dangerous goods item, which has different rates. | \--  
total-incentive-fee-amount | Amount of monthly storage fee incentive that applies to this ASIN. | 0.010  
breakdown-incentive-fee-amount | Description of the incentive type that applies to this ASIN. | FBA-NEW-SELECTION  
average-quantity-customer-orders | Daily average quantity of items which customers ordered but have not shipped from the fulfillment center. | 0.05

