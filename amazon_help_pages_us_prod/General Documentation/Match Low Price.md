---
title: Match Low Price
url: https://sellercentral.amazon.com/help/hub/reference/G200836360
section: General Documentation
---

The **Match Low Price** feature helps you quickly and easily match the current
lowest prices on Amazon for the products you offer. "Current lowest price" is
based on your [Manage Pricing](/inventory?viewId=PRICING) details in **Manage
Inventory** , which allows you to compare offers using the following
variables:

  * Listing condition (based on the [Condition Guidelines](/gp/help/200339950)) 
    * All listings, regardless of condition.
    * Only listings in the same condition. For example, New or Used.
    * Only listings in the same sub-condition. For example, Used-Like New, or Used-Very Good.
  * Fulfillment method (whether Fulfillment by Amazon or seller-fulfilled) 
    * All listings, regardless of fulfillment method.
    * Only listings with the same fulfillment method as your listing.

##  Apply Match Low Price to single or multiple listings

#### Single listings

  

  1. Select **Manage Pricing** from the Pricing menu.
  2. Click **Match price** in the Lowest Price + Shipping column of the listing you want to change. Alternatively you can click the **Match low price** button for the listing.

The item price in the **Price + Shipping** column will update to match the
total price in the **Lowest Price + Shipping** column.

  3. Click the listing's **Save** button to complete the price change.
  4. To revert the change, type your desired price in the box in the listing's **Price + Shipping** column and click the **Save** button.

Or

  

  1. Select **Manage All Inventory** from the Inventory menu.
  2. Click on **Match** next to the Lowest Price in the Price + Shipping column of the listing you want to change.
  3. Click on the listing’s **Save** button to complete the price change.
  4. To revert the change, type your desired price in the box in the listing’s **Price + Shipping column** and click the **Save** button.

#### Multiple listings

**Note:** These changes apply only to the listings displayed on the same or
current page. If your inventory listings span multiple pages, repeat the
process for each page.

  

  1. Select **Manage Pricing** from the Pricing menu.
  2. Optional: Use the Search tool and Filters to narrow the number of listings that display.
  3. Click the checkbox in the heading row of the inventory listings table to select all listings on the page. Review the checked rows and deselect any that you do not want to match to the current lowest price.
  4. Click the **Action on [number] selected** button above the table of listings and select **Match low price** from the drop-down menu.
  5. A confirmation displaying the selected listings will open. Select **Yes, continue**.

The item price in the Price + Shipping column will update to match the total
price in the Lowest Price + Shipping column.

  6. Click **Save all** to complete the price change.
  7. To revert the changes, adjust and Save each listing's price individually, or use [inventory files](/gp/help/1641) to change prices in bulk.

Or

  

  1. Select **Manage All Inventory** from the Inventory menu.
  2. Optional: Use the Search tool and Filters to narrow the number of listings that display.
  3. Click the checkbox in the heading row of the inventory listings table to select all listings on the page. Review the checked rows and deselect any that you do not want to match to the current lowest price.
  4. Click the **Action on [number] selected** button above the table of listings and select **Match low price** from the drop-down menu.
  5. A confirmation displaying the selected listings will open. Select **Yes, continue**.

The item price in the Price + Shipping column will update to match the total
price in the Lowest Price displayed in the Price + Shipping column.

  6. Click **Save all** to complete the price change.
  7. To revert the changes, adjust and Save each listing's price individually, or use [inventory files](/gp/help/1641) to change prices in bulk.

##  Troubleshoot Match Low Price

**Match Low Price** considers all active listings on Amazon, including
products sold by Amazon. However, it might be unavailable for some listings
for any of the following reasons:

  * Your shipping charge is equal to or greater than the lowest price. 
    * For example, you list an item for $1.00 plus $3.00 shipping. Seller B lists the same item for 50 cents plus $2.50 shipping. Your shipping charge alone ($3.00) is equal to Seller B's total cost ($3.00). Therefore, you cannot match the lowest price without first reducing your shipping charges.
  * The listing has an active sale. 
    * **Match Low Price** does not consider offers with active sale events.
    * Either remove the sale or apply **Match Low Price** after the sale ends.
  * The listing does not have a shipping charge. 
    * This might be because your listing is inactive.
    * This is not the same as configuring your pricing settings not to display shipping.

[Shipping settings](/sbr/ref=xx_shipset_dnav_xx#shipping_templates) can also
affect **Match Low Price**

  * If you configured your shipping settings based on price bands, shipping charges will not be displayed and **Match Low Price** will be based only on item price.
  * If you configured your preferences not to display the shipping charge, **Match Low Price** will be based only on item price.

##  How Match Low Price works

This example illustrates more about how **Match Low Price** works.

You have a listing for a product that is in "Used-Like New" condition. The
listing is seller-fulfilled for a price of $26.00 + $5.50 shipping (Listing 2
in the chart below). There are three other listings on Amazon for the same
product. Referring to the chart below, the current lowest price would be
selected as follows:

  * **Listing 1 ($29.00):** Displays if your Low Price Comparison preferences are set to compare offers in all conditions and, all fulfillment methods.
  * **Listing 3 ($29.50):** Displays if your Low Price Comparison preferences are set to compare offers in the same condition and, all fulfillment methods.
  * **Listing 4 ($30.00):** Displays if your Low Price Comparison preferences are set to compare offers in the same sub-condition and same fulfillment method.

Listing | Condition | Sub-condition | Fulfillment Method | Item Price + Shipping | Total Price  
---|---|---|---|---|---  
1 | New | \-- | FBA | $28.00 + $1.00 | $29.00  
2 | Used | Like New | Seller | $26.00 + $5.50 | $31.50  
3 | Used | Very Good | FBA | $24.00 + $5.50 | $29.50  
4 | Used | Like New | Seller | $25.00 + $5.00 | $30.00  
  
##

