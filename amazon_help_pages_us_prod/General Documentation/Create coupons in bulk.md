---
title: Create coupons in bulk
url: https://sellercentral.amazon.com/help/hub/reference/G363YLQW4NB5L38V
section: General Documentation
---

To use spreadsheets to create coupons, follow these steps:  

  1. From the drop-down menu in Seller Central, select **Advertising** and then select **Coupons**.
  2. At the top right of the page, click **Create coupons in bulk** and click **Download template file**.
  3. Open the file and fill in the spreadsheet according to the instructions listed below.

**Note:** Each row in the spreadsheet is a separate coupon. If you want to add
multiple ASINs to the same coupon, add them in the same cell in column A,
separated by a semicolon.

Spreadsheet column | Column title | Details  
---|---|---  
A | ASIN list | Enter a list of participating child ASINs separated by a semicolon. Add between 15 and 2,900 ASINs per coupon. Adding a parent ASIN will automatically add all child ASINs. If you want to create a coupon with fewer than 15 child ASINs, use the normal coupon creation workflow.  
B | Discount type (**USD off** or **Percentage off**) | Choose either **Money off** or **Percentage off**.  
C | Coupon discount **Percentage off** value | Fill out this section only if you selected **Percentage off** in column B. Enter a discount percentage between 5% and 50%.  
D | Coupon discount **USD off** value | Fill out this section if you selected **USD off** in column B. Enter the discount value that you want to offer on the coupon. The discount value must be greater than zero.  
E | Coupon title |  Amazon automatically generates the beginning of your coupon title with the discount that you selected, for example, “Save 10% on ...” Enter the rest of the title that will be displayed to customers (limit 80 characters). We recommend using the brand and product name.  Offensive words, discount percentages, or reference to events such as Prime Day or Black Friday in coupon titles are prohibited. Failure to comply with these rules can result in your coupon being deactivated.  
F | Coupon budget | Enter the budget amount that you want to add to the coupon. The minimum is $100. Coupon budgets are not hard limits. For more information, go to [Why is my spending higher than my budget?](/gp/help/GRTVWTKPM8NLQQT2)  
G | Coupon start date | Choose a start date within the next three months. Your coupon will start at midnight on the start date. It can take up to six hours for a coupon to appear in the store after it is activated.   
H | Coupon end date | Choose an end date within 30 days for standard coupons, 365 days for Subscribe & Save coupons, or 180 days for reorder coupons. Coupons end at 11:59 p.m. on the end date.   
I | Limit redemption to one per customer |  For **Percentage off** coupons: 
     * When you select **Yes** , your coupon will apply to only **one unit per customer**. Example: If a customer clips a 10% off coupon and buys eight units in a single order, they can use the coupon on only one unit. If the customer places another order on the same ASIN, no discount will be applied.
     * When you select **No,** your coupon will apply to **multiple units per customer** but will be restricted to a **maximum of five units per order**. Example: If a customer clips a 10% off coupon (offer price $50) and buys eight units in a single order, they can use the coupon on five units for a total discount of $25 ($5 off each unit with the 10% coupon). If the customer places another order on the same ASIN and buys three additional units, they’ll get a discount on all three units because the maximum is five units per order.
For **Money off** coupons:

     * When you select **Yes** , your coupon applies to only **one unit per customer**. Example: If a customer clips a $5 off coupon and buys eight units in a single order, they can use the coupon on only one unit. If the customer places another order on the same ASIN, no discount will be applied.
     * When you select **No,** your coupon applies to **multiple units per customer** but will be restricted to **one unit per order**. Example: If a customer clips a $5 off coupon (offer price $50) and buys eight units in a single order, they can use the coupon on only one unit for a total discount of $5. If the customer places another order on the same ASIN and buys three additional units, they’ll get a discount on only one unit.  
J | Targeted segment | Specify the customer segment that your coupon should be visible to. For example, if you choose **Amazon Prime** , your coupon will be visible only to Amazon Prime customers.  
  4. Save your file as XLS.
  5. Click **Choose file** , select the XLS file you saved in the previous step, and then click **Upload**.
  6. Our system will start processing your spreadsheet. To review the status of your coupon spreadsheet, click **Recent uploads**. The status could be one of the following: 
     * **Processing** : The spreadsheet is going through basic validations. The status will change to **Success** or **Error**.
     * **Success** : The spreadsheet was processed successfully, and coupons were created. This doesn’t automatically mean that your coupon will run. After the spreadsheet has been processed successfully, our systems will run a number of validations on the coupon. You can monitor the status of the coupon on the **Coupons** dashboard.
     * **Error** : There were errors in creating coupons. Download the status file to review the errors and take the required actions to correct them. For more information, go to [Fix spreadsheet errors in coupon uploads](/gp/help/GXRK7QW9Y7WZJ4MM).

It can take four to six hours after creation for a coupon to be activated.
Coupons created with a same-day start date require at least six hours for our
systems to run a number of validations on them to ensure that they offer a
good value to customers.

## Overlapping coupons

If you create a coupon for an ASIN that already has a scheduled coupon, the
most recently created of the overlapping coupons will be suppressed to avoid
discount stacking. Example: a customer clips a 10% off coupon and 15% off
coupon to receive 25% off at checkout.

There’s an exception to this rule: Subscribe & Save coupons and Reorder
coupons can be scheduled at the same time on the same ASIN. Discounts on
Reorder coupons and Subscribe & Save coupons cannot be stacked because they’re
restricted to different buying options. Reorder coupons can only be redeemed
on a one-time purchase, while Subscribe & Save coupons can only be redeemed on
the Subscribe & Save buying option.

**Example:** A 10% off Reorder coupon and a 20% off Subscribe & Save coupon
are scheduled on the same ASIN at the same time. If a customer clips both
coupons, they receive either of the following:

  * A 10% off Reorder coupon, if they order via the **One-time purchase** buying option
  * A 20% off Subscribe & Save coupon, if they order via the **Subscribe & Save** buying option.

Our system does not check if a coupon overlaps with other types of promotions.
Example: coupon and deal overlap.

