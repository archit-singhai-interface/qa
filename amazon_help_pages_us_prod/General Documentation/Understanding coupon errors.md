---
title: Understanding coupon errors
url: https://sellercentral.amazon.com/help/hub/reference/GLBL4T5C9UAB9T5P
section: General Documentation
---

Approximately six hours before your coupon start time, our system validates
your coupon to make sure that it offers a good value to customers. These
validation rules are continuously enforced as long as your coupon is active.
If one or more of the products in your coupon don't pass any of these rules,
we disable the coupon offer on that product or products and activate the
coupon on the rest of the products that pass validation.  
  
Here are some of the errors that you might see on your dashboard and what you
can do to remedy them.

## Pricing and discount validation errors

Error message examples | Details  | What can you do if you see this error?  
---|---|---  
**Insufficient Sales History** ASINs do not have a sufficient sales history |  This ASIN does not have a **Was Price**. A **Was Price** is automatically computed and changes over time. The **Was Price** is determined using the 90-day median price paid by customers for the product on Amazon. We exclude prices paid by customers for the product during a limited time deal. For more information, go to [Amazon policy on Reference Prices](/gp/help/G202170370). We exclude new ASINs from this rule. Also, if your ASIN is old and has 4 stars and above rating (with total ratings of 5 and above), and it does not have a **Was Price** , we exclude your ASIN from this rule. |  You can leverage other promotional levers like [Amazon Ads](/gp/help/G200663330) or [Price discounts](/gp/help/G7F8CQ4EJ5YA4272), so that your ASIN can generate sales for **Was Price** to get generated. Note that canceled orders, B2B offers or customizable ASINs are not included in **Was Price** calculation.  
**Decrease Your Price to be eligible for the coupon** Your Price: $140 Decrease Your Price to $130  |  **Your Price** can be maximum of 30% higher than the **Was Price**. We exclude new ASINs from this rule. Also, if your ASIN is old and has 4 stars and above rating (with total ratings of 5 and above), and it does not have a **Was Price** , we exclude your ASIN from this rule. |  In this case, decrease the **Your Price** of the ASIN to the suggested price as shown in the error on the Coupons page. In the example stated here, decrease **Your Price** of your ASIN to $130 (current Your Price: $140) in order to run a coupon. Once done, wait for four hours for coupon to be unsuppressed on that ASIN.  
**Increase Coupon Discount to be eligible for the coupon** Current Net Price: Your Price - Coupon Discount = $115 Required Net Price: Your Price - Coupon Discount = Maximum $100 Increase Coupon Discount by at least $15 |  The **Net Price** (Your Price - Coupon Discount) must be such that it must beat the **Was Price** by at least 5%. We exclude new ASINs from this rule. Also, if your ASIN is old and has 4 stars and above rating (with total ratings of 5 and above), and it does not have a **Was Price** , we exclude your ASIN from this rule. |  In this case, increase the discount as shown in the error on the Coupons page. In the example stated here, Current Net Price: Your Price ($125) - Coupon Discount ($10) = $115  Required Net Price: Your Price ($125) - Coupon Discount ($25) = Maximum $100 Increase discount by $15 in order for coupon to run. If your coupon has certain percentage off discount, convert the discount amount to discount percentage. In this case, New Discount/Your Price: ($10+$15)/$125 = 20%  Once done, wait for four hours for coupon to be unsuppressed on that ASIN. In case you are not able to edit the discount, re-create the coupon with the required discount amount.  
**Minimum/Maximum Discount Issue** Discount must be a minimum of 5% of ASIN’s **Your Price** or Discount must be a maximum of 50% of ASIN’s **Your Price** For more information, go to [Understanding coupon errors](/gp/help/GLBL4T5C9UAB9T5P). |  The minimum discount that can be offered is 5% and the maximum discount that can be offered is 50% of **Your Price**. Example:  **Your Price** : $100 Minimum discount (Coupon Discount/Your Price) can be $5 or 5% Maximum discount (Coupon Discount/Your Price) can be $50 or 50% |  Increase or decrease discount as per limits. Once done, wait for four hours for coupon to be unsuppressed on that ASIN. In case you are not able to edit the discount, re-create the coupon with the required discount amount or percentage.  
  
