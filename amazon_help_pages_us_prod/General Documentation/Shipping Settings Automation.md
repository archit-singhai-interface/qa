---
title: Shipping Settings Automation
url: https://sellercentral.amazon.com/help/hub/reference/G8WRJF2N5B787XKQ
section: General Documentation
---

Shipping Settings Automation (SSA) is a feature on your shipping templates
that automatically calculates more accurate delivery dates for your customers
based on:

  * Your warehouse location
  * The location of the customers
  * Up-to-date carrier transit time for the shipping services you use based on data from their past deliveries

Enabling SSA will set automated transit times that reflect carrier's actual
delivery capabilities for the shipping services you already use, thus avoiding
manual transit time calculation efforts. It will also let you provide
customers with more accurate delivery promises, which will increase the
likelihood of them making a purchase and helping you to be featured more
frequently.

## Benefits of Shipping Settings Automation (SSA)

Customers like to buy products with fast and accurate delivery dates, which
requires you to calculate transit time and track the delivery capabilities of
the shipping services you use. This may be hard to do by yourself, and
consequently many sellers choose to set unnecessarily long transit times for
standard deliveries or limit fast delivery regions. This leads to buyers
seeing delivery dates that look less attractive. SSA can simplify this process
with just a few clicks.

By telling us where you ship from and what shipping services you use, Amazon
will apply more accurate transit times using the most recent carrier delivery
performance data. With SSA, your delivery promises will be more accurate and
attractive to customers.

SSA automates transit time calculation for the following seller-fulfilled ship
options:

  * Standard shipping for domestic and China-based warehouses.
  * Prime shipping with one-day and two-day delivery from domestic warehouses.
  * Premium shipping with one-day and two-day delivery from domestic warehouses.

## Enable Shipping Settings Automation (SSA)

**Steps to enable SSA for seller-fulfilled non-Prime products**

  

  1. From the **Settings** drop-down menu on the top right of Seller Central, click **Shipping Settings**.
  2. Go to the **Shipping Templates** tab.
  3. On the **Shipping Templates** tab, you can enable Shipping Settings Automation on:
     * New shipping templates by clicking Create New Shipping Template, entering the Shipping Template Name (for example, "My Self-fulfilled Shipping") and choosing from either Per Item/Weight-Based or Price banded as your shipping rate model.
     * Existing shipping templates by choosing the existing shipping template, then clicking **Edit Template** on the right side of screen.
  4. Turn on the **Shipping Settings Automation** toggle.
  5. Select your **Ship-from location** , and click **Next**.
  6. Select "I want to automate my Self-fulfilled (non-Prime) shipping settings" and click **Next**.
  7. On the **Standard Shipping Automation Preferences** page, you can enable automated transit time for Standard Shipping by:
     * Selecting the carriers and shipping services you currently use in the **Carrier Preferences** section.
     * Managing your Standard Shipping Regions by clicking **Edit** in the **Region Preferences** section.
     * Selecting the **Shipping Services Priority rule** you prefer to be considered for generating a delivery promise.
     * Click **Next**.
  8. If you are shipping from domestic warehouses, you can enable Premium Shipping region automation for Self-fulfilled One-Day Delivery and Two-Day Delivery. Select the carriers and shipping services you use in the **Carrier Preferences** section on the **Premium Shipping Automation Preferences** page. Click **Next**.
  9. Review your SSA preferences and click **Confirm**.
  10. Review and edit **shipping fee** for your shipping regions.
  11. Click **Save** template.
  12. Assign your Self-fulfilled SKUs to the shipping template.

**Steps to enable SSA for Seller Fulfilled Prime products**

