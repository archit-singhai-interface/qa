---
title: Amazon Warehousing and Distribution fee types and reports
url: https://sellercentral.amazon.com/help/hub/reference/GPB467PZW3AZC4V3
section: General Documentation
---

There are three types of fees for Amazon Warehousing and Distribution (AWD):
storage fees, processing fees, and transportation fees.

## Storage fees

We charge monthly AWD storage fees for the space that your inventory occupies
in our distribution centers. Monthly storage fees are calculated by
multiplying the applicable storage rate by the average volume that was used
over the month for all stored boxes.

To check the applicable storage fee rate, go to [Amazon Warehousing and
Distribution fees](/gp/help/GAYG62Q3MPE6STFS). The fee is charged on the 6th
of each month.

**Calculation example:**

  * Storage fee per cubic foot: $0.48 
  * Average storage volume for the entire month for a given shipment and FNSKU: 100 cubic feet

The storage fee is calculated as $0.48 x 100 = $48

## Processing fees

Processing fees are charged when a replenishment order is successfully
delivered to Amazon’s fulfillment network or your distribution channel. The
fee is calculated by multiplying the applicable processing rate by the number
of boxes that were delivered as part of the replenishment order.

**Calculation example:**

  * Processing fee per box: $2.50
  * Number of boxes that were delivered for the replenishment order: 10 

The processing fee is calculated as $2.50 x 10 = $25

Starting April 1, 2025, the processing fee will be charged separately at
inbound when your inventory is received in our distribution center, and again
at outbound when a replenishment order is successfully delivered to Amazon’s
fulfillment network or your other sales channels. To view the processing fee
rate, go to [Amazon Warehousing and Distribution
fees](/gp/help/GAYG62Q3MPE6STFS).

**Calculation example:**

  * Processing fee per box (charged at inbound and outbound separately): $1.35
  * Number of boxes received in AWD distribution center: 25 
  * Number of boxes that were delivered for the replenishment order: 10 

The processing fee at inbound is calculated as $1.35 x 25 = $33.75

The processing fee at outbound is calculated as $1.35 x 10 = $13.50

## Transportation fees

Transportation fees are charged when a replenishment order is successfully
delivered to Amazon’s fulfillment network or your other sales channels. The
fee is calculated by multiplying the applicable transportation rate by total
volume of boxes in cubic feet that were delivered as part of the replenishment
order to FBA. To view the transportation fee rate, go to [Amazon Warehousing
and Distribution fees](/gp/help/GAYG62Q3MPE6STFS)**.**

**Calculation example:**

  * Transportation fee per cubic foot: $$1.15
  * Total volume of the boxes in the replenishment order: 100 cubic feet

The transportation fee is calculated as $1.15 x 100 = $115

**Note:** There’s no separate labeling fee for automated replenishments from
AWD to FBA. The label that’s applied to the box for the shipment to the
distribution center is used for automated replenishment. For more information,
go to [Send shipments to Amazon Warehousing and Distribution
(AWD)](/gp/help/GTPL7PGKU7WUKJSW).

## Fee reports

We have separate monthly reports for storage, processing, and transportation
fees:

  * [Monthly Storage Fee report](/awd/fee/reporting) shows a breakdown of the storage fee at the FNSKU level. 
  * [Monthly Processing Fee report](/awd/reports/fee?reportType=AwdProcessingFee) and [Monthly Transportation Fee report](/awd/reports/fee?reportType=AwdOutboundTransportationFee) collate the processing and transportation fees for the entire month across all replenishment orders. Starting April 1, 2025, the monthly processing fee report will provide details on processing fees charged at inbound and outbound separately.

You can view AWD storage fee, processing fee, and transportation fee
transactions in the [Payments
dashboard](/payments/dashboard/index.html/ref=xx_payments_dnav_xx). Once you
download and open the report, the transaction type will appear as **Service
fees** and the product details will appear as **AWD storage fee** , **AWD
processing fee** , and **AWD transportation fee**.

## Fees reports glossary

**Monthly Storage Fee report (fee reports through September 2023 are in the
old format)**

