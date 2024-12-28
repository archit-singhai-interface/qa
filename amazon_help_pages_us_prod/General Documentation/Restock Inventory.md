---
title: Restock Inventory
url: https://sellercentral.amazon.com/help/hub/reference/G201634550
section: General Documentation
---

The [Restock Inventory](/restockinventory/recommendations) tool helps you plan
how much inventory to send to Amazon fulfillment centers and when to send it.
Recommendations show in these columns: **Recommended replenishment QTY** and
**Recommended ship date.**

The tool takes into account your sales history, demand forecast and
seasonality, and replenishment settings. By customizing your replenishment
settings, you can optimize factors such as lead time, case pack quantity,
replenishment frequency, and supply chain settings.

Although you’re not required to use the replenishment and ship-by
recommendations, we encourage you to follow them. You can create shipments on
Restock Inventory as you would on any other inventory page.

For more information, watch [What Is the FBA Restock
Tool?](/learn/courses?ref_=selleru_athena&courseId=8&moduleId=c695d4ec-e65c-4d40-a993-102507e3d6bc&modLanguage=English&contentType=VIDEO&category=TUTORIAL&videoPlayer=airy)

## Customizing your replenishment settings

To customize your replenishment settings for an individual SKU, do the
following:  

  1. On Restock Inventory, select the SKU.
  2. In the **Action** column to the right, select **Customize SKU settings**. The SKU details page will open.
  3. Adjust your replenishment settings.

To customize your replenishment settings for multiple SKUs, do the following:  

  1. On Restock Inventory, click **Customize SKU settings** at the top right of the page.
  2. On **Inventory product settings** , click **Generate report**.
  3. Under **Report status** , click **Download** after the report is complete.
  4. Open the report as a text file (Notepad on Windows computers).*
  5. Select all the text and copy it.
  6. Create an Excel file, click on the first cell in the upper left corner, and paste in the copied content.
  7. Adjust your replenishment settings, then save the file.
  8. Upload the spreadsheet by clicking **Upload file**.

*If Excel is an option for opening the report after you click **Download** , skip steps 5 and 6.

## Frequently asked questions

#### Why does Amazon generate restock recommendations?

Good inventory management can be challenging because the right amount of stock
varies based on future demand and the cost of carrying too much or too little
inventory.

Based on the information that you provide and estimates of future demand, we
suggest a replenishment quantity and ship date for your products. The
recommendations are intended to provide you with information that you can use
to balance the cost of running out of stock (lost sales) vs. the cost of
carrying too much inventory (capital costs and storage fees).

#### I want to keep my supplier’s name private. Am I required to enter the
supplier’s name?

No. You can enter a nickname or code to represent your suppliers. Your restock
recommendations won’t be affected.

#### How do I flag ASINs as not replenishable?

To indicate that a SKU is not replenishable, do the following:  

  1. On Restock Inventory, select the ASIN or ASINs that are not replenishable.
  2. In the **Action** column to the right for each ASIN, select **Hide recommendation**. By hiding all SKUs that are associated with an ASIN, you exclude the ASIN from your in-stock rate and estimated lost sales.

Note that hiding replenishable SKUs is not an effective way to increase your
Inventory Performance Index (IPI) score for the following reasons:

  * Hidden SKUs don’t change your IPI score. 
  * The SKUs that you hide will no longer show restock recommendations.
  * Inaccurate FBA inventory settings may cause you to miss valuable restock opportunities. 

## Glossary

#### Days of supply

The estimated number of days your current inventory supply will last based on
the projected demand for your product.

####  Estimated shipment value amount

The estimated value of the inventory that you're restocking for a particular
product from your supplier. It’s calculated by multiplying your recommended
replenishment quantity with your cost of purchase.

#### Low stock

This alert identifies items for which the days of supply is less than the lead
time. Low stock indicates that replenishment shipments may have to be
expedited so that the item doesn’t go out of stock.

#### Out of stock

This alert shows for items that are no longer in your inventory.

#### Recommended ship date

The recommended ship date helps you avoid low- or out-of-stock scenarios,
based on your estimated days of supply and lead time.

#### Recommended replenishment quantity

The recommendation for the number of units to be restocked for FBA.

#### Replenish settings

Enter information in these fields to fine-tune the recommendations for your
business.

  * **Cost of purchase** is the per-unit cost that you pay to order the specified product from your supplier. 
  * **Per-unit variable costs** is the additional per-unit cost that you pay, not including Amazon fees (for example, shipping cost per unit). 
  * **Supply chain setting** indicates how your supply chain is configured for the specified product so that we can calculate the appropriate lead time. Select one of these three choices:
    * **Supplier ships directly to Amazon** indicates that the product is directly shipped from your supplier to Amazon. When you select this supply-chain type, only supplier lead time will be used recommendations. 
    * **Supplier ships to your facility, and then you ship the same amount to Amazon** indicates that the full order for the product is shipped from your supplier, then prepped before sending to Amazon. When you select this supply-chain type, **supplier lead time plus seller lead time** will be used for recommendations. 
    * **Supplier ships supply in bulk to your facility, then you ship units to Amazon as needed** indicates that you typically store inventory for this product at your facility and replenish to Amazon directly from that facility. When you select this supply-chain type, only seller lead time will be used for recommendations. 
  * **Your lead time** is the number of weeks that are required for you to ship a product from your facility to Amazon.
  * **Supplier lead time** is the amount of time needed for your supplier to deliver a product to your facility.
  * **Replenishment frequency** is the frequency at which you typically replenish the specified product. 
  * **Case pack quantity** , also known as order multiple, is the number of sellable units per case or box that is ordered from your supplier. 
  * **Minimum replenishment quantity** is the minimum number of units that you send when restocking FBA inventory.

#### Sales (last 30 days)

The value for the total shipped units of this SKU in the last 30 days. The
units shipped data is refreshed daily.

