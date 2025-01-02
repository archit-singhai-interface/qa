---
title: Confirm multiple shipments with feeds
url: https://sellercentral.amazon.com/help/hub/reference/G641
section: General Documentation
---

**Note:** This feature is only available to sellers with [Professional selling
plans](/gp/help/64491).

After you receive an order notification and ship the order, you must confirm
the shipment.

The [shipping confirmation template](/gp/help/13491) allows you to upload
confirmation information for multiple orders in a single file.

**Note:** If you divide an order into multiple shipments, the entire order is
charged and assigned a status of **Payment complete** as soon as the first
shipment for the order is confirmed, even if there are more shipments yet to
be made.

If you are shipping from a non-UK or non-EU country, to customers in the UK or
in EU countries, you must ship each order that is received under a single
order number from the customer, in a single shipment. You must not divide a
single order number into multiple shipments or combine multiple order numbers
into a single shipment. If you do, this may affect customer experience (for
example through additional tax collection) which in turn may affect your
product reviews.

If you divide the shipments for the orders ship to UK or EU countries all
shipments must be shipped from the same country as the first shipment. If you
are unable to fulfill the second package from the same country, cancel the
partial shipment. This is because the tax collection model is determined based
on the ship from address provided for the first shipment. Further information
on situations in which Amazon is required to collect and remit taxes by third
party sellers is available [here](/gp/help/G201468380).

**To download, edit, and upload shipping confirmations via bulk upload, do the
following:**

  1. Download and save a copy of the **shipping confirmation template**. Review the instructions on the **Data definitions** tab, especially the **Accepted values** column and any **Important notes** below the table. Also, see the **Shipping confirmation glossary** below.

  2. On the **Shipping confirmation** tab, enter your shipping information. Some tips to remember are as follows:
     * The shipping confirmation template contains validation macros to help you fill out the template correctly. The macros can be turned off, but we encourage you to keep them on if you are learning how to use the template.
     * Set all of the columns to **Text** format (including **ship-date**) to prevent Excel from removing any leading zeroes.
     * Enter the **ship-date** in the following format: **yyyy-mm-dd**.
     * Actual ship-from-address: The actual address from which the shipment was shipped.

  3. When updating previously existing shipping information, select from the following options based on the result you want:
     * **Overwrite previously existing data:** New data will overwrite the existing data. Example: New data in the **tracking-number** field will overwrite the existing tracking number data.
     * **Do not overwrite previously existing data:** An empty (blank) field will not overwrite or nullify the existing data. Example: Leave **tracking-number** blank so the previously uploaded data is not overwritten or nullified.
     * **Delete previously existing data:** Enter "NULL" (without quotation marks) and the data in that field will be deleted. Example: Type "NULL" in the **tracking-number** field to erase previous data.

**Note:** If an order includes more than one product or more than one unit of
a product, and you are splitting the order into more than one shipment, then
you must include the following fields for each of the shipping confirmation
records:

     * **order-id**
     * **order-item-id**
     * **quantity**
     * **ship-date**
     * **carrier-code**
     * **carrier-name (only when using "Other" as carrier-code)**
     * **ship-from-address**
     * **supply-source ID**

