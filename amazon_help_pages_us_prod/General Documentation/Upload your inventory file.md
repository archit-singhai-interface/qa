---
title: Upload your inventory file
url: https://sellercentral.amazon.com/help/hub/reference/G601
section: General Documentation
---

## Fulfillment by Amazon

If you are uploading inventory for Fulfillment by Amazon, follow the
additional instructions provided in [List FBA Products in
Bulk](/gp/help/200327780).

After you [build](/gp/help/581) or [modify](/gp/help/G201576660) your
inventory file, you can save the file either as tab-delimited text (.txt) or
excel (.xls) format.

To upload the file, follow these steps:

  

  1. Under **Catalog** on Seller Central, go to **Add Products via Upload**. 

**Note:** If you have a [North America Unified Account](/gp/help/201394090),
check the website selected or switch stores to select the preferred store and
ensure you upload inventory files to the correct website. Also, check your
file to be sure the quantity value is greater than 0 (zero) for listings that
use a global SKU. If you change the quantity to 0 in one store, the listing
will be removed from all Amazon North America stores.

  2. Click **Upload your spreadsheet** tab. In the **Upload File** box, drag and drop the inventory file (You could click **Browse files** instead). When file is selected, the status bar will load from 0 to 100%, validating the file. 

**Note:** Validation completed status does not finish upload process.

Once file validation is complete, **File type** is automatically detected for
most cases, except for inventory loader and non-Amazon files. If the **File
type** is not automatically selected, use the drop-down to select your file
type.

If you are using a product file to create new pages in the Amazon catalog, you
will usually choose the first option for "Inventory Files for non-BMVD
Categories."

**Note:** For BMVD Product files and Inventory Loader files, the upload box
will contain additional options for shipping settings. For more information
about using these options, see [Ship BMVD Products](/gp/help/200384330).

  3. If required, see below for information about the "Purge and Replace" option.
  4. Once you confirm all the information on the page, click **Upload file** at the bottom of the page.

Uploading your inventory file is not enough to ensure success. After uploading
your inventory file, follow the link to review your results. For more
information, see [Review my inventory results](/gp/help/611).

## Purge and replace your inventory

If you want to remove your entire inventory and replace it with only what is
in the file you are uploading, click **Purge and replace your inventory** on
the right upper corner of the **Upload File** box.

**Note:** This will cause any listings which are not in the inventory file to
be deleted.

We recommend that you run an [Active Listing Report](/gp/help/200385890)
before using the Purge and Replace option. This report provides information
about all of the product listings in your seller account, including SKUs with
no quantity (0) available. The Active Listings Report provides a good basis
for reviewing your existing inventory records and can also serve as a backup
file in case there is an error in the file you send when you perform a Purge
and Replace.

You will normally add or modify listings by submitting your inventory file
with the **Add** option selected for the SKU you are adding or changing. This
is also the default option, so if you don't specify a different option, we
will assume you are adding or modifying your inventory data as described in
the record. (The add option and the purge and replace operation do not apply
to Price & Quantity Files, which are modify-only).

Instead of using the Purge and Replace option to remove items that are out of
stock, set the quantity to zero (0) in your inventory file or use a Price &
Quantity file for quick updates. Using Purge and Replace will permanently
delete your SKU along with associated product data contributions. If you want
to sell the product again, you must re-submit all of your product data using a
category-specific inventory file. For more information, see [Modify my
inventory file](/gp/help/G201576660).

If you are making a very substantial change to your listings, involving many
adds and deletes, you might choose to submit only the products you are adding
or modifying, and select the Purge and Replace option. However, since this
will cause any listings which are not in the inventory file to be deleted, if
the file you use for the Purge and Replace option does not contain all of your
available inventory, you may then need to submit another file with the **Add**
option to reload any listings that you still want to make available for sale
on Amazon. For more information, see [Use the purge and replace
option](/gp/help/G201576690).

Also, while it can be convenient to remove all your listings and start from
scratch, especially if you have lost track of the inventory you have listed on
Amazon. Be aware that selecting Purge and Replace can slow down the overall
processing of your inventory file.

Using the **Remove Existing Listings** option when sending a file will not
remove any listings that you created and managed exclusively using the Add a
Product tool. You cannot remove these listings using the Purge and Replace
option. If necessary, you must delete these manually through your **Manage
Inventory** page. Optionally, you can use an Inventory Loader file with the
'x' option to remove these listings. You may want to use an Active Listings
Report and convert it into an Inventory Loader file for this purpose. See
[Using reports to update inventory](/gp/help/200388940).

**Note:** When using the **Purge and Replace** option, if you have a North
America unified account and use global SKUs to share inventory, deleting the
listing in one Amazon site will also remove the listing from other Amazon
sites.

