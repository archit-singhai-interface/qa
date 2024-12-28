---
title: Manage your handling time
url: https://sellercentral.amazon.com/help/hub/reference/G200955560
section: General Documentation
---

Amazon provides the estimated delivery time to customers on the offer listing
and checkout pages. We base this estimate on the time between when the buyer
places an order and when the delivery reaches the customer's address. There
are two parts to that calculation, handling time and transit time. This help
page discusses handling time.

## Types of handling time

Handling time, also known as production time or lead time to ship, is the time
between when the customer places the order up to when you hand over the order
to a carrier. Handling time is part of the delivery date calculation displayed
to customers on the offer listing and checkout page.

There are three ways to set your handling time:

  * Automated handling time (Amazon managed handling time for each SKU)
  * SKU-specific handling time (Seller set for each SKU)
  * Default handling time (Seller set for the account)

When a product has a SKU-specific handling time, it will override the default
handling time.

When a seller enables automated handling time, it will override Default and
SKU-specific handling time, unless there isn’t enough shipping history to do
so, or an override exception is approved. See more details in the sections
below on the history needed by AHT and override exceptions.

**Automated handling time (AHT)**

AHT automatically sets your handling time and Order Handling Capacity for you
based on your historic performance per SKU. AHT helps reduce unnecessarily
long handling times (known as a handling time gap) that make your delivery
dates less appealing to customers, and also to increase the handling time for
products that take longer to handle than what you have manually set, which
could lead to late shipments. AHT sets more accurate handling times per SKU
based on how long it historically takes you to pass each SKU to carriers,
removing your need to estimate and manually configure handling times.
Additionally, with AHT enabled, because Amazon is making calculations which
affect your ship-by dates, your seller-fulfilled listings will not be
deactivated if your Late Shipment Rate (LSR) does not meet the [LSR Policy
requirement](/gp/help/G200285190).

When AHT is enabled, it will override both your SKU-specific handling time and
your default handling time. For any new SKU, until there are enough historical
shipments for automated handling time (AHT) to learn from and set an accurate
handling time, your manually set [SKU-specific handling
time](/inventory/ref=xx_invmgr_dnav_xx?tbla_myitable=sort:%7B%22sortOrder%22%3A%22DESCENDING%22%2C%22sortedColumnId%22%3A%22date%22%7D;search:;pagination:1;)
will be used, or the automated default handling time if there is no SKU-
specific handling time for that SKU. This helps ensure all of your listings
have an achievable handling time from the moment you list a new product.

For certain product types, such as custom, heavy and bulky, handmade,
perishable, or media SKUs, you can request an exception to manually set a SKU-
specific handling time that will override what AHT has configured. To request
an exception of your handling time, please contact [Selling Partner
Support](/help/center) and ask them to create a ticket for you to have a
handling time exception. We recommend doing this for SKUs where your handling
time may be very unpredictable and using your history may be inaccurate.

AHT will also set your Order Handling Capacity for you based on your
fulfillment history, and you can also choose to update this setting manually
in your [Shipping Settings](/fbm/handling-time). Your Order Handling Capacity
is the limit for how many orders you can ship in a day, and once this limit is
reached you will receive an extra day of handling time to ship that order. For
example, if you normally ship 100 orders in a day, and AHT sets your Order
Handling Capacity to 100, once you receive the 101st order, all subsequent
orders will have 1 more day to handle. This will help you if there are order
surges caused by peak demand.

