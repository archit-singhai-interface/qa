---
title: Same-day handling time FAQ
url: https://sellercentral.amazon.com/help/hub/reference/GB96WHU9AT74W2T3
section: General Documentation
---

#### 1\. What is the difference between Same-day handling time and Same-day
delivery?

Same-day handling time applies only to Domestic Standard and Expedited
delivery options. Orders are only required to be picked, packed, shipped, and
confirmed the same day (subject to order cut-off times) when Same-day handling
time is enabled.

In contrast, Two-day shipping is a premium shipping option available to
sellers who meet high delivery standards. Amazon mandates that orders using
this option be picked, packed, and shipped the same day. To learn more about
premium shipping options and Two-day delivery, go to [Premium
shipping](/gp/help/201503640).

#### 2\. What are my options to update Same-day handling time?

Your options to update Same-day handling time are as follows:

  * SKU level handling time
  * Default handling time

**Note:** If you have automated handling time turned on, you cannot edit your
default handling time.

**Options to update SKU-specific 0-day (same day) handling time set on Seller
Central**  

  1. In Seller Central, go to **Inventory** > **Manage All Inventory**. Locate the SKU and click **Edit** > **Offer** > **Handling Time set to 0**. For more information, go to [Manage inventory](/inventory/ref=xx_invmgr_dnav_xx?tbla_myitable=sort:%7b%22sortOrder%22:%22DESCENDING%22,%22sortedColumnId%22:%22date%22%7d;search:;pagination:1;).
  2. Upload a feed file via API that can be found in developer docs by clicking [here](https://developer-docs.amazon.com/sp-api/docs/feed-type-values#listings-feeds).
  3. Upload a feed file via **Add Products via upload**.

**0-day handling time default handling time page**  

  1. On Seller Central, go to **Settings** > **Shipping settings** > **General shipping settings**.
  2. Scroll down to **Handling time** and click **Edit**.
  3. Select **Same day (0 day)** and click **Save**.

**Note:** You can only change your default handling time once in a 24-hour
window, and it can take up to 24 hours for the change to take effect.

**Steps to update SKU-specific 0-day (same day) handling time set via feed
file**

  * **Using Inventory Loader:**   

    1. On the [Inventory file templates, style guides, and browse tree guides](/gp/help/G1641) page, navigate to the **Choose a file template** section and download your **Inventory Loader file**.
    2. Read through the instructions in the **Data definitions** tab, in the Inventory Loader file.
    3. In the **Template** tab, fill all the required fields (One SKU per row) 
    4. Save the file in text-tab-delimited format (.xls or .tsv).
    5. Upload the file through **Catalog** > **Add products via upload** > **Upload your spreadsheet**. 
  * **Using Price and Quantity file:**   

    1. On the [Inventory file templates, style guides, and browse tree guides](/gp/help/G1641) page, navigate to the **Choose a file template** section and download your **Price & Quantity file**. 
    2. Read through the instructions in the **Data definitions** tab, in the Price & Quantity file.
    3. In the **Template** tab, fill all the required fields (one SKU per row).
    4. Save the file in text-tab-delimited format (.xls or .tsv).
    5. Upload the file through **Catalog** > **Add products via upload** > **Upload your spreadsheet**. 
  * **Using Listing Loader:**   

    1. On the [Upload inventory using the Listing Loader](/gp/help/G201576570) page, download your **Listing Loader file**.
    2. Read through the instructions in the **Data definitions** tab in the Listing Loader file.
    3. In the **Template** tab, fill all the required fields (one SKU per row).
    4. Save the file in text-tab-delimited format (.xls or .tsv).
    5. Upload the file through **Catalog** > **Add products via upload** > **Upload your spreadsheet**.

#### 3\. How does this feature apply to Prime orders?

By default, Prime orders with Standard delivery are expected to be shipped the
next day after receiving an order. You can enable Same-day default handling
time. When enabled, this will require you to ship orders on the same day for
all shipping methods.

**Note:** All shipping templates that are for seller-fulfilled prime will have
Same-day handling time configured.

#### 4\. Is Same-day handling time applicable to scheduled delivery?

No, at this time Same-day handling time is not applicable to scheduled
delivery. You can choose Same-day handling time for arranged delivery options.
For more information on arranged delivery, go to [Freight-shipping templates
for less-than-truckload (LTL) shipments](/gp/help/G202188040).

#### 5\. Do I need to ship every order the same day I receive it?

No, all orders received **before the order cut-off time** must be shipped and
confirmed **during the day the order was received** to avoid late shipments.
All orders received **after the order cut-off time** must be shipped and
confirmed no later than **the next day after** the order was received.

**Note:** The default cut-off time is 2 p.m. local time, but you can edit it
the time in your [Shipping settings](/sbr/ref=xx_shipset_dnav_xx).

#### 6\. Does Same-day handling time apply to all of my products?

It depends how you set up Same-day handling time. When you set Same-day
handling time as your default account handling time, it will apply to all
ASINs that do not have an ASIN-specific handling time configured. If you
configure an ASIN-specific handling time, it will override your default
handling time for that specific ASIN. If you are eligible and set Same-day
handling time on your shipping template, it will only apply to ASINs assigned
to that shipping template and those that do not have an ASIN-specific handling
time.

