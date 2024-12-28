---
title: Listing Loader overview
url: https://sellercentral.amazon.com/help/hub/reference/G200231900
section: General Documentation
---

Listing Loader is a template for uploading your inventory on Amazon for
products that already exist in Amazon's catalog. It enables you to provide the
listing attributes without the product attributes, which are required when
using product feeds.

For products that do not exist in the Amazon catalog, they need to be added to
the catalog before you can use the Listing Loader. To learn about adding
products to the catalog, see **Add products to the Amazon catalog** under
[Product detail pages and offers](/gp/help/G51). To create new product detail
pages or update an existing product detail page (information like the title,
description, and so on.), you have to continue using [Inventory File
Templates](/gp/help/G1641).

**Note:** You must be registered with Release Package 1.7, 1.9, or 4.1 to use
the Listing Loader. See [Inventory file templates and BTG](/gp/help/G1641) to
confirm which release package you have and which templates are available to
you.

## Functionality

Listing Loader provides the following functionality:

  * Match products in all categories you are eligible to sell using a single template.
  * Match based on standard product ID alone, reducing data required to list on Amazon.
  * Upload directly from Excel, saving you time.

**Note:** The Listing Loader does not have fields for sellers to enter
shipping options for BMVD products. We recommend the [Inventory
Loader](/gp/help/G202154120) for listing BMVD products.

## Using Listing Loader

**Note:** You can use the Amazon Standard Item Number (ASIN) if you do not
have the product identifier to use the Listing Loader. Similarly, for
categories that do not require a product identifier such as UPC, EAN or JAN,
you can enter the ASIN in the product-id field in the template and set the
product-id type to ASIN for creating or updating your listing. For detailed
instructions, see [Use the Listing Loader](/gp/help/G201584910).

## Eligible categories

You can use the Listing Loader to create or update your listings in the
supported categories below. You might not be eligible to sell in certain
categories.*

  * Apparel* 
  * Automotive
  * Baby
  * Beauty
  * Electronics
  * Grocery & Gourmet Food
  * Health & Personal Care* 
  * Home & Garden
  * Industrial
  * Kitchen* 
  * Miscellaneous
  * Musical Instruments
  * Office Products
  * Outdoor Living* 
  * PC Hardware
  * Pet Supplies
  * Software
  * Sporting Goods* 
  * Tools
  * Toys
  * Video Games
  * Watches
  * Wireless Accessories

**Important:** Do not use ASINs as the product ID for variation-enabled
categories.

**Note:** For basic matching in all product categories, either the Listing
Loader or Inventory Loader can be used. The Listing Loader will allow sellers
to enter information for non-BMVD Products, with optional fields such as sale-
start-date and is-gift-wrap-available. The Listing Loader does not have fields
for sellers to enter BMVD Product shipping settings.We recommend the Inventory
Loader if your inventory includes BMVD Products. In cases where multiple
matches are found for a product, however, the Listing Loader may help you
resolve this issue more easily.

## Products Not Found

Some categories may require additional approval to list, and you can request
approval through Manage Your Inventory and [Fix Your
Product](/fixyourproducts) after Listing Loader submission. If you are listing
in a category not supported by Listing Loader, product lookup, when used in
conjunction with a product identifier (UPC, EAN or JAN), you will see errors
in the processing summary. You must use other tools like the Inventory File
Templates or [Add a Product](https://sellercentral.amazon.com/product-search)
tool to add or update your listing.

It is also possible that a product already in Amazon's catalog does not have a
product identifier associated with it. In such cases, product lookup will put
your listing on "Products Not Found" sheet. To create a listing for such a
product, you must use the associated ASIN as the product-id and set the
product-id-type to ASIN.

If, however, the product is not in Amazon's catalog, you must first create the
product.

## Listing photos

You can use Listing loader to add Listing photos in bulk to your existing
listings in categories where Listing Photos is enabled. When using the Listing
Loader to upload your listing photos, you are only required to provide the SKU
and the URLs of your photos in the **Offer XX** field. All other fields are
not required.

