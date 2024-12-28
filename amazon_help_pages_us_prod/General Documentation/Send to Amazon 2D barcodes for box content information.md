---
title: Send to Amazon: 2D barcodes for box content information
url: https://sellercentral.amazon.com/help/hub/reference/GJWALJCN6JKWJX5A
section: General Documentation
---

You can use 2D barcodes to provide product quantities for each box in your
shipment.

**Note:** This option is now available in the [Send to
Amazon](/gp/help/G6925SDD66GDLXJW) workflow. The 2D barcode option will be
available in step 1b of the workflow if you add inventory as individual units
earlier in step 1.

If you use 2D barcodes, you do not need to provide box content information
through Seller Central. Instead, you can select **Use 2D barcodes** in the
shipment creation workflow and then apply a 2D barcode to each of your boxes.
We can then simply scan your barcodes to determine the contents of a specific
box.

**Important:** Failure to provide accurate box content information may result
in blocking of future shipments, and a manual processing fee will be applied.

Providing box content information helps reduce the time needed between your
products arriving at the fulfillment center and your products being available
for sale. 2D barcodes are especially useful for drop shipping inventory
directly from suppliers. Your supplier can provide box information without
having access to the details of your FBA shipment. If you manage high-volume
operations, 2D barcodes will scale to larger shipments more easily.

**Note:** Accurate box weight and dimensions are required for all shipments,
even if you opt to not provide box content information in Seller Central. For
more information, go to [Shipping and routing
requirements](/gp/help/G200141510).

Please note that you will need to use a third-party application or website to
generate 2D barcodes. 2D barcodes do not replace Amazon shipping labels.
Amazon shipping labels are still required.

**Important:** The use of 2D barcodes may cause delays in receiving your
shipment. Shipments with 2D barcodes require more processing time than
shipments with box content information.

## 2D barcode requirements

Amazon accepts all 2D barcodes that meet the following standards:

PDF417 (Recommended)  
---  
Module width | Minimum: 0.020 inch (0.508 mm)  
Row height | Minimum: 3 modules  
Error correction | Minimum: Level 6  
Data Matrix  
---  
Supported versions | 14x14, 16x16, 18x18, 20x20, or 22x22  
Module width and height | Minimum: 0.040 inch (1.016 mm)  
QR Code  
---  
Module width and height | Minimum: 0.040 inch (1.016 mm)  
Error correction | Minimum: High level  
  
Barcode labels should be printed in black on a white label at a minimum of 600
dpi.

**Note:** We strongly recommend thermal or laser printers for printing your 2D
barcode labels. Do not use inkjet printers. To prevent the PDF print area from
scaling, make sure the printer’s scaling settings are set to **none** or
**100%**. We also recommend that you periodically test your barcodes by
scanning them.

The barcode must contain the following information in the order listed:

  1. Begin with the characters **AMZN**

  2. FBA Shipment ID, also referred to as the PO (Code: **PO**)

  3. Item ID (Code: **ASIN, UPC, EAN, ISBN, or FNSKU**)

**Note:** The Item ID should match the unit expected. For example, if the unit
is listed as an FNSKU on the shipment, provide the item ID as FNSKU.

  4. Quantity (Code: **QTY**)

Separate codes and their values with a colon, and separate each segment with a
comma—for example:

UPC:847603044631,QTY:24

Additional guidelines:

  * Use only uppercase letters.
  * Do not enter any spaces in the data.
  * Enter a value for each field. Null or zero values are not valid.
  * Do not list an ASIN with a quantity of 0. Exclude the ASIN from the data.
  * Do not pack more than 100 different ASINs in a single box.
  * Pack each box with only one expiration date per ASIN. 

## Sample barcodes

**Note:** Images are not to scale. Actual size depends on several factors,
including the barcode type and the number of ASINs in your shipment.

Box with UPC product  
---  
Shipment ID (PO)=FBA23JFC2G UPC=847603044631 Quantity=24 |  ![](https://d1n436oh1t0g4d.cloudfront.net/GUID-EEBDF4A3-56FB-4B77-8FEE-AF04814884DF_Global_en-US.png)  
This barcode reads: AMZN,PO:FBA23JFC2G,UPC:847603044631,QTY:24  
Box with ASIN and UPC products  
---  
Shipment ID (PO)=FBA23JFC2G ASIN=B00H1BPQ1Y Quantity=12 |  Shipment ID (PO)=FBA23JFC2G UPC=847603044631 Quantity=24 |  ![](https://d1n436oh1t0g4d.cloudfront.net/GUID-5888903C-2FFE-4FDD-8045-C109AAA092A9_Global_en-US.png)  
This barcode reads: AMZN,PO:FBA23JFC2G,ASIN:B00H1BPQ1Y,QTY:12,
UPC:847603044631,QTY:24  
Box with two UPC products  
---  
Shipment ID (PO)=FBA23JFC2G UPC=776403045720 Quantity=10 |  Shipment ID (PO)=FBA23JFC2G UPC=847603044631 Quantity=24 |  ![](https://d1n436oh1t0g4d.cloudfront.net/GUID-333006D3-8F98-45F4-81BA-3B8DDA10909B_Global_en-US.png)  
This barcode reads: AMZN,PO:FBA23JFC2G,UPC:776403045720,QTY:10,
UPC:847603044631,QTY:24