Column headers | Description | Example value  
---|---|---  
**merchant_customer_id** | The unique ID that’s associated with your seller account. | 80457449302  
**purchase_order_id** | The Amazon reference ID that’s generated for your shipment to Warehousing and Distribution.  | 3LX3PGHW  
**asin** | ASINs are unique blocks of 10 letters or numbers that identify items.  | B07FZ8S74R  
**fnsku** | The fulfillment network SKU is the unique identifier that FBA assigns to your product. | X000A8GG1A  
**warehouse_id** | The distribution center identifier for Warehousing and Distribution. | IUSL  
**country_code** | The country where a distribution center is located. | US  
**month_of_charge** | The month when a storage fee is charged. | 12  
**total_carton_weight** | The average weight of boxes for the entire month for a given purchase-order ID and FNSKU. | 28.34  
**weight_units** | The unit of measurement for the total box weight, which is represented in pounds.  | LBS  
**number_of_days_in_dc** | The number of days in which at least one box is in a distribution center for a given purchase-order ID and FNSKU. | 20  
**total_carton_volume** | The average volume of boxes for the entire month for a given purchase-order ID and FNSKU. | 102.56  
**volume_units** | The unit of measurement for the volume of boxes, which is represented in cubic feet.  | Cu_ft  
**fee_type** | The type of fee for Warehousing and Distribution.  | STORAGE_FEE  
**fee_rate** | The applicable rate that’s used to calculate fees. There are different values for each of the fee types.  | 0.42  
**fee_rate_units** | The measurement that’s used for the fee rate.  | $ PER_CUFT  
**total_fee_amount** | The total fee is calculated by multiplying the following: the fee rate per cubic foot and the average volume of boxes.  | 1000.67  
**currency** | The currency of the storage fee.  | USD  
  
**Monthly Storage Fee report (fee reports from October 2023 onward will be in
the new format)**

**Note:** The Storage Fee report will contain two tabs: 1) Detailed view and
2) Consolidated view.

**1\. Detailed view**

**Column headers** | **Description** | **Example value**  
---|---|---  
**merchant_customer_id** | The unique ID that’s associated with your seller account. | 80457449302  
**inbound_purchase_order_id** | The Amazon reference ID that’s generated for your shipment to Warehousing and Distribution.  | 3LX3PGHW  
**asin** | ASINs are unique blocks of 10 letters or numbers that identify items.  | B07FZ8S74R  
**fnsku** | The fulfillment network SKU is the unique identifier that FBA assigns to your product. | X000A8GG1A  
**msku** | Represents unique merchant-supplied identifier for a specific SKU. | B1P5012BT7-8UPC  
**warehouse_id** | The distribution center identifier for Warehousing and Distribution. | IUSL  
**country_code** | The country where a distribution center is located. | US  
**month_of_charge** | The month when a storage fee is charged. | December  
**year_of_charge** | The year when a storage fee is charged. | 2023  
**monthly_average_weight** | The average weight of boxes for the entire month for a given inbound purchase-order ID and FNSKU. | 28.34  
**weight_units** | The unit of measurement for the monthly average weight, which is represented in pounds.  | LBS  
**monthly_average_utilized_volume** | The average volume of boxes for the entire month for a given inbound purchase-order ID and FNSKU. | 102.56  
**volume_units** | The unit of measurement for the volume of boxes, which is represented in cubic feet.  | Cu_ft  
**fee_type** | The type of fee for Warehousing and Distribution.  | STORAGE_FEE  
**fee_amount** | The fee amount calculated based on the monthly_average_utilized_volume and the rate card (see rate details in the consolidated view). | 30  
**promotion_amount** | The amount offered as a discount. | 0  
**tax_amount** | The taxation amount | 0  
**total_charged_amount** | The total charged amount calculated based on the fee, promotion and tax amounts | 30  
**currency** | The currency of the storage fee.  | USD  
  
**2\. Consolidated view**

**Column headers** | **Description** | **Example value**  
---|---|---  
**merchant_customer_id** | The unique ID that’s associated with your seller account. | 80457449302  
**warehouse_id** | The distribution center identifier for Warehousing and Distribution. | IUSL  
**country_code** | The country where a distribution center is located. | US  
**chargeable_volume** | The volume amount used for charging. If you are reserving storage with Warehousing and Distribution and the utilized volume is less than the reserved volume., this number will reflect the reserved volume for charging | 102.56  
**volume_units** | The unit of measurement for the volume of boxes, which is represented in cubic feet. | Cu_ft  
**fee_amount** | The fee amount calculated by multiplying chargeable_volume and fee_rate. | 30  
**promotion_amount** | The amount offered as a discount. | 0  
**tax_amount** | The taxation amount | 0  
**total_charged_amount** | The total charged amount calculated based on the fee, promotion, and tax amounts. | 30  
**currency** | The currency of the storage fee. | USD  
**charge_type** | The type of rate applied on the chargeable_volume | BASE_RATE, STORAGE_RESERVATION_RATE  
**fee_rate** | The applicable rate that’s used to calculate fees. There are different values for each of the fee types. | 0.42  
**fee_rate_units** | The measurement that’s used for the the fee rate. | $ PER_CUFT  
  
