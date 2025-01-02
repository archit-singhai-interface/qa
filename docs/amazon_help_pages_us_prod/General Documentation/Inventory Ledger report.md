---
title: Inventory Ledger report
url: https://sellercentral.amazon.com/help/hub/reference/G4FKT5KQWFFJ7LDN
section: General Documentation
---

The Inventory Ledger report is like a bank statement for your inventory. It
provides end-to-end inventory reconciliation capability by showing your
starting inventory balance, received inventory, customer orders, customer
returns, adjustments, removals, and ending balance.

Use this report to analyze your inventory movements to and from fulfillment
centers, including products that are sold, returned, removed, disposed of,
damaged, lost, and found. You can view all historical movements of your
inventory for 18 months in this report.

To learn more about how to use the Inventory Ledger report in lieu of the
Daily Inventory History report, Monthly Inventory History report, Inventory
Event Detail report, Inventory Adjustments report, Inventory Reconciliation
report, and Received Inventory report, go to [Inventory Ledger report: How to
find the information you need](/gp/help/GCRWH2T93NYDHBXU).

## Summary view

The summary view of the [Inventory Ledger
report](/reportcentral/LEDGER_REPORT/0) shows a history of inventory events
(such as receipts, shipments, and adjustments) by SKU and disposition (such as
sellable, customer-damaged, carrier-damaged, fulfillment center-damaged,
expired, distributor-damaged, and defective).

The freshness of the data depends on the time period by which the report is
aggregated. For **Daily** , yesterday's data will generally be available
within 24 hours. For **Weekly** , last week's data will generally be available
by the end of the day on Monday. For **Monthly** , last month's data will
generally be available by the end of the second day of the month.

## Detailed view

The detailed view of the Inventory Ledger report shows details about all
inventory events in fulfillment centers, including event type, quantity,
location, country, and disposition. Data in the detailed view is updated in
near real time.

If you notice any discrepancies, try expanding the dates of your report. An
inventory event could have occurred in the previous month, which would affect
your data in the report window. Expanding the dates of your report can give
you a better understanding of your inventory movements.

**Tip:** The best way to reconcile inventory is to use the FNSKU field to
specify the product in each report.

You can also view your reimbursements in the online report by clicking
**Reimbursements** for the reported dates. Reimbursements for lost or damaged
units may take up to 4-5 business days to post to your account. To learn more
about reimbursements, go to [FBA inventory reimbursement
policy](/gp/help/200213130).

## Summary view parameters

Parameter | Description | Required?  
---|---|---  
**ASIN** | Unique blocks of 10 letters or numbers that identify items. ASINs are assigned by Amazon. You can find the ASIN on the product detail page. |  Not required To generate a report for a specific product, enter the ASIN, MSKU, or FNSKU. Leaving these fields blank will generate a report for all products.  
**Merchant SKU** | Unique identifier that you assign to products |  Not required To generate a report for a specific product, enter the ASIN, MSKU, or FNSKU. Leaving these fields blank will generate a report for all products.  
**Fulfillment network SKU (FNSKU)** | Unique identifier that Amazon assigns to products stored in and fulfilled from an Amazon fulfillment center |  Not required To generate a report for a specific product, enter the ASIN, MSKU, or FNSKU. Leaving these fields blank will generate a report for all products.  
**Aggregate report by location** | For the summary view, select **Country** to display inventory location by country or **Fulfillment center** to display inventory location by fulfillment center. **Note:** If you are selling items in the Low-Cost Store, you can identify them on the report by aggregating by **Country = CN** or **FC = XCND**. | Required  
**Aggregate report by time period** | For the summary view, select the desired time period for the report, such as monthly, weekly, or daily. | Required   
**Date range** | The start and end dates for the report | Required  
  
## Summary view report fields

