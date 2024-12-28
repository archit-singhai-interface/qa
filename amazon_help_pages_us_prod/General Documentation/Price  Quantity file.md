---
title: Price & Quantity file
url: https://sellercentral.amazon.com/help/hub/reference/G200385490
section: General Documentation
---

The Price & Quantity file allows you to make modifications to the price and
quantity of your current inventory without the need to supply all the fields
that the Inventory Loader or the larger inventory files require. The Price and
Quantity file is the smallest format with the fastest processing time.

**Download:** [Price & Quantity file
template](https://sellercentral.amazon.com/listing/api/partner/template?feedVariant=priceandqty&mkid=ATVPDKIKX0DER).

It is also possible to update price and quantity information using the Listing
Loader or Category-specific inventory files. Use larger inventory files only
in the following situations:

  * You have additional products to list.
  * You need to change the details of an existing product (for example, change the "Item Note").
  * You need to delete products.

## Required fields

This upload file must be populated with the **SKU** field, as well as at least
one of the following additional fields that you are choosing to modify: the
**price** field or the **quantity** field.

  * **SKU:** Stock Keeping Unit, used to track inventory. A SKU can be any alpha-numeric string. Each SKU you submit in your file must be unique to an individual product in your existing listings. Do not submit duplicate SKUs. Submit your SKU exactly as it appears in your Amazon inventory listings. You must supply a SKU in your Price & Quantity file.
  * **Price:** The price of the product, in U.S. dollars. Do not enter the "$" symbol. Blank entries or a zero price (0.00) for any product will result in an error and the inventory file will be rejected. You can leave this field empty only if you are adjusting quantities.
  * **Quantity:** The quantity of the product you have for sale. Use a whole number greater than zero for available inventory. Set the quantity to "0" to indicate that a product is out of stock. You can leave this field empty if you are only adjusting prices.
    * **Seller-fulfilled products:** Enter the quantity of the product you have for sale. This is your current inventory commitment. The quantity must be a whole number that is greater than zero.
    * **Amazon-fulfilled products:** Leave this field empty. Do not enter a quantity as it is not applicable for products fulfilled by Amazon.

**Note:** You can leave the **quantity** field empty if you are only adjusting
prices.

## Optional fields

  * **minimum-seller-allowed-price and maximum-seller-allowed-price** : This field helps Amazon identify potential pricing errors with your listings. To use this functionality, enter your minimum allowable price for this product. If you attempt to set your price for the product below your minimum or maximum allowable price, your offer will become inactive and you will be notified via email. You can always change your minimum and maximum allowable price by modifying the value in this field and uploading the updated file to Amazon.

**Note:** To remove the maximum or minimum price value for a product, enter
the value "delete" in the corresponding field. Do not enter "0" or other
numeric values. If you include this field but do not provide a value, no
change will be made to your existing maximum or minimum price value.

  * **fulfillment-channel:** Use this field to specify the fulfillment channel (seller or Amazon) for your product.
    * **Amazon-fulfilled products** : Enter "amazon" to specify that orders for the product will be fulfilled by Amazon. Do not use the "quantity" field when you enter "amazon" as your fulfillment channel. If you provide a quantity for a product that is currently Amazon-fulfilled and leave the fulfillment-channel field empty, or enter the "default" value, your listing will be converted to a seller-fulfilled product.
    * **Seller-fulfilled products** : Leave this field empty or enter "default" to indicate that you will fulfill orders for the product. Also enter a value in the quantity field. If you specify "amazon" for a product that is currently seller-fulfilled, your listing will be converted to an Amazon-fulfilled product.

## Managing out-of-stock products

The best and fastest way to indicate that a product is out of stock is to use
a Price & Quantity file feed to set the quantity to zero. When you restock the
product under the same SKU, use a product-specific inventory file or an
Inventory Loader file feed to set the quantity to your on-hand quantity.

We do not recommend deleting SKUs that are temporarily out of stock. Use a
product-specific inventory file or an Inventory Loader file feed to explicitly
delete the SKU, only if you do not plan to restock the product in the future.

