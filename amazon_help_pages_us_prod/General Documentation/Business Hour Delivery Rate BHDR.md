---
title: Business Hour Delivery Rate (BHDR)
url: https://sellercentral.amazon.com/help/hub/reference/GL6AWZ3XEHAQ66M8
section: General Documentation
---

Business Hour Delivery Rate measures the number of Amazon Business shipments
that were delivered on the first attempt and within business hours. This is
done as a percentage of your total Amazon Business shipments during a given
30-day time period. This metric is only applicable to seller-fulfilled orders
that are destined to Amazon Business and Business Prime customers with
commercial addresses.

Getting deliveries within operating hours is a key request from Amazon
Business customers, who want their packages delivered when their businesses
are open to minimize delivery reattempts and lost or stolen packages. It
provides customers with confidence to buy your products.

BHDR currently does not impact any program eligibility and is provided for
your information only.

## BHDR calculation

BHDR is calculated for a 30-day time period, based on shipments with a
promised date between start date and end date. For example, on February 3,
your BHDR would be calculated for shipments with a promised delivery date
between December 24 and January 23. This metric is refreshed daily.

Business days and hours are determined by the delivery preferences set by
business customers on their account. If the customer does not indicate
preferences, the default business days and hours are Monday to Friday, from
9:00 a.m. to 5:00 p.m. local time.

## Expected BHDR

Delivering outside business hours can lead to customer frustration and prevent
repeat purchases from that customer. We recommend you maintain a Business Hour
Delivery Rate greater than 95% in order to maintain customer trust. However,
there is no penalty for not meeting the performance target at this time.

## View my BHDR

You can view your Business Hour Delivery Rate in [Fulfillment Insights
dashboard](/seller-fulfilled-
product/analytics/ref=xx_msfp_dnav_xx#FULFILLMENT_INSIGHT_DASHBOARD). In
addition, you can download a report to see details on your BHDR performance by
Order ID.  

  1. Go to [Fulfillment Insights dashboard](/seller-fulfilled-product/analytics/ref=xx_msfp_dnav_xx#FULFILLMENT_INSIGHT_DASHBOARD)
  2. Click **Download report**
  3. Open .xls report from Downloads

This report measures shipments delivered during a rolling 30-day period.

## Unable to view my BHDR

You can’t see BHDR on your **Fulfillment Insights dashboard** if you haven’t
delivered any Amazon Business shipments in over 3 months. To learn more on how
to understand, manage, and grow your sales from customers on Amazon Business,
go to [B2B central](/business/b2bcentral)

If your BHDR shows as N/A, it means that, even though you delivered Amazon
Business shipments over the past 3 months, there were no Amazon Business
shipments during the latest BHDR 30-day time period.

## BHDR report details

In the first tab you can see the definitions for each column of the report.

Table 1. Data definitions for full report Field name | Definition | Example   
---|---|---  
**Order ID** | Amazon Order number | 114-3731971-4697006  
**Tracking ID** | Shipment tracking number | 1Z7A9V040397481680  
**Promised Delivery Date** | The latest date a customer is expecting your shipment to be delivered on. | 11/25/2022  
**First Attempt Delivery Date** | The date the carrier tried to deliver your shipment for the first time. | 11/23/2022  
**First Attempt Delivery Time** | The time the carrier tried to deliver your shipment for the first time. | 11:05 p.m.  
**Business Hour Delivery** | Whether the shipment was delivered on the first attempt and within business hours. | Yes  
**Failure Reason** | Why Business Hour Delivery failed? | First Attempt Unsuccessful  
**Customer Business Hours on First Attempt Date** | The customer operating hours on the date of first attempt. These hours are based on the delivery preferences set on business customer’s account or by default from Monday to Friday, 9:00 a.m.-5:00 p.m., in case they did not set any preferences. | 8:00 a.m.-5:00 p.m.  
**Final Attempt Delivery Date** | The date of final delivery by the carrier. | 11/24/2022  
**Final Attempt Delivery Time** | The time of final delivery by the carrier. | 10:04 a.m.  
**Carrier Name** | The carrier you used to deliver the shipment. | UPS  
**Ship Method** | The shipping method you used to deliver the shipment. | UPS Ground  
**Is Buy Shipping** | Whether you purchased your shipping method through Amazon’s Buy Shipping. | Yes  
  
## Improve my BHDR

**Leverage best-performing carriers and ship methods**

  * Use the BHDR report to identify the best performing services you have used over 30 days and prioritize those for business orders.
  * Adopt **Carriers** and **Ship Methods** that focus on commercial deliveries. Check with your preferred carriers what ship methods guarantee deliveries from Monday to Friday, 9:00 a.m.-5:00 p.m. and prioritize those for business orders.
  * Use [Buy Shipping](/gp/help/G200202220) to fulfill your Amazon Business orders. Amazon will automatically filter out shipping methods that do not adhere to the customer’s operating days, improving your BHDR. For more information, go to [Missing carrier or ship method in Buy Shipping](/gp/help/GTQMVHPB94LP2355).

**Leverage customer preferences when planning your deliveries**

  * Use the [Orders API](https://developer-docs.amazon.com/sp-api/docs/amazon-business-orders-use-case-guide) to access detailed customer delivery preferences and improve your planning.
  * Use [Buy Shipping](/gp/help/G200202220) to view customer operating hours at an order level by visiting [Manage Orders](/orders-v3/ref=xx_myo_dnav_xx) and selecting **Buy Shipping**.

