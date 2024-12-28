---
title: Modify Your Inventory File
url: https://sellercentral.amazon.com/help/hub/reference/G201576660
section: General Documentation
---

You can modify your inventory files to:

  * Update existing products and offerings on Amazon.
  * Create new products and offerings on Amazon.
  * Delete existing products and offerings on Amazon.

If you have not built an inventory file, refer to [Build My Inventory
File](/gp/help/201576650).

##  Update existing products

Updating the product or offering data associated with one of your SKUs is as
simple as uploading an inventory file containing the modified information. If
you are using a product file or matching file, you have to also include all
the data for that SKU that is not changing. The Price & Quantity file only
accepts three columns (SKU, price, and quantity) and is the quickest way to
update inventory levels, including setting out-of-stock items to zero (0)
quantity.

To edit or modify a listing, follow these steps:

  

  1. On the Inventory tab, select 'Manage All Inventory'
  2. Click the Action link for the SKU you want to edit.
  3. Select Edit details from the drop-down list.
  4. When you finish editing, click Save and finish.

If you are following the data management tips below, you can change the entry
for that SKU in your primary product template, paste the modified row into
your blank template, repeating as necessary for other SKUs, save the new
template as a tab-delimited text file, and then upload it.

**Data Management Tips**

When working with incremental uploads, you might lose track of your full data
set. Here are a few pointers to help maintain your data integrity:

  * Always maintain a primary product template in each category you sell that contains your latest product data. The product template is the Microsoft Excel file you use to generate your inventory files.
  * Keep a blank product template on hand. Then, when you make changes to your primary file you want reflected in the Amazon.com catalog, you can delete the modified rows from the primary template and paste them in the blank template. Then, you can create a new inventory file containing data for just the items you want to update.
  * Never change the value in a product's SKU field. We use the SKU to match your product data with the appropriate entry in the catalog.

Always review your results following any upload, to verify success.

##  Incremental uploads

You do not have to upload an inventory file containing all of your product
listings every time you want to update information about your SKUs. When
uploading the file, you can upload an inventory file containing information
about only those SKUs that you want to create, update or delete.

If you uploaded a product matching file, your listing data will remain on
Amazon until you upload a new file to modify or delete the specific SKUs
matched to pages in Amazon's catalog.

If you uploaded a Listing Loader file, or Inventory Loader, your listing data
will remain on Amazon until you upload a new file to modify or delete the
specific SKUs matched to pages in Amazon's catalog.

The following table shows how this incremental upload process affects the data
in the Amazon catalog after four separate inventory file uploads:

| Inventory File Contents |  | Catalog Data  
---|---|---|---  
Attempt | SKU | Name | Price | Operation | SKU | Name | Price  
1 | 001 | Big Shirt |  45.00 | Update |  | 001 | Big Shirt | 45.00  
002 | Small Shoes | 39.00 | 002 | Small Shoes | 39.00  
2 | 003 | Long Pants | 23.00 | Update |  | 001 | Big Shirt | 45.00  
002 | Small Shoes | 39.00  
003 | Long Pants | 23.00  
3 | 002 | Small Shoes | 0.00 | Delete |  | 001 | Big Shirt | 45.00  
003 | Long Pants | 23.00  
4 | 001 | Men's Big Shirt | 44.99 | Update |  | 001 | Men's Big Shirt | 44.99  
003 | Men's Long Pants | 38.99 | 003 | Men's Long Pants | 38.99  
  
In the example above, each upload either updated or deleted data in the
catalog. You can modify, create, and delete products in the catalog using
several feeds or using just a single feed.

##  Create new product listings

Creating a new product page in the Amazon.com catalog is as simple as
uploading a new inventory file containing product data for the new item. If
you follow the data management tips above, you can add the entry for that SKU
in your primary product template, paste the new row into your blank template,
repeating as necessary for any other new SKUs. Next, save the new template as
a tab-delimited text file and [Upload Your Inventory
File.](/gp/help/201576670)

As always, [Review Processing Reports](/gp/help/201576740) following any
upload, to verify success.

##  Delete existing products

The specific process for deleting products depends on the type of file you are
submitting.

**Delete products for non-BMVD categories**

To delete a product from your inventory and remove your product data
contributions for that product using a category-specific file for a non-BMVD
product category, submit your category-specific inventory file with no value
for the price and quantity data for the selected SKU. Also, enter "delete"
into the "update-delete" field for selected SKUs.

**Delete products for BMVD categories**

To delete a product from your inventory and remove your product data
contributions for that product using a category-specific files for a BMVD
product category, submit your category-specific file with a value of zero (0)
quantity for the selected SKUs. Also, enter "x" into the "add-delete" field
for the selected SKUs.

**Delete products from inventory loader files (all product categories)**

To explicitly delete a product from your inventory and remove your product
data contributions for that product using an Inventory Loader File, submit a
file with a zero (0) quantity value for the selected SKUs. Also, enter "x"
into the "add-delete" field for the selected SKUs. For more information, see
[Delete SKUs Using Inventory Loader.](/gp/help/201576560)

If you follow the data management tips above, you can cut the entry for the
SKU you want to delete from your primary product template and then paste the
entry into your blank template, repeating for other SKUs if necessary. Next,
remove any price- and quantity-related values. Then, code the explicit delete
field for your file type as explained above. Finally, save the template as a
tab-delimited text file and then upload it.

##  Special considerations

There are a few special things to consider when you use inventory files to
update, modify, or delete your inventory.

  

  1. A child item cannot be assigned a new **parent-sku** value without first removing the relationship to its original parent item. To eliminate the relationship, you can delete either the parent or child product SKU.
  2. When you delete a parent, you remove the relationship between that parent and all of its children. When you delete a child item, you eliminate the relationship between just that child and its parent.
  3. After the original relationship is removed, you can re-assign the child item to a new parent item by entering that parent item's SKU in the child item's **parent-sku** field.
  4. For some products, your upload might trigger Error Code 8005. This error occurs when you attempt to change certain fields for items with current offers on Amazon. For more information about this error and corrective steps to take, see [Error 8005](/gp/help/23191).

