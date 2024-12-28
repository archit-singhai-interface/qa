---
title: Stranded inventory report
url: https://sellercentral.amazon.com/help/hub/reference/G201835130
section: General Documentation
---

Stranded inventory is inventory in a fulfillment center that does not have an
active offer on Amazon. Stranded inventory report shows a breakdown of units
in your inventory that are in stranded status.

Inventory can become stranded for many reasons. Amazon provides a **Stranded
reason** column on [Fix stranded
inventory](https://sellercentral.amazon.com/inventoryplanning/stranded-
inventory). This column shows why each listing is stranded. Hovering over the
**Stranded reason** for a listing displays more information and
instructions.For example, the listing for that product might have been
suppressed or might have never been created, resulting in stored inventory
that is accumulating storage fees but cannot be sold because the listing is
not active.

**Important:** Amazon will notify you when you have stranded inventory. If you
do not or cannot create a listing for your stranded inventory, or order its
removal within 30 days of this notice, it will be designated unsellable. You
are required to remove unsellable units, (which are “Unsuitable Units” as
defined in the [Amazon Services Business Solutions Agreement](/gp/help/G1791))
as described in our [Required removals](/gp/help/G202000820) policy.

**Note:** To know about how to get your inventory out of stranded status,
refer to [Resolve stranded inventory issues](/gp/help/GEYJTVJPWRYUTADQ).

## Field definitions

Field name  | Description  
---|---  
**primary-action** | Action needed to bring your inventory out of stranded status. The possible actions are:

  * **Relist** : For products that have been listed previously but do not have an active offer, click **Add a Product** in the **Inventory** drop-down menu to create an offer. If you see a message indicating that your product is already listed but needs to be edited, click the provided link to update your listing.
  * **Create removal order** : For products you no longer want to sell, go to the **Manage FBA Inventory** page, select the product, and choose **Create Removal Order** from the drop-down menu on top.
  * **Change to Fulfilled by Amazon** : If you have an offer, but it is for a product that you fulfill yourself, none of your FBA inventory for that product will be available for sale. On your **Manage Inventory** page, select the product and click **Change to Fulfilled by Amazon** in the **Action** drop-down menu to enable FBA to pick, pack, and ship those products.
  * **Create a new listing** : If you have FBA inventory of a product that has never been listed, create a listing for your SKU by clicking **Add a Product** in the **Inventory** drop-down menu. 

**Note:** When relisting a product or creating a listing, the following
information must match the units in your FBA inventory:

  * ASIN
  * Condition
  * Merchant SKU

If these fields don’t match, the stranded inventory in the fulfillment center
won’t be associated with the new listing.  
**date-stranded** | This date shows how long your inventory has been stranded and without an active offer.  
**date-classified-as-unsellable** | This is the date when the inventory will be classified as unsellable unless the offer is made buyable. You are required to remove unsellable units (which are “Unsuitable Units” as defined in the Amazon Services Business Solutions Agreement) as described in our [Required removals](/gp/help/G202000820) policy.   
**status-primary** | Identifies whether the offer is active, inactive, or incomplete. Incomplete offers are those missing price or condition.  
**status-secondary** | For inactive offers, this field identifies the reasons — for example, blocked or out of stock.   
**error-message** | For select inactive offers, additional information is displayed here — for example, quality alerts.  
**asin** | Unique blocks of 10 letters or numbers that Amazon assigns to identify products. You can find the ASIN on the product details page.  
**sku** | Unique blocks of letters or numbers that you assign to identify your products  
**fnsku** | Unique identifiers that Amazon assigns to items stored in and fulfilled from a fulfillment center  
**product-name** | The name of your product  
**condition** | The condition of your product  
**fulfilled-by** | Indicates whether the product is listed for fulfillment by Amazon or by you.  
**fulfillable-quantity** | The number of units of a SKU that you have in Amazon fulfillment centers and that can be picked, packed, and shipped  
**your-price** | Your current selling price  
**unfulfillable-qty** | The number of units of a SKU that you have in Amazon fulfillment centers and that are in unsellable condition  
**reserved-quantity** | The number of units of a SKU that you have in Amazon fulfillment centers and that are currently being picked, packed, and shipped or that are sidelined for measurement, sampling, or other internal processes  
**inbound-shipped-qty** | The number of units of a SKU that you have shipped to Amazon and that are in transit