**Note:** This option is available only if you are in the Seller Fulfilled
Prime trial or enrolled in the Seller Fulfilled Prime program.

  

  1. From the **Settings** drop-down menu on the top right of Seller Central, click **Shipping Settings**.
  2. On the **Shipping Templates** tab you can enable **Shipping Settings Automation** on:
     * **New shipping templates** by, clicking **Create New Shipping Template** , entering the Shipping Template Name (for example, "My Self-fulfilled Shipping") and choosing from either Per Item/Weight-Based or Price banded as your shipping rate model.
     * **Existing shipping templates** by choosing the existing shipping template then clicking **Edit Template** on the right side of screen.
  3. Turn on the **Shipping Settings Automation** toggle.
  4. Select your **Ship-from location** , and click **Next**.
  5. Select "I want to automate my Seller Fulfilled Prime shipping settings" and click **Next**.
  6. Select the carrier and shipping services for Prime one-day and two-day delivery.
  7. Select delivery zone limit if needed. Delivery zone limit can help you manage shipping costs. For example, if you select zone 2 for UPS Next Day Air for one-day delivery, SSA will automatically calculate which shipping regions UPS Next Day Air can deliver to in two days from your warehouse and within the scope of UPS Next Day Air zone 2. Leave Amazon's default value if you do not have shipping zone restrictions. Click **Next**.
  8. Review shipping settings and click **Confirm**.
  9. Review and edit shipping fees for non-Prime customers. (Prime customers will receive free shipping.)
  10. Click **Save** template.
  11. Assign your Prime SKUs to the Prime shipping template.

## Shipping Settings Automation (SSA) FAQ

**For Self-fulfilled Standard Shipping**

#### Will SSA consider changes in carrier delivery performance to calculate
delivery time?

Amazon tracks carrier delivery performance for the carriers you use and
maintains accurate transit time from your ship-from location to different
customer locations.

Additionally, with SSA enabled, your account health is protected from negative
feedback due to late deliveries. We will suppress negative feedback related to
late deliveries on your SSA orders, as long as:

  * You shipped the orders on-time
  * You provided valid tracking information
  * You used the same or faster shipping service than what was used by SSA used to calculate the delivery promise, which can be seen on the Order Detail page and the Order API.

#### What are the order fulfillment requirements for SSA orders?

You are expected to use one of the shipping services you enabled on your
Shipping template with SSA that can meet the delivery promise for orders of
SKUs linked to this shipping template. You can find the shipping service that
was used to generate the delivery promise for these order on the Order Detail
page (or the Order API).

You can also use Amazon Buy Shipping to select any shipping service that meets
your delivery promise. Similar to orders that are for SKUs not linked to a
shipping template with SSA enabled, we will monitor your delivery performance
and may add extra time to your delivery promise to protect customers if your
On-Time Delivery (OTD) rate fails to meet the OTD requirement.

#### How does SSA calculate the delivery promise if I enable multiple
warehouses in my shipping templates?

SSA will calculate delivery promise for each warehouse and select the
warehouse with the fastest delivery promise to the customer to make your offer
more attractive to customers.

#### How does SSA calculate the delivery promise if I enable multiple shipping
services in my shipping templates?

When you have two or more shipping services enabled on SSA, you can specify
the shipping service priority rules. SSA will follow these rules to select the
appropriate shipping service and generate a delivery promise for you. You can
choose from the following rules:

  * **Condition:** This will select the shipping service based on rules you configure for the item price, region, and weight. For example, you can select that if the product price is greater than $20, use shipping service X, but if the price is less than $20, use shipping service Y. You can also combine up to two rules. For example, if the weight of the product is above 10 lb and the delivery region is the north west of the USA, use shipping service Z.
  * **Longest delivery time:** This will select the shipping service that takes the longest time from your warehouse to the customer locations (likely cheaper). For example, if shipping service X takes 3 days, and shipping service Y takes 6 days, this option will automatically choose the slowest, in this case, shipping service Y.
  * **Fastest delivery time:** This will select the shipping service that will deliver the item faster from your warehouse to the customer locations. For example, if shipping service X takes 3 days, and shipping service Y takes 6 days, this option will automatically choose the fastest, in this case, shipping service X.
  * **Preferred ranking:** You can drag and drop to arrange and rank shipping services based on your preferred order. As long as the shipping service ranked first can deliver to this address, it will be used to make the delivery promise. If the top ranked shipping service can't deliver to that address, the next one on the list will be used until a suitable shipping service is found.

#### How can I downgrade my shipping templates by disabling SSA and reverting
to manually calculated transit times?

