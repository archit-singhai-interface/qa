---
title: UPS shipping services and restrictions
url: https://sellercentral.amazon.com/help/hub/reference/G200785110
section: General Documentation
---

## Using UPS through Amazon Buy Shipping

When you buy UPS shipping services through Amazon Buy Shipping, the carrier’s
fees for shipping and related services will be billed to your Seller Central
account. If you have a shipper account directly with UPS, you can link that
account with your Seller Central account to access your negotiated UPS rates.
In that case, you’ll pay the UPS fees directly to UPS.

If you have any issues buying UPS shipping labels through Amazon Buy Shipping,
make sure that your ship-from address is properly formatted and represents a
valid street address. The address line must be less than 30 characters, it
must contain a two-character state code, and it cannot be a PO box unless
you’re using UPS® Ground Saver.

By buying labels through Buy Shipping, you’re agreeing to the [Amazon Buy
Shipping services terms and conditions](/gp/help/G200672320).

## Access Amazon’s negotiated rates or connect your own UPS rates

[Amazon Buy Shipping](/gc/sell-online/amazon-buy-shipping) enables you to buy
labels from trusted carriers through Amazon, while getting account health
protection related to delivery issues. We’re constantly negotiating better
rates with carriers on your behalf.

You can access Buy Shipping through [Seller
Central](https://www.youtube.com/watch?v=gHN4V2K38ZA&t=226s), [Shipping API
v2](https://developer-docs.amazon.com/amazon-shipping/docs/shipping-
api-v2-reference), or select [multi-channel
integrators](/gp/help/GZZPMC9QLNBX48RP). Additionally, if you’d like to use
your own rates, you can [connect your UPS rates](/carrier-preferences/main)
directly on Seller Central and access them on your preferred channel.

**Tip:** To learn how to link your UPS account with your seller account, go to
[Manage your carrier accounts](/gp/help/200785170).

Whether you connect your own rates or use Amazon’s negotiated rates, you’ll
have access to the account health protection that Buy Shipping offers:

  * Get up to 31% lower shipping rates for your orders.1
  * Use trusted carriers with high confidence of on-time delivery and get up to six times more refunds for A-to-z claims2 and 1.5 times more SAFE-T claim reimbursements.3 
  * Reduce invalid tracking on shipments by up to 85% by buying labels from trusted carriers.4
  * Get automatic tracking ID upload and shipping confirmation for all orders.
  * Decrease the likelihood of late deliveries by 20% on average, by accessing shipping methods that reliably deliver on time.5 

1 Compared with retail ground rates of the US Postal Service, FedEx, and UPS.

2 Compared with claims received for orders shipped on time outside Amazon Buy
shipping. To be eligible for A-to-z claim protection you must buy the shipping
label on Amazon Buy Shipping; ship on time, which will be considered at the
moment of the carrier’s first scan, not when you confirm shipment; and respond
to any buyer inquiry in Buyer-Seller Messages within 48 hours.

3 Compared with claims submitted for orders shipped on time outside Amazon Buy
Shipping. To be eligible for SAFE-T claim reimbursement you must buy the
shipping label on Amazon Buy Shipping and ship on time, which will be
considered at the moment of the carrier’s first scan, not when you confirm
shipment.

4, 5 Compared with Amazon sellers who buy shipping labels outside Amazon Buy
Shipping and ship on time.

## Shipping rates

When you buy delivery or related services from UPS via your Seller Central
account, you’re agreeing to pay the fees associated with those services,
including the higher of weight-based rates versus dimension-based rates and
any surcharges billed by the carrier in accordance with its policies. Rates
are subject to change at any time without notice. For more information go to
[Buy Shipping services terms and conditions](/gp/help/G200672320).

## UPS size and weight restrictions

