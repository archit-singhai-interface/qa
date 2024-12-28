---
title: How to read an active listings report
url: https://sellercentral.amazon.com/help/hub/reference/G200385890
section: General Documentation
---

The **Active Listings Report** is a tab-delimited file that you can open in
any spreadsheet or database program, such as Microsoft Access or Microsoft
Excel. Listing data and file columns can then be modified within the
spreadsheet, and uploaded at any time using the **Inventory Loader** or
**Listing Loader**. For more information, see [Using Reports to Update
Inventory](/gp/help/200388940).

If you open the report in Microsoft Excel, the leading zeroes for ISBNs in the
**product ID** column will be dropped by Excel. You can prevent this by using
the import wizard and forcing the **product-id** column to be imported as
text. Please see Microsoft Excel help for more information on this feature.

Below is a list of fields that appear in the report, as well as definitions of
those fields and examples for each. The unused fields are provided for
backwards compatibility to allow sellers who originally integrated their
business using these fields to continue with their current software programs.
If you do not need any of these fields, you may simply delete the columns from
your downloaded report.

Please review these fields to understand the **Active Listings Report**.

Field name | Definition | Example  
---|---|---  
item-name | The title of the item listed. This will be populated with Amazon catalog data. | The Taking [Mass Market Paperback] by Dean Koontz  
item-description | This is used for backwards compatibility only. | &#xA0;  
listing-id | An identifier created by Amazon when you create a listing. Consists of 4 digits, a capital letter, and 6 more digits. | 1234A123456  
seller-sku | Stock Keeping Units (SKUs) are unique blocks of letters and/or numbers that identify your products. SKUs are assigned by you as the seller. | 154844  
price | The price you are asking for the product. | 12.99  
quantity | The quantity of the product available for purchase. | 15  
open-date | The date the listing was created. | 2008-02-27 20:15:20 GMT  
item-is-marketplace | This will always be y. | y  
product-id-type | A numeric entry that indicates if the product-id is an ASIN, ISBN, UPC, or EAN code/number. When uploading files in Standard Book format, this field value will default to 2 (ISBN) unless otherwise specified.1 = ASIN 2 = ISBN 3 = UPC 4 = EAN | 1  
zshop-shipping-fee | This is used for backwards compatibility only. | &#xA0;  
item-note | Your description of the listing. | read once, no scratches, normal condition  
item-condition | This is your condition code for the listing.1 = Used; Like New 2 = Used; Very Good 3 = Used; Good 4 = Used; Acceptable 5 = Collectible; Like New 6 = Collectible; Very Good 7 = Collectible; Good 8 = Collectible; Acceptable 10 = Refurbished 11 = New | 1  
zshop-category1 | This is used for backwards compatibility only. | &#xA0;  
zshop-browse-path | This is used for backwards compatibility only. | &#xA0;  
zshop-storefront-feature | This is used for backwards compatibility only. | &#xA0;  
asin1 | This is not used. The field is populated with the **product-id**. | &#xA0;  
asin2 | This is used for backwards compatibility only. | &#xA0;  
asin3 | This is used for backwards compatibility only. | &#xA0;  
will-ship-internationally | 2 = listings that are available to customers outside the U.S.1 = listings that are available only to customers in the U.S. | 2  
expedited-shipping | **Second** = listings that are available for second day shipping to U.S. domestic addresses **Next** = listings that are available for next day shipping to U.S. domestic addresses **Same** = listings that are available for same day shipping to U.S. domestic addresses **n** = not offered | n  
zshop-boldface | This is used for backwards compatibility only. | &#xA0;  
product-id | ASIN, ISBN, UPC, or EAN for the item | 0312306180  
bid-for-featured-placement | This is used for backwards compatibility only. | &#xA0;  
add-delete | This field will be empty in the report; it enables you to use an open listings report to update online inventory. | &#xA0;  
pending-quantity | This is the quantity of the item that is pending purchase at the time of the report. | 0  
fulfillment-channel | This will indicate for FBA sellers if the listing is set for seller fulfilment or fulfilment by Amazon. | Amazon-fulfilled

