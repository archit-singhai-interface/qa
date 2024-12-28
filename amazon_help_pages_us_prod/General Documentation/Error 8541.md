---
title: Error 8541
url: https://sellercentral.amazon.com/help/hub/reference/G200692330
section: General Documentation
---

## What causes this error

This error occurs when a listing attribute, such as the brand, title, UPC, or
color, submitted by the seller corresponds to the product ID of an existing
ASIN. This means a similar product was found in Amazon’s catalog and there is
a discrepancy in the information provided by the seller versus what is
recorded in Amazon’s product catalog.

General guidance on changes to Detail Pages:

  * Some attributes can be changed as much as you want as long as they do not change the identity of the ASIN. Please note that if we find that these values are inconsistent or misrepresent the product, action may be taken on the ASIN or seller. Examples include product descriptions and bullet points.
  * Some attributes may be allowed to change slightly after ASIN creation to enrich the product’s information. For example, it may be possible to change the color from blue to light blue or add an adjective to the title.
  * Some attributes cannot change after ASIN creation. Examples include attributes like GTIN and item package quantity.

To learn how you can resolve a product matching error, watch this Seller
University video.

## Error message

The standard product information provided in SKU[SKU] conflicts with the
Amazon catalog. The conflicting attribute value(s) are brand(Merchant:
[Merchant_Value]/Amazon:[Amazon_Value]). If your product is this ASIN, modify
these attributes to reflect Amazon catalog value. If your product is different
from this ASIN, check if the standard product ID (e.g UPC, ISBN, EAN, or JAN
codes) values are correct.

[Overview of category UPC requirements](/help/hub/reference/G200317520)

If you are brand owner for this product, ensure that you have a Brand Registry
account.

## How to solve this error

The data submitted by you should match the catalog data to clear the conflict.
If the catalog data is incorrect, you can contact Selling Partner Support to
evaluate your request to fix the data.

## My submission was incorrect

To fix error 8541, first check if the product found is the same as the one you
are trying to list by searching the ASIN in Amazon. Please refer to [Match
your products](/help/hub/reference/G1471) for tips for successful product
matching.

You can complete your listing in individual listing experience or through the
**Fix Your Products** page.

You can resolve error 8541 in the individual listing experience as shown
below:  

  1. Note the error in the listing page for the incorrect attribute (example below).