**Note:** In case your ASIN has **Sale Price** live, use **Sale Price** in
above scenarios instead of **Your Price**. The above rules apply to **Sale
Price** or **Your Price** whichever is live for your ASIN.

**How do you update the 'Your Price'?**

  

  1. Go to **Manage All Inventory** page.
  2. Select **Edit Listing** against the corresponding ASIN from the dropdown menu.
  3. Change the **Your Price** under the **Offer** tab.

**Note:** If the ASIN has **Sale Price** live, change the **Sale Price** under
the **Offer** tab.

## Inventory error

**We temporarily excluded this ASIN from your coupon due to insufficient
inventory.**

You don’t have enough inventory to accommodate the customer demand that your
coupon might generate. When this happens, we disable the coupon offer on the
related product.

**What can you do if you see this error?**

Send in more inventory and recheck all the product attributes. Once you’ve
added inventory or changed a product attribute, then create the coupon again.

## Star rating is below 3.0

To be eligible for Coupons, below criteria applies for product eligibility:

  * Products with no ratings are eligible without additional criteria.
  * If a product has ratings, it must meet following criteria:
    * Products with 1-4 ratings must have an average rating of at least 1 star.
    * Products with 5+ ratings must have an average rating of at least 3 stars.

**What can you do if your ASIN does not meet the above listed criteria and you
see an error?**

Run the coupon with the rest of the products that aren’t excluded because of
this error. You can also re-create the coupon without the products that caused
the error.

##  Potentially embarrassing, adult or refurbished error

We temporarily excluded this ASIN from your coupon because the product has
been identified as potentially embarrassing or offensive.

The product is not eligible for coupons if any of the criteria listed below
are true:

  * It is an adult product. To learn more, visit our [adult products policy](/gp/help/G200339940). 
  * It has content on the product detail page that may be offensive, embarrassing, or inappropriate. To learn more, visit our [offensive and controversial materials policy](/gp/help/G200164670). 
  * It is in used condition, collectibles, or certified refurbished.
  * It falls within one of the following categories: sexual wellness, hunting and fishing, guns and gun accessories, books, music, video, and DVDs.

**What can you do if you see this error?**

Make sure that the product doesn't fall within the criteria listed above. Run
the coupon with products that aren’t excluded, or re-create the coupon without
the excluded products.

Run the coupon with those ASINs that are not suppressed with this kind of
error, or re-create the coupon without those ASINs in error.

##  Selling price error

We temporarily excluded this ASIN from your coupon as it is does not satisfy
the following condition.

"current price + shipping price must be higher than the <minimum seller price
for each respective store>”.

Store | Minimum seller price | Currency  
---|---|---  
US | 5 | USD  
UK | 5 | GBP  
DE | 5 | EUR  
FR | 5 | EUR  
IN | 5 | INR  
JP | 1 | JPY  
BR | 20 | BRL  
MX | 100 | MXN  
AU | 1 | AUD  
AE | 5 | AED  
SG | 1 | SGD  
CA | 5 | CAD  
SA | 5 | SAR  
EG | 5 | EGP  
  
**What can you do if you see this error?**

Make the changes to the current price or shipping price so that the coupon
price is higher than the minimum seller price for each respective store. We'll
automatically reactivate the coupon offer within approximately 24 hours after
the ASIN meets this eligibility rule again.

## Frequently asked questions

#### How do I know my Was Price?

We cannot share the exact **Was Price** against an ASIN. However, the reason
for not having **Was Price** is that the ASIN does not have enough sales
history in last 90 days. Also, note that only non - promotional sales
contribute towards calculating the **Was Price**.

#### What can I do if I want to increase sales, but I am unable to run a
coupon on my product because there is no 'Was Price' defined?

We highly recommend leveraging other promotional levers like [Amazon
Ads](/gp/help/G200663330) or [Price discounts](/gp/help/G7F8CQ4EJ5YA4272).

#### Why is my coupon not going live in spite of increasing discount or
lowering 'Your Price' as per suggestion?

It takes up to four hours for system to validate the revised values and hence
we recommend waiting for at least four hours for your coupon to get
unsuppressed and go live. If the error still persists, contact [Selling
Partner Support](/help/center).

#### What can I do if my coupon shows a failed status in the dashboard?

Check on errors by clicking on the Coupon page. Fix the errors and try
submitting a new coupon again.

