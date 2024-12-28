---
title: Relisting ‘Inactive’ Handmade listings
url: https://sellercentral.amazon.com/help/hub/reference/G2YC8BRR324G39TY
section: General Documentation
---

Following the reinstatement of your Handmade selling privileges, you will find
that your ASINs remained in ‘Inactive’ status.

## Manually Reactivate Listings

The easiest way to reactivate your listings is to attempt a manual
reactivation by doing a simple edit on each of your ASINs.  

  1. Go to your [Manage Inventory](/hz/inventory) page.
  2. Click **Edit** on the right of each Handmade listing.
  3. Make a small update by adding space or punctuation to your description.
  4. Click **Save and Finish**

Your Handmade listings should be active in a few minutes. If these steps do
not work, follow the instructions below for using Inventory Loader.

## Utilize Inventory Loader

If you have a lot of ASINs to reactivate or manually reactivation does not
work, you can try re-uploading your listings using Inventory Loader. The
following instruction walks you through this process.

**Step 1: Create an Inactive Listings Report**  

  1. Go to [Inventory Reports](/listing/reports/ref=xx_invreport_dnav_home).
  2. From the **Select Report Type** drop-down menu, select **Inactive Listings Report**.
  3. Click **Request Report**.
  4. When the report is ready, click **Download**.
  5. Save this file to your desktop.

**Step 2: Download and Fill Out an Inventory File**  

  1. Download the [Inventory Loader Template](https://s3.amazonaws.com/seller-templates/ff/na/us/Flat.File.InventoryLoader_b2b.xls)
  2. Copy the following information from the **Inactive Listings** report that you downloaded in Step 1 and paste into your Inventory Loader Template.
     * SKUs
     * Product-id = _Enter the ASIN associated with your item_
     * Product-id-type = 1
     * Price
     * Item-condition = 11 – _this indicates that the item is new_
     * Quantity _– leave blank if item is FBA_
     * Add-delete = a _\- indicates that you are _adding_ a product, not deleting it_
     * Fulfillment-center-id – _only required if the ASIN is FBA_
  3. Once you have entered information in all of the required fields, save the file.

**Step 3: Upload the Inventory File**  

  1. Go to [Add Products via Upload](/listing/upload?ref_=xx_upload_tnav_download).
  2. Select the **Upload your Inventory File** tab.
  3. Upload File: 
     * From the **File type** field, select **Inventory Loader File**.
     * In the **File Upload** field, Select **Choose File** and upload your updated/saved file.
     * Enter your email address in the **Email Alert** field. We will contact you through this email address after your file has been uploaded.
     * Select whether you would like the Processing Report (Output) Format in Excel (recommended) or Text.
     * Click **Upload**.

**Note:** Following your upload, you can Review Processing Reports for
instructions on identifying any potential inventory file upload errors.

