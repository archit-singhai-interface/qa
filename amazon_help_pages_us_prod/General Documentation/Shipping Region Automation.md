---
title: Shipping Region Automation
url: https://sellercentral.amazon.com/help/hub/reference/G237WEY9JD2VQQZQ
section: General Documentation
---

## Shipping Region Automation

Shipping Region Automation helps in setting up delivery regions for One-Day
Delivery and Two-Day Delivery based on the delivery speeds of your preferred
shipping services and your fulfillment center location. Amazon will
periodically refresh these regions to reflect the latest speeds of your
shipping services. With Shipping Region Automation enabled, you will not need
to manually configure your delivery regions for Premium Shipping Options.

## Create a new Prime shipping template

To create an automated Prime shipping template, perform the following steps:

  

  1. From the **Settings** drop-down menu on the top right of Seller Central, click **Shipping Settings**.
  2. On the **Shipping Templates** tab, click **Create New Shipping Template**.
  3. In the pop-up window, click **Create a new shipping template** , and click **OK**.
  4. Enter the **Shipping Template Name** (for example, "Prime Shipping").
  5. Choose from either a **Per Item** /**Weight-Based** or **Price banded** rate model for your shipping rates.
  6. Click the toggle to enable **Shipping Region Automation**.
  7. Select your **Shipping address** and **Preferred carriers** in the pop-up window.

**Note:** Select a Preferred carrier to enable the **Next** option.

  8. Using the toggle enable **Yes, I want to enable Prime for SKUs assigned to this template** and click **Next**.

**Note:** This option is available only if **seller is eligible for Prime**.

  9. Select the **Shipping services** for Two-Day and One-Day delivery based on the shipping services coverage. 
  10. Select Delivery zone limit if applicable. This is a proxy for shipping cost. For example, if you select zone 8 for UPS Ground for Two Day Delivery, the automated shipping regions will be limited to where UPS can deliver in two days from your selected fulfillment center address within the scope of UPS Ground zone8. Leave Amazon’s default value if you do not need have any zone restrictions. Click **Next**.
  11. Review Prime shipping settings and click **Confirm**.
  12. Review and edit shipping rates for Non-Prime customers.
  13. Click **Save** template.
  14. **Assign SKUs** to the Prime shipping template.

For more information, see Shipping Settings Automation FAQ section on this
page.

## Upgrade an existing Prime shipping template

To upgrade an existing Prime shipping template, follow the steps below:

  

  1. From the **Settings** drop-down menu on the top right of Seller Central, click **Shipping Settings**.
  2. On the **Shipping Templates** tab, select the template you want to edit from the list.
  3. Click **Edit Template** on the right side of the screen.
  4. Click the toggle to enable **Shipping Region Automation**.
  5. Select your **Shipping address** and **Preferred carriers** in the pop-up window.

**Note:** Select a **Preferred carrier** to enable the **Next** option.

  6. Using the toggle enable **Yes, I want to enable Prime offer for SKUs assigned to this template** and click **Next**.

**Note:** This option is available only if **seller is eligible for Prime**.

  7. Select the **Shipping services** based on the shipping services coverage
  8. Select Delivery zone limit if applicable. This is a proxy for shipping cost. For example, if you select zone 8 for UPS Ground for Two Day Delivery, the automated shipping regions will be limited to where UPS can deliver in two days from your selected fulfillment center address within the scope of UPS Ground zone 8. Leave Amazon’s default value if you do not need have any zone restrictions. Click **Next**.
  9. Review Prime shipping settings and click **Confirm**.
  10. Review and edit shipping rates for Non-Prime customers.
  11. Click **Save** template.
  12. **Assign SKUs** to the Prime shipping template.

For more information, see Shipping Region Automation FAQ section on this page.

## Shipping Settings Automation FAQ

#### How does Amazon automate Prime shipping regions?

Prime-eligible regions are determined based the carrier’s delivery performance
(such as on-time delivery) from your shipping location to destination regions
where customers order from that are enabled for Prime in your shipping
templates. Changes are made periodically to ensure maximum possible Prime
coverage with high on-time delivery for Prime shipments.

#### How many shipping locations can I select?

You can select up to 10 shipping location. Prime regions will be a set of
union (or sum) or all regions that the selected shipping services can deliver
from each shipping location for Two-Day and One-Day Delivery orders.

#### What carriers/ship methods should I select?

Select the carriers/shipping services that you are using to ship Prime orders
(standard, two-day, and one-day delivery). All the displayed shipping services
in the Shipping Preference Selector are eligible for selection.

#### Can I select multiple carriers/shipping services?

Yes. Select all shipping services that you intend to use for Prime orders.
Prime regions will be set as a union (or sum) of all regions that the selected
shipping services can deliver.

#### What is Delivery zone limit?

Delivery zone limit allows you to control more precisely the Prime shipping
regions. If a ship method’s eligible 2-day coverage spans across multiple
zones, and consequently results in different shipping costs, you can control
Prime shipping costs by limiting the Prime regions using delivery zone. You
can leave the Amazon default value if they do not need to restrict shipping
regions by zone. You can verify the shipping costs by zones on the carriers’
website ([UPS](https://www.ups.com/us/en/shipping/rates.page?),
[FedEx](https://www.fedex.com/en-us/online/rating.html#),
[USPS](https://postcalc.usps.com/DomesticZoneChart)). Prime badge will only be
visible to customers in the regions within the delivery zone limit that can be
reached in 1 or 2 days by your shipping services from your shipping locations.

#### How are Prime coverage percentages determined?

Prime coverage is calculated as the percentage of US population that are
within the Prime regions covered by your selected shipping services from your
shipping location.

#### Why is Prime coverage determined by Amazon smaller than what I usually
get?

We enable a region as Prime when the selected shipping service can deliver on-
time to all ZIP codes in that region. If we find that some of the ZIP codes in
that region cannot be delivered on time, we may turn off that region as Prime
to protect the customer experience. However, as delivery speeds of shipping
services improve, a non-Prime region may be upgraded to a Prime region.

#### How do I know when regions are changed?

Whenever Amazon updates a Prime region in Automated shipping template, Amazon
will create a new version of the shipping template. You can review and see all
these changes in shipping template’s history.

#### What happens if I can’t buy the designated shipping services in Buy
Shipping?

You will be able to use the designated shipping services in Buy Shipping if
you:  

  1. Bought the shipping label on-time and before the [pick-up time](https://sellercentral.amazon.com/sbr/order-fulfillment) for the shipping service.
  2. Selected a shipping location that was also defined on your shipping template.

If for any reason you fulfilled all requirements (i.e., shipped on time) and
still were not able to buy your preferred shipping service on Buy Shipping,
you may buy the shipping label outside of Buy Shipping but ensure that the
shipping service bought can deliver the products on time. We will
automatically ensure that such orders are not counted towards your Buy
Shipping eligibility metrics and remove them from your [defect
report](https://sellercentral.amazon.com/seller-fulfilled-prime/seller-
performance). It may take up to 4 business days from the date of the order for
the change to reflect on your account. If you continue to see these orders on
your defect report after 4 business days of receiving the order, contact us.
Note that this only applies to orders tied to automation templates.

## Shipping Settings Automation User Guide

This page provides instructions for the new Prime Automation feature.  

  1. From the **Settings** drop-down menu on the top right of Seller Central, click **Shipping Settings**.
  2. On the **Shipping Templates** page, click the **Create New Shipping Template** option.
  3. In the pop-up window, click **Create a new shipping template** , and click **OK**.
  4. Enter the **Shipping Template Name** (for example, "Prime Shipping").
  5. Choose from either a **Per Item** /**Weight-Based** or **Price banded** rate model for your shipping rates.
  6. Click the toggle to enable **Set shipping regions based on ship-from location and ship services**.
  7. Ensure the shipping location is correct.
  8. Select the preferred carriers you use for Prime orders.
  9. Click the toggle for **Yes, I want to enable Prime offer for SKUs assigned to this template** to enable Prime.
  10. Select the ship service you use for standard orders under Standard Shipping and click **Next**.
  11. Select the ship service you use for Two-Day Delivery. You can see the population coverage that can be reached by the selected ship services in 2 days.
  12. Select Delivery zone limit if applicable. This is a proxy for shipping cost. Leave Amazon’s default value if you do not need have any zone restrictions. Click **Next**.
  13. Select the ship service you use for One-Day Delivery. Click **Next**.
  14. Check all the selection again before clicking **Confirm**.