**Processing Fee report (fee reports through December 2023 are in the old
format)**

Column headers | Description | Example value  
---|---|---  
**merchant_customer_id** | The unique ID that’s associated with your seller account. | 80457449302  
**purchase_order_id** | The purchase-order ID that’s generated for shipments from Warehousing and Distribution to FBA.  | 3LX3PGHW  
**replenishment_order_id** | The unique identifier for replenishment orders from Warehousing and Distribution to FBA. There can be multiple purchase-order IDs for each of these orders.  | repl-53ca9d8b-1367-4063-bc6b-f985f9547015  
**shipment_id** | The Amazon reference ID that’s generated for each shipment created in a replenishment order.  | repl-ship-06e14427-d6d9-4874-b0c1-6bfa84034c35  
**shipment_tracking_id** | The shipment ID that’s generated for each shipment created in a replenishment order, which is used to track the shipment. | FBA16YR3R2Z4  
**asin** | ASINs are unique blocks of 10 letters or numbers that identify items. | B07FZ8S74R  
**fnsku** | The fulfillment network SKU is the unique identifier that FBA assigns to your products. | X000A8GG1A  
**warehouse_id** | The distribution center identifier for Warehousing and Distribution. | IUSL  
**country_code** | The country where a distribution center is located.  | US  
**month_of_charge** | The month when a processing fee is charged.  | 12  
**total_carton_weight** | The average weight of the boxes for a given purchase-order ID and FNSKU.  | 28.34  
**weight_units** | The unit of measurement for the total box weight, which is represented in pounds.  | LBS  
**length_per_carton** | The length of the box for a given purchase-order ID and FNSKU. | 10.45  
**width_per_carton** | The width of the box for a given purchase-order ID and FNSKU. | 29.89  
**height_per_carton** | The height of the box for a given purchase-order ID and FNSKU. | 30.34  
**measurement_units** | The unit of measurement for the dimensions of a box, which is represented in inches.  | IN  
**total_carton_volume** | The total volume of boxes in a replenishment order for a given purchase-order ID and FNSKU.  | 102.56  
**volume_units** | The unit of measurement for the volume of boxes, which is represented in cubic feet.  | Cu_ft  
**container_qty** | The total number of boxes in the replenishment order. | 10  
**fee_type** | The type of fee for Warehousing and Distribution.  | PROCESSING_FEE  
**fee_rate** | The applicable rate that’s used to calculate fees. There are different values for each of the fee types.  | 2  
**fee_rate_units** | The measurement that’s used for the fee rate. | $ PER_CASE  
**total_fee_amount** | The total fee is calculated by multiplying the fee rate per box by the total number of boxes in a replenishment order.  | 100.56  
**currency** | The currency of the processing fee.  | USD  
  
**Processing Fee report (fee reports from January 2024 onward will be in the
new format)**

