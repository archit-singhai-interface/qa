---
title: Switch from using Amazon barcodes to virtual tracking
url: https://sellercentral.amazon.com/help/hub/reference/GGU374R3WCTMFK8L
section: General Documentation
---

This page describes the methods for switching your preference from using
Amazon barcodes for existing product listings to using manufacturer barcodes.
Switching your preference allows you to participate in virtual tracking and
send your inventory to fulfillment centers with only the manufacturer barcode.

Learn about the general requirements for changing your preference, how to
verify that your products are eligible for virtual tracking, and what to be
aware of after you change your preference to manufacturer barcode.

## Before you switch to manufacturer barcodes

Not all products are eligible for virtual tracking with the manufacturer
barcode. Also, Amazon updates product eligibility for this service
periodically. Before you change your preference to manufacturer barcode, go to
[Using manufacturer barcodes with FBA virtual tracking](/gp/help/200141480) to
review the eligibility requirements.

For FBA products that already have inventory in a fulfillment center and that
are tracked using an Amazon barcode, you must create a new listing with a new
SKU to use the manufacturer barcode. Products that have inventory in a
fulfillment center and that are tracked using an Amazon barcode must be sold
through or removed by submitting a [removal order](/gp/help/G201436560) before
the product listing can be switched to using the manufacturer barcode.

Barcode preference cannot be changed for shipments that have already been
created or for inventory that is already in a fulfillment center. Changes
apply to future shipments only.

## How to switch to manufacturer barcodes

Three options are available to confirm product eligibility and switch to using
the manufacturer barcode for tracking:

  * Change listings in bulk
  * Use the **Send to Amazon** workflow
  * Create a new SKU

#### Change listings in bulk

You can view and change listings in bulk by generating an Excel file with
eligibility details for your existing inventory, along with instructions on
how to update and upload the file to convert your eligible offers.

To convert listings in bulk, follow these steps:  

  1. Go to [Manufacturer barcode: Convert eligible offers](/c2c/feeds) and click **Generate download file** under step 1.
  2. Once the file is generated, click **Download File**.
  3. Once you open the file, read the help instructions and navigate to the worksheet labeled Manufacturer Barcode. For the products that you want to convert, enter a new SKU in the **SKU: Manufacturer barcode** column and type "Yes" in the **Enable manufacturer barcode tracking** column.
  4. After you complete the changes, upload the file following step 2.

**Note:** Not all SKUs that are eligible for manufacturer barcode can be
converted directly. Some SKUs may need to be relisted as a new SKU. This may
happen if there are open shipments or inventory associated with the existing
SKU in the network or due to other systemic restrictions.

#### Send to Amazon workflow

You can use manufacturer barcodes for individual eligible offers.

To use the Send to Amazon workflow to convert an individual listing, follow
these steps:  

  1. From the **Inventory** drop-down menu, select **FBA Inventory**.
  2. From the **Edit listing** drop-down menu to the right of the ASIN, select **Send/Replenish inventory**.
  3. On the step 1 of the Send to Amazon workflow, your eligible SKUs will have the link suggesting **Save using manufacturer barcode** under **Information/Action**.
  4. Click the **Save using manufacturer barcode** link and follow the directions to switch your barcode preference on your offer listing.

**Note:** If **Save using Manufacturer barcode** is not available in the
listing, the product may be ineligible for manufacturer barcode with virtual
tracking.

#### Create a new SKU

You can change barcode preferences for individual listings one at time by
creating a new SKU. A new SKU is required because the existing SKU is already
associated with inventory in the Amazon fulfillment network.

To create a new SKU for an existing listing, follow these steps:  

  1. From the **Inventory** drop-down menu, select **Manage All Inventory**. 
  2. From the **Edit** drop-down menu to the right of the ASIN, select **Add another condition**. 
  3. On the offer creation page, enter a new **Seller SKU** , fill out the remaining required fields, and click **Save and finish**. 
  4. On the **List as FBA** page, go to **Choose barcode type** page, select **Manufacturer barcode** from the drop-down menu and click **Confirm** and **List as FBA**.

**Note:** If **Save using Manufacturer barcode** is not available in the
listing, the product may be ineligible for manufacturer barcode with virtual
tracking.

**Note:** If your product doesn’t meet the virtual tracking eligibility
requirements, you may be able to get an exemption to use the manufacturer
barcode by applying with [Amazon Brand Registry](/gp/help/G202130410) and
enrolling your ASIN in the program. Non-brand-registered sellers would be
required to apply Amazon barcodes for the ineligible product.

## After you switch to manufacturer barcodes

When you create a new offer after you switch to using the manufacturer
barcode, information from the previous seller SKU typically won’t apply. The
table below summarizes the changes and recommended steps for your new SKU.

Area affected | Change | Recommended action  
---|---|---  
Inventory recommendations | The new SKU will have its own [inventory recommendations](/hz/sellingcoach?reportId=INVENTORY). | To avoid confusion, consider closing the old SKU’s offer and placing a removal order to have units returned to you.  
Pricing recommendations | [Pricing recommendations](/hz/pricing/dashboard) will not be available for the new SKU. That’s because certain nudges will show when a product has sold in the past 60 days but not in the past seven days. | We recommend using the past pricing recommendation for the new SKU.  
Advertising recommendations | [Advertising recommendations](/hz/sellingcoach/?reportId=ADVERTISING) will not be shown on the new SKU until a certain number of customers have viewed it. | If you received a notification on the old SKU and want to use available promotions, apply them to the new SKU.  
Business prices and quantity discounts | If you are an Amazon Business seller, you receive related [recommendations](/gp/help/201740300), and these may not be immediately available for the new SKU. | Consider applying past recommendations to the new SKU.  
Inventory planning | Your new and old SKUs will have separate entries under [Manage Excess Inventory](/inventoryplanning/excess-inventory), [FBA Inventory Age](/inventoryplanning/inventory-age), and [Fix Stranded Inventory](/hz/inventory?viewId=STRANDED). | Be sure to manage the correct inventory entries.  
Targeted advertising | Targeted advertising, such as [Sponsored Products](https://services.amazon.com/advertising/overview.html), won't automatically apply to the new SKU. | Launch new targeted advertising campaigns for the new SKU, or add the new SKU to existing advertising campaigns.  
Other advertising  | Deals, Coupons, Prime exclusive Discounts and Promotions won’t automatically apply to the new SKU. | Launch new advertising options for the new SKU.  
Subscribe & Save | [Subscribe & Save](/gp/help/G201620110) subscriptions won’t automatically apply to the new SKU. | Create a transfer subscription request for your new SKU in [Manage Subscribe & Save products.](/gp/help/G201958650)  
Virtual Bundles | Existing [virtual product bundles](/gp/help/G87HAE6PMKKM23Z7) won’t automatically combine with the new SKU. | Create a new virtual bundle including the new SKU.  
ASINs in the program | Converted ASINs may no longer be eligible for [Seller Fulfilled Prime](/gp/help/G201812230). | Check eligibility requirements and enroll products as appropriate.  
Selling globally | The new SKU will be created only for your home store. | If you want to [sell globally](/global-selling/dashboard), you must complete the same process to change the setting in each desired store. Barcode eligibility may vary by store.  
  
## More resources

  * [Using FBA virtual tracking](/gp/help/200141480)
  * [Create a new listing that uses virtual tracking](/gp/help/GCKCNHZRCF7SNQZR)
  * [Change to Amazon barcode by creating a new product offer](/gp/help/G9P8W8RZ96JFHVZH)
  * [Use an Amazon barcode to track inventory](/gp/help/G200141490)

