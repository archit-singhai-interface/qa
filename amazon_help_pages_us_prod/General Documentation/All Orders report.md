---
title: All Orders report
url: https://sellercentral.amazon.com/help/hub/reference/G200547170
section: General Documentation
---

This report provides order and item information for both FBA and seller-
fulfilled orders including order status, fulfillment and sales channel
information, and item details.

An online view of this report is not offered.

This report includes recent orders regardless of whether they have been
shipped. Both FBA and seller-fulfilled orders are included enabling you to
monitor and analyze demand across fulfillment and sales channels.

The report can be requested in two ways:

  

  1. **By order date:** Orders placed in the specified date range will be returned
  2. **By last update:** Orders that have changed (been placed or updated) in the specified date range will be returned.

The report does not include customer-identifying information.

## Field definitions

Field name | Description | Example  
---|---|---  
amazon-order-id | Amazon's unique, displayable identifier for an order | 058-3718414-0463502 or S01-3718414-0463502  
merchant order-id | A unique identifier optionally supplied for the order by the seller | my-order  
purchase-date | The date the order was placed  | 2003-07-14T18:53:56+ 00 :00  
last-updated-date | The date of the most recent order update | 2003-07-14T18:53:56+ 00 :00  
order-status | Current status of the customer order | Complete  
fulfillment-channel | Indicates how the order was fulfilled, via Amazon (AFN) or Merchant (MFN) | AFN or MFN  
sales-channel | Channel through which the order was purchased | Amazon.com  
order-channel | The sub channel through which a sale was made for CBA/WBA orders | Phone  
ship-service-level | An enumerated value that determines the type of fulfillment service that the buyer expects the seller to use (for example, standard versus expedited) | Standard  
product-name | The short title for the product, displayed in bold on the detail web page and in the title bar of the browser window | Chocolate Truffles  
sku | A seller-defined unique identifier for a product | HarryPotter  
asin | Amazon inventory ID | B000WON1Z0  
item-status | Current status of this item within the order | Shipped  
quantity | The number of this item that were purchased | 1  
currency | The currency used for the purchase. Supported currencies include USD, CAD, GBP, EUR, and JPY. | USD  
item-price | The amount the buyer paid for the item. Amount is aggregate of the quantity, not unit price | 15  
item-tax | The amount the buyer paid for item tax. Amount is aggregate of the quantity, not unit price | 0  
shipping-price | The amount the buyer paid for shipping. Amount is aggregate of the quantity, not unit price | 4.99  
shipping-tax | The amount the buyer paid for shipping tax. Amount is aggregate of the quantity, not unit price | 0  
gift-wrap-price | The amount the buyer paid for gift wrap. Amount is aggregate of the quantity, not unit price | 4.99  
gift-wrap-tax | The amount the buyer paid for gift wrap tax. Amount is aggregate of the quantity, not unit price | 0  
item-promotion-discount | Total of all promotion discounts applied to the order item | -6.5  
ship-promotion-discount | Promotion discount applied to shipping | -4.25  
ship-city | The city of a standard address | Los Angeles  
ship-state | The state or region of a standard address | California  
ship-postal-code | The postal (zip) code of a standard address | 90039  
ship-country | ISO 3166 standard two-letter country code | US  
promotion-ids | List of all item promotions applied to this order item |   
Licensee name | Name of the individual on the professional license that has been provided by the customer | Jane Doe  
License number | Professional license number provided by the customer | 12345  
License state | State where professional license number is valid | California  
License expiration date | Professional license expiration date provided by the customer | 2017-08-20  
default-ship-from-address-name | The warehouse or business name used in the Seller Central account shipping settings or template | John Doe  
default-ship-from-address field-1 | First line of "Default Ship From" address | 4270 Cedar Ave  
default-ship-from-address-field-2 | Second line of "Default Ship From" address | Optional  
default-ship-from-address-field-3 | Third line of "Default Ship From" address | Optional  
default-ship-from-address-city | City of "Default Ship From" address | SUMNER PARK  
default-ship-from-address-state | State of "Default Ship From" address | FL  
default-ship-from-address-country | Country of "Default Ship From" address | US  
default-ship-from-address-postal-code | ZIP code or postal code of "Default Ship From" address. Value format depends on destination country. | 32091  
actual-ship-from-address-name | The warehouse or business name that is chosen while confirming the order | John Doe  
Actual Ship From Location (3 columns) actual-ship-from-address-1 | First line of "Actual Ship From" address | 4270 Cedar Ave  
actual-ship-from-address-field-2 | Second line of "Actual Ship From" address | Optional  
actual-ship-from-address-field-3 | Third line of "Actual Ship From" address | Optional  
actual-ship-from-address-city | City of "Actual Ship From" address | SUMNER PARK  
actual-ship-from-address-state | State of "Actual Ship From" address | FL  
actual-ship-from-address-country | Country of "Actual Ship From" address | US  
actual-ship-from-address-postal-code | ZIP code or postal code of "Actual Ship From" address. Value format depends on destination country. | 32091  
tax-collection-model | Tax Collection Model or Tax Collection Responsible Party | MarketplaceFacilitator  
IOSS Number | Import One Stop Shop (IOSS) number for the store. Sellers shipping to the EU from non-EU must provide this IOSS number to their carrier where Amazon has collected the VAT on the sale. 12 alphanumeric characters with the following structure IMXXXYYYYYYZ | IMXXXYYYYYYZ  
Amazon Programs | The list of names of Amazon programs that the order item belongs to. | SUBSCRIBE_AND_SAVE, AMAZON_TODAY

