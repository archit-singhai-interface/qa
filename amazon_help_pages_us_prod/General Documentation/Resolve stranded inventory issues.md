---
title: Resolve stranded inventory issues
url: https://sellercentral.amazon.com/help/hub/reference/GEYJTVJPWRYUTADQ
section: General Documentation
---

Amazon provides a **Stranded reason** column on [Fix stranded
inventory](/inventoryplanning/stranded-inventory). This column shows why each
listing is stranded. The **Additional information** column displays more
information and instructions.

See the table below for a list of every **Stranded reason** and **Additional
information** , including recommended actions.

##  Key features on the new Fix stranded inventory page

#### More accurate and up-to-date

Sometimes, a listing shows as **Active** in **Manage inventory** while it
shows as **Stranded** on [Fix stranded inventory](/inventoryplanning/stranded-
inventory). Note that **Fix stranded inventory** has the most accurate and up-
to-date information.

#### "Stranded reason" column

This column gives you information about the stranded inventory. You can also
see more details and what action to take.

#### Filtering by "Stranded reason" and "Recommendations"

These features allow you to sort and better understand why listings are
stranded and what to do to resolve each issue.

#### "Date of stranded event column

This column shows how long your inventory has been stranded while accumulating
storage fees. You can also use the date shown in this column to help locate
email and performance notifications related to the listing.

#### 1-click actions

**1-click relist** allows you to relist with a single click without leaving
the page. If you have to make edits to the listing before activating the
listing, click **Edit listing** or **Relist**.

**1-click change to FBA** allows you to change fulfillment channels with a
single click without leaving the page. This option is only available for
listings where dangerous goods information is provided. A dangerous goods
submission is required for all listings. If you have not previously provided
this information or if you have to change previously provided information,
click **Change to FBA** to change fulfillment channels.

#### Bulk and automatic actions

**Bulk relist** allows you to select up to 25 items to relist at once. After
choosing these items, you can relist all listings at once with **1-click
relist** as the recommended action.

**Note:** When relisting in bulk, you cannot make catalog or listing changes
for any of the affected listings. To edit the listing before activating it,
click **Edit** or **Relist**.

**Bulk 1-click change to FBA** allows you to select 25 items at once to change
fulfillment channels. After choosing these items, you can relist all listings
at once with **1-click change to FBA** as the recommended action.

**Note:** When using **1-click change to FBA** in bulk, you cannot provide or
update dangerous goods information. To provide dangerous goods information,
use **Change to FBA**.

**Automatic relist** automatically relists inventory that has been stranded
for seven days under these stranded reasons:

  * Listing closed
  * Item discontinued

You can adjust this setting by clicking **Edit automatic-action settings**.
For listings that you don't want automatically relisted, select **Opt out of
auto action** in the drop-down arrows to the right of the listing.

**Automatic change to FBA** automatically changes the fulfillment channel to
FBA for inventory that has been stranded for five days under the stranded
reason **Merchant fulfilled**. You can adjust this setting by clicking **Edit
automatic-action settings**. For listings that you don't want changed to FBA,
select **Opt out of auto action** in the drop-down arrows to the right of the
listing.

**Auto-relist** can be set to relist in as little as two days. **Auto-change
to FBA** can change fulfillment channels in less than one day if you set it to
0 days.

**Important:** If you manage expiration dates by stranding inventory, you can
avoid automatic reactivation by setting the **Start selling date/Offer start
date** to strand the inventory until a future time. Automatic actions will not
apply to these listings.

Here are some tips for using automatic actions:

  * You can prevent accidentally stranding inventory via bulk upload templates or APIs. Set the **Auto-change in FBA** settings to 0 or 1 day to make sure that your inventory is quickly unstranded and available for sale.
  * Temporarily close listings for vacation, product evaluation, or religious observance. Close your listings in **Manage inventory** and set auto-relist to have them automatically relisted after the desired number of days.
  * Prevent lost sales when you have to close a listing for a restricted ASIN that will be reinstated. After the listing is reinstated, it stays stranded as a closed listing. Change your **Auto-relist** settings to activate the listing more quickly.

## How to resolve stranded inventory

All sellers are expected to update their stranded auto-removal settings to
remove stranded inventory automatically. Note that if you have an account in
multiple stores, you must configure your auto-removal settings in each store.
If you have designated Amazon to accelerate the removal of stranded inventory,
the units will be removed more quickly.