![](https://m.media-amazon.com/images/G/01/fba-help/Value_error.jpg)  

  2. You can update the value in the field to align with the pre-existing value as shown in the error message. Please note that the value must be an exact match with what is provided in the error message. Ensure that the spacing, capitalization, and singular or plural spelling match with the conflicting attribute to resolve the conflict.

Alternatively, you can resolve the issue in **Fix Your Products** :

To see the list of products affected by conflicting information:  

  1. Go to **Catalog** in Seller Central.
  2. Select **Complete Your Drafts**.
  3. On the **Fix Your Products** page, select **Incomplete listings** , and click **Matching Reconciliation conflicts**.

Check the issue description to see what information has been submitted by you
and what information is pre-existing in Amazon’s catalog. Additionally, you
can click the link above the Amazon information to see the detail page of the
item. This will be the page shown to customers containing all the information
available for this product.

![](https://m.media-amazon.com/images/G/01/rainier/help/image_IN2.png)  

After you have ensured that they are actually the same product, you can choose
to accept Amazon’s information, and your submission will be processed in the
next 15 minutes, after which your product will be shown on your **Inventory**
page in Seller Central.

If after this time your product does not appear in your inventory, another
issue may have occurred. Go to **Fix your products** > **All issues** and
search for your product. Once found, resubmit the information regarding the
other type of issue found. If you are not able to find your product, contact
Selling Partner Support.

**Solve and prevent error 8541 using flat files or APIs**

To resolve this error, ensure the Product ID you have provided is correct. If
it is incorrect, provide the correct product ID in your file and resubmit.

If you have provided the correct product ID, perform a full update and ensure
that the attributes in your file match those in the catalog (these attributes
are provided in the error report), and resubmit your file.

## A different product was found

If the product Amazon found is different than the one you are submitting,
click **Request product detail page change** and create a new request. A pop-
up window will appear and you will be required to provide more information
about the discrepancy found. Amazon will analyze the information provided and
reply on Seller Central. To keep track of your request, go to **Help** >
**Case log**. When you submit the information, please share the sku_id,
conflicting ASIN, and other information that the associate can investigate for
prompt resolution.

**Product ID conflict:** A common cause of this error is the result of
manufacturers reusing UPCs or EANs. For example, in apparel, barcodes are
sometimes reused after three years. Ensure that you match your product to the
correct ASIN. If there is a product ID conflict, then you can contact Amazon
through the Seller Central page or via the appeal process. You will be asked
to provide proof of ownership (GS1 certificate or image clearly displaying the
GTIN value) for resolving the issue.

**Non-product ID attributes:** A common cause of this error is that the
product ID assigned is correct but one or more of the other attributes
conflicts with the attribute information of an existing product in Amazon’s
catalog. For example, the brand name entered doesn’t match the brand name of
the existing product. You can contact Selling Partner Support and provide
proof (like a brand trademark registered or image of the product) for the
correction of the brand name of the existing product.

## I want to correct a product fact on a Detail Page

**Guidance for Brand Representatives and Authorized Resellers:** If you’re the
Brand Representative or Authorized Reseller for the brand, corrections to the
ASIN may be allowed if proof can be provided that there is a mistake that’s
mis-representing the product to buyers. In this case, contact Selling Partner
Support.

When contacting Selling Partner Support, provide a copy of the error message,
your SKU (ASIN optional), the attribute you are trying to update, and proof
that the existing Amazon value is incorrect. Accepted proofs include product
manuals, links to manufacturer websites, or a product image clearly displaying
the information.

**Guidance for sellers who are not associated with the brand on the ASIN:** If
you do not have a relationship with the brand on the ASIN, but are selling the
product and believe there is a factually incorrect statement on the detail
page, please contact Selling Partner Support and provide evidence of the
problem.

When contacting Selling Partner Support, provide a copy of the error message,
your SKU, the attribute you are trying to update, and proof that the existing
Amazon value is incorrect. Accepted proofs include product manuals or links to
manufacturer websites.

## Common examples

#### Marketing update (I’m trying to change a value on an existing ASIN for
marketing reasons)

**Common attributes that are allowed to change after ASIN creation for
marketing reasons:** Title, description, and bullet points.

**Guidance:** If you’re the Brand Representative or Authorized Reseller for
the brand, changes to marketing content that do not change the identity of the
product are allowed. Please attempt to make the update yourself using a
listing tool and only contact support if you are unable to make the change.
When contacting support, please provide either an error code or reason that
you cannot make the change in a self-service fashion. If you do not have a
relationship with the brand of the ASIN, we do not allow changes to marketing
content.

**Example of an allowed change:**

  * **Old Title:** Filtrete AC Furnace Air Filter, MERV 11, MPR 1000, Micro Allergen Defense, 3-Month Pleated 1-Inch Electrostatic Air Cleaning Filter, _20x20x1_ , 4 Pack (Actual Size 19.69x19.69x0.81 in)
  * **New Title:** Filtrete _20x20x1_ AC Furnace Air Filter, MERV 11, MPR 1000, Micro Allergen Defense, 3-Month Pleated 1-Inch Electrostatic Air Cleaning Filter, 4 Pack (Actual Size 19.69x19.69x0.81 in)

#### Identity update (I’m trying to change a product fact after ASIN creation.
I need to change this attribute because the brand name of my product has
changed but the product itself is the same)

**Guidance:** It’s against Amazon policy to update identity attributes on
ASINs except in exceptional circumstances, like correcting a typo. Instead, we
require you to create a new ASIN. We strongly believe that what a buyer buys
today should look the same tomorrow and changes to attributes like the brand
name can erode customer trust, even if the underlying product is the same. In
order to preserve reviews and point buyers at your new product, we recommend
you use the the Newer Version widget to tie the old ASIN to the new one. This
feature adds a notice to your existing detail page that points at a newer
version of the product.

**Example of a change that is not allowed:**

  * **Old Title:** _Filtrete_ 20x20x1 AC Furnace Air Filter, MERV 11, MPR 1000, Micro Allergen Defense, 3-Month Pleated 1-Inch Electrostatic Air Cleaning Filter, 4 Pack (Actual Size 19.69x19.69x0.81 in)
  * **New Title:** _Simply Filters_ 20x20x1 AC Furnace Air Filter, MERV 11, MPR 1000, Micro Allergen Defense, 3-Month Pleated 1-Inch Electrostatic Air Cleaning Filter, 4 Pack (Actual Size 19.69x19.69x0.81 in)

#### Add offer to an existing ASIN (I'm running into an error and I just want
to add an offer to an ASIN. I do not want to add or modify product data on the
ASIN)

**Guidance:** Please use one of our offer-only experiences to create your
offer. These experiences include listing feeds, the **Add Offer** page in
Seller Central, and listing APIs. You may need to delete, recreate, or update
your SKU in order for this to work. There is no need to wait between these
actions.

#### I have a conflict but the error message cites a value in the wrong
language

Amazon checks some attributes globally, not specific to a regional store. So
these attributes will be checked against ASIN and SKU values for all stores,
not just for the store you are submitting on. If you are receiving an error
message in one store with a language relevant to another, you need to check
submissions in other stores for the conflict and resolve this before you can
submit data to any other store. Contact Selling Partner Support if you need
help identifying the conflict source.

