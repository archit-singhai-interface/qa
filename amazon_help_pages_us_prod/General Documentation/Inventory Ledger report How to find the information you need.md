---
title: Inventory Ledger report: How to find the information you need
url: https://sellercentral.amazon.com/help/hub/reference/GCRWH2T93NYDHBXU
section: General Documentation
---

On this page, you’ll learn how to use the [Inventory Ledger
report](/reportcentral/LEDGER_REPORT/0) as a replacement for the following
reports, which will be discontinued effective January 31, 2023:

  * Daily Inventory History 
  * Monthly Inventory History 
  * Inventory Event Detail 
  * Inventory Adjustments 
  * Received Inventory 
  * Inventory Reconciliation 

**Note:** We recommend that you start using the Inventory Ledger report now to
avoid disruption when these reports are discontinued. For more information, go
to our [Inventory Ledger report](/gp/help/G4FKT5KQWFFJ7LDN) help page.

Below, we provide details for each report that is being discontinued, as well
as steps on how to use the Inventory Ledger report to access the information
that is contained in the old report.

These instructions are generally applicable for viewing reports online,
downloading reports, or accessing reports via API. In cases where the
instructions vary based on how the report is accessed, we note that below.

If you download reports via API, go to our [developer
documentation](https://developer-docs.amazon.com/sp-api/docs/report-type-
values#inventory-reports) to learn more about setting request filters.

## Daily Inventory History report

This report provided daily inventory quantity, location, and disposition. To
get that information using the Inventory Ledger report, follow these steps:

  1. Go to the [Inventory Ledger report](/reportcentral/LEDGER_REPORT/0).

  2. Select **Summary view**.

  3. Under **Aggregate report by location** , select **Fulfillment center** or **Country**.

  4. In the **Aggregate report by time period** drop-down menu, select **Daily**.

  5. Click **Generate report**.

In the Daily Inventory History report, quantities that were in transit between
fulfillment centers were shown in a separate row, with ***XFR** appearing in
the **Warehouse ID** column. In the Inventory Ledger report's summary view,
these quantities are shown in an additional column called **In transit between
warehouses**. Adding up the quantities in the **In transit between
warehouses** column by fulfillment center or country will give you total in-
transit quantities equivalent to ***XFR**.

**Note:** If you are selling items in the Low-Cost Store, you can identify
them on the report by aggregating by **Country = CN**.

## Monthly Inventory History report

This report provided monthly inventory quantity, location, and disposition. To
get that information using the Inventory Ledger report, follow these steps:

  1. Go to the [Inventory Ledger report](/reportcentral/LEDGER_REPORT/0).

  2. Select **Summary view**.

  3. Under **Aggregate report by location** , select **Fulfillment center** or **Country**.

  4. In the **Aggregate report by time period** drop-down menu, select **Monthly**.

  5. Click **Generate report**.

In the Monthly Inventory History report, quantities that were in transit
between fulfillment centers were shown in a separate row, with ***XFR**
appearing in the **Warehouse ID** column. In the Inventory Ledger report's
summary view, these quantities are shown in an additional column called **In
transit between warehouses**. Adding up the quantities in the **In transit
between warehouses** column by fulfillment center or country will give you
total in-transit quantities equivalent to ***XFR**.

**Note:** If you are selling items in the Low-Cost Store, you can identify
them on the report by aggregating by **Country = CN** or **FC = XCND**.

## Inventory Event Detail report

This report included all your inventory events and allowed you to filter by
date range and event type. To get that information using the Inventory Ledger
report, follow these steps:

  1. Go to the [Inventory Ledger report](/reportcentral/LEDGER_REPORT/0).

  2. Select **Detailed view**.

  3. If desired, use the drop-down menu to filter by **Event type**. Filtering by event type will reduce the file size so that your report will be generated faster.

  4. Select a date range from the drop-down menu or enter a custom date range. 

  5. Click **Generate report**.

**Note:** The report will include all transactions, formerly called **Events**
, and the fulfillment center where the transaction took place, formerly called
**Warehouse ID**.

**Note:** If you are selling items in the Low-Cost Store, you can identify
their events by filtering for **FC = XCND**.

## Inventory Adjustments report

This report provided corrections and updates to your inventory in fulfillment
centers. To get that information using the Inventory Ledger report, take the
following steps:

  1. Go to the [Inventory Ledger report](/reportcentral/LEDGER_REPORT/0).

  2. Select **Detailed view**.

  3. In the **Event type** drop-down menu, select **Adjustments**.

  4. Select a date range from the drop-down menu or enter a custom date range. 

  5. Click **Generate report**.

**Tip:** If you’re looking for a particular adjustment and you’re using the
online view, you can filter for the adjustment in the **Reference ID** field
(**Reference ID** is equivalent to **Transaction item ID**). Filtering for
reference ID is available only in the online view. It isn’t available for
downloads or API access, because using this filter will return only one
record.

**Note:** If you download the report or access it via API, the report will
include **Reconciled quantity** and **Unreconciled quantity** columns, similar
to the Inventory Adjustments report.

**Note:** If you are selling items in the Low-Cost Store, you can identify
their events on the report by filtering for **FC = XCND**.

## Received Inventory report

This report showed inventory that has completed the receive process at
fulfillment centers. To get that information using the Inventory Ledger
report, follow these steps:

  1. Go to the [Inventory Ledger report](/reportcentral/LEDGER_REPORT/0).

  2. Select **Detailed view**.

  3. In the **Event type** drop-down menu, select **Receipts**. 

  4. Select a date range from the drop-down menu or enter a custom date range. 

  5. Click **Generate report**.

**Tip:** If you're looking for a particular shipment, you can filter for the
shipment in the **Reference ID** field (**Reference ID** is equivalent to
**FBA shipment ID**). Filtering for reference ID is available only in the
online view. It isn’t available for downloads or API access, because using
this filter will return only one record.

**Note:** If you are selling items in the Low-Cost Store, you can identify
their events on the report by filtering for **FC = XCND**.

## Inventory Reconciliation report

This report showed your net inventory details for a specific time period. It
was used to analyze your inventory movements to and from fulfillment centers,
including products that are sold, returned, removed, disposed of, damaged,
lost, and found. To get that information using the Inventory Ledger report,
follow these steps:

  1. Go to the [Inventory Ledger report](/reportcentral/LEDGER_REPORT/0).

  2. Select **Summary view**. 

  3. Under **Aggregate report by location** , select **Country**.

  4. In the **Aggregate report by time period** drop-down menu, select **Monthly**. You can also filter by **Merchant SKU** or **Fulfillment Network SKU (FNSKU)** if desired. 

  5. Select a date range from the drop-down menu or enter a custom date range. 

  6. Click **Generate report**.

**Tip:** To view details about a specific event from fields such as
**Returned** or **Received** in the Inventory Ledger report’s **Summary view**
, click the quantity link. Clicking that link will open a new tab for the
report’s **Detailed view** , with details on those events. This process
replaces the previous process, in which clicking a link in the Inventory
Reconciliation report would open the Inventory Adjustments or Inventory Event
Detail report.

**Note:** If you are selling items in the Low-Cost Store, you can identify
them on the report by aggregating by **Country = CN** or **FC = XCND**.

**Inventory that is in transit**

The Inventory Reconciliation report included **In transit** quantities in the
calculation of **Beginning quantity** and **Ending quantity**. The Inventory
Ledger report’s **Summary view** does not include in-transit quantities by
default. Instead, the report has an additional column called **In transit
between warehouses**. To get the same beginning or ending quantity as shown in
the Inventory Reconciliation report, use the calculations below:

  * Inventory Reconciliation report **Beginning quantity** = Inventory Ledger report **Starting warehouse balance** \+ **In transit between warehouses** at the end of the previous month or date range
  * Inventory Reconciliation report **Ending quantity** = Inventory Ledger report **Ending warehouse balance** \+ **In transit between warehouses** for the current month or date range

**Example:** Here is an example that compares the Inventory Reconciliation
report with the Inventory Ledger report.

Let’s say that you want to get reconciliation data for FNSKU X001SL for the
date range 7/1/2022 to 7/31/2022. Go to the Inventory Ledger report, select
**Summary view** , enter X001SL in the **Fulfillment network SKU (FNSKU)**
field, and enter the date range 6/1/2022 to 7/31/2022.

In the tables below, you can see a comparison of the output that you would
have gotten from the Inventory Reconciliation report and the output that you
will get from the Inventory Ledger report.

**Inventory Reconciliation report view**

Merchant SKU | Fulfillment Network SKU | ASIN | Title | Condition | beginning-quantity | ending-quantity | Received | FBA customer returns | found | sold | removed | lost | Inventory disposed of | Other | discrepant-quantity  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
SLU_2PK | X001SL | B0000COYXD | How Deep Lies the Shadow | SELLABLE | **21** | **10** | 11 | 0 | 0 | -22 | 0 | 0 | 0 | 0 | 0  
  
**Inventory Ledger report Summary view**

Date | FNSKU | ASIN | MSKU | Title | Disposition | Starting warehouse balance | In transit between warehouses | Receipts | Customer shipments | Customer returns | Vendor returns | Warehouse transfer in/out | Found | Lost | Damaged | Disposed | Other events | Ending warehouse balance | Unknown events | Location  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
7/22/2022 | X001SL | B0000COYXD | SLU_2PK | How Deep Lies the Shadow | SELLABLE | **20** | **0** | 11 | -22 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **10** | 0 | US  
6/22/2022 | X001SL | B0000COYXD | SLU_2PK | How Deep Lies the Shadow | SELLABLE | 31 | **1** | 0 | -10 | 0 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | US  
  
**Beginning quantity** = **Starting warehouse balance** (20) + **In transit
between warehouses** for previous month (1) = 21

**Ending quantity** = **Ending warehouse balance** (10) + **In transit between
warehouses** for current month (0) = 10

**Tip:** If the FNSKU has multiple dispositions on the Inventory Ledger report
(for example, **Sellable** and **Damaged**) be sure to add all of them when
you calculate the beginning and ending quantities.