Stranded reason | Additional information  
---|---  
B2B restricted | This item can only be sold by approved B2B sellers. Create a removal order and delete the listing to remove it from **Manage inventory**.  
Blocked listing |  This ASIN is restricted and not available to sell due to intellectual property concerns, quality issues, or product safety. For specific details, see your email or [Performance notifications](/performance/notifications). You can either file an appeal or create a removal order for this inventory. If you create a removal order, you must also go to the **Manage inventory** page and delete the listing. For more information, go to [Blocked listings](/gp/help/GGGKKCTPTVTF95E5).  
Dangerous goods (in review) | This item is currently under dangerous goods review. You don't have to take any action for this product at this time.  
Dangerous goods (upload documents and wait for review) | Additional information is needed for this product before the dangerous goods review can be completed. Click **Manage dangerous goods** to upload the necessary documents. The Dangerous goods team will review the uploaded documents within two business days, Monday to Friday, excluding public holidays.  
Deleted listing | This listing has been deleted. To activate an offer, select **Create a new listing**.  
Discontinued listing | To resolve this issue, click **Create a new listing** and create a listing with the same ASIN and SKU as your FBA inventory.   
Expired product | This product is past the printed expiration date and cannot be sold. Create a removal order for this inventory.  
Food safety investigation |  This item has been suppressed due to an ongoing safety investigation. In order to relist your product, contact the manufacturer or Intellectual Property owner for applicable product safety testing and compliance documents.  Note that submission of documentation does not guarantee reinstatement.  
Future listing sell date | Your product is not available for sale because the **Start selling date** or **Offer start date** is set to a date in the future. Click **Edit listing** to change the date.  
Inventory under review | This inventory is under customer service review. No action is currently required. There might be additional information in the [Case log](/gp/case-dashboard/lobby.html). If it is determined that your inventory cannot be relisted, you are required to create a removal order.   
Item discontinued | This ASIN violates FBA policy or has chronic damage or defect problems and has been discontinued. You are required to create a removal order. After the removal order is processed, delete the listing from the **Manage inventory** page.  
Item merged | The ASIN or SKU for this listing has been merged with another ASIN. Contact Selling Partner Support for more information.  
Item restricted | This is a restricted item. Create a removal order or contact Selling Partner Support for more details.  
Listing closed | The end date for this listing has passed or the listing has been closed. To activate your listing, click **Relist** , then **Save and finish**.  
Listing error | This listing has an issue with the listing attributes. See [Add one product at a time](/help/hub/reference/G200220550) for information on relisting to correct the listing attributes.  
Miscategorized ASIN | This inventory is listed in the incorrect category. Products should be correctly matched to a category or subcategory. For example, a mobile phone charger should not be categorized as a mobile phone. Sellers are not allowed to categorize items incorrectly to bypass Amazon category restriction processes. Go to the [Change a product’s category](/gp/help/G201950630) tool to make necessary changes.  
Missing price | There is no price for your listing. You must include a price in the **Price** column, or click **Edit** to update your listing.  
Missing SKU | Your inventory is stranded because the FBA and **Manage inventory** SKUs or ASINs for this listing do not match. This might be because your product ID, such as the UPC or ASIN, changed, or because there is no listing in **Manage inventory** for this SKU. One of the steps below might resolve this issue:   

  1. Click **Create new listing**. Set a price, select **I want to ship this item myself to the customer if it sells** , set quantity to "0", then click **Save and finish**. Once finished, click **Change to FBA**. It might take a few minutes between steps and up to 24 hours for the listing to be fully updated.
  2. Delete the listing, then follow Step 2 above.