The following are examples of UPS size and weight restrictions, which may
result in surcharges from the carrier:

  * **Additional handling surcharge:** Any package that requires special handling, as determined by UPS, including packages with a weight exceeding 50 lb or a combined length plus girth exceeding 105 inches, and additional criteria defined by the carrier
  * **Large package surcharge:** Any package with a combined length plus girth exceeding 130 inches, or a length exceeding 96 inches, and additional criteria defined by the carrier
  * **Over maximum limits surcharge:** Any package with an actual weight exceeding 150 lb or with a length exceeding 108 inches, or with a combined length plus girth exceeding 165 inches, and additional criteria defined by the carrier

Learn more about the carrier’s policies, including the examples listed above,
by reviewing their rate guides found at [UPS.com](https://www.ups.com/).

**Note:** Shipping a package via UPS® Ground Saver that exceeds the specified
weight and size restrictions will incur an "over maximum limits" surcharge of
$1,150 from UPS.

For information about the applicable shipping services, go to the following
pages on the UPS website:

[**Domestic shipping methods**](https://www.ups.com/us/en/support/shipping-support/shipping-services/domestic.page) | [**International shipping methods**](https://www.ups.com/us/en/support/international-tools-resources/international-shipping-services.page)  
---|---  
  
  * UPS Ground 
  * UPS Next Day Air
  * UPS 2nd Day Air
  * UPS 3 Day Select 
  * UPS® Ground Saver

|

  * UPS Standard
  * UPS Worldwide Expedited
  * UPS Worldwide Express
  * UPS Worldwide Saver

  
  
**Important:** UPS shipping options are not available for orders with a PO box
delivery address, except for UPS® Ground Saver.

## Declared value limitations

Amazon Buy Shipping, you can buy [UPS shipping
services](https://www.ups.com/us/en/support/shipping-support/shipping-
services.page) for packages with declared values of $999 or less, whether
charged to your seller account or your linked UPS account. For information on
using UPS for packages with declared values greater than $999, or for
international shipments, go to UPS.com or [contact
UPS](https://www.ups.com/content/us/en/contact).

##  **UPS ® Ground Saver restrictions**

Packages delivered via UPS® Ground Saver must meet the following criteria:

  * At least 4 inches high, 6 inches long, and 0.75 inch wide
  * May not exceed 130 inches in length and girth combined 
  * No single dimension may exceed 60 inches in length
  * No commercial destinations

To save time, we recommend pre-configuring package sizes that match these
specific dimensions so that on future orders you can quickly use the package
drop-down menu on Amazon Buy Shipping. To do this, follow the steps below:

  

  1. Go to [Buy Shipping preferences](/sbr/buyShippingPreferences?ref_=macs_xxbysprf_cont_acinfohm#buy_shipping_preferences).
  2. To the right of **Preferences for all ship-from locations** , click **Edit**.
  3. Click **Add new package** and enter the name (UPS® Ground Saver) and dimensions. 
  4. Click **Save**.

Now the next time you visit Amazon Buy Shipping, your newly configured package
will appear in the packaging drop-down menu. Once you assign it, it will load
UPS® Ground Saver rates.

## Amazon Buy Shipping APIs

Sellers, integrators, and developers may be required to manually add the
shipping method name and ID, represented by the following attributes, to use
UPS® Ground Saver:

ShippingServiceId/ServiceId | ShippingServiceName/ServiceName  
---|---  
UPS_PTP_GROUNDSAVER | UPS Ground Saver  
  
To learn more about Amazon Buy Shipping APIs, go to [Merchant Fulfillment API
v0 reference](https://developer-docs.amazon.com/sp-api/docs/merchant-
fulfillment-api-v0-reference#geteligibleshipmentservices) and [Shipping API v2
reference](https://developer-docs.amazon.com/amazon-shipping/docs/shipping-
api-v2-reference#getrates).

## Contact UPS

To locate your nearest UPS drop-off location or to track a package go to
[UPS.com](https://www.ups.com/). For special needs such as scheduling a
pickup, inquiring about weekend services, and filing claims of loss or damage,
call UPS directly at 1-800-711-5914.

