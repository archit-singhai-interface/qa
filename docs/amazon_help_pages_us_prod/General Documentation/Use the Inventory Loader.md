---
title: Use the Inventory Loader
url: https://sellercentral.amazon.com/help/hub/reference/G202154120
section: General Documentation
---

You can use the Inventory Loader to add your listings to existing products on
Amazon.

For more information, see [Upload inventory using the Inventory
Loader](/gp/help/201576540).

Steps to use the Inventory Loader file template:

  

  1. Download the [Inventory Loader file template](https://seller-templates.s3.amazonaws.com/xlsx/US/Flat.File.InventoryLoader.us.xlsx).
  2. In the **Template** tab in the file, enter SKU, product identifier, and listing data for the products that you want to offer for sale.
  3. Verify the entered information, and save the template as a tab-delimited text (.txt) file.
  4. Go to [Add Products via Upload](/listing/upload) in Seller Central. In **Upload your spreadsheet** tab, upload your file.

## Inventory Loader fields

Though all the fields are not required, it is recommended that you provide as
much information as possible.

Recommended (or desired) fields give customers the basic information they need
to make informed decisions. Not providing data in desired fields can result in
poor product descriptions, and make your product hard to find. If a product on
Amazon does not have a price or quantity, customers can't purchase it.

Field name | Definition | Required  | Accepted values | Example  
---|---|---|---|---  
sku | A SKU (stock keeping unit) is used to track inventory. Each SKU that you create must be unique to an individual product in your current template and existing listings. | Yes | Alpha-numeric text 3-7-7 format | 058-356377-75518068  
product-id | This is the industry standard [product identifier](/gp/help/200211450). This field is required for product matching when you create new listings. **ISBN**(International Standard Book Number): A unique number assigned to each book published in the world. Usually located on the back cover next to the bar code, following the identifier **ISBN**. It can also be found on the inner page along with the copyright notice. **UPC** (Universal Product Code): A number used to identify products in the US. UPC is located under the bar code that appears on the product label. **ASIN** (Amazon Standard Identification Number): A number that is uniquely assigned to each product sold on Amazon. The system recognizes any product by its assigned ASIN, regardless of whether the product has an assigned ISBN or a UPC. **EAN** (European Article Number): An identifier assigned for products sold in Europe. EANs are used in Europe in the same way as UPCs are used in the US. | No (desired) | - | -  
product-id-type | This is a numeric entry that indicates whether the product-id is an ASIN, ISBN, UPC, or EAN. This is a required field if product-id is provided. | No (desired) |    

  * 1 = ASIN
  * 2 = ISBN
  * 3 = UPC
  * 4 = EAN

| 3  
item-condition | This is a numeric entry that indicates the condition of the item. This field is required for creating a new listing. **Note:** Not all conditions are available for all categories. For more information about which conditions you can use in your product category, see [Condition guidelines](/gp/help/200339950). | No (desired) | Condition types:   

  * 1 = Used; Like new
  * 2 = Used; Very good
  * 3 = Used; Good
  * 4 = Used; Acceptable
  * 5 = Collectible; Like new
  * 6 = Collectible; Very good
  * 7 = Collectible; Good
  * 8 = Collectible; Acceptable
  * 9 = Not used
  * 10 = Refurbished
  * 11 = New

| 7  
price |  This is price per item, in US dollars. Do not include the currency symbols. This is a required field if product-id is provided, and if you are creating new listings. You must provide a price to make the product available for purchase on Amazon. | No (desired) | Numeric value, greater than zero (0.00) | 5.00  
quantity | Enter a quantity when you add a new SKU. This is a required field for seller-fulfilled products if product-id is provided, and to make the product available for purchase on Amazon. Products must be in-stock and on-hand at the time a purchase is made.  **Note:** For Fulfillment by Amazon (FBA) products, do not enter a quantity. Instead, provide a fulfillment-center-id in the last column of the template. | No (desired)  | Numeric value, between 1 and 1000 | 720  
item-note | This is the description of any differences your item may be having, from the new item sold on Amazon (for example, if your hardcover book is missing the dust-jacket). | No (desired) | Alpha-numeric text, 1000 characters or less | -  
will-ship-internationally |  **Note:** The will-ship-internationally column does not apply to the new [shipping settings](/gp/help/202062600). Shipping templates define these characteristics. [Learn more](/gp/help/201841600). A code that indicates the countries to which you are willing to ship. If you do not enter an option, the general setting you chose when you signed up to sell, is used as the default. If you do not enter the value "international" in the expedited-shipping column, only International Standard shipping will be available. You can offer International Standard, International Expedited, both, or neither. **Note:** Domestic Two Day, Domestic One Day, and International Expedited are for books, music, videos, and DVDs (BMVD) only. For BMVD, you can offer multiple expedited shipping options. When you choose to ship internationally, your product appears on other Amazon sites when there are no offers from a marketplace seller. You are solely liable to comply with the laws and regulations of the country you're shipping from, and also of the country you're shipping to, as applicable. The international customer might have to pay customs duties, taxes, and processing fees for your product. **Note:** Some products, including consumer electronics, software, and video games, cannot be shipped internationally or can be shipped only to eligible countries. | No (desired) |  1 or n = Ship only domestically 2 or y = Ship internationally | 2  
expedited-shipping |  **Note:** The expedited-shipping column does not apply to the new [shipping settings](/gp/help/202062600). Shipping templates define these characteristics. [Learn more](/gp/help/201841600). | No (desired)  |  n = Use this value when you will not offer any expedited shipping option at all.  y = Use this value when you offer domestic expedited shipping other than Domestic Two Day and Domestic One Day. Use it when you offer only this expedited shipping option. **Note:** If you offer more than one expedited shipping option for a BMVD product, use only the words `domestic, second, next, and international`, in any combination. Use the words exactly as listed, and separate them with commas. For example: domestic = Use this value when you offer domestic expedited shipping other than Domestic Two Day and Domestic One Day. Use it when you offer this expedited shipping option as well as other options. | domestic  
add-delete | This is about listings.See [Delete SKUs Using Inventory Loader](/gp/help/201576560) for more information about deleting SKUs. If you don't populate the **add-delete** field, the system uses these default settings:   

  * **For new SKUs** : Add a listing
  * **For existing SKUs** : Modify listing data

| No (optional) |  a = Add new products d = Deactivate offer (remove all inventory and make the offer inactive without deleting the SKU) or set your inventory quantity to 0 (zero). x = Delete offer and product data, including the SKU | a  
minimum-seller-allowed-price | This field helps Amazon identify potential pricing errors with your listings. To use it, enter your minimum allowable price for the product. If you try to set your price below your minimum allowable price, your offer becomes inactive, and you are notified via email. You can change your minimum allowable price by editing the value in this field and uploading the updated file to Amazon.  **Note:** To remove the minimum price value for a product, enter the value `delete` in this field. Do not enter `0` or other numeric values. If you include this field, but you don't provide a value for a product, your existing minimum price value will not change. | No (optional) | Numeric value | 5  
maximum-seller-allowed-price | This field helps Amazon identify potential pricing errors with your listings. To use it, enter your maximum allowable price for the product. If you try to set the price above your maximum allowable price, your offer becomes inactive, and you are notified via email. You can change your maximum allowable price by editing the value in this field and uploading the updated file to Amazon.  **Note:** To remove the maximum price value for a product, enter the value `delete` in this field. Do not enter `0` or other numeric values. If you include this field, but you don't provide a value for a product, your existing maximum price value will not change. | No (optional) | Numeric value | 20  
fulfillment-center-id | This field is required only if you use Fulfillment by Amazon (FBA). If you don't use FBA, leave this column blank. | No (optional) | - | -  
leadtime-to-ship | The time, in days, between when you receive an order and when you can ship the product. The default leadtime-to-ship is 1 to 2 business days. Use this field if your leadtime-to-ship is greater than two business days. Do not specify a range of days or use the word "days" at the end. **Note:**

  * Do not use this field for BMVD products. Sellers are expected to ship all BMVD orders within two business days of the date when the order notification is made available by Amazon.
  * Do not leave this field blank. If no value is entered, the default value is 1 to 2 business days.

| No (optional) | Numeric value, whole number only | 5  
product-tax-code | Your item level product tax code (PTC) is used to designate a specific PTC to a specific item, and will be used instead of your default PTC.See [PTC help page](/gp/help/G200794510) for more information. | No (optional) |  Product tax codes (PTC) listed on the [Available PTC List](/tax/nexus/settings/ptc) | A_BOOKS_GEN  
merchant_shipping_group_name | Use this field to assign SKUs to a shipping template that was configured in shipping settings. If the field is left blank, new SKUs are assigned to the default template, and existing SKUs remain assigned to the existing shipping template. For more information, see [What is a Shipping Template?](/gp/help/201841280) | No (optional) | One of the shipping template names (string) configured in the shipping settings | Free Shipping Template, Default Template

