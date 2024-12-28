---
title: Use the purge and replace option
url: https://sellercentral.amazon.com/help/hub/reference/G201576690
section: General Documentation
---

If you decide to change the SKU naming convention you use to reference your
products, you can use the purge and replace option to do this. In general, it
is not recommended to use the purge and replace option to routinely manage
your inventory levels. Use the purge and replace option sparingly and for
special cases where you need to start from scratch with new inventory counts
or need to make changes to your SKU-naming conventions.

**Important:** We recommend that you request and download an [Active
Listing](/gp/help/G200385890) report before using the purge and replace
option. The Active Listings report provides a good basis for reviewing your
existing inventory records and can also serve as a backup file in case there
is an error in the file you send when you perform a purge and replace.

**Note:** When using the purge and replace option, if you have a North America
Unified Account and use global SKUs to share inventory, deleting the listing
in one Amazon site will also remove the listing from other Amazon sites.

## How to use the purge and replace option

Purge and replace deletes your entire inventory and replaces it with the
contents of the file you are uploading. To upload a purge and replace feed,
follow the steps below.  

  1. In Seller Central, click the **Catalog** tab. 
  2. Go to **Add products** and click **Spreadsheet**.
  3. On the right upper corner of **Upload Your Spreadsheet** box, click **Purge and replace your inventory** link.
  4. Under **Purge and replace your inventory** section, drag and drop the inventory file. You could click **Browse files** instead and select the excel file or tab-delimited text file (*.txt) you created earlier.
  5. After you select your file, status bar will load from 0 to 100%, validating the file.

**Note:** Validation completed status does not finish the upload process.

Once file validation is complete, **File type** is auto-detected for most
cases, except inventory loader and non-Amazon files. If the **File type** is
not auto-selected, use the drop-down menu to select your file type.

  6. Once you confirm all the information on the page, click **Purge and Replace** to upload your file.

## When to avoid the purge and replace option

You should not use the purge and replace option to change your SKUs in the
following two cases:

  * If there is overlap between your old and new set of SKUs, where any new SKU references a different product than the old one, don't use purge and replace.
  * If you are using the Fulfillment by Amazon (FBA) service, don't use purge and replace. It is not possible to use a different SKU for a product fulfilled by Amazon. In this case, you can create new SKUs for all your products not fulfilled by Amazon and then delete all old SKUs. 

Specifically, we don't recommend using purge and replace to perform the
following tasks:

## Disabling out-of-stock offers

If you have a large inventory, it is not recommended to make regular purge-
and-replace uploads with inventory files containing only in-stock products. If
your file does not contain a complete list of the products you want to make
available for sale, you may unintentionally remove listings and product data
contributions for some of them. Also, the processing time of a file with the
purge and replace option may take several hours and your available inventory
levels may change during that time.

If you run out of stock on some products, use the [Price and Quantity
file](/gp/help/G200385490) to set the stock levels to 0. You can use this file
to modify all of your listings, including those that were submitted manually
through the [Add a Product](https://sellercentral.amazon.com/product-
search?ref=xx_addlisting_dnav_xx) tool. It is also a more efficient process
that saves you the additional effort of re-listing your products later.

## Synchronizing your product database with your Amazon product listings

Although it is not recommended, you may use the purge and replace option to
keep the products you list on Amazon synchronized with your own product
database. The risk with this practice is having an error in your inventory
file or uploading the wrong file, which may potentially erase your entire
inventory on Amazon. This could result in lost sales opportunities while you
re-list your products.

**Important:** We recommend that you explicitly delete a product from your
inventory only if you know that you are never going to sell that product
again. If you are just temporarily out of stock, do not delete the product but
do set the quantity to zero (0).

