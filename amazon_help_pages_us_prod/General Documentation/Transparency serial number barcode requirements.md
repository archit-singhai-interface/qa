---
title: Transparency serial number barcode requirements
url: https://sellercentral.amazon.com/help/hub/reference/G202008510
section: General Documentation
---

Some manufacturers now label their products with Transparency 2D barcodes or
serial number barcodes to better track their inventory and ensure its
authenticity. Your Transparency-enabled products for sale on Amazon must be
appropriately labeled with Transparency codes or brand-issued serial number
barcodes. The Transparency-enabled ASINs you source from vendors must also
include Transparency codes or serial number barcodes.

Click [here](https://brandservices.amazon.com/transparency) to learn more
about Transparency.

## Identifying Transparency enabled serial numbers on a product

Transparency enabled products have a serial number applied to the product
packaging.

These codes can be available in 5 formats. The two most common are:  

  1. A 26 digit alpha-numeric identifier beginning with AZ: or ZA:. For example, AZ:L1Z2H38F4C5Q6R7E5K6Z1C2K3E; total length is 29 characters.
  2. A Serialized Global Trade Item Number or SGTIN. For example, 0100376204200301214P1OZMT7D8B81EMF4WW4; total length is 38 characters.

**Transparency code examples**

![](https://d1n436oh1t0g4d.cloudfront.net/G3TJ7D79PGC48LGD_Global_en-US.png)  

![](https://d1n436oh1t0g4d.cloudfront.net/GUSZKWBMV5JDTLD3_Global_en-US.gif)  

![](https://d1n436oh1t0g4d.cloudfront.net/G5VWFFJK64N4XEFH_Global_en-US.gif)  

![](https://d1n436oh1t0g4d.cloudfront.net/GB5Y8T9CNFVJ962E_Global_en-US.gif)  

**Serial number examples**

If you cannot find a code with a **T** logo, look for a serial number code
that is between 7-20 characters long. The serial number can be a 1D, 2D or QR
code and will likely include the pre-fix "SN". The serial number code will be
applied to the same side of the packaging as the GTIN (UPC/EAN/ISBN) barcode.

**Note:** When entering the serial number, don't include the pre-fix like
**SN** or **Service Tag**. Start by entering the characters in the serial
number itself.

![](https://d1n436oh1t0g4d.cloudfront.net/GTAG3PHSS5N44JZ6_Global_en-US.png)

## How to identify Transparency enabled serial numbers on customer orders

You can identify Transparency-enabled items in two ways:

Transparency-enrolled ASINs are highlighted with either a blue Transparency
badge ![](https://m.media-amazon.com/images/G/31/rainier/IMG13.png) or an
orange Serial number required badge
![](https://d1n436oh1t0g4d.cloudfront.net/GKJGK6SNE6NCCQVS_Global_en-US.png)
on the **Manage Orders** page in Seller Central. For these ASINs, you must
provide Transparency codes or serial numbers when you confirm your shipment.

You can also go to [Order Reports](/order-reports-and-feeds/reports):

  

  1. On **Order Reports** , click the [Add or remove order report columns](/order-reports-and-feeds/column-picker) link below the page title.
  2. On **Add or remove order report columns** , under **Optional columns** , turn on the **Transparency** column.

Once complete, the Transparency field will automatically display when you
download your report.

If the value in this field ("is-Transparency") is set to “True” in the order
report, you must upload Transparency codes for these ASINs when confirming the
shipment.

If no Transparency code is present, you are required to upload a serial
number. Look for a serial number code that is between 7-20 characters long.
The serial number can be a 1D, 2D or QR code and will likely include the pre-
fix **SN**. The serial number code will be applied to the same side of the
packaging as the GTIN (UPC/EAN/ISBN) barcode.

**Note:** The number of Transparency codes or serial numbers you upload must
match the number of Transparency-enabled items in your order. For example, if
the quantity of Transparency-enabled items are 3, ensure to upload 3 unique
Transparency codes or serial numbers.

When you retrieve order details in the Amazon Selling Partner (SP) API, use
getOrderItems API to identify orders with Transparency-enabled items. For more
information, go to [getOrderItems](https://developer-docs.amazon.com/sp-
api/docs/orders-api-v0-reference#getorderitems).

## Use a Shipping Confirmation file to upload Transparency codes or serial
numbers

Follow the steps below to download the file template in Seller Central.

  

  1. Go to the **Orders** tab, and select **Upload Order Related Files** from the drop-down
  2. Under **1\. Prepare Your Shipping Confirmation File** , click **Download Template**
  3. Once you have populated the template, click **Choose File** under **2\. Upload Your Shipping Confirmation File**

You can use this template to upload Transparency codes or serial numbers (if
the Transparency code is not present) even if you confirmed your shipment in
another tool, such as Selling Partner API (SP-API) or a third-party software.

## Upload Transparency codes or serial numbers in Seller Central

Your Transparency-enrolled ASINs are highlighted with either a blue
Transparency badge ![](https://m.media-
amazon.com/images/G/31/rainier/IMG13.png) or an orange Serial number badge
![](https://d1n436oh1t0g4d.cloudfront.net/GKJGK6SNE6NCCQVS_Global_en-US.png)
on the [Manage Orders](/orders-v3?page=1) page in Seller Central.

Follow the steps below to confirm, upload, and ship products with Transparency
codes or serial numbers:

  

  1. Go to [Manage Orders](/orders-v3?page=1) to identify the order with a Transparency or serial numbers badge.
  2. Click the **order number** to go to the **Order details** page.
  3. Click **Buy shipping** or **Confirm shipment** to open a new section at the bottom. Enter your Transparency codes or serial numbers in the new section at the bottom.
  4. At the bottom of the **Order details** page, there is a **T** logo right under the **Qty** field. Click the **Enter Transparency codes or serial numbers** link. Enter or scan Transparency codes or serial numbers in the text box.
  5. Once you have entered the code or serial number, you can proceed with shipping your order.

## Confirm shipments and upload Transparency codes in SP-API CreateFeed API

If you confirm your shipments in Amazon SP-API, you can use the CreateFeed API
to upload Transparency codes for orders with Transparency ASINs. For more
information, go to [CreateFeed](https://developer-docs.amazon.com/sp-
api/docs/feeds-api-v2021-06-30-reference#createfeed).

**Note:** You can only upload Transparency codes using **CreateFeed API**. For
serial numbered products, upload the serial numbers on the **Order Details**
page or using the **Shipping Confirmation** file.

## Purchase shipping and upload Transparency codes in SP-API CreateShipment
API

If you buy shipping in Amazon SP-API, you can use the **CreateShipment API**
to upload Transparency codes for orders with Transparency ASINs. For more
information, go to [CreateShipment](https://developer-docs.amazon.com/sp-
api/docs/merchant-fulfillment-api-v0-reference#createshipment).

**Note:** You can only upload Transparency codes using **CreateFeed API**. For
serial numbered products, upload the serial numbers on the **Order Details**
page or using the **Shipping Confirmation** file.