**Column headers** | **Description** | **Example value**  
---|---|---  
**merchant_customer_id** | The unique ID that’s associated with your seller account. | 80457449302  
**replenishment_order_id** | The unique identifier for replenishment orders from Warehousing and Distribution to FBA. There can be multiple purchase-order IDs for each of these orders.  | repl-53ca9d8b-1367-4063-bc6b-f985f9547015  
**shipment_id** | The Amazon reference ID that’s generated for each shipment created in a replenishment order.  | repl-ship-06e14427-d6d9-4874-b0c1-6bfa84034c35  
**shipment_tracking_id** | The shipment ID that’s generated for each shipment created in a replenishment order, which is used to track the shipment. | FBA16YR3R2Z4  
**asin** | ASINs are unique blocks of 10 letters or numbers that identify items. | B07FZ8S74R  
**fnsku** | The fulfillment network SKU is the unique identifier that FBA assigns to your products. | X000A8GG1A  
**msku** | Represents unique merchant-supplied identifier for a specific SKU. | B1P5012BT7-8UPC  
**outbound_purchase_order_id** | The purchase-order ID that’s generated for shipments from Warehousing and Distribution to FBA. | 3LX3PGHW  
**warehouse_id** | The distribution center identifier for Warehousing and Distribution. | IUSL  
**destination_code** | Refers to the sales channel of the replenishment order. AFN represents Amazon FBA channel and Non-AFN represents locations outside of Amazon. | AFN or Non-AFN  
**month_of_charge** | The month when a processing fee is charged.  | December  
**year_of_charge** | The year when a Processing fee is charged. | 2023  
**total_box_weight** | The total weight of the boxes for a given outbound purchase-order ID and FNSKU.  | 28.34  
**weight_units** | The unit of measurement for the total box weight, which is represented in pounds.  | LBS  
**length_per_box** | The length of the box for a given outbound purchase-order ID and FNSKU. | 10.45  
**width_per_box** | The width of the box for a given outbound purchase-order ID and FNSKU. | 29.89  
**height_per_box** | The height of the box for a given outbound purchase-order ID and FNSKU. | 30.34  
**measurement_units** | The unit of measurement for the dimensions of a box, which is represented in inches.  | IN  
**total_box_volume** | The total volume of boxes in a replenishment order for a given outbound purchase-order ID and FNSKU.  | 102.56  
**volume_units** | The unit of measurement for the volume of boxes, which is represented in cubic feet.  | Cu_ft  
**box_qty** | The total number of boxes in the replenishment order. | 10  
**fee_type** | The type of fee for Warehousing and Distribution.  | PROCESSING_FEE  
**fee_rate** | The applicable rate that’s used to calculate fees. There are different values for each of the fee types.  | 2  
**fee_rate_units** | The measurement that’s used for the fee rate. | $ PER_BOX  
**calculated_fee_amount** | The total fee is calculated by multiplying the fee rate per box by the total number of boxes in a replenishment order.  | 100.56  
**promotion_amount** | The amount offered as a discount. | 1  
**charged_amount** | The charged amount calculated based on the fee, promotion and tax amounts | 99.56  
**currency** | The currency of the processing fee.  | USD  
  
**Transportation Fee report (fee reports through December 2023 are in the old
format)**

Column headers | Description | Example value  
---|---|---  
**merchant_customer_id** | The unique ID that’s associated with your seller account. | 80457449302  
**purchase_order_id** | The purchase-order ID that’s generated for your shipment from Warehousing and Distribution to FBA. | 3LX3PGHW  
**replenishment_order_id** | The unique identifier for replenishment orders from Warehousing and Distribution to FBA. There can be multiple purchase-order IDs for each of these orders. | repl-53ca9d8b-1367-4063-bc6b-f985f9547015  
**shipment_id** | The Amazon reference ID that’s generated for each shipment created within a replenishment order. | repl-ship-06e14427-d6d9-4874-b0c1-6bfa84034c35  
**shipment_tracking_id** | The unique shipment ID that’s generated for each shipment created within a replenishment order, which is used to track the shipment.  | FBA16YR3R2Z4  
**asin** | ASINs are unique blocks of 10 letters or numbers that identify items. | B07FZ8S74R  
**fnsku** | The fulfillment network SKU is the unique identifier that FBA assigns to your products. | X000A8GG1A  
**warehouse_id** | The distribution center identifier for Warehousing and Distribution. | IUSL  
**country_code** | The country where a distribution center is located. | US  
**month_of_charge** | The month when a transportation fee is charged.  | 12  
**total_carton_weight** | The average weight of boxes for a given purchase-order ID and FNSKU.  | 28.34  
**weight_units** | The unit of measurement for the total box weight, which is represented in pounds. | LBS  
**length_per_carton** | The length of the box for a given purchase-order ID and FNSKU. | 10.45  
**width_per_carton** | The width of the box for a given purchase-order ID and FNSKU.  | 29.89  
**height_per_carton** | The height of the box for a given purchase-order ID and FNSKU.  | 30.34  
**measurment_units** | The unit of measurement for the dimensions of a box, which is represented in inches. | IN  
**total_carton_volume** | The total volume of boxes in a replenishment order for a given purchase-order ID and FNSKU.  | 102.56  
**volume_units** | The unit of measurement for the volume of boxes, which is represented in cubic feet.  | Cu_ft  
**fee_type** | The type of fee for Warehousing and Distribution.  | TRANSPORTATION_FEE  
**fee_rate** | The applicable rate that’s used to calculate fees. There are different values for each of the fee types. | 1  
**fee_rate_units** | The measurement that’s used for the fee rate.  | $ PER_CUFT  
**total_fee_amount** | The total fee is calculated by multiplying the fee rate per cubic foot by the total volume of boxes. | 100.56  
**currency** | The currency of the transportation fee. | USD  
  
**Transportation Fee report (fee reports from January 2024 onward will be in
the new format)**

