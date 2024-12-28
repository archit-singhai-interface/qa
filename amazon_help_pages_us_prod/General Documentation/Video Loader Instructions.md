---
title: Video Loader Instructions
url: https://sellercentral.amazon.com/help/hub/reference/G200482410
section: General Documentation
---

The [Video Loader](/gp/help/200482400) is a bulk page-creation and page-
matching tool for sellers who list products in our Video & DVD category. The
Video Loader template has tabs with Instructions, Image information, Data
definitions, Examples, and Valid values. The template also has four macros.

When you submit an Inventory File using the Video Loader, Amazon will either
match your listing data to an existing product page in the Amazon catalog or
create a new product detail page if none exist.

###  The Video Loader File Template

An Inventory File is a tab-delimited text file that contains the product-
related data Amazon needs to create product detail pages for listing your
products in our catalog. The information in inventory files is also used to
classify products for inclusion in browse structures and search results.

A Video Loader file is an Inventory file that contains the information we need
to list your Video (tape media) and DVD (disc media) products in our catalog
and to offer them for sale on Amazon. With the Video Loader, you can create
multiple new product pages and offerings using a single file. This is more
efficient than using the Add a Product tool, with which you may create only
one product page at a time.

There are four basic steps to using the Video Loader:

#### Download the template:

Download the Video Loader File template from the templates table on the
[Inventory File Templates](/gp/help/1641) page. You can also access this page
from the menu in the Upload Products & Inventory tool in Seller Central. Save
the template to your desktop.

#### Create your inventory file:

Enter detailed information about the products you want to sell on the "Video
Template" tab of the file to build your spreadsheet. You can manually enter
product details one-by-one, or if you have macros enabled, you can import an
existing file containing your product information using the Import File macro.

#### Validate your listing data:

Check the product information you entered for errors. If you have macros
enabled, you can automate this process by clicking the "Validate" button from
the Video Loader File menu. The macro checks data completeness and greatly
reduces upload failures due to input errors.

#### Upload your file to Amazon:

Click the "Upload File" button from the Video Loader File menu and enter the
email address and password for your selling account.

###  Downloading the template

To create your file, first download the [Video Inventory file
template](/gp/help/1641) to your hard drive. The template is a Microsoft Excel
file that contains a pre-formatted worksheet where you provide your product
data. It also includes additional worksheets to help you complete the
template.

###  Video Loader file tabs

When you open the template, you will see several tabs along the bottom of the
workbook:

Tab name | Description  
---|---  
**Instructions** | An overview of how to use the product template.  
**Image Info** | Information on how to include images in your upload. Includes file type requirements and naming conventions as well as size, DPI, and style requirements.  
**Data Definitions** |  A detailed review of each field in the inventory file, including label name, definition, use case, accepted values, and an example. Yellow rows indicate **required information**. To have your product listing upload properly, you must complete all required fields. Orange rows indicate **desired information**. Desired columns give customers the basic information they need to make an informed purchasing decision. It is highly recommended that you fill in all desired cells. Not doing so may result in poor product descriptions, and/or make your product offering hard to find. White rows indicate **optional information**. Optional information may be useful, but not critical, when offering a product for sale. We encourage you to fill out all optional cells that apply to your products.  
**Template** | This is the actual worksheet in which you enter your product data using the specifications listed in the Data Definitions tab. This worksheet contains a row to help Amazon know which template you are using and another row with column headings (label names) representing each of the fields in your inventory file. It has color-coded column headers to indicate whether the field is required (yellow), desired (orange), or optional (white).  
**Examples** | Example of a completed template tab with product data entered correctly.  
**Valid Values** | Lists of valid values for each type of data found in the template tab.  
  
###  Video Loader file macros

On the Add-Ins menu in the toolbar at the top of the template, you will find
four macros:

  * Validate
  * Upload file
  * Import file
  * Update template

With these macros, you can validate your data and learn how to correct any
errors, as well as automate some of the tasks in populating and uploading your
file. These macros are designed to simplify your experience and are highly
recommended.

###  Building your Video Loader file

On the Video Template tab of your Video Loader File template, enter the
product data for those items you want to list on Amazon. You'll find that each
column is color-coded to match the corresponding row on the explanatory Data
Definitions tab that indicates whether the field is required, desired, or
optional.

The Data Definitions tab contains details for each field in the template,
including a label name, definition, use case, accepted values, and an example.
The Valid Values tab has lists of the values accepted for some types of data
found in the template tab. Refer to these tabs to complete your template
correctly.

When you have finished entering product information in your file, we recommend
that you use the Validation macro in the template to make sure that your
information meets the requirements for each field.

Additional information about required, desired, and optional fields is
provided below.

###  Required Video Loader fields

The following is a description of the required fields in the Video Loader File
template. If these fields are not populated, your product listings will not be
accepted.

#### sku:

