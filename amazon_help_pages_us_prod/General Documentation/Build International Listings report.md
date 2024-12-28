---
title: Build International Listings report
url: https://sellercentral.amazon.com/help/hub/reference/G202121620
section: General Documentation
---

The Build International Listings report is a snapshot of your source
marketplace offers that you can use to review and understand the connection
results in all connected target marketplaces.

If you have a second source marketplace, a separate report is available for
each source marketplace.

With the report, you can see the following:

  * Status of your source marketplace offers
  * Status of your target marketplace offers
  * Pricing data for source and target marketplace offers (list price and sale price)
  * Reasons why a source marketplace offer was not created or synchronized to target marketplaces
  * Recommendations for resolving the reason why an offer was not created or synchronized to the target marketplaces

**Note:** The report is available only if you have an active Build
International Listings connection between a source marketplace and at least
one target marketplace.

The report is generated automatically for the following events:

  * A new Build International Listings connection is created.
  * A new target marketplace is added to an existing connection.
  * Existing target marketplace connection settings are edited.
  * An existing marketplace connection is removed.
  * The exclusion list for a target marketplace is edited.

You can generate an updated report at any time.

## Accessing and generating a report

Follow these steps to get a Build International Listings report:

  

  1. Go to the [Build International Listings](/global-selling/listings/connect?ref_=ag_agsBGB_snav_agsLand) tool.
  2. Click **Generate report** on the **Status report** widget at the top right of the page.

**Note:** If you have set up a second source marketplace, use the marketplace
switcher at the top of the page to select the source marketplace for which you
want a report.

  3. Wait for the new report to be generated. You may need to refresh the page after a couple of minutes.
  4. Click the **Download** button next to the report you want to see.

## Data available for the Status report

The following table provides an overview of the data available in the Status
report.

Download column  |  Description  |  Example   
---|---|---  
Synchronization Date | The most recent date on which the source offer was synchronized with the target offer | Dec 10, 2016 12:12 p.m.  
Seller SKU | Your item identifier | EE-D-001-10  
ASIN | Amazon Standard Identification Numbers (ASINs) are unique blocks of 10 letters or numbers that identify products. Amazon assigns ASINs. You can find the ASIN on the product detail page. | B01EEV97IE  
Product Name (Source Marketplace) | The product name in the source marketplace language | Water bottle (12 oz)  
Product Name (Target Marketplace) | The product name in the target marketplace language | Wasserflasche (12 oz)  
Target Marketplace | The target marketplace for the offer | Amazon.de  
Target Marketplace Listing Price | The list price in the target marketplace based on the price rule and currency exchange rate | €10.50  
Target Marketplace Listing Currency | The currency in the target marketplace | Euro  
Synchronization Status | The synchronization status between the source and target marketplaces | Complete  
Reason | The reason why a source marketplace offer could not be created or synchronized to a target marketplace | See examples in table below  
Recommended Next Step | Suggested steps to take to resolve the reason why an offer could not be created or synchronized to a target marketplace | See examples in table below  
Target Marketplace Sale Price | The sale price in the target marketplace based on the price rule and currency exchange rate | €8.40  
Target Marketplace Sale Start Date | The date the offer starts using the sale price | Oct 9, 2016  
Target Marketplace Sale End Date | The date the offer stops using of sale price | Dec 31, 2016  
  
The following table provides an overview of the sync status reasons and next
steps used in the Status report.

Target synchronization status | Synchronization status reason | Next steps  
---|---|---  
Not Synchronized | You are blocked or suspended from selling in the target marketplace. | Refer to the target marketplace in Seller Central for details about a block or suspension. Contact Seller Support if necessary to resolve an issue.  
Not Synchronized | A detail page for this ASIN does not exist in this marketplace. |  To solve this issue, create this ASIN in your target marketplace in the appropriate language. The ASIN will be excluded at the time of creation. Use **Build International Listings** >**Reconnect Offers** to remove the exclusion, and the offer will be connected and synchronized if eligible.  
Not Synchronized | An offer is not active in the source marketplace. | Only active offers are synchronized. Make an offer active in the source marketplace and it will connect and synchronize if eligible.  
Not Synchronized | The condition is supported, but the note cannot be translated. | Remove the condition note from the offer.  
Not Synchronized | The SKU is excluded for connection and synchronization in this marketplace. This may be the result of changes made to the offer in the target marketplace. | See the list of excluded SKUs and reconnect them on the **Reconnect Offers** tab on the **Build International Listings** page.  
Not Synchronized | This is a restricted product, and approval is required to list it. | Request approval to sell products with offer limitations. You can submit a request at **Inventory** >**Add a Product** >**Selling application status**.  
Not Synchronized | Internal error | An internal error occurred. Contact Seller Support for help.  
Not Synchronized | Cannot create offers for legal or product-compliance reasons. | Refer to the Seller Central help topic for restricted products.  
Not Synchronized | Only "New" offers were selected for connection and synchronization in this marketplace. | If you selected "New" offers, edit the connection for the target marketplace and change the **Offer Type** to "New and Used."  
Not Synchronized | Only "Self-fulfilled" offers were selected to be connected and synchronized, or "Used" products are not eligible to be sold in this marketplace. | Edit the connection for the target marketplace and change the fulfillment type to "FBA and Self-Fulfilled."  
Not Synchronized | Only "FBA" offers were selected to be connected and synchronized in this marketplace. | Edit the connection for the target marketplace and change the fulfillment type to "FBA and Self-Fulfilled."  
Disconnected | FBA offers were not deleted to prevent stranded inventory in target marketplace fulfillment centers. | You can allow the inventory to be sold out, returned to you, or disposed of. You can manage these options in the target marketplace on your **Manage FBA Inventory** page.  
Disconnected | FBA offers were not deleted to prevent stranded inventory due to a sale in the last 60 days, subjecting it to possible return actions. | You can delete an offer 60 days after the last sale using the **Manage Inventory** page.  
Disconnected | FBA offers were not deleted to prevent stranded inventory due to inventory in transit to target marketplace fulfillment centers. | You can allow the inventory to be received and sold out, returned to you, or disposed of. You can manage these options in the target marketplace on your **Manage FBA Inventory** page.

