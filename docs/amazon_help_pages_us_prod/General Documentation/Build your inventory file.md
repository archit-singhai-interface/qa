---
title: Build your inventory file
url: https://sellercentral.amazon.com/help/hub/reference/G581
section: General Documentation
---

**Individual sellers:** This feature is only available to sellers with a
Professional selling plan. Learn more by visiting [Selling plan
comparison](/gp/help/64491).

You can use inventory file templates to list your products in the Amazon
catalog and to offer them for sale on Amazon. Inventory file templates let you
add or edit product listings in bulk. You can create a template to suit your
specific requirements and list different types of products across multiple
categories using one template. First, create your template by visiting [Add
Products > Spreadsheet > Download a blank template](/product-
search/bulk/generate). For more information, go to [Create your inventory file
template](/gp/help/202094740).

## Tips for building an inventory file

#### Backups

We recommend that you keep a backup copy of your completed template on your
computer hard drive so that you can use it later to make updates to your
listings.

#### SKU

The SKU is the key field in every inventory file and should not be altered or
reused. Amazon uses the SKUs in your inventory file to associate your product
listings (the product detail page and you offer) with your individual
inventory level records in the Amazon catalog. This means:

  * Every product in your inventory file must have a unique SKU.
  * Every new SKU you upload to Amazon results in the creation of a new record in the Amazon catalog.
  * Because each record is unique, an existing SKU cannot be changed. It remains in the catalog until you delete it.
  * If you upload an inventory file with data for a SKU that already exists, the most recent data replaces data from previous feeds.

#### Standard product identifier

We recommend that you always provide the UPC, EAN, JAN, or ISBN when creating
a new listing on Amazon. For more information, go to [Listing requirements:
Product IDs (GTINs)](/gp/help/G200317470). For the requirements for each
category, including exceptions and exemptions where available, go to [Product
ID (GTIN) requirements by category](/gp/help/G200317520).

#### Search terms

Customers primarily use search terms (keywords) to find products on Amazon.
Good search terms go a long way toward increasing product visibility. Most
products can support five keywords. Think like customers do and use search
terms that are popular on your own website or for your product line. For more
information, go to [Optimize your product discoverability](/gp/help/10471).

**Note:** Standard Book Loader files do not support search terms (keywords).
Amazon assigns search and browse information for products listed in the Books
category. However, you can use the [Add a Product](/product-search) tool to
increase the number of search keywords for your Books products.

#### Variation relationships

Some categories support variation relationships that include single parent
product and multiple child products.

Parent products are non-sellable products that you list in your inventory file
so you can create relationships between products.

Child products are unique, sellable products linked to a parent product. The
child product is similar to other child products (or siblings) linked to the
same parent product. However, the child varies from its siblings according to
specific criteria. These criteria are described in the variation-theme section
of the **Data Definitions** tab on the inventory file template. Acceptable
variation themes differ by category but might include attributes such as size,
color, and flavor.

Set up parent-child relationships in your inventory file whenever possible.
This makes search and browse results much more manageable for customers
because related child products are grouped together. When you set up parent-
child relationships, distinguish each child product in the title. For example,
if you sell shirts and some are red and some are blue, use "Shirt, Red" and
"Shirt, Blue."

**Note:** You must set up a parent-child relationship if an appropriate
variation theme exists for your products and category.

You can view the child ASINs for each parent ASIN in the Amazon catalog on the
**Add a Product** page in your seller account.

For more information, go to [Variation relationships](/gp/help/8831).

## Filling the template

You should use the Product template to add products that are not currently in
Amazon’s catalog. The template shows the required, conditionally required, and
recommended attributes. Conditionally required attributes become required
based on your inputs on the required attributes, optional attributes are
collapsed in each attribute group. To expand the optional attributes, click
the "+/-" signs on top of the column. Alternatively, on top left corner of the
sheet, you can select "1" or "2" to expand or collapse all the optional
attributes. The "1" button shows the default view and "2" button shows the
advanced view with all the attributes. In the default view, first attribute in
the group is not hidden so you can find the specific attribute group. For
further information, download and read the instruction in the template.

##  Save your inventory file

Before you upload your inventory file to Amazon, you need to save it as a text
(tab-delimited) file. Perform this step after you add products to your product
inventory file.