Name | Description  
---|---  
Date | The date the report was requested  
FNKSU | Unique identifier that Amazon assigns to products stored in and fulfilled from an Amazon fulfillment center  
ASIN | Unique blocks of 10 letters or numbers that identify items. ASINs are assigned by Amazon. You can find the ASIN on the product detail page.  
MSKU | Unique identifier that you assign to products  
Title | The title of your product  
Disposition | The status of the product, such as sellable or damaged  
Starting warehouse balance | Units that were available for this product in fulfillment centers at the start of the time period  
Receipts | Units that were received in shipments to fulfillment centers  
Customer shipments | Completed deliveries of customer orders that Amazon has fulfilled  
Customer returns | Units that buyers have returned to fulfillment centers and that have been returned to your inventory  
Warehouse transfer in/out | Aggregated number of units that have been transshipped into and out of fulfillment centers  
Found | Units that were missing but have been found and returned to your inventory  
Removed | Units that have been removed from your inventory via a removal order and shipped out of fulfillment centers  
Lost | Units that are missing from your inventory in fulfillment centers and that may be eligible for reimbursement or for which you have already been reimbursed  
Disposed | Units that have been removed from your inventory and disposed of  
Other events | Units that were identified as damaged and that may be eligible for reimbursement or for which you have already been reimbursed, as well as all other inventory dispositions that may not be covered under the other definitions  
Ending warehouse balance | Units that were available for this product in fulfillment centers at the end of the time period  
Unknown events | Units for which the specific event type is not known. This is primarily caused by parts of an event occurring across different reporting time periods. Expanding the reporting time period can reduce the number of unknown event units.  
In transit between warehouses  | Units that are in transit between fulfillment centers  
Location | The country or fulfillment center where your inventory is located, depending on your selection for the **Inventory location** parameter  
Store (Optional) | The store where the inventory is sold. For example: Low-Cost Store. If this column is empty, the inventory is sold through FBA only.  
  
## Detailed view parameters

Parameter | Description | Required?  
---|---|---  
**ASIN** | Unique blocks of 10 letters or numbers that identify items. ASINs are assigned by Amazon. You can find the ASIN on the product detail page. |  Not required To generate a report for a specific product, enter the ASIN, MSKU, or FNSKU. Leaving these fields blank will generate a report for all products.  
**Merchant SKU** | Unique identifier that you assign to products |  Not required To generate a report for a specific product, enter the ASIN, MSKU, or FNSKU. Leaving these fields blank will generate a report for all products.  
**Fulfillment network SKU (FNSKU)** | Unique identifier that Amazon assigns to products stored in and fulfilled from an Amazon fulfillment center |  Not required To generate a report for a specific product, enter the ASIN, MSKU, or FNSKU. Leaving these fields blank will generate a report for all products.  
**Reference ID** | Transaction ID, such as a shipment ID or adjustment ID | Not required  
**Date range** | The start and end dates for the report | Required  
**Fulfillment Center (FC)** |  The fulfillment center where the event occurred.  **Note:** If you are selling items in the Low-Cost Store, you can identify their events by filtering for **FC = XCND**. | Not required  
**Event Type** | Type of event that caused a change in inventory, such as shipment, receipt, vendor return, warehouse transfer, adjustment, or customer return | Not required  
**Reason Group** | Refers to adjustment reason groups like Damaged, Inventory disposed of, Found, Lost and Other. View the Adjustment types and reason codes table below for a full list of codes and descriptions | Not required  
  
## Detailed view report fields