**Column headers** | **Description** | **Example value**  
---|---|---  
**merchant_customer_id** | The unique ID that’s associated with your seller account. | 80457449302  
**replenishment_order_id** | The unique identifier for replenishment orders from Warehousing and Distribution to FBA. There can be multiple purchase-order IDs for each of these orders. | repl-53ca9d8b-1367-4063-bc6b-f985f9547015  
**shipment_id** | The Amazon reference ID that’s generated for each shipment created within a replenishment order. | repl-ship-06e14427-d6d9-4874-b0c1-6bfa84034c35  
**shipment_tracking_id** | The unique shipment ID that’s generated for each shipment created within a replenishment order, which is used to track the shipment.  | FBA16YR3R2Z4  
**asin** | ASINs are unique blocks of 10 letters or numbers that identify items. | B07FZ8S74R  
**fnsku** | The fulfillment network SKU is the unique identifier that FBA assigns to your products. | X000A8GG1A  
**msku** | Represents unique merchant-supplied identifier for a specific SKU. | B1P5012BT7-8UPC  
**outbound_purchase_order_id** | The outbound purchase-order ID that’s generated for shipments from Warehousing and Distribution to FBA. | 3LX3PGHW  
**warehouse_id** | The distribution center identifier for Warehousing and Distribution. | IUSL  
**destination_code** | Represents the sales channel of the replenishment order, AFN represents Amazon FBA channel, Non-AFN represents other locations outside of Amazon. | AFN or Non-AFN  
**month_of_charge** | The month when a transportation fee is charged.  | December  
**year_of_charge** | The year when a transportation fee is charged. | 2023  
**total_box_weight** | The total weight of boxes for a given outbound purchase-order ID and FNSKU.  | 28.34  
**weight_units** | The unit of measurement for the total box weight, which is represented in pounds. | LBS  
**length_per_box** | The length of the box for a given outbound purchase-order ID and FNSKU. | 10.45  
**width_per_box** | The width of the box for a given outbound purchase-order ID and FNSKU.  | 29.89  
**height_per_box** | The height of the box for a given outbound purchase-order ID and FNSKU.  | 30.34  
**measurment_units** | The unit of measurement for the dimensions of a box, which is represented in inches. | IN  
**total_box_volume** | The total volume of boxes in a replenishment order for a given outbound purchase-order ID and FNSKU.  | 102.56  
**volume_units** | The unit of measurement for the volume of boxes, which is represented in cubic feet.  | Cu_ft  
**box_qty** | The total number of boxes in the replenishment order. | 10  
**fee_type** | The type of fee for Warehousing and Distribution.  | TRANSPORTATION_FEE  
**fee_rate** | The applicable rate that’s used to calculate fees. There are different values for each of the fee types. | 1  
**fee_rate_units** | The measurement that’s used for the fee rate.  | $ PER_CUFT   
**calculated_fee_amount** | The total fee is calculated by multiplying the fee rate per box by the total number of boxes in a replenishment order. | 100.56  
**promotion_amount** | The amount offered as a discount. | 1  
**charged_amount** | The charged amount calculated based on the fee, promotion and tax amounts | 99.56  
**currency** | The currency of the transportation fee. | USD  
  
## Frequently asked questions

#### Where will the reimbursement amount appear after it's approved?

You can view the reimbursement by going to the **Transaction view** tab on the
[Payments dashboard](/payments/dashboard/index.html/ref=xx_payments_dnav_xx).
Select **Standard orders** from the **Account type** drop-down menu and select
**Other** from the **Transaction type** drop-down menu. After selecting these
options, view the **Product details** where the reimbursement amount is
classified as **Others**.

#### How many decimal places are used when calculating fees?

We use two decimal places for calculating fees and Seller Central reports.

#### How is the processing fee rate defined and charged. Is it per shipment,
and does it also include pallets?

AWD only supports box-based inbound and storage, and the program doesn't have
pallet-based services at this time. A processing fee is charged when an
outbound replenishment order is successfully delivered from AWD to a
fulfillment center. Starting April 1, 2025, the processing fee will be charged
separately at inbound when your inventory is received in our distribution
center, and again at outbound when a replenishment order is successfully
delivered to Amazon’s fulfillment network or your other sales channels. To
view the processing fee rate, go to [Amazon Warehousing and Distribution
fees](/gp/help/GAYG62Q3MPE6STFS).

#### When automatically replenishing from AWD to Amazon's fulfillment network,
is there an individual ASIN-level label charge? If yes, are the fees tracked
in the Seller Central reports separately?

There are no separate labeling charges for outbound replenishment from AWD to
FBA. The label that's pasted on the box as part of inbound operations is also
used for outbound replenishment. There is no separate labeling required for
replenishment.