Here is how to save your updated inventory file:

  1. Save your work as an Excel workbook one final time. We recommend that you create a backup copy and add a date to the file name. This will help to keep a history of your work if you want to refer to prior versions or if there is an error in processing.

  2. Make sure the worksheet tab that contains your data is active.   

  3. On the **File** menu, click **Save As**. The **Save As** dialog box appears. 

  4. In the **Save As Type** select **Text (Tab-delimited) (*.txt)**. Browse to where you would like to save the file, rename the file, and click **Save**.
     * Click **Yes** if you see a warning that the selected file format (the tab-delimited file type) does not support workbooks containing multiple worksheets.
     * Click **Yes** if you see a warning that your file contains features incompatible with the selected Text (Tab delimited) file format.

You are now ready to upload your inventory file. For more information, refer
to [Upload your inventory file](/gp/help/201576670).

##  Set the lead time to ship in an inventory file

The lead time to ship is the time it takes you to get a product to your
shipment carrier. The total shipping time is then lead time \+ carrier time.

The following table identifies the fulfillment messaging that Amazon provides
to customers based on the product-level availability you provide in your
inventory data feed. Your product-level availability must be a number between
0 and 30.

Input (Days) |  Availability Message  
---|---  
Null, 0 | In stock  
1 | In stock  
2 | In stock  
3 | Usually ships in 2-3 days  
4 | Usually ships in 3-4 days  
5 | Usually ships in 4-5 days  
6 | Usually ships in 5-6 days  
7 | Usually ships in 6-7 days  
8 | Usually ships in 7-8 days  
9 | Usually ships in 8-9 days  
10 | Usually ships in 9-10 days  
11 | Usually ships in 10-11 days  
12 | Usually ships in 11-12 days  
13 | Usually ships in 12-13 days  
14 | Usually ships in 13-14 days  
15-21 | Usually ships in 2-3 weeks  
22-28 | Usually ships in 3-4 weeks  
28-30 | Usually ships in 4-5 weeks  
  
**Note:** If you do not specify a lead-time-to-ship value, the value is set to
1 to 2 days. If you use an inventory file template to update your inventory
amounts, be sure to specify your lead-time-to-ship value in the
**fulfillment_latency** field.

## Multi-Store Listing Template

If you selected multiple stores when generating your category-specific
inventory file on the [Download a blank template](/product-
search/bulk/generate) page, this section applies. Including additional stores
in your template will add columns for you to provide store-specific offer
data, including price. For each SKU, provide offer values for each store in
which you would like to list the item. The product data you provide in your
template will apply to the SKU in the store in which you submit your template.
If you provide offer data in your template for a marketplace in which the
detail page for your listing does not yet exist, Amazon will attempt to create
the detail page by translating your product data into the primary language of
the requested marketplace, which can take up to 48 hours to complete.

## Definitions

  * Home marketplace: marketplace in which you submit your Multi-Marketplace Template (MMT)
  * Secondary marketplaces: additional marketplaces that you select when generating a MMT in Seller Central.
  * Interactive Listing Workflow (ILW): This is the interactive web form that you can use to create and manage your listings one at a time instead of using a spreadsheet. Access by choosing [Add a Product](/product-search) from the Inventory drop-down.

## Frequently asked questions

## What is MMT?

MMT is an extension of the category-specific inventory file templates that you
can generate on the [Download a blank template](/product-search/bulk/generate)
page in Seller Central. You can generate MMT by visiting [Add
products](/product-search/bulk) under the Inventory menu in Seller Central. To
generate MMT, select multiple marketplaces before you generate your template.
The list of selectable marketplaces displayed includes all marketplaces in
which you are authorized to sell and have your accounts linked.

## Should I use a period (.) or a comma (,) as the decimal separator for my
prices in the template?

Use a consistent decimal separator throughout the template, including for
prices in each marketplace. This should be the decimal separator that you
normally use when using Amazon’s listing templates.

## Which currency is used for the prices I provide in my MMT for each
marketplace?

Prices must be provided in the primary currency of each marketplace. The
currency for each marketplace is shown in the column header.

## How is MMT different from the single-marketplace Inventory File template?

