---
title: Refund Orders - Order Adjustment Feed
url: https://sellercentral.amazon.com/help/hub/reference/G200387280
section: General Documentation
---

##

**Note:** Individual sellers: This feature is available for Professional
selling plans only. [Learn more](/gp/help/64491).

The [Order Adjustment feed](https://images-na.ssl-images-
amazon.com/images/G/01/rainier/help/xsd/release_1_9/OrderAdjustment.xsd)
allows you to issue a full refund (adjustment) for an order. You must provide
a reason for the adjustment, such as Customer Return, and the adjustment
amount, broken out by price component (principle, shipping, tax, and so on).
However, the buyer's credit card will only be credited one time for the total
amount.

Effective September 30, 2020, partial refunds for order or customer experience
issues can temporarily be initiated using the [Order Adjustment
Feed](https://images-na.ssl-images-
amazon.com/images/G/01/rainier/help/xsd/release_1_9/OrderAdjustment.xsd). For
more information, refer to [Issue Concessions](/gp/help/G200359070).

Although the adjustment feed allows for charging the buyer additional money
(for example: a restocking fee), the net amount of the adjustment must be a
credit to the buyer.

To cancel an entire order, you must use the [Order Acknowledgement
feed](/gp/help/200387140).

##  Dictionary

Element | Description  
---|---  
**AmazonOrderID** | Amazon's unique identifier for an order. Identifies the entire order regardless of the number of individual items in the order.  
**MerchantOrderID** | Optional seller-supplied order ID. The first step is to establish the MerchantOrderID in the Order Acknowledgement feed. Amazon will map the MerchantOrderID to the AmazonOrderID, and you can then use your own ID (MerchantOrderID) for subsequent feeds relating to the order. See the [Base Overview XSD](/gp/help/1011) for the definition.   
**AdjustedItem** | Container for order adjustment information, broken into the following components: 

  * **AmazonOrderItemCode:** Amazon's unique ID for an item in an order.
  * **MerchantOrderItemID:** Optional seller-supplied ID for an item in an order. It can be used in order processing if the pairing was established in the Order Acknowledgement feed.
  * **MerchantAdjustmentItemID:** Optional seller-supplied unique ID for the adjustment (not used by Amazon).
  * **AdjustmentReason:** Reason for the adjustment.
  * **ItemPriceAdjustments:** Amount the buyer is to be refunded for the item, broken down by type. See the [Base Overview XSD](/gp/help/1011) for the definition of type. All amounts are totals for the quantity, not unit prices. Amounts are signed: positive amounts are refunded to the buyer and negative amounts are charged to the buyer (for a restocking fee, for example).
  * **PromotionAdjustments:** Amount the buyer is to be refunded for a promotion, broken down by type. See the [Base Overview XSD](/gp/help/1011) for the definition of type. All amounts are totals for the quantity, not unit prices. Amounts are signed: positive amounts are refunded to the buyer and negative amounts are charged to the buyer.