The SKU (Stock Keeping Unit) is the key field in every Inventory File. Amazon
uses the SKUs in your file to associate your product data with records in the
Amazon catalog. The SKU is also used to track inventory levels for your
product offerings. A SKU is a unique identifier and is assigned by the seller.
After you have established a SKU for a product, please do not try changing it
without first explicitly deleting the associated product data from our system.

#### product-id:

A standard, alphanumeric string that uniquely identifies the product, a UPC or
EAN. The product-id must have a specific number of characters: a UPC is a
12-digit number and an EAN is a 13-digit number.

**Tip:** To be sure that leading zeros are not dropped when entering the
number into the spreadsheet, format these cells as Text (right-click the cell
or column, then choose **Format Cells** > **Number tab** > **Text** ), and
double-check the cells to ensure that no errors have occurred after entering
the numbers.

#### product-id-type:

A numerical entry that indicates if the product-id is a UPC (3) or EAN (4)
code or number.

#### title:

A short title for the product. This will be displayed in bold on the product
page and in the title bar of the browser window. Titles can be up to 100
characters in length. Titles should be visually consistent with the rest of
our catalog and not use all caps or all lower-case lettering.

#### product-type:

Indicates what type of product is being submitted. You must use one of the
values specified in the template: Video DVD (all disc media types) or Video
VHS (all tape media types).

#### media-type:

Indicates the specific media type. The accepted valid values are: dvd, hd_dvd,
blu_ray, videodisc, dvd_i, dvd_r, umd, video_cd, mini_disc, laser_disc,
VHStape, and videotape.

**Note:** Depending on your media-type, you may be required to provide
additional information. For **dvd** media-type, you must populate the
"dvd_region1" field. For **blu-ray** media-type, you must populate the "blu-
ray-region1" field. Do not use these fields for other media types. HD DVD is
not region coded.

#### mpaa-rating:

The rating set for the content by the Motion Picture Association of America
(MPAA). The accepted valid values are: g, pg, pg-13, r, nc-17, x, nr, and
unrated.

#### item-condition:

This is the condition of the specific item you are offering for sale,
represented by a number:  

  * 1 = Used; Like New
  * 2 = Used; Very Good
  * 3 = Used; Good
  * 4 = Used; Acceptable
  * 5 = Collectible; Like New
  * 6 = Collectible; Very Good
  * 7 = Collectible; Good
  * 8 = Collectible; Acceptable
  * 11 = New

#### price:

The price at which you are offering the item for sale, in US Dollars. This is
your price, not the Manufacturer's Suggested Retail Price (see the "msrp"
field in the template for more information). The price field is required if
the value of the "add-delete" field is "a" and you are creating a new product
offering.

#### quantity:

The quantity of the item you are making available for sale. This is your
current inventory commitment. The quantity field is required if the value of
the "add-delete" field is "a" and you are creating a new product offering.

###  Desired Video Loader fields

These Video Loader File fields are optional but desired. Providing detailed
information to buyers will generally increase your sales. For information
about additional desired fields, please refer to the Data Definitions tab of
the Video Loader File template.

#### item-note:

Use this field to describe any differences your item has from the new item
listed in the Amazon catalog (for example, your DVD cover shows wear or has
scratches). This field is limited to 2000 characters for all Used, New, and
Collectible items.

#### description:

A text description of the product itself (not your specific offering). This
field is limited to 2000 characters. Type 1 Extended ASCII characters, such as
copyright and trademark symbols or other special characters, are not
supported.

**Tip:** If you see #### signs where you should see the text, clear the format
of the cell. This can be done by clicking Edit in main menu, selecting Clear
and then Formats.

#### studio:

The film studio that produced the video or DVD. This is an alphanumeric string
of 1 character minimum and 50 characters maximum in length.

#### publication-date:

A date in the format yyyy-mm-dd.

#### theatrical-release-date:

A date in the format yyyy-mm-dd.

#### format1 - format10:

The release version or edition format of the production. For example:
widescreen, directors_cut, deluxe_edition. See the Valid Values tab in the
template for all available options.

#### number-of-discs:

The number of discs or video cassettes in the original package.

#### runtime:

The total run-time, in minutes.

#### main-image-url:

The URL where a main image of the product is located. Product images must
depict the general characteristics of a new product. Product images should not
show specific features of a "Used" or "Collectible" offering.

**Note:** Product images should have 72-pixels-per-inch resolution and be 500
pixels minimum in length (on the longest side). You may also use the **other-
image-url1 - other-image-url8** fields to provide additional images showing
other views of the product. The preferred file format is JPEG (.jpg). For more
information, see the Image Info tab in the Video Loader Template.

**Tip:** If you have trouble uploading images or do not have remote-hosted
image URLs, you can first upload your inventory file without the images and
later edit the product pages to add images one by one. For more information,
go to [Image Troubleshooting](/gp/help/17771).

#### bullet-point1 - bullet-point5:

