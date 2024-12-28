---
title: Order Report field definitions
url: https://sellercentral.amazon.com/help/hub/reference/G201648780
section: General Documentation
---

The following fields are available in the **Order Report**.

This list is not exhaustive. Additional fields may be available for the order
report. For more information, go to [CustomizationInfo and CustomerOrderInfo
Fields](/gp/help/200747980).

Column Name |  Definition  
---|---  
Order ID _order-id_ |  Amazon's unique identifying number for the order. Used for shipping confirmation and post-order processing. Example: 058-3563777-5518068  
Order item ID _order-item-id_ |  Amazon's unique identifying number for the item in an order. Used for shipping confirmation and post-order processing.  
Purchase date _purchase-date_ | Date the order was placed, in yyyy-mm-dd format. **Note:** Unless you specify a different shipping lead time, you have agreed to ship the order within two business days of this date.  
Payment date _payments-date_ |  Date that the buyer's credit card was charged and order processing completed, in yyyy-mm-dd format.  
Buyer email _buyer-email_ |  Buyer's email addressExample: johndoe@somecompany.com  
Buyer's full name _buyer-name_ |  Buyer's full nameExample: John Doe  
SKU _sku_ |  Stock Keeping Unit. The seller-defined unique identifier for a product. Example: AA786936215595  
Product name _product-name_ |  Short title for the product, displayed on the product detail page and in the browser title bar.Example: Snowboard  
Quantity purchased _quantity-purchased_ |  Quantity purchased.  
Currency _currency_ | Currency type Example: USD  
Item price _item-price_ |  Price a buyer paid for the item(s). All amounts are aggregates of the quantity, not unit prices.Example: Item Price = $10   
Quantity = 2  
Item price displayed = $20  
Gift wrap price _gift-wrap-price_ |  Price a buyer paid for gift wrap. All amounts are aggregates of the quantity, not unit prices.  
Shipping price _shipping-price_ |  Price a buyer paid for shipping. All amounts are aggregates of the quantity, not unit prices.  
Item _item-tax_ |  Tax a buyer paid connected to the item. All amounts are aggregates of the quantity, not unit prices.  
Gift wrap tax _gift-wrap-tax_ |  Tax a buyer paid connected to the gift wrap. All amounts are aggregates of the quantity, not unit prices.  
Ship service _ship-service-level_ |  Type of shipping selected by the buyer when ordering the item; for example, standard, expedited.  
Recipient name _recipient-name_ |  Name field of "Ship To" address.  
Recipient name + PO Number  |  Enables the purchase order (PO) number to append to the **Recipient name** field in Order Details, Order Reports, and SP-API when a business customer provides a PO number for seller-fulfilled orders. Disable if you are already including the PO number on the shipping label and packing slip or don’t want to include the PO number for other reasons. For more information, see our Help page, [What do I need to know about packing slips and purchase order numbers?](/gp/help/GQBDHEYGMALGGASA)  
Ship address (3 columns) _ship-address-1_ |  First line of "Ship To" address.  
_ship-address-2_ |  Second line of "Ship To" address.  
_ship-address-3_ |  Third line of "Ship To" address.  
Ship city _ship-city_ |  City of "Ship To" address.  
Ship state _ship-state_ |  State, province, or region of "Ship To" address. Varies with country of origin. **Note:** Abbreviations can vary depending on how it was entered by the buyer.  
Ship postal code _ship-postal-code_ |  ZIP code or postal code of "Ship To" address. Value format depends on destination country.  
Ship country _ship-country_ |  International Standards Organization two-letter country code ([ISO 3166-2 compliant](https://en.wikipedia.org/wiki/ISO_3166-2)).Example: US  
Gift wrap type _gift-wrap-type_ |  Type of gift wrap selected by the buyer.Example: Birthday balloons.  
Gift message text _gift-message-text_ |  Buyer's gift message.  
Gift wrap price _gift-wrap-price_ | The price of the gift wrap selected by the buyer.  
Gift wrap tax _gift-wrap-tax_ | The amount of tax paid on the gift wrap.  
Item promotion discount _item-promotion-discount_ |  Amount discounted from orders that qualify for either a money-off or a percent-off promotion.  
Item promotion ID _item-promotion-id_ |  Promotion ID associated with money-off or percent-off promotion.  
Shipping promotion discount _shipping-promotion-discount_ |  Amount discounted from orders that qualify for free shipping.  
Shipping promotion ID _shipping-promotion-id_ |  Promotion ID associated with free shipping promotion.  
Delivery instructions _delivery-instructions_ |  Additional delivery instructions.  
Order channel _order-channel_ |  Information about how an order was placed.  
Order channel instance _order-channel-instance_ |  Information about how an order was placed.  
Is business order? _is-business-order_ | Indicates if the order is from an [Amazon Business customer](/gp/help/201750810).Example: true, false  
Purchase order number _purchase-order-number_ | The buyer's purchase order number (for orders from [Amazon Business customers](/gp/help/201750810)). This must be included on the customer package packing slip or on the package shipping label. For more information on packing slips and purchase order numbers, click [here](https:/gp/help/QBDHEYGMALGGASA).   
Price designation _price-designation_ | Indicates the type of business price that the buyer used. [Learn more about business prices](/gp/help/201740300). ([Amazon Business Seller Program](/hz/b2bregistration) only.)  
Buyer company name _buyer-company-name_ | The registered company name of the Amazon Business customer who created the order. This is a freeform text field for alphanumeric characters. ([Amazon Business Seller Program](/hz/b2bregistration) only.)Example: Acme Business Supplies, Inc.  
Licensee name _licensee-name_ |  Name of the individual on the professional license that has been provided by the customer. Example: Jane Doe 12345  
License number _license-number_ |  Professional license number provided by the customer. Example: 12345  
License state _license-state_ |  State where professional license number is valid. Example: TX  
License expiration date _license-expiration-date_ |  Professional license expiration date provided by the customer. Example: 2016-08-20  
Address-Type _Address-Type_ | Informs you as to whether the customer Ship to address is commercial or residential.  
Number-of-items  _Number-of-items_ | Indicates the total number of items that are included in an ASIN.  
Is Transparency?  | Example: true, false; Indicates if ASIN is enrolled in Transparency. [Learn more.](/gp/help/202008510)  
Global Express _is-global-express_ | Indicates if the order is from Global Express ProgramExample: true, false  
_default-ship-from-address-name_ | The warehouse or the business name used in the Seller Central account shipping settings/template  
Default Ship From Location (3 columns) _default-ship-from-address-field-1_ | First line of "Default Ship From" address  
_default-ship-from-address-field-2_ | Second line of "Default Ship From" address  
_default-ship-from-address-city_ | City of "Default Ship From" address  
_default-ship-from-address-state_ | State of "Default Ship From" address  
_default-ship-from-address-country_ | Country of "Default Ship From" address  
_default-ship-from-address-postal-code_ | ZIP code or postal code of "Default Ship From" address, value format depends on destination country.  
_actual-ship-from-address-name_ | The warehouse or the business name that is chose while confirming the order  
Actual Ship From Location (3 columns)_actual-ship-from-address-1_ | First line of "Actual Ship From" address  
_actual-ship-from-address-field-2_ | Second line of "Actual Ship From" address  
_actual-ship-from-address-field-3_ | Third line of "Actual Ship From" address  
_actual-ship-from-address-city_ | City of "Actual Ship From" address  
_actual-ship-from-address-state_ | State of "Actual Ship From" address  
_actual-ship-from-address-country_ | Country of "Actual Ship From" address  
_actual-ship-from-address-postal-code_ | ZIP code or postal code of "Actual Ship From" address, value format depends on destination country  
TCM | Tax Collection Model, Tax Collection Responsible Party  
Fulfillment Plan _(Applicable for sellers with Multi Location Inventory Only)_ | Recommended fulfillment quantity by location and order item.  **Note:** This field will be blank if seller or ASIN is not enrolled in Multi-Location Inventory program. To learn more, go to [Inventory solutions for your business.](https://sell.amazon.com/programs/multi-location-inventory) Example: [{"supply-source-id":"dccb797a-e611-4399-a03e-e412636c8d5","item-quantity":3"}, {"supply-source-id":"af5980ec-a34a-41b6-8fa7-bc9b0514e3f4","item-quantity":3}]  
IOSS Number | Import One Stop Shop (IOSS) number for the store. Sellers shipping to the EU from non-EU must provide this IOSS number to their carrier where Amazon has collected the VAT on the sale. 12 alphanumeric characters with the following structure IMXXXYYYYYYZ  
Buyer Requested Cancel | The toggle button for Buyer Requested Cancel should be turned on for getting the status of the Buyer requested cancellation requests in the order reports  
Preferred Delivery Time _delivery-preferred-time_ |  Preference of when the buyer would like the package to be delivered. An empty field here means the business is closed during those times. Example: {"BusinessHours": [ {"DayOfWeek": "TUE", "OpenIntervals": [{ "StartTime": {"Hour": 8, "Minute": 0}, "EndTime": {"Hour": 16, "Minute": 0}}]}, {"DayOfWeek": "WED", "OpenIntervals": [{ "StartTime": {"Hour": 9, "Minute": 30}, "EndTime": {"Hour": 15, "Minute": 30}}]}, {"DayOfWeek": "THU", "OpenIntervals": [{ "StartTime": {"Hour": 7, "Minute": 0}, "EndTime": {"Hour": 15, "Minute": 0}}]}, {"DayOfWeek": "FRI", "OpenIntervals": [{ "StartTime": {"Hour": 9, "Minute": 0}, "EndTime": {"Hour": 17, "Minute": 0}}]}], "ExceptionDates": [ {"ExceptionDate": "2024-02-14", "IsOpen": true, "OpenIntervals": [{ "StartTime": {"Hour": 9, "Minute": 0}, "EndTime": {"Hour": 17, "Minute": 0}}]}, {"ExceptionDate": "2024-03-09", "IsOpen": false}, {"ExceptionDate": "2024-08-31", "IsOpen": false}]}  
Drop-off Location _drop-off-location_ | Preference of where the buyer would like the package to be dropped off. Examples: FRONTDOOR means deliver to the front door  REAR_DOOR means deliver to the back door  FRONTDESK means deliver to the front desk  LOADING_DOCK_STAFF means deliver to the loading dock  PROPERTYSTAFF_MAILROOM means deliver to the mail room  BUILDINGRECPTIONIST_CARETAKER means deliver to the receptionist  
Pallet Delivery _pallet-delivery_ |  Shipping constraints on the order, such as whether the order needs to be shipped on a pallet. Example: MANDATORY  
  
**Notes:**

  * **purchase-order-number** is added by default for all Amazon Business customers and can be toggled on or off using the Order Report Column Picker. The purchase-order-number must be provided on the customer package packing slip or on the package shipping label. For more information, click [here](/gp/help/QBDHEYGMALGGASA). Amazon Business customers can select or deselect **business-buyer** and **business-price** in a group, and select or deselect **company-name** separately.
  * Additional fields are available for the Orders Report if you use the SP-API to retrieve the report using an XML feed. Visit [CustomizationInfo and CustomerOrderInfo Fields](/gp/help/200747980).

**Important:** Your order reports now include an email address that you can
use to contact your buyer regarding your transaction with the buyer. Note that
if you choose to use this email address to communicate with your buyer, that
email message and all further communications between you and your buyer using
this service will be copied and stored by Amazon. By using this service, you
consent to this action. [Learn more about Buyer-Seller
Messaging](/gp/help/200383320).

