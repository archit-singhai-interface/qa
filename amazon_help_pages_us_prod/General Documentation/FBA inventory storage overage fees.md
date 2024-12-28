---
title: FBA inventory storage overage fees
url: https://sellercentral.amazon.com/help/hub/reference/GV8JEETWV9Q33CMX
section: General Documentation
---

**Important:** Effective July 1, 2024, we will no longer be charging FBA
inventory storage overage fees in the United States, Europe, United Kingdom,
and Canada stores.

If your inventory in Amazon's fulfillment centers (not including open
shipments) exceeds your capacity limit, you will be charged an **inventory
storage overage fee** in addition to [monthly inventory storage
fees](/gp/help/200612770) and, if applicable, an [aged inventory
surcharge](/gp/help/GJQNPA23YWVA4SBD).

The overage fee is based on how many days your capacity limits are exceeded,
and is calculated using the highest limit, either estimated or confirmed, that
we've provided for the given period.

This charge will occur even if your capacity usage is subsequently reduced to
a level below your capacity limits for that period. It will be charged monthly
at $10 per cubic foot based on the daily average volume (measured in cubic
feet) for any space your inventory occupies in fulfillment centers beyond your
capacity limits. For more information, go to [FBA capacity
limits](/gp/help/GAFNWEYTJUV2GBFC).

The volume measurement is based on unit size when properly packaged and ready
to ship in accordance with [FBA policies and
requirements](/gp/help/201030350).

Amazon reserves the right to measure or weigh packaged units or representative
samples and to determine the storage type. In the event of any conflict
between an Amazon measurement and information provided by the seller, Amazon's
measurement will govern.

**The following chart shows how the inventory storage overage fee is
calculated for one day.**

Line | Description | Details | Calculation | Example value  
---|---|---|---|---  
1 | Charged Date | Date the usage exceeded the limit and when the estimated fee applies. The format is month-day-year. | Based on date of overage | 9/1/2023  
2 | Charge Rate | Monthly inventory storage overage fee rate for a storage type. | Set by Amazon | $10 per cubic foot  
3 | Capacity Usage Volume | Capacity usage on the charge date. This applies to the storage type for which usage exceeded the limit and an estimated fee applies. | Based on seller’s usage volume | 600 cubic feet  
4 | Capacity Limit | Capacity limit for the storage type that exceeded its limit and for which an estimated fee applies. | Set by Amazon | 500 cubic feet  
5 | Overage Volume | The volume of capacity usage that exceeded the storage-type capacity limit on the charged date. | Line 3 - Line 4 | 100 cubic feet  
6 | Daily Overage Rate | The charge per day per cubic foot . | $10 (Line 2)/number of days in the month | $0.33  
7 | Charged Fee Amount | Amount of the inventory storage overage fee that was incurred by this storage type on the charged date. | Overage Volume (Line 5) x Daily Overage Rate (Line 6) | $33  
  
##  Determining capacity limit status

You can view your capacity limits and capacity usage in the Capacity Monitor
on the [FBA dashboard](/fba/dashboard/?ref=fbacentral_nav_fba) or [Inventory
Performance dashboard](/inventory-performance/dashboard) or in the [Shipping
Queue](/gp/fba/inbound-queue/index.html/). You’ll see an alert if your on-hand
inventory is over your capacity limit. We'll also send you monthly alerts if
you're over your limit for each storage type and you'll incur inventory
storage overage fees.

## Inventory Storage Overage Fees report

The [Inventory Storage Overage Fees
report](/reportcentral/OVERAGE_FEE_CHARGES/1) provides the inventory storage
overage fees for each storage type and day your inventory in fulfillment
centers exceeded your storage limits. This month-end report is available for
download starting the second day of the following month. It's available from
the **Reports** menu by selecting **Fulfillment** and on the resulting page
selecting **Inventory storage overage fees** under **Payments** on the left.

**Report field names**

