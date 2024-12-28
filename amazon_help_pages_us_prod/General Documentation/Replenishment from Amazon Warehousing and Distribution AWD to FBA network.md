---
title: Replenishment from Amazon Warehousing and Distribution (AWD) to FBA network
url: https://sellercentral.amazon.com/help/hub/reference/GKH7ASMAL93YECBF
section: General Documentation
---

Inventory replenishment at Amazon Warehousing and Distribution (AWD) can
either be managed by Amazon (Auto-Replenishment) or by you (Manual
Replenishment or Add-On). Upon enrollment, your inventories are automatically
managed through auto-replenishment but you will have the option to opt out at
SKU level to manually choose when to replenish your inventories.

## Auto-Replenishment

Through the Auto-Replenishment feature, AWD will move the inventory from the
Amazon Distribution Centers (DC) to the FBA network (Amazon fulfillment
centers) on your behalf to avoid stockouts. When the inventory is Auto-
Replenished to the FBA network, it is exempted from the capacity limits
through FBA and if 70% or more inventory of a given ASIN is sent to the Amazon
fulfillment centers through AWD’s Auto-Replenishment in the preceding 90 days,
certain FBA fees will not apply to the seller-ASIN. Please refer to [Amazon
Warehousing and Distribution fees](/gp/help/GAYG62Q3MPE6STFS) for the latest
policy on this. Additionally, in the event that an opted-in ASIN does run out-
of-stock in the FBA network, customers can continue to search and buy the
product on the store.

**Important:** The searchable amount is equal to the inventory that is in
transit from the DC to the FBA network, plus inventory in storage at the AWD
DC. Please note that the promised delivery date will differ from products in
the FBA network.

## Benefits of Auto-Replenishment and Calculation of Auto-Replenishment Ratio

Auto-Replenishment provides incentives like capacity limits exemptions through
FBA which, while not directly impacting the IPI scores, have a positive impact
on IPI’s calculation index. Also, sellers are not charged low inventory level
and storage utilization fees for the ASINs, where Auto-Replenishment ratio is
greater than or equal to 70%. To evaluate whether an ASIN qualifies for no low
inventory level and storage utilization fees, the Auto-Replenishment ratio is
calculated in the following way:

Auto Replenishment shipment quantity / (Auto + Manual + Add-on + Direct
Inbound to FBA) = Auto Replenishment Ratio

If the percentage is equal to or larger than 70%, then the ASIN will be exempt
from low inventory level and storage utilization fees. The Auto-Replenishment
ratio is calculated on a daily basis and takes the quantities shipped in the
past 90 days only. The 90 days calculation for an ASIN starts on the first day
an Auto-Replenishment shipment is created for that specific ASIN.

Below is a sample calculation for a particular ASIN:

  * Auto-Replenishment shipment quantity (on 10/14) = 7000 units (a)
  * Add-on Replenishment (on 10/14) = 500 units (b)
  * Direct to Inbound shipment quantity (on 11/6) = 500 units (c)
  * Manual Replenishment (on 12/2) = 1500 units (d)

Auto Replenishment ratio (on 12/10) = a / a + b + c + d

= 7000 / 7000 + 500 + 500 + 1500 = 73.6%

## How does the Auto-Replenishment trigger?

Auto-Replenishment uses a proprietary data science model to trigger
replenishment to the FBA network. When the combined quantity of **Available
inventory in FBA network** and **Inventory in transit to FBA network** falls
below the **Optimum level of supply** for a specific ASIN, the Auto-
Replenishment will be triggered during the next scheduled replenishment cycle
to ensure the ASIN does not go out-of-stock. Currently, the science model runs
7 days a week to monitor inventory in the FBA network and determine if an
Auto-Replenishment shipment needs to be triggered.

Each seller-ASIN will have its own optimal level. Additionally, the optimal
level for an ASIN will fluctuate over time. For specific quantities of
**Available inventory in FBA network** , **Inventory in transit to FBA
network** , and **Optimum level of supply** , refer to the **Auto-
replenishment quantity** section on the **View global inventory** page.

Below is a general Auto-Replenishment calculation:

  * Available in FBA network: 100 units
  * In-transit to FBA network: 300 units
  * Optimal level: 500 units

Science model recommendation (Auto trigger)

= Optimal level – (Available in FBA network + In-transit to FBA network)

= 500 – (100 + 300)

= 100

## Auto replenishment for seasonal and new ASINs

The Auto replenishment algorithm considers 5 years of historical data and
upcoming sales forecast to bake in increased demand for the ASIN at the seller
level. The auto-replenishment algorithm looks at similar ASINs and products in
addition to an ASIN’s sales history. Auto-replenishment is able to predict
demand without historical data for a specific ASIN based on how similar
product or product types have performed in the past. The algorithm will create
an optimum inventory level applicable for the ASIN that reflects the sales
forecast and auto-replenishment will move inventory from AWD to FBA to
maintain the science determined Optimum inventory level in FBA.