Name | Description  
---|---  
Date | The date of the event  
FNKSU | Unique identifier that Amazon assigns to products stored in and fulfilled from an Amazon fulfillment center  
ASIN | Unique blocks of 10 letters or numbers that identify items. ASINs are assigned by Amazon. You can find the ASIN on the product detail page.  
MSKU | Unique identifier that you assign to products  
Title | The title of your product  
Event type | Type of event that caused a change in inventory, such as shipment, receipt, vendor return, warehouse transfer, adjustment, or customer return  
Reference ID | Transaction ID, such as a shipment ID or adjustment ID  
Quantity | Unit quantity for the transaction  
Fulfillment center | Fulfillment center where the inventory is stored  
Disposition | Status of the product, such as sellable or damaged  
Reason (if available) | The downloaded report displays codes, while the online report shows descriptions. View the **Adjustment types and reason codes** table below for a full list of codes and descriptions.   
Country | Country where the inventory is stored   
Reconciled quantity | Number of units that have been reconciled with other adjustment events  
Unreconciled quantity | Number of units that have not been reconciled with other adjustment events  
Date and Time | The date and time of the event. Included in downloaded reports only.   
  
## Adjustment types and reason codes

Adjustment-type rows in the Inventory Ledger report's detailed view show the
history of adjustments to your inventory in response to issues such as
disposition changes, misplaced inventory, found inventory, and ownership
corrections.

Inventory adjustments are categorized by type and reason code.

  * The type shows whether an adjustment is an increase or decrease to your inventory level. 
  * The reason code describes the adjustment that was made. 

Inventory adjustments often occur in pairs. For example, if your inventory
changes disposition from sellable to expired, there will be two adjustments to
your inventory: a decrease in your sellable inventory and an increase in your
expired inventory. Here is an example:

Date | Fulfillment network SKU (FNSKU) | ASIN | Merchant SKU | Title | Event type | Disposition | Fulfillment center | Reason | Quantity | Reference ID | Country  
---|---|---|---|---|---|---|---|---|---|---|---  
05/26/2021  | X0000COYXD | X0000COYXD | 2Y-IQFY-RUQV | How Deep Lies the Shadow | Adjustments | Sellable | LEJ1 | Inventory disposition change | -1 | 13895071006 | US  
05/26/2021  | X0000COYXD | X0000COYXD | 2Y-IQFY-RUQV | How Deep Lies the Shadow | Adjustments | Expired | LEJ1 | Inventory disposition change | 1 | 13895071060 | US  
  
The following table lists all inventory adjustment reason codes and their
type.

Code  | Type | Reason | Definition  
---|---|---|---  
6  | - | Damaged at Amazon fulfillment center | A decrease to your carrier-damaged inventory level. This code is always followed by a P code increase to your fulfillment-center-damaged inventory level.  
7  | - | Damaged at Amazon fulfillment center | A decrease to your expired inventory level. This code is always followed by a P code increase to your fulfillment-center-damaged inventory level.  
E  | - | Damaged at Amazon fulfillment center | A decrease to your sellable inventory level. This code is always followed by a P code increase to your fulfillment-center-damaged inventory level.  
H  | - | Damaged at Amazon fulfillment center | A decrease to your customer-damaged inventory level. This code is always followed by a P code increase to your fulfillment-center-damaged inventory level.  
K  | - | Damaged at Amazon fulfillment center | A decrease to your defective inventory level. This code is always followed by a P code increase to your fulfillment-center-damaged inventory level.  
U  | - | Damaged at Amazon fulfillment center | A decrease to your distributor-damaged inventory level. This code is always followed by a P code increase to your fulfillment-center-damaged inventory level.  
D | - | Inventory disposed of | A decrease to your inventory level because inventory has been disposed of  
F  | + | Inventory found | An increase to your inventory level because missing inventory has been found  
N  | + | Inventory found | An increase to your inventory level because inventory that was incorrectly assigned has been transferred to your account or because you received an Amazon reimbursement   
M | - | Inventory misplaced | A decrease to your inventory level because inventory is missing from a bin location in a fulfillment center   
5  | - | Inventory misplaced | A decrease to your inventory level because inventory is missing from a bin location in a fulfillment center  
3  | + | Product redefinition transfer in | Two products with separate identifiers (SKUs) are determined to be the same item. One SKU will be removed from your inventory (code 4) and added (code 3) as the other SKU.   
4  | - | Product redefinition transfer out | Two products with separate identifiers (SKUs) are determined to be the same item. One SKU will be removed from your inventory (code 4) and added (code 3) as the other SKU.   
O | - | Inventory correction | Units that have been transferred out of your account because they were incorrectly received into your inventory or because Amazon has reimbursed you for them  
P  | + | Inventory disposition change | Units of a certain disposition are added to your inventory after the removal from a different disposition. This code always follows a code 6, 7, E, H, K, U, or Q adjustment.  
Q | - | Inventory disposition change | Units of a certain disposition are removed from your inventory and then added back to your inventory as a different disposition. This code is always followed by a P code adjustment.  
G | - | Inventory disposed of | Inventory was removed as part of a donation to charity.  
  