To enable AHT, take the following steps:  

  1. On Seller Central, go to **Settings** , select **Shipping settings** , and then select **General shipping settings**.
  2. Scroll down to **Handling time** and click **Edit**.
  3. Select **Automated handling time** and click **Save**.
  4. Optionally, you can also enter your order handling capacity and click **Save**. For more information, go to [Modify order handling capacity](/gp/help/GGKKJFSR59D8SFNP). This will allow you to set a limit for how many orders you can handle within your default handling time. Order handling capacity is applied when you receive too many orders by adding one additional day of handling time for all orders above your set capacity. For more information on order handling capacity, go to [Shipping settings](/developer-docs.amazon.com/sp-api/docs/feed-type-values#listings-feeds).

**Note:** You can enable automated handling time once in a 24-hour window and
it can take up to 24 hours for the change to take effect.

As of September 25, 2024, if you have a handling time gap of two days or more
between your set handling time and your actual handling time, AHT will be
automatically enabled for you and you will not be able to turn it off. AHT
will set a more accurate handling time for you, which makes your delivery date
more appealing to buyers and typically increases sales. Your handling time gap
is calculated over 30 days of shipments, using shipments from the last 40
days, and excluding the most recent 10 days. To see your handling time gap,
review your [Fulfillment Insight dashboard](/seller-fulfilled-
product/analytics/ref=xx_msfp_dnav_xx#FULFILLMENT_INSIGHT_DASHBOARD).

**SKU-specific handling time**

SKU-specific handling time allows you to set a unique handling time (faster or
slower) than your default handling time. If you set a SKU-specific handling
time for a product, that setting will override both the default handling time,
but if you have AHT enabled, AHT will automatically set a SKU-specific
handling time that will override your manually set SKU-specific handling time.
If you have a handling time exemption for the particular SKU, only your SKU-
specific handling time will be used.

To set or update SKU-specific handling time for each product, one at a time:

  * In Seller Central, go to **Inventory** and select **Manage all inventory**. Locate the SKU and click **Edit** , select **Offer** , and then select **Handling time****.**

To set or update SKU-specific handling time in bulk, you have three options:

  * **Using Inventory Loader:**   

    1. On the [Inventory file templates, style guides, and browse tree guides](/gp/help/G1641) page, navigate to the **Choose a file template** section and download your **Inventory Loader file**.
    2. Read through the instructions in the **Data definitions** tab in the Inventory Loader file.
    3. In the **Template** tab, fill all the required fields (one SKU per row).
    4. Save the file in text-tab-delimited format (.xls or .tsv).
    5. Upload the file through **Catalog** , select **Add products via upload** , and then select **Upload your spreadsheet**.

  * **Using Price and Quantity file:**   

    1. From [Inventory file templates, style guides, and browse tree guides](/gp/help/G1641) page, navigate to the **Choose a file template** section and download your **Price and Quantity file**.
    2. Read through the instructions in the **Data Definitions** tab in the Price and Quantity file.
    3. In the **Template** tab, fill all the required fields (one SKU per row).
    4. Save the file in text-tab-delimited format (.xls or .tsv).
    5. Upload the file through **Catalog** , select **Add products via upload** , and then select **Upload your spreadsheet**.

  * **Using Listing Loader:**   

    1. From [Upload inventory using the Listing Loader](/gp/help/G201576570) page, download your **Listing Loader file**.
    2. Read through the instructions in the **Data Definitions** tab in the Listing Loader file.
    3. In the **Template** tab, fill all the required fields (one SKU per row).
    4. Save the file in text-tab-delimited format (.xls or .tsv).
    5. Upload the file through **Catalog** , select **Add products via upload** , and then select **Upload your spreadsheet**.

**Note:** Leaving the **Handling time** or **Lead time-to-ship** fields empty
in the above templates will cause Amazon to revert to your account’s default
handling time. Your offer will update on Amazon within 15 minutes. In case of
maximum load on Amazon systems, it can take up to 24 hours for offer
information and 48 hours for product information.

**Default handling time**

Default handling time is set for all products on your account, and applies to
all of your products that do not have an SKU-specific handling time. If you
have AHT enabled, default handling time will be used for SKUs that don’t have
a shipping history. You can set your default handling time for your account to
either same-day or one-day.

  * If you set your default handling time to one-day, you will need to ship the product on the next business day after the order is received. 
  * If you set your default handling time to same-day, you will also need to configure your order-cut off time in your General Shipping Settings, which by default is set to 2:00 p.m. local time of the location of your default location. If an order is placed prior to your order-cut off time, you need to ship it on the same day the order was received. If an order is placed after your order cut-off time, you have until the next business day to ship it.

**Note:** For new professional sellers joining Amazon, the default handling
time is set to one day, and sellers can change their Default setting to
automated or same day.

Take the following steps to update default handling time:  

  1. On Seller Central, go to **Settings** , select **Shipping settings** , and then select **General shipping settings**.
  2. Scroll down to **Handling time** and click **Edit**.
  3. Select **Same day (0 day)** or **1-day** and click **Save**.
  4. Optionally, you can also enter your [order handling capacity](/gp/help/GGKKJFSR59D8SFNP) and click **Save**. This will allow you to set a limit for how many orders you can handle within your default handling time, and protect yourself against [Late shipment rate](/gp/help/G200285190). Order handling capacity is applied when you receive a large number of orders by adding one additional day of handling time for all orders above your set capacity.

**Note:** You can only change your default handling time once in a 24-hour
window, and it can take up to 24 hours for the change to take effect. It can
take up to one minute to change capacity input. Do not attempt to save more
than one time per minute.

**Configure handling time for same-day orders**

To set same-day handling time, you can either set same-day handling time as
your account default handling time, or you can update your SKU-specific
handling time by setting your handling time to 0 on the Manage all inventory
page or via the Feed file in Seller Central. This provides you with additional
flexibility to set same-day handling time for some or all of your products.

Additionally, you can configure same-day handling time on your shipping
templates for your standard and expedited shipping options. However, this
feature is only available to sellers who meet the required high-delivery
performance standard. For more information, go to [Same-day handling time
FAQ](/gp/help/GB96WHU9AT74W2T3).

For same-day handling time, all orders received **before the order cut-off
time** must be shipped and confirmed **the same business day you receive the
order to avoid late shipments**. All orders received **after the order cut-off
time** must be shipped and confirmed during **the following business day
after** the order was received. If you enable same-day handling time, you will
also need to configure your order-cut off time in your General Shipping
Settings, which by default is set to 2:00 p.m. local time of the location of
your default location.

For example, if you have same-day handling time with an order cut-off time of
12 p.m. and you receive an order on Monday at 11 a.m., that order must be
shipped and confirmed on the same day the order was received. If an order is
received on Monday at 4 p.m., which is after the cut-off time, that order must
be shipped by Tuesday.

**Note:** To calculate your cut-off time, we will consider your default
location’s time zone unless you have Location specific cut-off times
configured. To learn more, see [Location based Shipping
Settings](/gp/help/G4LD7W2EKPFK2ULE).

## Impact on account performance

The expected ship date for your seller-fulfilled orders is calculated based on
the order date plus the handling time. For example, if your default handling
time is one day, the expected ship date for orders placed before midnight will
be the next business day. For same-day handling time, all orders received
before the order cut-off time must be shipped and confirmed during the day the
order was received to avoid late shipments. With same-day handling time, all
orders received after the order cut-off time must be shipped and confirmed
during the next day after the order was received.

**Note:** The Default cut-off time is 2 p.m. local time, but you can edit it
in your [Shipping settings](/sbr/ref=xx_shipset_dnav_xx#shipping_templates).

It is important to confirm the shipment of orders by the expected ship by date
to meet the [Late shipment rate](/gp/help/G200285190) requirements for your
account. If you ship the product on time but do not confirm it by the ship by
date, it will be considered a late shipment. Not shipping on time may affect
your LSR. Refer to the [Modify order handling
capacity](/gp/help/GGKKJFSR59D8SFNP) to learn how to protect yourself against
order surges.

**Note:** With AHT enabled, your seller-fulfilled listings will not be
deactivated if your LSR does not meet the [LSR policy
requirement](/gp/help/G200285190).

## Seller Fulfilled Prime and Premium Shipping orders

Seller Fulfilled Prime (SFP) and Premium Shipping (same-day delivery, next-day
delivery, and two-day delivery) requires sellers to ship all orders received
before the order cut-off time during the same business day the order was
received to avoid late shipments. With same-day handling time, all orders
received after the order cut-off time must be shipped and confirmed during the
next business day after the order was received.

**Note:** The default cut-off time is 2 p.m. local time, but you can edit it
in your [Shipping settings](/sbr/ref=xx_shipset_dnav_xx#shipping_templates).

## Handling time settings

On this page you will see recommendations from Amazon for the ideal handling
time to set to match your actual handling time per SKU. You can choose to
manually adjust your SKU handling time with these recommendations, or to
enable automated handling time (AHT), in which case all recommendations will
be applied.

Amazon generates handling time recommendations for all your products that have
enough shipping history. For products where you have shown capabilities to
handle them faster than your ASIN-specific handling time currently configured,
we will recommend adjustments to set a shorter handling time. For products
where your handling time is slower than your configured handling time, we will
recommend adjustments to set a longer handling time. The recommendations are
updated regularly and are based on your recent handling time per SKU to ensure
the recommendations reflect your most recent capabilities to handle products
for delivery.

Unless you enable AHT, we encourage you to monitor and update your handling
time configuration accordingly. Setting accurate handling times will change
the delivery dates that customers see, and more accurate handling times are
typically shorter, which results in more sales. To view the recommended
handling times on Seller Central, follow these steps:  

  1. On Seller Central, go to **Inventory** , and then click [Manage seller-fulfilled products](/seller-fulfilled-product/analytics/ref=xx_msfp_dnav_xx).
  2. Select the **Handling time settings** tab to view all the products that have recommended handling times.
  3. Check back regularly to view updated handling time recommendations.

If you prefer to have your handling time automatically updated to the most
recent Amazon recommended value, we recommend enabling automated handling
time, which will configure your handling time per SKU based the Amazon
recommended handling time and on your historic performance. Additionally, with
AHT enabled, your seller-fulfilled listings will not be deactivated if your
late shipment rate (LSR) does not meet the [LSR Policy
requirement](/gp/help/G200285190).

The handling time settings page shows which handling time value is used to
calculate the ship by date of your SKU, and the source of how the handling
time was assigned. The source has the following options:

  * **Amazon managed (AHT)** : This value is displayed when the AHT recommendation is applied to the SKU. If there isn’t sufficient history, your SKU-specific handling time will be used instead, and if there isn’t a SKU-specific handling time, the default handling time is used. 
  * **Seller set** : This value is displayed when the SKU-specific handling time is applied, if there is no SKU-specific handling time, the default handling time is used. 
  * **Seller override to AHT** : This value is displayed if you requested an exemption for the handling time of that SKU.

