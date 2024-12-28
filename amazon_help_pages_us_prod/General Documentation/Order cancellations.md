---
title: Order cancellations
url: https://sellercentral.amazon.com/help/hub/reference/G201722390
section: General Documentation
---

**When can a buyer cancel an order?**

For the first 30 minutes after the order is placed, buyers can cancel their
own order using the **Cancel Items** option located in **Your Account** >
**Your orders** on Amazon.

After 30 minutes, the buyer can no longer cancel the order directly, they can
only submit a cancellation request for the seller to review. You will receive
an email when the buyer requests a cancellation.

If you have made changes to your [Buyer Auto- Cancellation
Window](https://sellercentral.amazon.com/fbm/buyerRequestCancellation), the
order will be automatically canceled by Amazon on your behalf based on your
settings and you will receive an email regarding such cancellations.

**What should I do when a buyer wants to cancel an order?**

Depending on the stage for processing the order, the following options may
help you to determine next steps:

**For Self Ship orders:**  

  1. **If you haven’t shipped or confirmed shipment for the order** , you can cancel it in [Manage orders](/orders-v3/ref=xx_myo_dnav_xx), or use an Order Cancellation feed to cancel orders by uploading a file or through an API. To cancel an order from the Manage orders, follow the steps mentioned under **Official cancellation process that will not count against your Cancellation Rate metrics**.
  2. **If you already shipped, but haven’t confirmed shipment** , you must confirm shipment and then contact the buyer via the [Buyer-seller messaging service](/gp/help/G200389080) and advise them to either refuse the shipment or initiate a return.
  3. **If you haven’t shipped, but you already confirmed shipment** , you can no longer cancel the order. You must begin a refund process and not ship the product.

**Note:**

  * When you cancel an order, Amazon automatically updates the order status in the buyer's Amazon account and sends an email notification to the buyer.
  * Messages about cancellation are considered a [critical message](/gp/help/GRZ5Y5YEN9J84NAC), and will be delivered to a buyer even if they have opted out of non-critical messages.
  * If the reason you have to cancel an order is not due to a Buyer-requested cancellation, you must cancel this order instead of requesting the buyer to cancel it.
  * Canceling orders when the buyer unofficially requests cancellation through Buyer-seller messaging will impact your Cancellation Rate metrics. Such messages are labeled as **Inquiry from Amazon customer**.
  * The buyer is not charged for an order until you confirm shipment.

**Official cancellation process that will not count against your Cancellation
Rate metrics:**

The process by which a buyer can request an order cancellation is by finding
the order they want to cancel in their Amazon account > **Your Account** >
**Your orders** > **Request Cancellation**.  

  1. If the buyer requests a cancellation after 30 minutes of placing their order, you will receive an email and will be able to view the cancellation request on the **Manage orders** page, right above the order information, with a banner stating “The buyer has requested that this order be canceled. Canceling this order will not affect your Cancellation Rate metric.”
  2. After you cancel the order, the buyer will receive an email confirming the order has been canceled. 

**Note:** Selecting the reason for cancellation as **Buyer Canceled** for an
order cancellation that was not initiated by a buyer will count against your
Cancellation Rate metrics.

## To process an order cancellation request by a buyer, follow these steps:

  

  1. From the **Orders** drop-down on Seller Central, select [Manage orders](/orders-v3/mfn/unshipped?). On the “Unshipped” tab you can click “Show filters” to open the filtering pane and then under the section of “Pending Action” you can check the box called “Buyer Requested Cancel” to filter orders that have a Buyer Requested Cancellation.
  2. The orders which have a buyer-initiated cancellation will show up with a banner stating “The buyer has requested that this order be canceled. Canceling this order will not affect your Cancellation Rate metric.”
  3. Click **Cancel order** under the **Actions** column.

**Note:** The **Cancel order** option is available only for **Unshipped**
orders.

  4. Click **Submit**.
  5. After you cancel the order, buyer will receive an email confirming that the order has been canceled.

The image below show example of Step 2 and 3. On your **Manage orders** page,
select the order you want to cancel and click **Cancel order**.

![](https://m.media-amazon.com/images/G/31/rainer/Picture1.png)

Example of Step 4: Buyer canceled is pre-selected and cannot be edited as we
know that this is a buyer requested cancellation.

![](https://m.media-
amazon.com/images/G/32/rainier/help/Buyer_requested_cancelation.png)  

**Note:** If you cannot fulfill the order due to scenarios such as no or low
inventory, you forgot to turn on vacation settings and received an order,
pricing errors, listing errors, shipping settings errors, technical issues at
your end, do not contact the buyer to cancel such orders. Select appropriate
reasons from the drop-down menu and cancel the order. Canceling these orders
will impact your cancellation rate.

##  Unofficial Buyer-initiated cancellation process that will count against
your metrics

A buyer requesting a cancellation solely via the Buyer-seller messaging tool
without following the proper cancellation process is considered the incorrect
manner for buyers to cancel orders. Such messages are labeled as “Inquiry from
Amazon customer”. Accordingly, if you cancel an order in response to a request
from a buyer via the Buyer-seller messaging tool, such cancellations will
impact your Cancellation Rate metric.

To avoid canceling an order in a manner that impacts your metrics, you can
respond to the buyer’s message and request the buyer to submit a cancellation
using the official process above.

Use the following instructions in your response: “You can cancel the order in
your Amazon account at **Your Account** > **Your orders** > **Request
Cancellation**."

To review your Cancellation Rate and policy requirements, go to [Cancellation
Rate](/gp/help/G200285210).

## Partial cancellation

Partial order cancellations are not supported at this time. However, you can
issue full and partial refunds for each item in an order by using either the
**Refund orders** tool or the [Order Adjustment Feed](/gp/help/1611).

**Note:** To start a refund, the order must have already had the shipment
confirmed.

For more information, go to [Cancel an order or multiple
orders](/gp/help/G200198080).

## Automatic cancellation

Amazon will automatically cancel orders if seven days have passed since the
expected shipping availability date and you have not yet shipped and confirmed
the shipment.

## What kind of cancellations negatively impact your Cancellation Rate metric?

**Cancellation initiated by** | **Cancellation scenario** | **Negatively impact Cancellation Rate?**  
---|---|---  
Buyer | 1\. I am canceling because the buyer submitted an official cancellation request  | No  
2\. I am canceling because the customer asked me to through the Buyer-Seller Messaging tool (unofficial cancellation processes; such messages are labeled as “Inquiry from Amazon customer”) | Yes  
Seller | 1\. I am canceling because my item went out of stock / pricing or listing error / incorrect shipping settings / received an order because I forgot to turn on vacation settings when I was on holiday | Yes  
2\. I am canceling because the address was undeliverable | Yes  
3\. I am canceling because the buyer was unresponsive | Yes  
Amazon  | 1\. The order was automatically canceled by Amazon because the seller did not confirm shipment within seven days of ship-by-date | Yes  
2\. The order was automatically canceled by Amazon because we detected the buyer to be fraudulent  | No  
3\. Payment verification failed so the order was canceled by Amazon | No   
  
## Order reports

For sellers who use order reports to process orders, an optional additional
field called **is-buyer-requested-cancellation** is available on your order
reports. The **is-buyer-requested-cancellation** column will have a “TRUE”
value if there is a buyer cancellation request for the order and “FALSE”
otherwise (shown below).

![](https://m.media-amazon.com/images/G/01/devarakg/order_reports_image.jpg)

You can view all orders which have buyer-initiated cancellation requests in
your order reports by switching on the toggle button for the field called
“Buyer Requested Cancel” (shown below) available by accessing [Add or remove
order report columns](/order-reports-and-feeds/column-picker?source=/order-
reports-and-feeds/reports/ref=xx_orderrpt_dnav_xx).

![](https://m.media-
amazon.com/images/G/01/devarakg/add_or_remove_report_columns_image.jpg)  

## APIs for buyer-initiated order cancellations

## Selling Partner (SP) - API

Similar to the orders API, for SP-API, when a buyer initiates an order
cancellation request:

  

  1. The **ordersV0GettOrderItemsList** operation will include an **isBuyerRequestedCancel** flag and **buyerCancelReason** string for each OrderItem in the response when the order has a buyer requested cancellation.
  2. The **isBuyerRequestedCancel** flag will be set to True if the order has a buyer cancellation request.
  3. The **buyerCancelReason** will display the reason for cancellation specified by the buyer.

**Selling Partner (SP)–Notification API**

ORDER_CHANGE Notification API is the upgraded version for ORDER_STATUS_CHANGE
Notification API. Sellers can subscribe to get proactively notified when there
are important changes such as order status change and buyer requested
cancellation. Once a seller subscribes, if a buyer initiates an order
cancellation request:

  

  1. An ORDER_CHANGE notification will be triggered to seller automatically.
  2. The **isBuyerRequestedCancel** flag will be set to True if the order has a buyer cancellation request.

Check the [SP user guide](https://developer-docs.amazon.com/sp-
api/docs/notifications-api-v1-use-case-guide#order_status_change) on how to
subscribe to ORDER_CHANGE Notification.

## See also

[Cancellation Rate](/gp/help/200285210)

Seller university video: [Order cancellations and Account
health](/learn/courses?moduleId=acb8f071-c398-4c09-97a8-15f81ec4ff62&ref_=su_refined_search&modLanguage=English&videoPlayer=youtube)

[Cancellations FAQs](/gp/help/GRXAS2XTAYEF77BG)