## Inventory dispositions

Inventory disposition represents the physical state of a unit or units. They
do not indicate if they unit is available to be picked, packed or shipped.

Inventory disposition | Inventory state | Definition  
---|---|---  
Sellable | Sellable | Inventory that looks and functions as described in the listing. This doesn’t indicate if the unit is available to be picked, packed or shipped. For more information, go to [FBA Inventory](/reportcentral/FBA_MYI_UNSUPPRESSED_INVENTORY/1) report.  
Defective | Unsellable | Inventory that does not look or function as described in the listing and is not visibly damaged, such as a recalled product  
Customer damaged | Unsellable | Inventory that was damaged by a customer  
Distributor damaged | Unsellable | Inventory that was damaged by the seller, vendor, or distributor during receiving  
Fulfillment center damaged | Unsellable | Inventory that was damaged at an Amazon fulfillment center  
Carrier damaged | Unsellable | Inventory that was damaged by a carrier during receiving, while in transit to the buyer, or while in transit back to Amazon due to a return  
Expired | Unsellable | Inventory that has passed its expiration date   
  
**Tip:** You can save on fees by removing inventory that is unsellable.

## How to read your report: online and download methods

You can view adjustments to your inventory online in Seller Central or by
downloading the Inventory Ledger report’s detailed view.

  * The **View online** method is recommended for quickly viewing inventory adjustments and reconciliations. When there is a reconciliation for an inventory adjustment, a link is provided that will connect you to either the reconciliation adjustment in the Inventory Ledger report’s detailed view or the reimbursement transaction in the Reimbursement report. 
  * The **Download** method is recommended for understanding the reconciliation status of inventory adjustments at scale. 

**To view your inventory adjustments online, follow these steps:**

  1. In the [Inventory Ledger report](/reportcentral/LEDGER_REPORT/0), click **View online**. 

  2. Select **Detailed view** and in the **Date range** drop-down menu select the desired date range.

  3. If you want to filter the results further, add the **Merchant SKU** , **Fulfillment Network SKU** , or **ASIN** , or any combination of those identifiers. 

  4. Click **Generate report**.

**Note:** If there are more than 50 inventory adjustments, the report will
generate multiple pages. Use the quick links at the top and bottom right of
the report to navigate between pages.

Here is an example of a report that was generated with the selected reason
group **Lost** , the date range **Last 365 days** , and the **FNSKU** X001SL.
Clicking **Inventory misplaced** in the report’s **Reason** column opens the
reconciliation status.

Date | Fulfillment network SKU (FNSKU) | ASIN | Merchant SKU | Title | Event type | Disposition | Fulfillment center | Reason | Quantity | Reference ID | Country  
---|---|---|---|---|---|---|---|---|---|---|---  
05/26/2021  | X001SL | B0000COYXD | SLU_2PK | How Deep Lies the Shadow | Adjustments | Sellable | LGB3 |  Inventory misplaced | -16 | 2108808 | US  
Inventory found | 5  
Remaining misplaced or damaged inventory | 11  
  
  5. Clicking the **Inventory found** reconciliation status will display the reconciliation events. As shown in the table below, a total quantity of five can be seen for five **Inventory found** adjustment reasons.

