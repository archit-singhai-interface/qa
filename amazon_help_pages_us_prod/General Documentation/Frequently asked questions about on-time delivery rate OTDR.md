---
title: Frequently asked questions about on-time delivery rate (OTDR)
url: https://sellercentral.amazon.com/help/hub/reference/G200847280
section: General Documentation
---

## What is Amazon’s policy for on-time delivery without promise extensions?

Effective September 25, 2024, you must maintain a minimum 90% on-time delivery
rate (OTDR) without promise extensions to have seller-fulfilled products
listed on Amazon.com. An OTDR below 90% can result in restriction of your
ability to have seller-fulfilled products listed. For a great customer
experience, we recommend that you maintain a 95% or greater OTDR for all
seller-fulfilled orders.

## What is changing?

Our updated policy requires a minimum 90% OTDR without promise extensions to
have seller-fulfilled products listed on Amazon.com. An OTDR below 90% can
result in restriction of your ability to have seller-fulfilled products
listed. To help provide a positive customer experience, we recommend that you
maintain a 95% or greater OTDR for all seller-fulfilled orders.

We are also changing the way we measure OTDR to now measure the percentage of
your tracked seller-fulfilled units that were delivered on or before the
seller-promised "Deliver by" date _prior to_ promise extensions being added.
Before this change, OTDR was measured after promise extensions were added.
Promise extensions are additional days that we may add to the delivery date to
account for logistical factors that may delay a delivery such as extreme
weather, transportation network constraints, or recent history of a seller
delivering shipments after their set delivery date. This policy does not apply
to offers using the Fulfillment by Amazon (FBA) service because sellers are
not responsible for on-time delivery promises for FBA orders.

**Note:** We will communicate as we roll out the OTDR policy, and any changes
from the policy as it stands today, that may affect you.

## What will happen to my account if my OTDR falls below the 90% minimum
requirement?

An OTDR below 90% can result in restriction of your ability to have seller-
fulfilled products listed. If that happens, we’ll notify you of the policy
violation and you can appeal by clicking the **Submit appeal** button at the
top of your [Account Health](/performance/dashboard?ref=ah_em%20_op) dashboard
to request reinstatement of your capabilities to list seller-fulfilled
products.

The request will be reviewed within 72 hours and should include the following
information:

  * The issues that led to a low on-time delivery rate
  * The actions that you’ll take to improve your on-time delivery rate
  * The steps that you’ve taken to prevent future issues regarding on-time delivery

On subsequent policy violations, if your OTDR is still below 90%, you can
appeal by clicking **Submit appeal** at the top of your Account Health
dashboard.