Sellers uploading feed files to confirm shipments will need to provide a
Supply Source ID (S2 ID) which is a unique identifier for a location. S2 IDs
can be found in their **Shipping** settings under the [Locations
tab](/fbm/locations) or on the [GET S2 API](https://developer-
docs.amazon.com/sp-api/docs/supply-sources-
api-v2020-07-01-reference#getsupplysources).

**Note:** Supply Sources and the Locations tab are currently available to
sellers selling in the US store (amazon.com).

If you are shipping to customers in the UK or EU countries from a non UK or
non EU country you must ship each order received under a single order number
from the customer in a single shipment. You must not divide a single order
number into multiple shipments or combine multiple order numbers into a single
shipment as that may impact customer experience (for example through
additional tax collection) which in turn may impact your product reviews.

If you divide the shipments for the orders ship to UK or EU countries all
shipments must be shipped from the same country as the first shipment. If you
are unable to fulfill the second package from the same country, cancel the
partial shipment. This is because the tax collection model is determined based
on the ship from address provided for the first shipment. Further information
on situations in which Amazon is required to collect and remit taxes by third
party sellers is available [here](/gp/help/G201468380).

  4. Click **Save as** and select **Text (Tab-delimited) (*.txt)** from the file type list. If you see a warning that the selected file format does not support workbooks containing multiple worksheets, click **Yes**. 

  5. In Seller Central, from the **Orders** menu, select **Upload order related files**.

  6. On the **Shipping confirmation** tab, under **Upload your shipping confirmation file** , click **Browse**.

  7. Locate your saved template, select the file, and click **Open**.

  8. Click **Upload Now**.

You can check the status of your uploaded file at the bottom of the upload
page under **Review file status and history**. Your processing report will
indicate any errors that might have occurred during upload.

## Shipping confirmation glossary

Not all fields are required. However, it is in your best interest to provide
as much information as possible.

Field Name | Definition | Required | Accepted Values | Example  
---|---|---|---|---  
order-id | Unique identifying number for an order. This number is provided in your Orders report and the Manage Orders tool. | Yes | Alphanumeric text, 3-7-7 format | 058-3563777-5518068  
order-item-id | Unique identifying number for an item in an order. This number is provided in your Orders Report and on the Order Details page in Manage Orders. **Note:** This is not the same as the product ASIN. The order-item-id differs from order to order. | No | Alphanumeric text | 05835637773450  
quantity | Item quantity included in this order if more than one unit of an item was ordered. **Note:** If you divide an order, you must include a quantity in the shipping confirmation for each shipment so that customers know how many items to expect in each package when it arrives. | No | A positive integer | 1  
ship-date | Date on which you shipped the order. | Yes | Format: yyyy-mm-dd | 2018-11-19  
carrier-code (CarrierCode field in API) | Amazon's code for the shipping carrier that delivered the order, chosen from a drop-down menu. **Note:** If you are using an unlisted carrier, select **Other** and then enter the carrier name in the **carrier-name** field. | Yes  | 4PX, A-1, AAA Cooper, ABF, Asendia, Best Buy, Blue Package, Canada Post, CEVA, China Post, Conway, DHL, DHL eCommerce, Estes, FedEx, Fedex Freight, FedEx SmartPost, First Mile, Hongkong Post, Hunter Logistics, India Post, JCEX, Lasership, Newgistics, Old Dominion, OnTrac, OSM, Pilot Freight, R+L, Roadrunner, Royal Mail, Saia, SF Express, SFC, StreamLite, UPS, UPS Freight, UPS Mail Innovations, Urban Express, USPS, XPO Freight, Yanwen, Yellow Freight, Yun Express, Other | Other  
carrier-name (CarrierName field in API) | Shipping carrier that delivered the order. Use only if **carrier-code** is **Other**. | Yes, only if **carrier-code** is **Other**. | Alphanumeric text, 1 to 50 characters | Any carrier not listed as an option under carrier code  
tracking-number | Shipping carrier's tracking ID for the order. | No | Alphanumeric text, 1 to 50 characters | 22344455  
ship-method | Shipping method used to deliver the order. Best practice is to include the carrier name to ensure clarity. | No | Alpha-numeric text, 1 to 50 characters |   
transparency_code | The Transparency code for the ASIN if it is enrolled in the Transparency program. For orders with multiple units ("quantity" is greater than 1), you must provide Transparency codes for each unit. | No |  Alphanumeric text, in 2 possible formats: Format 1- Starts with AZ: or ZA: followed by 26 characters (total length is 29 characters). Format 2- Serialized Global Trade Item Number (SGTIN) with total length is 38 character |  Format 1 - AZ:QNZGH88J4RCWPF8EDY3ZACZKEE  or Format 2 - 0100376204200301214P1OZMT7D8B81EMF4WW4  
ship-from-address-name | The actual warehouse location/address from where the item was shipped. The warehouse name or business name used in the shipping template/address book in Seller Central. | No | Alphanumeric text, 50 character maximum | John Doe  
ship-from-address-line1 | The street address information of the warehouse location | No | Alphanumeric text, 60 character maximum | 4270 Cedar Ave  
ship-from-address-line2 | Additional street address information of the warehouse location | No | Alphanumeric text, 60 character maximum(Optional field) | Optional  
ship-from-address-line3 | Additional street address information of the warehouse location | No | Alphanumeric text, 60 character maximum (Optional field) | Optional  
ship-from-address-city | The ship from address city of the warehouse location | No | Alphanumeric text, 50 character maximum (Optional field) | Sumner Park  
ship-from-address- county | The ship from address district/city of the warehouse location | No | Alphanumeric text, 50 character maximum (Optional field) | Optional  
ship-from-address-state-or-region | The ship from address state/province of the warehouse location | No | Alphanumeric text, 50 character maximum (Optional field) | FL  
ship-from-postalcode | The zip code of the warehouse from where the item was shipped. | No | Alphanumeric text, 50 character maximum (Optional field) | 32091  
ship-from-countrycode | The country from where the item was shipped. | No | ISO 3166 standard two-letter country code | US, GB  
  
**Note:** For [Premium Shipping](/gp/help/G201503640), a valid tracking ID is
required for most orders. Failure to meet the required tracking rate for
Premium Shipping orders may affect your eligibility to offer Premium Shipping
options.