Date | Fulfillment network SKU (FNSKU) | ASIN | Merchant SKU | Title | Event type | Disposition | Fulfillment center | Reason | Quantity | Reference ID | Country  
---|---|---|---|---|---|---|---|---|---|---|---  
05/26/2021  | X001SL |  B0000COYXD | SLU_2PK | How Deep Lies the Shadow | Adjustments | Sellable | JFK8 | Inventory found | 1 | 2108808 | US  
05/26/2021  | X001SL | B0000COYXD | SLU_2PK | How Deep Lies the Shadow | Adjustments | Sellable | PHX6 | Inventory found | 1 | 210190912 | US  
05/26/2021  | X001SL | B0000COYXD | SLU_2PK | How Deep Lies the Shadow | Adjustments | Sellable | MGE7 | Inventory found | 1 | 2101901 | US  
05/26/2021  | X001SL | B0000COYXD | SLU_2PK | How Deep Lies the Shadow | Adjustments | Sellable | MKE1 | Inventory found | 1 | 210188746 | US  
05/26/2021  | X001SL | B0000COYXD | SLU_2PK | How Deep Lies the Shadow | Adjustments | Sellable | MAN4 | Inventory found | 1 | 21188081 | US  
  
**Note:** For **Remaining misplaced or damaged inventory** , you may be
eligible for reimbursement under the [FBA inventory reimbursement
policy](/gp/help/200213130).

**To download your Inventory Ledger report and view adjustments, follow these
steps:**

  1. In the [Inventory Ledger report](/reportcentral/LEDGER_REPORT/0), click **Download**. 

  2. Select **Detailed view** and in the **Date range** drop-down menu select the desired date range. 

  3. If you want to filter the results further, add the **Merchant SKU** , **Fulfillment Network SKU** , or **ASIN** , or any combination of those identifiers. 

  4. Click either **Request .csv download** or **Request .txt download** for the format that you prefer. 

  5. Once the report status changes from **In progress** to **Download** , click the **Download** button. 

  6. Save the file and open the report in a spreadsheet or database program, such as Microsoft Excel or Microsoft Access. 

Here is an example:

Date | FNSKU | ASIN | MSKU | Title | Event type | Reference ID | Quantity | Fulfillment center | Disposition | Reason | Country | Reconciled quantity | Unreconciled quantity  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
05/26/2021  | X001SL | B0000COYXD | SLU_2PK | How Deep Lies the Shadow | Adjustments | 21188081 | -16 | LGB3 | Sellable | M | US | 5 | 11  
  
You can get more information in the online view about the reconciled
quantities with reason codes for **Damaged at Amazon fulfillment center** ,
**Inventory misplaced** , or **Inventory found**.

For unreconciled quantities with reason codes for **Damaged at Amazon
fulfillment center** and **Inventory misplaced** , you may be eligible for
reimbursement under the [FBA inventory reimbursement
policy](/gp/help/200213130).

## Reconciliation events

Inventory adjustments for **Inventory misplaced** , **Inventory found** , and
**Damaged at Amazon fulfillment center** will have corresponding
reconciliations. These reconciliations may be across different SKUs for the
same or different products. This occurs when physical product is incorrectly
labeled or a different product was shipped than what was expected to be
received by Amazon (case of item substitution).You can view these
reconciliations in both the online and downloadable view.

**Online**

When there is a reconciliation for an inventory adjustment, a link is provided
that will connect you to either the reconciliation adjustment in the Inventory
Ledger report’s detailed view or the reimbursement transaction in the
Reimbursement report.

**Downloadable**

You will be able to view **reconciled** and **unreconciled** quantity columns
for **Inventory misplaced** , **Inventory found** , and **Damaged at Amazon
fulfillment center**. For example, when an inventory adjustment is reimbursed
or reconciled, you will see the unreconciled quantity decrease and the
reconciled quantity increase.

Here is an example from the online view:

