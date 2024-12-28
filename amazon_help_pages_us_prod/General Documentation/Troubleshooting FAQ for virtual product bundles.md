---
title: Troubleshooting FAQ for virtual product bundles
url: https://sellercentral.amazon.com/help/hub/reference/G2BTQWUUDS3RV7WB
section: General Documentation
---

## Creating bundles

#### I don’t have access to the [tool](/bundles/create) or I see a ‘Page Not
Found’ error

  * First, refer to the [seller eligibility criteria](/gp/help/G87HAE6PMKKM23Z7). Note that you must have a [Brand Representative](/gp/help/GJ84K745AL3R5N3Q) role assigned to a brand in Brand Registry.
  * If you are a secondary user of the Seller Central account, check your [permissions](/gp/account-manager/home.html) to see if you have the ‘Product Bundles’ View & Edit permission. If you don’t, ask the primary account user to grant it.
  * If you are not a Brand Representative, request the role from your brand Administrator. If you cannot contact them, go to the [Brand Benefit Eligibility page](/brands/brand-relationships?ref=brnd_bndl_bssi_faq) to correct your status and gain access to all of your brand benefits.

#### An entire brand that you own is not available for bundling while you are
using the tool

If you are a brand owner, but a brand you own is not available for bundling,
go to the [Brand Benefit Eligibility
page](https://sellercentral.amazon.com/brands/brand-
relationships?ref=brnd_bndl_bssi_faq) to correct your status and gain access
to all your brand benefits.

#### An ASIN is not available for bundling, though other ASINs with the same
brand name are.

  * Check the [ASIN requirements](/gp/help/G87HAE6PMKKM23Z7) for virtual bundles. ASINs must have in-stock FBA inventory in the 'New' condition that is active and buyable.
  * The ASIN must belong to your brand. This is usually caused by inaccurate listing data on the ASIN. Most commonly, the brand name you submit must match exactly with the brand name recorded in Brand Registry (i.e. adding spaces or hyphens will lead to a mismatch). To update the brand name, follow these steps:
    * Download the correct category-specific [inventory file template](/listing/download).
    * Input all the mandatory fields into the template. Provide your brand name exactly as it is recorded in Brand Registry. Note that brand names are case sensitive.
    * In the **Update/Delete** field, select **Update** from the drop-down menu.
    * Save the file and upload it [here](/listing/upload) in the **Step 2- Upload File** section.
  * If the ASIN is still not available for bundling after 24 hours, you can contact us and reference **Virtual Bundles error code 7310c** and tell us which ASIN(s) are missing.

To ensure timely resolution of cases, before you contact us, use the bundles
tool to make a list of all the missing ASINs that you want to include in
bundles (if more than one). Add them all in the same case. Make sure the brand
name you have submitted for each ASIN matches exactly with the brand name in
Brand Registry, and that all the ASINs in the list have in-stock FBA
inventory.

## Managing Bundles

**Note:** If your bundle was not created correctly the first time, do not re-
create it without first referencing this FAQ section to fix the underlying
issue. Virtual bundles are designed to have a single offer and issues may
arise when multiple offers are submitted. If you have a bundle with multiple
offers, delete other offers until only one offer remains.

#### I submitted a bundle for creation; however, it does not show in [Manage
Inventory](/inventory)

  

  1. Make sure you have waited at least 24 hours.
  2. Check for your bundle in your [Drafts](/inventory/view/DRAFT/). If your bundle is here, delete the listing and re-create your bundle using the bundles tool. When recreating, to reduce the chance of errors, use a SKU that you are not using for any offer in any marketplace and make sure to fill out each field (including all five bullet points).
  3. Remove all filters from your view in Manage Inventory. Both the **Status** filter and the **Fulfilled by** filters should be set to **All**. Virtual bundles will show the word ‘Bundle’ in the **Status** column.

**Viewing bundles in Manage Inventory**

![](https://images-na.ssl-images-
amazon.com/images/G/01/rainier/help/fba/Viewing_bundles_in_Manage_Inventory.png)  

