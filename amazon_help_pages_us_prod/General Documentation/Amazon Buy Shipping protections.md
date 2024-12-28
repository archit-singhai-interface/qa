---
title: Amazon Buy Shipping protections
url: https://sellercentral.amazon.com/help/hub/reference/GB2FHL2QMQ5NT397
section: General Documentation
---

There are two types of protections available from Amazon Buy Shipping: Claims
Protection and OTDR Protection.

For Claims Protection: Amazon Buy Shipping shipments qualify for A-to-z and
SAFE-T claims protections against "Package didn’t arrive" claims when all of
the following conditions are true:  

  1. The buyer was reimbursed by Amazon for not receiving their package.
  2. The shipping label was purchased with Amazon Buy Shipping and was a "Claims Protected" shipping service. The "Claims Protected" badge will be displayed in the Amazon Buy Shipping user interface before purchase and in the order details page **Shipping label purchase** section after the label is purchased. (Note: "Late Delivery Risk" labels are ineligible for protections).

**Note:** Based on Amazon's observation of millions of shipments, we have a
high confidence that "Claims Protected" shipping services will deliver on
time. "Late Delivery Risk" shipping services are those that, according to
Amazon’s estimated delivery date, have a lower chance of being delivered on-
time for the specific order.

  3. The order was shipped on time, which will be considered at the moment of the carrier’s first scan, not when you confirm shipment.

When all of the above conditions are true, Amazon will fund the buyer
reimbursement and the customer-reported claim will not be counted against your
order defect rate.

For orders where you manage the customer support, the A-to-z claim process
will be followed. For more information, go to [Amazon’s A-to-z Guarantee
claims](/help/hub/reference/G27951).

For cases where Amazon manages the customer support, through the Customer
Service by Amazon (CSBA) or Seller Fulfilled Prime (SFP) programs, the SAFE-T
claim process will be followed. Read more at [Customer Service by Amazon
refund reimbursement policy](/help/hub/reference/G7KCD8BYQER79WWJ) and [Seller
Fulfilled Prime refund reimbursement policy](/help/hub/reference/G202109110).

For OTDR Protection: If you purchase a shipping label with the "OTDR
Protected" badge in Amazon Buy Shipping and use Automated Handling Time (AHT)
and Shipping Settings Automation (SSA), your OTDR will not be negatively
impacted by late deliveries. For more information, go to [On-time
delivery](/help/hub/reference/G200847280).

**Note:** Currently "OTDR Protected," "Claims Protected," and "Late Delivery
Risk" badges are visible in Seller Central and on [Veeqo (an Amazon
Company](http://go.amazonsellerservices.com/veeqo-otdr-launch)). When
purchasing Buy Shipping labels via API or from Multichannel Integrators
"Claims Protected" labels will be available and, if applicable, "OTDR
Protected" will be available. "Late Delivery Risk" labels will be filtered
out. However, there may be circumstances where you may want to access "Late
Delivery Risk" labels even though they are not OTDR Protected. In such
circumstances, to access "Late Delivery Risk" labels via API, see instructions
below.

The "Late Delivery Risk" labels cannot be accessed through multi-channel
integrators at this time, but Amazon is working to enable this functionality
with additional multi-channel integrators.

#### Access "Late Delivery Risk" labels (that are not "OTDR Protected") on
Seller Central or [Veeqo, an Amazon
Company](http://go.amazonsellerservices.com/veeqo-otdr-launch):

No action is required, and you already have access to these shipping labels
which will have the "OTDR Protected," "Claims Protected," and "Late Delivery
Risk" badges.

#### Access "Late Delivery Risk" shipping labels (that are not "OTDR
Protected") using API

To access "Late Delivery Risk" labels that are not "OTDR Protected" via Buy
Shipping APIs, see below:  

  1. Send an email request to [buy-shipping-feedback-us@amazon.com](mailto:%20buy-shipping-feedback@amazon.com) with your merchant token (see [this link](/sw/AccountInfo/MerchantToken)). Your account will be opted-in within 72 hours. 
  2. **If you use[Shipping V2 API](https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference)**: Once we enable your account to purchase "Late Delivery Risk" labels, when you call the [getRates](https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference#getrates) API, as a part of the [GetRatesResult](https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference#getratesresult), the API returns both eligible and ineligible shipping service offerings. The "Late Delivery Risk" shipping service offerings will be available for purchase as a part of the [GetRatesResult](https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference#getratesresult) eligible services and the [ExcludedBenefits](https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference#excludedbenefits) list will contain the CLAIMS_PROTECTED and OTDR_PROTECTED benefits with LATE_DELIVERY_RISK in the reason codes list.
  3. **If you use[Merchant Fulfillment API](https://developer-docs.amazon.com/sp-api/docs/merchant-fulfillment-api-v0-reference)**: Once we enable your account to purchase "Late Delivery Risk" labels, when you use the operation [getEligibleShipmentServices](https://developer-docs.amazon.com/sp-api/docs/merchant-fulfillment-api-v0-reference#geteligibleshipmentservices), you will receive an output of eligible and ineligible ship methods under [GetEligibleShipmentServicesResponse](https://developer-docs.amazon.com/sp-api/docs/merchant-fulfillment-api-v0-reference#geteligibleshipmentservicesresponse). You will now find under the eligible ship methods the "Late Delivery Risk" labels with the tag of "LATE_DELIVERY_RISK" in the reason code, and the tag of CLAIMS_PROTECTED and OTDR_PROTECTED be in the [ExcludedBenefits](https://developer-docs.amazon.com/sp-api/docs/merchant-fulfillment-api-v0-reference#excludedbenefit). 

