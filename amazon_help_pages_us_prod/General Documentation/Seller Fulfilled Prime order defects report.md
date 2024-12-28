---
title: Seller Fulfilled Prime order defects report
url: https://sellercentral.amazon.com/help/hub/reference/G202072570
section: General Documentation
---

The Seller Fulfilled Prime order defects report identifies the orders that
missed any of the fulfillment performance requirements for Seller Fulfilled
Prime. These fulfillment requirements include on-time delivery, valid tracking
rate, and cancellation rate. To download the report, visit your [Seller
Fulfilled Prime performance dashboard](/seller-fulfilled-prime/seller-
performance) and select **Download defects report** under the **Fulfillment
metrics** section.

##  **Fields included in the Seller Fulfilled Prime order defects report**

####  **Order ID**

The unique ID of the order.

#### Order date and time

The date and time when you received the order. This is the **purchase date**
shown on the order details page.

#### Promised ship date

The date you must ship the order. This is the **Ship by** date shown on the
order details page.

#### Promised delivery date without a promise extension

The promised delivery date for the order, excluding any effect of a promise
extension. This is the **Deliver by** date shown on the order details page.
This date is the same as the promised delivery date shown to the customer when
no promise extension is applied to the order.

#### Promised delivery date with a promise extension

The delivery date that is promised to the customer, including the effect of a
promise extension. This date is the same as the promised delivery date without
promise extension when no promise extension is applied to the order.

#### Actual ship date and time (carrier first scan)

The date and time when the carrier scanned the package for the first time.

#### Actual delivery date and time

The date and time of the first delivery attempt made by the carrier.

#### Carrier name

The name of the carrier you selected to deliver the order.

#### Ship method

The carrier’s ship method you selected to deliver the order.

#### Tracking ID

The carrier’s tracking ID for the shipment.

#### Unit count

The number of units shipped.

#### Origin zip

The origin zip code for the order.

#### Destination zip

The destination zip code for the order.

#### Eligibility metric: Delivered late without a promise extension?

This column indicates if the order was delivered after the promised delivery
date without a promise extension, that is, the **Deliver by** date in the
order details. The value in this column will be "X" if the order was delivered
after the promised delivery date without a promise extension.

#### Eligibility metric: Canceled by seller?

This column indicates if the seller canceled the order. The value in this
column will be "X" if the order was canceled by the seller.

#### Eligibility metric: Invalid tracking?

This column indicates if the order did not have valid tracking. The value in
this column will be "X" if the order did not have a valid first scan from an
Amazon-integrated carrier.

**Note:** Orders in the defect report are only included if they miss one or
more of the eligibility metrics listed above. An order listed in the defect
report for missing an eligibility metric will also indicate if it missed any
of the three supporting metrics listed below with an "X" under the applicable
supporting metric column. However, if an order only misses one or more
supporting metrics and no eligibility metrics, it will not be included in the
order defects report.

#### Supporting metric: Delivered late with a promise extension?

This column indicates if the package was delivered after the promised delivery
date with a promise extension. The value in this column will be "X" if the
package was delivered after the promised delivery date with a promise
extension.

#### Supporting metric: Shipped late (carrier first scan)?

This column indicates whether or not the order had a carrier first scan after
the promised ship date. The value in this column will be "X" if the order had
a carrier first scan after the promised ship date.

#### Supporting metric: Purchased label outside Amazon Buy Shipping Services?

This column indicates whether the shipping label was purchased outside of
Amazon's Buy Shipping Services. The value in this column will be "X" if the
shipping label was purchased outside of Amazon's Buy Shipping Services.