## Select SKU level replenishment settings

You can enroll into auto replenishments at SKU level, allowing for tailored
and efficient inventory management that will suit your business needs.
Additionally, you will now have the ability to set the maximum number of units
limit for FBA inventory that should be maintained through auto replenishments.
Auto replenishment system will consider the lower of the two values - 1)
Amazon determined optimal quantity, 2) Maximum number of units limit which you
set - to determine the auto replenishment quantity. This allows you to set the
upper limit of FBA units to prevent overstocking of seasonal and new ASINs,
ensuring optimal inventory levels and lower storage costs.

To access your SKU level replenishment settings, follow below steps on [AWD
Inventory](https://sellercentral.amazon.com/fba-inventory/gim/inventory-list)
or Move from AWD pages:

  1. From under the FBA replenishment column, click the Auto replenishment link which will open up a modal.

  2. Option 1: FBA auto-replenishment (using Amazon recommended FBA units)–Choose this option to leverage Amazon’s science model to determine the optimal inventory levels required in FBA and automatically create replenishments on your behalf, ensuring consistent stock availability in your FBA inventory.

  3. Option 2: FBA auto-replenishment (Using custom Max FBA unit limit)–Choose this option to set the maximum number of units limit for FBA inventory. AWD will use the lower of two values - 1) Amazon determined optimal quantity, 2) Maximum number of units limit which you set - to determine the auto replenishment quantity. Note that if you have multiple SKUs that roll up to the same FNSKU or ASIN, we will use the highest maximum number of units limit which you have set.

  4. Option 3: Disable auto replenishments–Choose this option to disable auto replenishments for this SKU. By selecting this option, you will assume responsibility for transferring inventory from AWD to FBA each time.

  5. If you choose Option 2 or Option 3, you will have to provide the reason for the choice and acknowledge the risk of over-stocking or out of stock inventory that could result from this selection.

  6. Note that 1) The Max FBA unit limit may take up to 24 hours to become effective, 2) If your current FBA inventory exceeds the Max FBA unit limit, the restriction will only apply to future replenishments.

## Request manual replenishments

When you believe the auto-replenishment won’t be enough to meet expected
sales, click **Move from AWD** on the top right corner of the page and request
for additional inventory or you can request through the Move Inventory section
on the [AWD program
page](https://sellercentral.amazon.com/asdn/about?ref=esp_asdn#manage-
service). The link will take you to the **Move from storage** page, which will
be accessible to all AWD sellers. To initiate replenishment to FBA through
this page, select the SKU, carton configuration, and carton counts to be
replenished.

  1. Enter the number of units to move to select the SKUs you want to manually replenish.

  2. Click **Confirm** to confirm the move and then click **Review Move Request**.

  3. On the **Review Move Request** page, confirm the move request by clicking **Confirm move request** post, which you will get a confirmation module.

## Track manual replenishment orders

On the [AWD program page](/asdn/about?ref=esp_asdn#manage-service), click
**Track replenishments** and you will be directed to the **Activity Monitor**
page, where you will be able to track your manual replenishment orders. By
filtering shipment IDs and others metrics, you could search and review the
status of your manual replenishment orders.

## Important information about FBA capacity limits on Add-On and Manual
Replenishment

**Note:** Since Add-on and Manual Replenishments are subject to FBA capacity
limits, the requested inventory replenishment will get rejected if the
shipment created would go above the limits.

This is different from the case where the shipment created is for more
inventory than what is available at the distribution center. In this case, a
shipment with the available amount of inventory at the distribution center
would be created.

## Comparison between Auto-Replenishment and Manual Replenishment

Replenishment type | Sub-replenishment type | Replenishment quantity decided by | Bypass FBA capacity limit | Out of stock purchase  
---|---|---|---|---  
Auto-Replenishment | Auto-Replenishment | Amazon | Yes | Yes  
Manual Replenishment | - | Seller | No | Yes - only when there are in-transit inventory  
  
## AWD Replenishment frequently asked questions

#### How long does it take for inventory to replenish from the AWD storage
facility to FBA?

The replenishments take up to an average of 14 days to move from an AWD center
to the FBA network.

**Note:** Expect delays in processing during the peak period due to the
increased volumes.

#### How can I start the investigation for the missing units from an AWD
Replenishment shipment?

For any discrepancies in the AWD Replenishment shipments, raise a support case
per shipment to start the investigation. Also, it is crucial that you attach
the Proof of Ownership of the ASIN associated with the specific shipment
relating to your support case.

#### What if an Auto or Manual Replenishment order does not contain whole
carton units?

Inventory movement in AWD warehouses is done at the carton level. AWD will
round down orders to the closest carton at a SKU level when moving them. For
example, if you request to move 19 units of a SKU with 5 units per carton, AWD
would move 3 cartons containing 15 units. In the move inventory page you can
directly select the number of cartons that needs to be moved.