Unlike the single-marketplace template, MMT contains columns for each
secondary marketplace that you can use to provide information about your offer
(e.g. price). These columns of the template are marked with headers indicating
the marketplace to which the columns apply (e.g. UK, DE). At a minimum, you
must provide a price to create a listing in a secondary marketplace. If the
ASIN does not already exist in the secondary marketplace, Amazon will attempt
to create the listing in that marketplace for you.

  * If a detail page for the ASIN in the language of the secondary marketplace does not exist, Amazon uses detail page content from a marketplace where the ASIN already exists as the source content for the translations. In addition, Amazon uses the offer data you provided in MMT for the secondary marketplace to create or edit your offer in that marketplace. It is possible that due to legal and compliance reasons, Amazon may not be able to create a detail page on your behalf in a secondary marketplace.
  * If the product does exist as an ASIN in the Amazon catalog in the secondary marketplace, Amazon does not translate your product data for use on the detail page in the secondary marketplace. 

## Does MMT enable me to improve my detail page for multiple marketplaces?

Yes. As you update your product data over time in the home marketplace, your
updated product data is translated into the languages of the secondary
marketplaces and updated on the product detail pages in those marketplaces.
Note that if you provide your own translated content directly into a secondary
marketplace using another listing tool, that content will take precedence over
any current or future translations performed by Amazon.

## Am I required to list all products in my template in every marketplace in
the template?

No. For each SKU, you can provide offer data for any marketplaces in which you
want to list your item. Each SKU can be listed in one or multiple marketplaces
in the template. The red highlighted cells are only required if you wish to
list in that marketplace.

## Before I submit MMT, do I need to check whether the detail page for an ASIN
exists in each of the secondary marketplaces?

No. If the detail page exists in a secondary marketplace and you provide
values for the secondary marketplace for price and currency in MMT, Amazon
will create the offer for the ASIN in the secondary marketplace. If the detail
page does not exist in the secondary marketplace, Amazon will attempt to
create the detail page on your behalf.

## How long does it take Amazon to create ASINs in secondary marketplaces?

The process of creating a detail page with your offer can take up to 48 hours,
but usually completes within 24 hours. When you provide values for price and
currency for a secondary marketplace, you are expressing an intent to list in
that marketplace and Amazon will attempt to create the listing in that
marketplace for you. It is possible that due to legal and compliance reasons,
Amazon may not be able to create a detail page on your behalf. We recommend
that you check your secondary marketplace’s Manage Inventory directly after 48
hours to ensure your listings have been created successfully.

## Where can I learn more about Amazon’s listing policies for each
marketplace?

For information, go to [Amazon’s Category, Product, and Content
Restrictions](/gp/help/G200301050) page.

## Does the Processing Report on the Add Products via Upload page inform me
about whether the detail page exists in each of the secondary marketplaces
after submission?

Yes. For each SKU in your MMT for which the detail page does not exist in a
secondary marketplace and for which you provided a price, the processing
report will contain a message to indicate that Amazon is attempting to create
the detail page on your behalf. Because the processing report is generated
before the detail page creation process in secondary marketplaces is
completed, the processing report does not provide information about the status
of listing creation in secondary marketplaces.

## After submitting MMT, where can I see the status of detail page creation in
the secondary marketplaces?

Go to the**Inventory** menu on the top navigation bar, and select **Manage All
Inventory**. Find the SKU you wish to check and click **Edit** in the right
column. On the **Offer** tab, scroll to the bottom of the page to find the
status of the ASIN in each marketplace. If Amazon is still translating your
listing, it will show as ''in progress''. If translation cannot be completed,
this will also be shown.

## What attributes do I need to provide in my template to improve the
likelihood that detail page creation in secondary marketplaces will be
successful?

In addition to providing values for all required attributes, Amazon recommends
that you provide values for compliance attributes such as power_plug_type.
Note that these attributes are not applicable to all product types and
marketplaces and therefore may not exist in the template for all product
types.

## If Amazon is not able to create a detail page for my ASIN in a secondary
marketplace after I submit MMT, does this mean I am not allowed to sell the
product in that marketplace?

You must comply with all applicable laws when listing and selling products on
Amazon, including applicable laws in each jurisdiction in which your products
are sold. If you determine that you are allowed to sell a product in a
marketplace for which MMT did not result in successful detail page creation,
you can create the detail page by using another listing tool, such as a
single-marketplace listing template or the Interactive Listing Workflow.

## How does Amazon choose the source content to be used for translations when
creating a detail page for an ASIN in a secondary marketplace?

