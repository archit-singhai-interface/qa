---
title: Error 8542
url: https://sellercentral.amazon.com/help/hub/reference/G200692340
section: General Documentation
---

## What Causes Error 8542?

This error is commonly referred as “multiple matching error” and occurs when
your Product ID (UPC, EAN, JAN, ISBN, etc.) is currently associated with two
or more ASINs, but the other attributes you have provided in your inventory
template (title, brand, color, size, etc.) do not match with any of these
ASINs.

## Error Message:

The provided SKU [SKU], conflicts with the Amazon catalog. The Standard
Product ID value(s) provided for this SKU corresponds to the ASIN [ASIN];
however, some information is in conflict with the Amazon catalog. Following
are conflicting attribute value(s): Item Package Quantity (Merchant: [Merchant
Value] / Amazon: [Amazon Value]) or Part Number (Merchant: [Merchant Value]/
Amazon: [Amazon Value]). If your product is this ASIN, modify these attributes
to reflect Amazon catalog values. If your product is different from this ASIN,
check if the Standard Product ID value(s) are correct.

## How to Solve and Prevent Error 8542:

  * Check to make sure that the Product ID you have provided is correct. If it’s incorrect, enter the correct Product ID in your file and resubmit.
  * If you have provided the correct Product ID, follow these steps: 
    * Update the attributes in your file to match those in the catalog (these attributes are provided in the error report) and resubmit your file; OR
    * Replace your entry under the **Product ID** and **Product ID Type** column with the ASIN provided in the error report and resubmit your file.

If the information in the Amazon catalog for this product appears to be
incorrect, contact Selling Partner Support.

**Note:** A common cause of this error is the result of manufacturers reusing
UPCs or EANs; for example, in apparel, barcodes are sometimes reused after 3
years. Ensure you are matching your product to the correct ASIN.

