---
title: Create a business pricing rule
url: https://sellercentral.amazon.com/help/hub/reference/GD29LN5JBS94EL4L
section: General Documentation
---

A Business Price and Quantity Discount pricing rule establishes what will
happen to your business price and quantity discounts when you update your
standard (consumer) price. For example, you can create a rule that keeps your
business price 5% below your standard price. Any time you update the standard
price for SKUs in this rule, your business price would automatically update to
remain 5% below the updated standard price.

To create a Business Price and Quantity Discount rule, do the following:

  1. Go to Pricing in Seller Central, navigate to [Automate Pricing](/automatepricing/home). If you have already created a pricing rule and want to create another, click **Create a new pricing rule** on the same page.

  2. For the type of rule you want to create, select **Business Price and Quantity Discount** from the drop-down menu.

  3. Enter a rule name. This name should be short but descriptive enough to remember later. For example, '5% off business price rule' or 'BISS quantity discount price rule.'

  4. Specify the percentage discount you want to provide for a single unit (that is, the business price).

**Note:** You can set your business price equal to your standard price by
entering 0%.

  5. To specify quantity tiers and discounts, click **Add a quantity discount threshold**. You can add up to five quantity tiers.

**Note:** 1\. The quantity and the percentage discount entered must be higher
with each subsequent tier.

**Note:** 2\. The percentage discount you entered for each quantity tier will
be used to determine the minimum price applicable for that specific quantity
tier. For example, if the minimum price for a SKU is $20, and you entered 10%
as the discount on 5+ units, the minimum price applicable for quantity tier 5+
units would be $20 * (1-10%) = $18.

  6. To confirm your rule parameters, read the **Rule Summary** that appears below the filters.

  7. When you are finished, click **Save and select SKUs** to move to the next step in the Automate Pricing workflow. When you click **Save and select SKUs** , your rule will be saved, whether or not you add any SKUs to the rule. Automate Pricing will not change any prices on your SKUs until you assign SKUs to your rule.

## Business Catalog Rules

Business Catalog rule is a pre-existing business pricing rule that you can
apply across the entirety of your listed products. When active, the Business
Catalog rule is applied to your entire catalog (including newly added SKUs),
across all marketplaces and will set your business prices and quantity
discounts dynamically relative to your standard prices. SKUs with Business-
Only offers will not be repriced. SKUs that are assigned to other business
pricing rules (example., a Business Price and Quantity Discount rule) will be
excluded.

To setup a Business Catalog rule, do the following:

  1. Go to Pricing in Seller Central, navigate to [Automate Pricing](/automatepricing/home). Go to **Business Catalog Rule by Amazon** , click **Setup** on the same page.

**Note:** The Business Catalog rule is pre-created for you, and you cannot
delete the Business Catalog rule. Your only option is to choose to activate
the rule by clicking on setup.

  2. In **Review and activate rule** page, check the option **Replace all existing Business Discounts that are not managed by other Business Pricing rules** if you would like SKUs with existing business prices to be managed by Business Catalog rule.

  3. Set the default price limit as a percentage of your standard price. This percentage will be applied to SKUs (existing or newly added) that do not have minimum prices set at the time of rule set up.

  4. Specify the percentage discount you want to provide for a single unit (that is, the business price).

  5. To specify quantity tiers and discounts, click **Add a quantity discount threshold**. You can add up to five quantity tiers.

  6. When you are finished, click **Save and activate** to activate Business Catalog rule. When you click **Save and activate** , all SKUs that are not being assigned to a business pricing rule in your catalog will be automatically assigned to Business Catalog rule, and you do not need to manually assign SKUs to this rule.