You can disable SSA on your shipping templates by following the below steps:

  * Go to [Shipping Templates](/sbr/ref=xx_shipset_dnav_xx#shipping_templates)
  * **Select** the template you would like to edit
  * Click **Edit** Template
  * Click **Shipping Settings Automation (SSA)** toggle to disable it

**Note:** Before disabling SSA, we recommend evaluating adjustments to the
shipping services you have enabled and the method used to prioritize them. You
can review these by visiting your shipping template and the SSA section by
clicking **Edit**.

#### Will enabling SSA unexpectedly increase my shipping costs?

No. Enabling SSA should not increase your costs unexpectedly and does not
require you to use faster ship methods because it applies the carrier transit
time based on the shipping service you specified and the rules you
prioritized.

#### Will I need to reconfigure my shipping charges if I enable SSA?

No. Once you enable SSA, all of your shipping charges will remain the same on
your template. SSA will only manage your transit time.

#### If I changed ship-from location or my shipping services, can I update my
automated shipping settings?

Yes, you can update your automated shipping settings at any time. Select the
shipping template and click **Edit Template**. In the shipping template edit
page, click **Edit Information** on the right side of the SSA toggle. From
there you can update your ship from locations and shipping services. After you
click **Confirm** , Amazon will reflect updated automated shipping settings
based on your SSA preferences.

**SSA FAQ for Prime/Non-Prime Premium Shipping**

#### How does Amazon automate Prime or Premium Shipping regions?

Prime or Premium Shipping regions are automatically calculated based on where
a shipment can reach within one day and two days using your SSA preferences,
including your ship-from location, your shipping service, and your delivery
zone limits (available only for Prime one-day and two-day region automation).
Amazon also helps you adjust the shipping regions periodically based on the
latest shipping service delivery performance to ensure maximum possible Prime
or non-Prime Premium Shipping coverage with high on-time delivery performance.

If you have enabled multiple warehouses, the Prime or Premium Shipping one-day
and two-day regions will cover all locations that your selected shipping
services can deliver from each ship-from location for one-day and two-day
delivery orders.

#### What are delivery zone limits for Prime region automation?

Delivery zone limits allow you to control Prime one-day and two-day delivery
regions more precisely. If a shipping service's eligible one-day or two-day
coverage spans across multiple zones, which results in varying shipping costs
by region, you can control Prime shipping costs by matching the Prime one-day
and two-day delivery regions to the carrier's delivery zones. You can verify
the shipping costs by zones on the carriers' websites
([UPS](https://www.ups.com/us/en/support/shipping-support/shipping-costs-
rates/daily-rates.page),
[FedEx](http://www.fedex.com/ratetools/RateToolsMain.do),
[USPS](https://postcalc.usps.com/DomesticZoneChart)). If you do not need to
restrict Prime one-day and two-day delivery regions, you can leave the Amazon
default value in place.

#### Why are the Prime one-day and two-day delivery regions determined by
Amazon smaller than what I usually get?

We determine a region is a Prime one-day or two-day delivery region when the
selected carrier can deliver on-time to all zip codes in that region. If we
find that some of the zip codes in that region cannot be delivered to on time,
we may remove that region from one-day or two-day delivery to protect the
customer experience. However, as delivery speeds of shipping services improve,
a standard shipping region may be upgraded to a one-day or two-day delivery
region.

#### Can I purchase the shipping service used to calculate the delivery
promise in Buy Shipping?

Yes, you will be able to purchase the shipping service used to calculate the
delivery promise in Buy Shipping if you:

  * Buy the shipping label on-time and before the pick-up time for the shipping service; and
  * Select the same shipping location in Buy Shipping as the ones defined on your automated shipping template.

If for any reason you fulfilled all requirements and still were not able to
buy your preferred shipping service in Buy Shipping, you may need to buy the
preferred shipping label outside of Buy Shipping.

**Note:** Use of Amazon Buy Shipping Services for Seller Fulfilled Prime
orders is now optional. Learn more at [Seller Fulfilled Prime performance
requirements](/gp/help/G202072550).