If these solutions are unsuccessful, contact Selling Partner Support for
assistance.  
Packaging issue | This listing is not certified for Frustration Free Packaging. Create a removal order for this item. After the removal order is processed, delete the product and listing from the **Manage inventory** page.  
Review for quality issues | Your listing has been paused. This might be due to a listing quality issue, such as a pricing error. Review your listing and verify that all information is correct. To resume selling, click **Edit listing** , update the listing, then click **Save and finish**.   
Potential logo misuse | We removed your listing due to potential misuse of trademarked images on the product detail page. To learn more, see [Intellectual Property Policy](/gp/help/G201361070). Click **Edit** to inspect your images and remove or replace the infringing images. If you believe your ASINs were removed in error, you can contact Selling Partner Support with supporting documentation, such as a letter of authorization or licensing agreement.  
Potential high pricing error | Your listing has been paused due to a potential high pricing error. Click ‘Update price’ and update your offer price in accordance to Amazon Marketplace Fair Pricing Policy to reactivate your listing. For more information, go to [Pricing Health warning and error messages](/gp/help/GM665AS5HYKFJB8Z?ignore_selection_changed=true).  
Potential low pricing error | Your listing has been paused due to a potential low pricing error. Click ‘Update price’ and update your offer price in accordance to Amazon Marketplace Fair Pricing Policy to reactivate your listing. For more information, go to [Pricing Health warning and error messages](/gp/help/GM665AS5HYKFJB8Z?ignore_selection_changed=true).  
Potential trademark misuse (self-reinstate) | Your listing was removed due to potential misuse of trademarked terms on the product detail page. If your ASIN improperly uses a trademarked term, click **Edit** to update the product detail page to ensure that you are not engaging in the unauthorized use of any trademarks. Once your product is updated, click **Save and finish** , and it will be automatically reinstated within 24 hours. If no modifications are made, these ASINs will not be reinstated. To learn more about our policies, see [Intellectual Property Policy](/gp/help/G201361070). If you believe your ASINs were removed in error, you can contact Selling Partner Support with supporting documentation, such as a letter of authorization or licensing agreement.  
Product recall | This item has been flagged as a recalled item. In order to relist your product, remove all inventory and request a letter of compliance from the Intellectual Property owner. For more information, go to [Recalled products](/gp/help/G200164750) and [Recalled products FAQ](/gp/help/A67MCULL8TFREGA).  
Product safety investigation |  This item has been suppressed due to an ongoing safety investigation. In order to relist your product, contact the manufacturer or Intellectual Property owner for applicable product safety testing and compliance documents. Note that submission of documentation does not guarantee that the product will be reinstated. For more information, go to [Product safety and compliance](/gp/help/UH6FA4XSJ2LZFLY).  
Product update required | This listing requires a product update. Click **Edit** and update any field except for **Price** or **Quantity**. For example, go to **Keywords** and add a term to the **Subject** field, then click **Save and finish**. It might take a few minutes to update. If this doesn’t work, **Delete the listing** and **Create a new listing** with the same SKU and ASIN.  
Qualification required (brand) | You must be approved to sell this brand. You can request approval by clicking **Edit** and then, **Request approval** if available. If you receive approval, click **Edit** , then **Save and finish** to activate the listing. If the **Request approval** option is not available, or if you are not approved to sell this item, you must create a removal order for the item, then go to the **Manage inventory** page and delete the listing.  
Qualification required (category) | You must be approved to sell items in this category. You can request approval by clicking **Edit** and then, **Request approval** if available. If you receive approval, click **Edit** , then **Save and finish** to activate the listing. If the **Request approval** option is not available, or if you are not approved to sell this item, you must create a removal order for the item, then go to the **Manage inventory** page and delete the listing.  
Qualification required (item) | You must be approved to sell this item. You can request approval by clicking **Edit** and then, **Request approval** if available. If you receive approval, click **Edit** , then **Save and finish** to activate the listing. If the **Request approval** option is not available, or if you are not approved to sell this item, you must create a removal order for the item, then go to the **Manage inventory** page and delete the listing.  
Restricted ASIN |  This restricted ASIN is not available for sale. This may be due to intellectual property infringement, product quality issues, or safety concerns. For details about this ASIN, check your email or your [Performance notifications](/performance/notifications). **Note:** You can file an appeal or create a removal order for this inventory. Once the appeal is approved, you must relist the ASIN to activate your offer. If you process a removal order, delete the listing from the **Manage inventory** page.  
Restricted product ASIN | This ASIN has been identified as a restricted product. If you believe the product should be permitted for sale on Amazon, contact Selling Partner Support and include documentation demonstrating that your account has not violated our policies.  
Restricted program | Item cannot be sold due to a program-level restriction. Create a removal order for this item.  
Review for quality issues | Your listing has been paused. This might be due to a listing quality issue, such as a pricing error. Review your listing and verify that all information is correct. To resume selling, click **Edit listing** , update the listing, then click **Save and finish**.  
Seller-fulfilled | Your inventory is not available for sale because the fulfillment channel is set to**Seller-fulfilled**. To activate the listing, click **Change to FBA**.  
Seller-fulfilled (DG info required) | Your inventory is not available for sale because the fulfillment channel is set to **Seller-fulfilled** , and the ASIN does not have required dangerous goods information. To activate the listing and provide the required information, click **Change to FBA**.   
Trademark misuse | Your listing was removed because you might have used trademarks or patents that you do not have the right to use. Create a removal order or your inventory will be changed to unsellable and disposed of after 30 days. To learn more about our policies, see [Intellectual Property Policy](/gp/help/G201361070). If you believe your ASINs were removed in error, you can contact Selling Partner Support with supporting documentation, such as a letter of authorization or licensing agreement.  
Unexpected inventory received  | We received unexpected inventory in your shipment. To make it available for sale, create a new listing. For additional help, contact Selling Partner Support.  
  
## Bulk fix stranded inventory

If you have large quantities of stranded inventory, you might be able to fix
these issues in bulk.

Use [Bulk Fix Stranded Inventory](/reportcentral/STRANDED_INVENTORY_UI/1) to
update prices or change listings to Fulfilled by Amazon. The tool does not
support actions requiring special documentation, such as an appeal or approval
process. Currently, we cannot support bulk actions for these cases.  

  1. Go to [Bulk Fix Stranded Inventory](/reportcentral/STRANDED_INVENTORY_UI/1) and click **Request Download**. It might take a few minutes for the download to complete. 
  2. When the report is ready, click **Bulk Fix Stranded Inventory** above the page title and open your report in the bottom left corner of the page.
  3. Add any missing attributes, such as **Price** , **ASIN** , **SKU** , and **Condition**.

For more information, see [Bulk Fix Stranded Inventory
Report](/gp/help/201968550).

