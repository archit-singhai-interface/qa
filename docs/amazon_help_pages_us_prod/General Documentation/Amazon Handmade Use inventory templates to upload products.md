---
title: Amazon Handmade: Use inventory templates to upload products
url: https://sellercentral.amazon.com/help/hub/reference/GMU4YRNPVSDUGJZX
section: General Documentation
---

You can use inventory template files to upload listings to Handmade in bulk.
Handmade has a unique listing process that differs from other Amazon
categories, so there are some differences to keep in mind.

  * Listing attributes: 

**Global Trade Item Numbers (“GTIN”)** : Because all products listed in
Handmade are new, unique listings, Global Trade Item Numbers such as UPC, EAN,
JAN or ISBN are not required for Handmade products.

  * Amazon template instructions: 

**Example tab** : The Example tab does not apply to Handmade ASINs. Disregard
this tab for Handmade listings.

## List new Handmade ASINs using inventory templates

**Note:** Due to required customizations built into the listing process for
our apparel and shoe categories, you will be unable to use inventory templates
to upload items under these product types.

  

  1. Go to [Add Products via Upload](/listing/download?ref_=xx_download_tnav_upload)
  2. Under **Step 1: Select the types of products you want to sell** section, select **Handmade Products** from the **Product Classifier** menu and then continue on selecting until you run out of options.

**Note:** There is no restriction on generating a single template that
contains multiple Handmade product types. However, when you generate your
template it will be based on what you selected here and will not include
additional fields that may be required for other categories. This is why we
recommend creating separate templates for each product type you are listing.
For example, Baby in one file, Pet Supplies in another. That will ensure that
you are providing and legally required or sensitive information needed for
your items.

  3. Under **Step 2: Select marketplaces** , select the stores where you would like to list your products.
  4. Under **Step 3: Select the type of template**
     * For **Template Language** , select the template language of your choice.
     * For Mode, select **Custom**.
     * For **Available Attribute Groups** , add **Images** and **Offer**. If you are planning to sell your items via FBA, select **FBA** as well.
  5. Click **Generate Template** .
  6. Open the template and save it to the location of your preference on whichever device you will be uploading the template from. 
  7. With your template open, select the **Template** tab and update it with the information being requested. The following fields will always be mandatory:
     * **Product Type** : This will not auto-populate in the template field, but there is a drop-down selector where the product type you selected in the generation of your inventory file.
     * **Seller SKU** : SKU or Stock Keeping Unit is defined by you and can be any combination of alpha-number characters
     * **Sub** **Category** : This will not auto-populate in the template field, but there is a drop-down selector where the product type you selected in the generation of your inventory file.

**Note:** Depending on the _Product Type_ selected for your template,
additional details may be required. Those additional required details will
display in the template using the same color as Product Type, Seller SKU, and
Sub Category. For more information on filling out your template, go to [How do
I fill Out a Template?](/gp/help/G201467230).

  8. Navigate back to [Add Products via Upload](/listing/download?ref_=xx_download_tnav_upload) and select the **Upload your Inventory File** tab. Follow instructions on screen to upload your inventory file template.

**Note:** Once your items have been uploaded, you can [review processing
reports](/gp/help/G201576740) for instructions on identifying any potential
inventory file upload errors.

Uploaded ASINs are available in **Manage Your Inventory** and the Handmade 1x1
listing tool. If the quantity for your ASINs is greater than or equal to “1”,
they are immediately buyable once they display in Seller Central. If your
intent is to offer customizations, you will set the quantity to “0”, which
will enable you to set up the customizations first before it is available in
the Handmade store.

**Note:** Images may not immediately display in Seller Central or the product
detail page.

## Product Customizations

You cannot add product customization via inventory templates; however, you can
create the basic listing first and add customization details afterwards. Go to
[Amazon Handmade: Customizable products](/gp/help/G201817850) for more
details.

## Edit existing Handmade ASINs using inventory templates