Date | Fulfillment network SKU (FNSKU) | ASIN | Merchant SKU | Title | Event type | Disposition | Fulfillment center | Reason | Quantity | Reference ID | Country  
---|---|---|---|---|---|---|---|---|---|---|---  
05/26/2021  | X001SL | B0000COYXD | SLU_2PK | How Deep Lies the Shadow | Adjustments | Sellable | LGB3 |  Inventory misplaced | -16 | 2108808 | US  
Inventory found  
Remaining misplaced or damaged inventory  
  
Here is an example from the download view:

Date | FNSKU | ASIN | MSKU | Title | Event type | Reference ID | Quantity | Fulfillment center | Disposition | Reason | Country | Reconciled quantity | Unreconciled quantity  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
05/26/2021  | X001SL | B0000COYXD | SLU_2PK | How Deep Lies the Shadow | Adjustments | 21188081 | -16 | LGB3 | Sellable | M | US | 5 | 11  
  
The following table lists all possible original event and reconciliation event
combinations.

Inventory adjustment reason | Reconciliation reason (displayed in drop-down menu) | Definition  
---|---|---  
Damaged at Amazon fulfillment center | Inspected and disposition corrected | Inventory that an inspection found was not damaged at the fulfillment center  
Reimbursed | Inventory for which you have been reimbursed  
Remaining misplaced or damaged inventory | The remaining inventory that has not been reconciled  
Inventory misplaced | Inventory found | Misplaced inventory that was found  
Reimbursed | Inventory for which you have been reimbursed  
Damaged inventory misplaced |  **Damaged at Amazon fulfillment center** inventory that was misplaced.  **Note:** The reconciliation will be applied to the **Damaged at Amazon fulfillment center** inventory.   
Remaining misplaced or damaged inventory | The remaining inventory that has not been reconciled  
Inventory found | Replacement inventory found | Inventory that was replaced to compensate for inventory that was lost or damaged, in accordance with the [FBA inventory reimbursement policy](/gp/help/200213130).  
Missing inventory found | Misplaced inventory that was found  
Inventory ownership correction | Incorrectly assigned found inventory that was moved to the correct owner  
  
**Note:** Inventory adjustments other than **Inventory misplaced** ,
**Inventory found** , and **Damaged at Amazon fulfillment center** will not
show a reconciliation reason in the online view or the downloadable view.

**Note:** In case of reconciliation with different SKU of the same or
different product (in case of item substitution), in the Inventory Ledger
Report, your inventory in the Amazon network for the found SKU item will
account for the original misplaced SKU inventory defect.

## Why are my items being researched?

You will notice a new inventory classification on the **FBA inventory** page
and report, called **Researching**. This represents the misplaced or
fulfillment-center-damaged inventory that is actively being confirmed at our
fulfillment centers.

A timeline shows the duration of the research, which will never exceed 60
days. Once the inventory that is being researched has been reimbursed or has
exceeded the 60-day duration, you will see the corresponding adjustment move
to the Inventory Ledger report’s detailed view.

Why do I see my product being found as merchant SKU “Amazon.Found.Bxxxxxxxxx”?

When your product is not labeled correctly it is received as non-labeled
inventory for the same ASIN, with merchant SKU as Amazon.Found.Bxxxxxxxxx Or,
if you ship a different product than what we expected to receive and it is not
the same ASIN, the received product is assigned to you as merchant SKU
Amazon.Found.Bxxxxxxxxx. These merchant SKUs are created so that your product
can be assigned back to your account. Since these are your products, you can
sell them to customers by creating an offer listing for the
Amazon.Found.Bxxxxxxxxx merchant SKU. These products will appear in Stranded
inventory report if you do not have an active listing for
Amazon.Found.Bxxxxxxxxx. If you create a listing for the
Amazon.Found.Bxxxxxxxxx merchant SKU, your inventory for this merchant SKU
will be subject to virtual tracking. Rest of your labeled inventory is not
affected.