To get reinstated, the following is required:

  * If you have an Individual selling plan or a Professional selling plan shipping from countries outside of the US or China, you must submit an appeal request that indicates how you’ll improve OTDR.
  * If you’re a Professional seller who ships from the US and China, you’ll be required to meet the 90% OTDR requirement by using the following Amazon free-to-use fulfillment and shipping tools for your seller-fulfilled orders for the next 180 days:
    * [Shipping Settings Automation](http://go.amazonsellerservices.com/ssa-otdr-launch) (SSA) to set accurate delivery dates through automated transit time calculations of your preferred ship methods.
    * [Automated handling time](http://go.amazonsellerservices.com/aht-otdr-launch) to set accurate handling times per SKU, based on how long it usually takes you to pass each SKU to carriers. For new SKUs, the default handling time will apply until there are enough shipments for your automated handling time to be calculated. 
    * [Amazon Buy Shipping](http://go.amazonsellerservices.com/abs-otdr-launch) to buy shipping labels that use highly reliable shipping methods for both Professional and Individual selling plans. You can use Amazon Buy Shipping through [Manage Orders](/orders-v3/ref=xx_myo_favb_xx), [Shipping API](https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference), [Veeqo](http://go.amazonsellerservices.com/veeqo-otdr-launch), or [select multi-channel integrators](/help/hub/reference/GZZPMC9QLNBX48RP) with access to Amazon Buy Shipping. 

## How is OTDR calculated?

OTDR measures the percentage of your tracked seller-fulfilled units that were
delivered on or before the seller-promised "Deliver by" date. OTDR is the
average of all of your tracked shipped units, not just a specific SKU or
shipment.

To calculate OTDR without promise extensions, we’ll consider a 14-day window
of time. We’ll pull data from shipments that had a promised delivery date in
the last 21 days, and exclude the most recent 7 days as the shipments from
last 7 days may still be in the process of being delivered. For example, if
you had 130 units with a promised delivery date in the last 21 days, and 30 of
those has a promised delivery date in the last 7 days, OTDR will be calculated
excluding the 30 units from the last 7 days (130 – 30 =100). Of those 100
units delivered, if 90 were delivered on or before the promised "Deliver by"
date, your OTDR would be 90%.

Seller’s promised “Deliver by” date is calculated using seller-set handling
and transit time, prior to the addition of promise extensions. This date may
be different than the delivery date shown to customers if promise extensions
were added.

For example, for a seller with a set handling time of 1 day and set transit
time of 2 days:

  * The promised “Deliver by” date will be in 3 business days.
  * So, if an order is received on a Monday, this order would need to be delivered by Thursday (seller-promised “Deliver by” date) to be considered delivered on time.
  * However, if 1 day of promise extensions was added to that offer, the promised delivery date the customer saw while purchasing would have been Friday. Irrespective of the date shown to the customer (Friday), sellers must deliver by their set “Deliver by” date (Thursday) for the shipment to be considered delivered on-time.

Shipped units will be considered as OTDR compliant if either the delivery
occurred on or before the “Deliver by” date shown on Seller Central, or the
following 3 conditions were met:

  * The shipped SKU was assigned to a shipping template with Shipping Settings Automation (SSA) enabled.
  * Your account has automated handling time enabled.
  * You bought an “OTDR Protected” shipping label on Amazon Buy Shipping.

**Note:** OTDR Protection is currently only applicable to Professional sellers
who ship from the US and China. We will let you know once this changes.

**Note:** For the US store, the "Deliver by" date is measured in Pacific Time
(PST/PDT). For example, if an order has a "Deliver by" date of Jan 1, all
items in the order must be delivered by Jan 1, 11:59:59 p.m. PST/PDT to be
OTDR compliant.

## Does Amazon offer tools that can help me improve my OTDR and meet the
Amazon’s OTDR requirements?

Yes. You can manage your delivery dates using the tools we’ve provided, or you
can manually adjust your **Transit time** and **Handling time** settings. We
designed these tools to set accurate delivery dates, reduce late deliveries,
and to meet or exceed the minimum OTDR requirement. And because Amazon is
making calculations on your behalf that affect OTDR, you'll get OTDR
protection from late deliveries on units shipped through standard shipping if
you use all three tools as follows:

  * [Shipping Settings Automation](http://go.amazonsellerservices.com/ssa-otdr-launch) (SSA), for Professional selling plans, sets accurate delivery dates through automated transit time calculations of your preferred shipping services. You must choose one of the preferred ship methods in the SSA templates, which will mark the transit time on the shipping template as "Managed by Amazon".
  * [Automated handling time](http://go.amazonsellerservices.com/aht-otdr-launch), for Professional selling plans, sets accurate handling times per SKU based on how long it usually takes you to pass each SKU to carriers. You must ensure that automated handling time is enabled in your shipping settings.
  * [Amazon Buy Shipping](http://go.amazonsellerservices.com/abs-otdr-launch), for both Professional and Individual selling plans, sells shipping labels that use highly-reliable ship methods. You can use Amazon Buy Shipping through [Manage Orders](/orders-v3/ref=xx_myo_favb_xx), [Shipping API](https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference), [Veeqo](http://go.amazonsellerservices.com/veeqo-otdr-launch), or [select multi-channel integrators](/help/hub/reference/GZZPMC9QLNBX48RP) with access to Amazon Buy Shipping. You must choose shipping labels marked as “OTDR Protected” when using Amazon Buy Shipping or Veeqo.

**Note:** OTDR Protection is only available for units shipped through Standard
Shipping, units shipped through other shipping options such as Free Economy,
Standard Prime, or Premium Shipping, are not eligible for OTDR protection.

For example, if a seller shipped 100 units and 15 were delivered late:

  * Scenario A: If a seller **did not use all three** of Amazon’s free fulfillment and shipping tools for any of those 15 late deliveries, all 15 of their late deliveries will negatively impact their OTDR. As a result, their OTDR will be (100-15/100) = 85%.
  * Scenario B: If a seller **used all three** of Amazon’s free fulfillment and shipping tools for 5 of those 15 late deliveries, only the 10 late shipments that were not using Amazon’s tools will negatively impact OTDR. As a result, the seller’s OTDR will be (100-10/100) = 90%.

**Note:** OTDR Protection is currently only applicable to Professional sellers
who ship from the US and China. We will let you know once this changes.

## Can I be exempted from the OTDR requirement if delivery delays are caused
by weather or carrier network issues beyond my control?

Sellers must meet the 90% OTDR requirement without promise extensions.
However, if there is a major disruption event that impacts all sellers
shipping to a specific region, Amazon will not count deliveries that are late
as a result in your OTDR. Whether a disruption is considered to be major is a
discretionary decision made by Amazon.

## What changes are you making to handling time and transit time settings?

**Transit time changes:** As of August 25, 2024, transit time requirements
were updated to further align with the delivery capabilities of shipping
services. If you’re shipping within the contiguous US (excluding Hawaii,
Alaska, and US territories), you can set a maximum transit time of five days
for standard shipping (previously eight days) and eight days for free economy
shipping (previously 10 days). To learn more, go to [Default transit
time](/help/hub/reference/G202169120).

Starting October 25, 2024, the transit time settings for shipping from China
to the continental US (all states in the contiguous US, excluding Hawaii,
Alaska, and US protectorates) will change. You’ll have more transit time
ranges to choose from on your shipping templates, with options ranging from
2-4 days to 14-20 days. The maximum transit time will be reduced from 28 days
to 20 days. If you have 14-28 days as your manually set transit time prior to
October 25, it will be automatically updated to 14-20 days as a part of this
change.

**Note:** The five-day maximum transit time applies to all SKUs except media,
such as Books, Magazines, and DVDs.

**Handling time automation:** As of September 25, 2024, to improve handling
time accuracy, automated handling time was enabled for sellers who have a
handling time gap of two days or more between their set handling time and
their actual handling time. To help you keep in good standing with other
account health metrics related to handling time, if you have automated
handling time enabled, your seller-fulfilled listings will not be deactivated
if your late shipment rate (LSR) does not meet the [LSR policy
requirement](/help/hub/reference/G200285190). To see your handling time gap,
review your [Fulfillment Insight dashboard](/seller-fulfilled-
product/analytics/ref=xx_msfp_dnav_xx#FULFILLMENT_INSIGHT_DASHBOARD).

## How can I view my on-time delivery (OTD) metric and report?

To view your OTD metrics and report on Seller Central:  

  1. On the **Performance** menu, select [Account Health](/performance/dashboard).
  2. Locate the Shipping Performance section and select **On-time delivery rate**.
  3. You can see your [OTDR metric](/performance/detail/shipping?t=otd&ref=sp_st_dash_csp_otd) on the Shipping Performance page. Only orders included in the current OTD defect report count against the OTDR metric. If the report contains no orders, it means either all of the units in those orders were delivered on time or they were fulfilled using Amazon’s free fulfillment tools.
  4. To download the OTD defect report, click **View details** and then **Download report**.

**Important:** Allow 72 hours for the report and metrics to reflect any
updates or edits.

## How can I maintain a healthy OTDR?

To keep a healthy OTDR without promise extensions we recommend that you do the
following:

  * Review your OTDR without promise extensions metric on your [Account Health dashboard](/performance/dashboard?ref=ah_em%20_op). You can also download a report of which orders were delivered after the delivery date without promise extensions.
  * Review the “Deliver by” date for every order. This date corresponds to the expected delivery date without promise extensions. Note that the actual delivery date that customers see may be longer because of promise extensions. 
  * If you are a Professional seller, use [automated handling time](http://go.amazonsellerservices.com/aht-otdr-launch) to set accurate handling time per SKU based on how long it has taken you historically to hand off each SKU to carriers. Additionally, with automated handling time enabled, your seller-fulfilled listings will not be deactivated if your late shipment rate (LSR) does not meet the [LSR policy requirement](/help/hub/reference/G200285190).
  * If you are a Professional seller, enable [Shipping Settings Automation](http://go.amazonsellerservices.com/ssa-otdr-launch) (SSA), which sets accurate delivery dates for your orders by automatically calculating transit times of your preferred ship methods from your warehouse to each customer's location.
  * Select a ship method with a high reliability to deliver your order on time. You can also use [Amazon Buy Shipping](http://go.amazonsellerservices.com/abs-otdr-launch) to buy shipping labels that have been identified to have a high reliability for On-time delivery based on Amazon’s data from millions of shipments. These ship methods have a shield icon next to them, marked as **OTDR Protected**. You can use Amazon Buy Shipping through [Manage Orders](/orders-v3/ref=xx_myo_favb_xx), [Shipping API](https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference), [Veeqo](http://go.amazonsellerservices.com/veeqo-otdr-launch), or [select multi-channel integrators](/help/hub/reference/GZZPMC9QLNBX48RP) with access to Amazon Buy Shipping. To learn more about purchasing OTDR protected shipping labels, go to [Amazon Buy Shipping](http://go.amazonsellerservices.com/abs-otdr-launch).

## What does OTDR protection for “Standard Shipping” mean?

You'll get OTDR protection from late deliveries on orders shipped using the
“Standard Shipping” option in your shipping template if you use all three
tools:

  * Shipping Setting Automation (SSA)
  * Automated Handling Time (AHT)
  * Amazon Buy Shipping.

OTDR protection is only applicable on Standard Shipping and will not be
applicable on Free Economy, Expedited Shipping and Premium Shipping (1-day and
2-day deliveries).

For more information about Shipping templates, go to [Create, edit, or delete
shipping templates](/help/hub/reference/G201834090).

**Note:** Customers can choose their preferred shipping option if you have
enabled multiple shipping options. Once you receive the order, you'll see the
chosen shipping option in [Manage Orders](/orders-v3/ref=xx_myo_dnav_xx).

## What counts as a received scan by a carrier?

A package is considered received by the carrier when they perform their first
scan. This typically occurs in two situations:

  * When carriers pick up packages from your location
  * When you drop off packages at carrier locations

In both cases, the package status changes to "received" after the initial
carrier scan.

## What happens if a customer is not available to receive an order, will it be
considered as delivered late if the carrier’s attempted delivery fail, and
will this impact my OTDR?

When a carrier attempts to deliver a package but fails due to customer
unavailability, we consider the date of this attempted delivery in calculating
your OTDR. This applies even if the actual delivery occurs later. For an
attempted delivery to count the carrier must document the attempt. Also, if
the package is redirected to a pick-up location, we still consider it
delivered on the initial attempt date.

If you notice any discrepancies in this process, contact Selling Partner
Support with the specific order number or tracking details for investigation.