Brief descriptive text regarding specific aspects of the product, for display
directly under or next to your product image(s). For each bullet point, use an
alphanumeric string of 500 characters maximum and do not include an actual
bullet point object. (Type 1 High ASCII characters, such as copyright and
trademark symbols, or other special characters are not supported.)

**Note:** Additional information about the production may be provided in the
following fields:

  * actor1 - actor10
  * host1 - host10
  * narrator1 - narrator10
  * director1 - director10
  * producer1 - producer10

#### audio-encoding1 - audio-encoding3:

The format(s) used to deliver audio content. For example: stereo,
quadraphonic, or dolby_digital_live. See the Valid Values tab in the template
for all available options. If you populate the audio-encoding field, you must
also specify language.

#### language1 - language3:

The primary language or languages in which the work is performed. If you
populate the language field, you must also specify audio-encoding.

#### subtitle-language1 - subtitle-language3:

The language or languages for which sub-titles are available.

#### expedited-shipping:

Enter "y" if you will only offer Domestic Expedited, but not Domestic Two Day
or Domestic One Day, and not International Expedited. Enter "n" if you will
not offer expedited shipping at all for the item. You can also enter multiple
expedited shipping options.

**Valid Values for the expedited-shipping field:**

  * **n**

Use this value when you will not offer any expedited shipping option at all.

  * **y**

This is for domestic expedited shipping other than Two Day or One Day. Use
this value when you will offer only this expedited shipping option.

  * **domestic**

This is for domestic expedited shipping other than Two Day or One Day. Include
this value when you will offer this expedited shipping option and others as
well.

  * **second**
  * **next**
  * **international**

When you use this option, be sure to select "y" for the will-ship-
internationally column.

If you offer more than one expedited shipping option, don't use the "y" value;
use only the words domestic, second, next, and international, in any
combination. Use the words exactly as listed and separate them with commas.
Here are some examples of valid entries for the expedited-shipping column:

  * domestic, second, next
  * domestic, second, next, international
  * domestic, second
  * second, international
  * domestic, next
  * next, international
  * second

###  Optional fields

These Video Loader File fields are optional. For information about other
optional fields, see the Data Definitions tab in the Video Loader File
template.

#### will-ship-internationally:

A code that indicates the countries to which you are willing to ship. Use a 1
or "n" to indicate listings that are available only to customers in the U.S.
Use a 2 or "y" to indicate listings that are available to customers outside
the U.S. In the absence of a value in this field, the default global shipping
settings will be used.

**Note:** Unless you also enter the value "international" in the expedited-
shipping column, only International Standard shipping will be available. You
can offer International Standard, International Expedited, both, or neither.

#### country-of-origin:

The country that the item was manufactured in. See the Valid Values tab for a
list of country codes.

#### add-delete:

By including specific values in this field, you can add, update, and close
listings or delete SKUs from your current inventory.

  * Adding products - To add a new product to your current inventory, upload your file with an "a" in this column for the desired product. When no value is provided in this field, the record will be applied as an add/modify.
  * Updating listings - To update an existing listing with new product information, upload your file with this field blank. When no value is provided in this field, the record will be applied as an add/modify.
  * Closing a listing - To remove an offer from sale but retain the product listing details, upload your file with a "d" in this field for the desired listings. The product listing data will remain in the system. (Alternatively, you may leave the add-delete field blank and set the quantity field to "0" to remove a listing from sale. You may then update the quantity once your stock has been replenished.)
  * Deleting a listing record (SKU) - To delete a listing and remove all product data related to a SKU, upload your file with an "x" in this field for the desired listing. All product information for these listings will be completely removed and cannot be recovered. If you want to offer this product again, you will need to re-add it. It is recommended that you not delete your listings, but close them instead, so that the data will be retained.

###  Uploading your file

When you have finished entering product information in your file, we recommend
that you use the Validation macro in the template to make sure that your
information meets the requirements for each field. Once you have validated
your data and corrected any errors, you are ready to upload your file.

To upload your completed file to Amazon, we recommend that you save your
template to your hard drive as an Excel file and then use the Upload macro in
your template to submit the file. When the upload is complete, the macro
provides the batch ID number for the upload (important if you need to contact
our support team about upload issues) as well as a "Check status" link which
takes you directly to the processing report in Seller Central where you'll
find the current status of your uploads.

You can also upload your file using the Upload Products & Inventory tool in
Seller Central. To upload your file through Seller Central, first save the
"Video Template" worksheet to your hard drive in tab-delimited text (.txt)
format. See [Saving Your Inventory File](/gp/help/581) for instructions. For
information about using the Upload Products & Inventory tool, see [Upload My
Inventory File](/gp/help/201576670).

When your upload is complete, you can review the results in a processing
report. This processing report identifies whether your feed was successful and
the specific errors, if any, encountered during processing. Processing reports
are found in the Review File Status and History of the Upload Products &
Inventory page. Learn more in [Review My Inventory Results](/gp/help/611).