You can edit your existing Handmade ASINs by using the [Add Products via
Upload](/listing/download?ref_=xx_download_tnav_upload) tool. Follow the steps
above to download a new Inventory File template, fill it out with the
appropriate edits, and upload the new Inventory file to Seller Central.

Here, the **update_delete** attribute offers three options for Makers to
update existing ASINs by SKU in inventory templates: **Delete** ,
**PartialUpdate** , or **Update (full)**.

  * **Delete** : Removes the selected SKUs.
  * **PartialUpdate** : Changes only SKU attribute cells where data is entered.
  * **Update (full)** : Overwrites all existing SKU attributes. If an attribute cell is left blank, selecting Update (full) will delete those attributes. Performing an Update (full) will also delete Customizations from existing SKUs. Only users experienced with inventory template functionality should perform an Update (full).

On the Handmade Inventory template, enter the relevant SKU for the product you
want to update. Select the appropriate option under the previously mentioned
**update_delete** attribute and enter the value you want to adjust. Once you
have entered all relevant information, upload the template and allow the
system up to 15 minutes for changes to display to your listings.

**Downloading current inventory information**

To facilitate access to the current product information, you have the option
to generate a Report with your Inventory details, which you can then copy and
paste to the Handmade Inventory template you will be using to edit the
listings. To generate this report:

  

  1. In Seller Central, hover over Inventory and choose “Inventory Reports” from the drop-down options.
  2. Select the type of Inventory report that best meets your needs for the items you want to edit.
  3. Click on the yellow “Request Report” button for a .txt file to generate. You can select all of the information and copy it and paste it on an Excel file.

## FAQs

#### When should I use the Inventory File Upload?

You should use the Inventory File Upload when you want to create or edit
Handmade listings in bulk instead of using the 1x1 Add a Product tool.

#### Is this available for all Handmade categories?

You can use the Inventory File Upload feature for all categories, except the
Handmade Apparel and Shoes categories. These are currently unavailable.

#### What is the “customizable_template_name” attribute?

This attribute should only be used in the following situations:

  * When performing an **Update (full)** on an existing SKU:
    * Select the **GuildCustomization** value from the **customizable_template_name** drop-down. This will preserve your existing customizations when performing an Update (full).
  * If you perform an unintended **Update (full)** : This attribute will re-enable any deleted Customizations.
    * Enter the affected SKUs or use the existing template.
    * Select **PartialUpdate** under the **update_delete** attribute.
    * Select the **GuildCustomization** value from the **customizable_template_name** drop-down.
    * Upload the inventory template file.

#### How do I tell from the template if I am listing in Handmade?

The attribute **Product Type (feed_product_type)** determines the category in
which you are listing. Handmade Product Types are listed as guilds:

  * guildaccessories
  * guildbaby
  * guildbeautygrooming
  * guildhome
  * guildjewelry
  * guildpetsupplies
  * guildtoysandgames

You can tell that the subcategory chosen is within Handmade if Valid Values
under the **Summary of your selected products** in Add Products via Upload
starts with ‘handmade’; for example – handmade-engagement-rings.

#### Are products buyable once uploaded?

Once you have completed all the steps required, your items will be ready for
purchase immediately once processed within Seller Central. If you do not want
your products to be available immediately, set your Quantity to 0.

#### What are Lite, Advanced, or Custom templates?

The Lite option contains “Required” attributes associated with the selected
products. “Required” attributes are the minimum values necessary to create
your product in the Amazon catalog (for example, item_sku).

The Advanced option contains all attributes groups associated with the
selected products. This option includes “Required”, “Preferred”, and
“Optional” attribute groups.

The Custom option allows you to choose attribute groups associated with the
selected products that you can add to your template. This option includes the
“Required” attribute fields.

#### Can I transfer information from other websites?

Yes. If you have products listed on Etsy, for example, you can transfer some
product details onto your Amazon Inventory File Template. For more
information, go to [Transfer product details from Etsy to Amazon
Handmade](/gp/help/GRDU4XCFF6GFRFE8).