Download header | Description | Example value  
---|---|---  
charged_date | Date the usage exceeded the limit and when the estimated fee applies. The format is month-day-year. | 8/1/2020  
country_code | Country in which the overage usage occurred. | US  
storage_type | Type of storage for which the usage exceeded the limit and an estimated fee applies. | Sortable (Standard-size) or Non_Sortable (Oversize)  
charge_rate | Monthly inventory storage overage fee rate for a storage type. | 10.00  
capacity_usage_volume | Capacity usage on the charge date. This applies to the storage type for which usage exceeded the limit and an estimated fee applies. | 600  
capacity_limit | Capacity limit for the storage type that exceeded its limit and for which an estimated fee applies. | 500  
overage_volume | The volume of capacity usage that exceeded the storage-type capacity limit on the charged date. | 100  
volume_unit | Unit of measurement for the capacity limit, usage, and overage. | cubic feet  
charged_fee_amount | Amount of the inventory storage overage fee that was incurred by this storage type on the charged date. | 32.26  
currency_code | Currency of the overage fee. | USD  
  
## How we calculate the monthly inventory storage overage fee estimate

We provide an estimate of your monthly inventory storage overage fee by
storage type using the following formula:

Estimated monthly overage fee = (current overage x daily overage rate x charge
days remaining in month) + monthly overage fees incurred to date

Current overage = current usage – current limit

Daily overage rate = $10 / number of days in current month

Charge days remaining in month = number of days in current month – current day
number + 1

## Calculate cubic feet from inches

  1. Multiply length x width x height in inches to get the volume in cubic inches. 

  2. Divide by 1,728.

**Example:** A unit measuring 47 x 12 x 10 inches divided by 1,728 = 3.3 cubic
feet.

## Frequently asked questions

#### How do I know if I'm subject to the inventory storage overage fee?

If you have a Professional selling account that’s been active in FBA for more
than 39 weeks, you are subject to inventory storage limits. If you’ve exceeded
your current limits for a given storage type by the end of the day, for any
day in a given month, you’ll be subject to the overage fee. This charge will
occur even if your inventory was subsequently reduced to a level below your
capacity limits allocated for that month.

#### How can I determine what inventory is contributing to my current usage
for a storage type?

Current usage is a real-time representation of your inventory at a fulfillment
center minus any pending removals. Open shipments count toward your total
capacity usage but are not included in the overage calculation. [FBA
Inventory](/inventoryplanning/manageinventoryhealth) provides a list of all of
your active FBA listings, along with their storage type (standard-size,
oversize, apparel, footwear, flammable, or aerosol) and how much volume the
ASIN is taking up (available units x volume per unit = cubic feet).

While using Manage Inventory Health is a good way to approximate current
usage, it may not match your current usage value shown on the Capacity Monitor
on the [FBA dashboard](/fba/dashboard), [Inventory Performance
dashboard](/inventory-performance/dashboard), or [Shipping
Queue](/gp/ssof/shipping-queue.html?ref=fbacentral_nav_fba#fbashipment).
Storage volume in the Inventory Age report and on the Manage Inventory Health
page equals the available inventory. The current usage by storage type that is
shown on your capacity monitor equals the available inventory plus
unfulfillable and reserved units minus units that are pending removal or
liquidation.

#### When will I be charged inventory storage overage fees?

You'll be charged applicable inventory storage overage fees after the end of
the month in which the fees were incurred. For example, let’s say that you
exceeded your storage limit on July 1 and removed inventory to a level below
your limit by July 5. On August 1, you would be charged for the four days you
were over the limit in July.

#### Do inventory storage overage fees apply to flammable and aerosol storage?

No, overage fees only apply to standard-size, oversize, apparel, and footwear
storage types.

#### Why do I have overage fees when I don't have any excess inventory?

If your inventory at a fulfillment center exceeds your capacity limits for a
given month, you'll be charged an inventory storage overage fee. Your FBA
capacity limit is influenced by your IPI score, as well as other factors such
as sales forecasts for your ASINs, shipment lead time, and fulfillment center
capacity. For more information about how capacity limits are determined, go to
[FBA capacity limits](/gp/help/GAFNWEYTJUV2GBFC).

For information about how excess inventory is calculated, go to [Inventory
Performance](/gp/help/202174810).

If you're over your capacity limits but you don't have excess inventory, we
suggest you reduce or remove your oldest or slowest-moving inventory as soon
as possible.

#### What if I believe I've been charged incorrectly for overage fees?

If you believe you've been charged incorrectly, you can submit a reimbursement
request within 90 days of the date the fee was charged.

To see if you're eligible for an overage fee reimbursement due to dimension
issues, go to [FBA fees reimbursement policy: Weight and
dimensions](/gp/help/GGL7U4JFSDXUTQAJ).