#### I created a bundle and I can see it in Manage Inventory; however, I see a
404 error page (i.e. “Sorry, we couldn’t find that page”) when trying to visit
the bundle’s detail page

  

  1. Make sure you have waited at least 24 hours.
  2. Check for your bundle in the [Restricted Products](/performance/account/health/product-policies?t=restricted) dashboard and in your [Performance Notifications](/performance/notifications). If your bundle was restricted incorrectly, follow the instructions on that page to address the issue.
  3. Search for the bundle ASIN in [Manage Inventory](/inventory/). If two or more offers are returned for the same ASIN, you have created a duplicate bundle. Since virtual bundles are designed to have just one offer, we may temporarily remove or ‘yank’ virtual bundles with multiple offers to prevent issues. To restore the ASIN, first delete the extra offers until only one remains and then contact us and request that we ‘un-yank’ the bundle ASIN.

#### My bundle is out of stock, but I have inventory

  

  1. Check in [Manage Inventory](/inventory) that each of the component items is in stock with active FBA inventory
  2. If that doesn’t work, re-publish your bundle by clicking **Edit** in **Manage Inventory** and clicking **Save & Publish**. Wait for 1 hour.

In rare cases, sellers may face issues when one or more component ASINs in the
bundle has an FBA offer and a Fulfilled by Merchant offer with the same SKU.
This may happen when using a third-party application or connecting via API to
manage listings/inventory.

To check if this could be an issue, in **Manage Inventory** look up each of
the component ASINs to see if they have an FBA and an FBM offer with the same
SKU. If this is the case, you must close the FBM offer and stop feeding
inventory from any third-party software. Then, change the FBA offer to
Fulfilled by Merchant. Finally, immediately change that offer back to FBA and
wait for 24 hours.

#### My bundle does not show a Buy Box

  

  1. Check the prices of your component ASINs and make sure that the price you entered into the bundles editor is less than the sum of the prices of the components.
  2. Go to [Manage Inventory](/inventory) to edit your bundle.
  3. Click **Edit** , check that your bundle price shows correctly in the editor, click **Save & Publish**, and wait 24 hours.

#### My bundle is not showing images

  

  1. Go to [Manage Inventory](https://sellercentral.amazon.com/inventory) to edit your bundle. Double check that your images show correctly in the editor. Virtual bundle images must follow the [product image requirements](/gp/help/G1881).
  2. Click **Edit** , click **Save & Publish**, and wait 24 hours.

#### I do not see the ‘Make it a bundle’ widget on the detail page of my main
component ASIN

The widget is not visible on mobile browsers and apps at this time. The widget
may not appear on ASINs that are not the ‘main component’ ASIN. The widget may
not appear when a bundle loses its Buy Box or is unavailable for purchase. The
widget is not guaranteed to display at all times or on all ASINs.

#### One of my SKUs for a component ASIN that was being included in virtual
bundles has changed (or “remapped”), and now it is being used for a different
component ASIN

This may cause problems with all bundles that contain those component ASINs.
It is recommended that you identify any bundles that contain those component
ASINs and delete all of the applicable bundle offers from **Manage Inventory**
and your [Drafts](/inventory/view/DRAFT/) by clicking **Delete product and
listing**.

Confirm your bundle offers were deleted successfully by going to the bundle
detail pages. You can then re-create the bundle offers. The bundle ASINs will
retain any reviews, sales history, etc.

#### I have a bundle with multiple offers on it

Virtual bundles are currently expected to have only a single offer at a time.
Having multiple offers will cause problems with the bundle. If you notice this
issue, delete the extra offers from Manage Inventory and your Drafts until
only a single offer remains.

#### I use third-party listings/inventory software and I am having trouble
managing virtual bundles

At this time, virtual bundles can only be created and should only be managed
in Seller Central. Contact your integrator or service provider if you notice
issues.

## Tips for Bundles

#### How do I increase my bundle sales?

  * Add a discount.
  * Keep your bundle titles under 65 characters. Titles longer than that will be truncated when displayed in the ‘Make it a bundle’ widget.
  * Help shoppers discover your bundle:
    * Add it to your Store page.
    * Include it in your on-Amazon and off-Amazon marketing campaigns.
    * Use bundles to create unique offerings during key sales periods like Prime Day and Black Friday.