If the detail page for your product does not exist in any Amazon marketplace
worldwide prior to your submission of MMT, Amazon will use the content you
provide in MMT for the home marketplace as the source for translations when
attempting to create the Detail Page in the secondary marketplace. If you have
already created the ASIN in multiple marketplaces and have linked your
accounts across those marketplaces, Amazon will use listing contributions from
one of the marketplaces in which you have a listing for ASIN as the source
content for the translations.

## Can I use MMT to provide values for bullet points in my home marketplace
and have Amazon translate those values to be added to my listings in the other
European marketplaces for existing ASINs?

No. Product data provided in MMT is not translated and contributed to the ASIN
in a secondary marketplace if the detail page already exists in the secondary
marketplace at the time that you submit MMT. Translation and contribution of
product data to a secondary marketplace occurs only in the scenario that the
ASIN does not exist in the secondary marketplace at the time of MMT
submission.

## On the Add Products via Upload page, how is the list of selectable
marketplaces determined?

The list includes all marketplaces in which you are registered and are able to
create listings in. You must have linked your accounts to access marketplaces
outside of a region such as Europe or North America.

## Can I have multiple home marketplaces?

Yes, you can download and submit MMT in any marketplace in which you are
authorized to list products in bulk. The home marketplace is not determined by
an account setting, but rather determined by the marketplace in which you
download and submit your MMT.

## Can I use MMT to provide a unique set of product images for each
marketplace?

No, MMT does not provide this capability. The product images that you provide
in MMT will be used for all marketplaces.

## Can I use MMT to provide my own translations for important product
attributes such as Product Attribute Bullet Points?

No, MMT does not provide this capability. To provide your own translated
product content for secondary marketplaces, use a single-marketplace template
for each marketplace or the Interactive Listing Workflow for each marketplace.

## How can I view and edit the translated content in secondary marketplaces?

Select the marketplace for which you want to view the translated content using
the marketplace switcher at the top of the Seller Central page. You can then
view and edit the translated content by visiting the Manage Inventory page
under the Inventory menu, and clicking Edit for the SKU you want to change. If
you would like to overwrite the translation with your own content, you can
submit content in the text box for the attribute.

## What is the difference between Build International Listings (BIL) and MMT?
Why should I use one or the other?

  * BIL is typically used to synchronize all listings in an account from one marketplace to another. MMT attempts to create offers in secondary marketplaces only for ASINs that you have expressed an intent to list in that marketplace by providing a price for the marketplace in MMT.
  * BIL sets prices based on rules (e.g. same as source marketplace), while MMT uses the marketplace-specific prices you provide for each SKU.
  * BIL continuously updates prices in secondary marketplaces based on changes in the currency exchange rate, while the prices provided in MMT are static.
  * BIL requires you to define a source marketplace, from which your catalog is replicated, and a target marketplace. MMT can use as the source marketplace any marketplace in which you are authorized to list products in bulk.

## How does the submission of MMT affect the settings of my ASINs in BIL?

You can use both BIL and MMT. However, if you have an SKU whose price for a
particular marketplace is defined using a BIL price rule, the BIL price rule
will be turned off for that SKU in the target marketplace if you provide a
price in MMT or other listing tool for that marketplace and SKU. If you want
to revert to using the BIL price rule, remove this ASIN from the BIL exclusion
list for that marketplace using the Build International Listings page in
Seller Central. Conversely, if you previously provided the price for an ASIN
in a marketplace using MMT, and you subsequently create a BIL connection with
that marketplace as the target marketplace, the BIL price rule that was
defined when setting up the BIL connection will take precedence over the price
previously provided in MMT.

## Do I need to request authorization to sell in my product category in each
marketplace?

You must request approval separately in each marketplace for most approvals.

## How can I see marketplace-specific errors for my listing submission?

Marketplace-specific errors for offer data that you provide in MMT will appear
in the processing report that Amazon provides after you submit your template.
If the errors do not prevent SKU creation, you can also view the errors by
signing in to Seller Central for the marketplace you want to check and then
viewing your SKU in Manage Inventory.

## Does the Update operation also delete my pre-existing product data in the
secondary marketplaces and replace it with translated content from MMT?

No. The product data for your listing in the secondary marketplaces is not
deleted. The submission of MMT affects only the offer data (for example,
price) for your listing in the secondary marketplace.

