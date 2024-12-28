---
title: Inventory file upload FAQ
url: https://sellercentral.amazon.com/help/hub/reference/G201201070
section: General Documentation
---

## How long does it take for an inventory file upload to process?

Processing time will depend on the file size. Small files may load in minutes,
while larger files (greater than 5 MB) may take up to eight hours to process.
If a small file is not processed within an hour, it is potentially stuck.
Likewise, if a large file is not processed within eight hours, it is
potentially stuck. In the event that this occurs, contact [Seller
Support](/hz/contact-us) to cancel the inventory file upload so it can be
resubmitted.

## How can I fix inventory file upload errors?

If you receive any errors after you upload an inventory file, refer to the
processing report to obtain more information about each error. We recommend
that you open your inventory file and processing report side-by-side, so you
can determine which fields in your inventory file resulted in upload errors.

To download and review processing reports, see [Review a processing
report](/gp/help/200194300)

## Why won’t product information that I submitted in an inventory file upload
successfully?

There are several reasons why product information might not appear to upload
successfully.

#### Has the inventory file been delayed?

To determine if a submitted inventory file has been processed, go to [Check
Upload Status](/product-search/bulk/status) within the [Add
Products](/product-search/bulk) page in Seller Central. The status of
submitted inventory files will appear as **Request Submitted** , **In
Progress** , or **Done**. Processing time will depend on the file size. Small
files can load in minutes, while larger files (greater than 5 MB) might take
up to eight hours to process. If a small file is not processed within an hour,
it is potentially stuck. Likewise, if a large file is not processed within
eight hours, it is potentially stuck. In the event that this occurs, contact
[Selling Partner Support](/cu/contact-
us?categoryId=30002&typeId=30007&itemId=0) to abort the inventory file upload
so it can be resubmitted.

#### Did any records have errors?

To determine if a processed inventory file had any errors, , go to [Check
Upload Status](/product-search/bulk/status) within the [Add
Products](/product-search/bulk) page in Seller Central. In the **Upload
Status** column, you will see the number of records with errors, and you can
find details in the [Processing reports](/gp/help/201576740). To troubleshoot
inventory file errors, see the FAQ above: How can I fix inventory file upload
errors?

#### Are any records suppressed?

It’s possible for you to submit an inventory file that processes without
errors, but when you visit the associated product detail page, the listing
cannot be found. This usually occurs when one or more detail pages lack
product images. In this scenario, the SKU might be
[suppressed](/gp/help/200898440).

#### Do you have detail page control?

It is possible that product data you upload will not be reflected in the
catalog due to [detail page control](/gp/help/200335450). Detail page control
rolls up contributions from multiple sellers into a single **reconciled** view
for buyers in the catalog.

## How do I use inventory files to create variations (that is, parent-child
relationships)?

You can create variations in most product categories on Amazon. In inventory
files, you use variation themes (i.e. Size, Color, SizeColor) to describe how
your products vary. Variation themes differ by category. To view a list of
available variation themes, go to [Download a blank template](/product-
search/bulk/generate) to download the inventory file template for your
product’s category and refer to the Data Definitions tab; the Variation
Information section will contain a list of available variation themes. You can
also refer to the Valid Values tab of the inventory file template for a list
of available variation themes.

When you create variations, you create a child SKU for each variation (Size,
Color, etc.) of the product, and you create a single parent SKU that acts as a
display case in the catalog for the child SKUs. For instructions on how to
create variations after you’ve downloaded an Inventory File Template and
chosen a variation theme for your product, see [Create parent-child
relationships](/gp/help/8841).

## Can I modify shipping settings using inventory files?

Use the [Shipping Settings](/sbr) feature in your account to customize your
standard service levels, shipping regions, and shipping rates. To make
product-level shipping exceptions, use the [Shipping Overrides
Template](/gp/help/200212820). Sellers typically use shipping overrides to
offer free shipping on products and to set custom shipping rates for oversized
or overweight items.

## Can I upload images in bulk using inventory files?

Yes, include URLs to your images in your inventory files.

You can also match or create product listings in bulk using Add Products via
Upload on Seller Central.

Additionally, check the [Preparing Product Images](/gp/help/G16881) Help page
and for more information.

## How can I fix inventory file upload errors related to a product identifier?

  

  1. Confirm the UPC is valid; locate a check digit calculator online to check the validity of the UPC
  2. If the UPC begins with a leading zero (e.g. 013803156881), format the standard product ID column to ensure the leading zero isn’t removed after you enter the UPC
  3. If you received a [UPC exemption](/gp/help/200426310) in a category:   

    1. Ensure the brand of the item is not included in one of the following lists: 
       * [Baby category brands that require UPCs](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/Baby.Required.Brands.xlsx)
       * [Beauty Major Brands Requiring UPCs](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/Beauty_Major_Brands_With_UPCs.xls)
       * [Clothing, Accessories & Luggage Brands Requiring UPCs](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/Shoes_Clothing_Handbags_Sunglasses_Major_Brands_Requiring_UPCs2.xls)
       * [Health & Personal Care Major Brands Requiring UPCs](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/HPC_UPCRequiredBrandList.xlsx)
       * [Sports & Outdoors UPC Required Brands](https://images-na.ssl-images-amazon.com/images/G/01/rainer/help/sports_store_brands_to_require_upc.xlsx)
    2. Refer to the instructions in the email you received when you were granted the exemption for instructions on how to use it

## How can I update the price and quantity of my products using inventory
files?

You can update the price and quantity of your products by using:

  * The [Price & Quantity](/gp/help/201576480) file (the easiest way)
  * The [Inventory Loader](/gp/help/201576540) file
  * The appropriate [category-specific inventory](/gp/help/1641) file

**Note:** you can update prices and quantities by modifying your existing
inventory file, or you can upload a new inventory file that contains only
SKUs, prices and quantities, and use the Partial-update feature.

## Can I update sales tax information using inventory files?

Yes, you can. After you’ve configured your [Tax Settings](/gp/tax-
manager/dashboard.html), you can use the **Product Tax Code** field in
inventory files to add or remove product tax codes from SKUs and collect tax
accordingly. Learn more about [Tax Calculation Services](/gp/help/200787660).

## Can I update the category of a product using inventory files?

You can change the category of a product by including the product in an
[inventory file](/gp/help/1641) for the category you prefer; however, the
category must be appropriate for the product and the change is subject to
[Detail Page Control](/gp/help/200335450).

