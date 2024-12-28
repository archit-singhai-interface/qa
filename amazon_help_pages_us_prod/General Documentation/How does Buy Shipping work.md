---
title: How does Buy Shipping work?
url: https://sellercentral.amazon.com/help/hub/reference/GLXKP5E6P6QTSSU8
section: General Documentation
---

Watch these videos:

<param name="allowfullscreen">

[Setting Buy Shipping
Preferences](https://www.sellercentral.amazon.dev/learn/courses?moduleId=f2ea93b7-5cb5-45ad-9c17-6c40d7ad5e27&ref_=su_refined_search&modLanguage=English)

With Amazon Buy Shipping, you can buy shipping labels individually or in bulk,
ship and confirm your orders, and track your shipments. Buy Shipping ensures
that your products are delivered to your customers using a trusted network of
shipping carriers.

To start taking advantage of Amazon’s Buy Shipping services, see also:

  * [Buy shipping through Seller Central](/gp/help/G200202280)
  * [Buy shipping in bulk](/gp/help/G202168950)
  * [Buy shipping using the Merchant Fulfillment API](https://www.sellercentral.amazon.dev/help/hub/reference/G201950090)
  * [Use Buy Shipping services](https://www.sellercentral.amazon.dev/help/hub/reference/G200202220)
  * [Manage your carrier accounts](https://www.sellercentral.amazon.dev/help/hub/reference/G200785170)
  * [Missing carrier or ship method in Buy Shipping](https://www.sellercentral.amazon.dev/help/hub/reference/GTQMVHPB94LP2355)
  * [Buy Shipping preferences](https://www.sellercentral.amazon.dev/help/hub/reference/G202086070)
  * [Ship from China with Buy Shipping](https://www.sellercentral.amazon.dev/gp/help/GSL4PTYW5Y6Q6ACK)
  * [QZ Tray](https://www.sellercentral.amazon.dev/gp/help/GKULTMACW6HHP7AD)
  * [Amazon Print Connect](https://www.sellercentral.amazon.dev/gp/help/GQ8WSSALNXZJEW3S)
  * [Reprint a shipping label](https://www.sellercentral.amazon.dev/help/hub/reference/G200202250)
  * [Shipping integrators](https://www.sellercentral.amazon.dev/help/hub/reference/GZZPMC9QLNBX48RP)
  * [Veeqo](https://www.sellercentral.amazon.dev/help/hub/reference/GPW2UV7N2KW2GZHD)
  * [Refunds of Buy Shipping fees](https://www.sellercentral.amazon.dev/help/hub/reference/G200202270)
  * [Amazon Sponsored Discount for Buy Shipping services](https://www.sellercentral.amazon.dev/gp/help/G7X4G8VWJS9B8UUN)
  * [Link Carrier Accounts In Seller Central To Use Your Own UPS/FedEx Rates](https://www.sellercentral.amazon.dev/learn/courses?ref_=selleru_athena&courseId=d027e66e-d731-462a-9f0d-7afe4cbfba12&moduleId=b70e661e-4dae-45be-913d-a46ad2fe147e&modLanguage=English&contentType=VIDEO&category=TUTORIAL)

## How does Buy Shipping work?

Buy Shipping protects sellers’ performance metrics by providing ship methods
with a high likelihood of meeting the buyer’s delivery promise. Buy Shipping
uses a ship method’s Transit Time (TT), the ship date, and the promised
delivery date to determine whether a ship method is likely to be delivered on
time.

Transit Time (TT) is the estimated time that the carrier has stated for them
to deliver a package after they pick up from the seller. The TT is based upon
a ship lane, which is the "Ship From" and "Ship To" zip code pair. For
example, if you are shipping from New York City to Los Angeles, CA, the ship
lane could be 10001 to 90001.

## Promised delivery date

Buy Shipping will use the order’s "Ship From" and "Ship To" addresses to query
carriers for their eligible ship methods that will meet the buyer’s "Promised
Delivery Date" (PDD). After Buy Shipping receives the carriers’ eligible ship
methods, it will use Amazon transportation data to validate that the actual TT
on the order’s ship lane is similar to what was provided by the carrier.

## Expected delivery date

Buy Shipping will use the "Ship Date" and TT to determine the "Expected
Delivery Date" (EDD) of the order. If the EDD is after the PDD, the ship
method will be ineligible to fulfill the order.

**Note:** Amazon uses internal transportation data to identify eligible ship
methods. It is possible for a ship method to be available on a carrier’s
website and not available on Buy Shipping. This is expected as our internal
transportation data may surface those ship methods that have been shown to
meet the delivery promises provided by the buyer.

