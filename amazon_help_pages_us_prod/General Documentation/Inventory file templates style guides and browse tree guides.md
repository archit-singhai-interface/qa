---
title: Inventory file templates, style guides, and browse tree guides
url: https://sellercentral.amazon.com/help/hub/reference/G1641
section: General Documentation
---

**Individual sellers:** This feature is only available to sellers with a
Professional selling plan. Learn more by visiting [Selling plan
comparison](/gp/help/64491).

**Note:** Macros in inventory file templates are no longer supported.

## Overview

An inventory file template is a Microsoft Excel spreadsheet that contains
multiple data columns for describing your products. You can use inventory file
templates to upload and update listings on Amazon.

You can generate customized inventory templates specific to the types of
products you sell. You can also list information for different types of
products across multiple categories in one template. To learn more about
building and uploading your file templates, go to the the following page:

  * [Create your inventory file template](/gp/help/G202094740) using the Search tool or Product Classifier.
  * [Build your inventory file](/gp/help/G581) and learn how to populate and manage your template.

## Search for products and download a pre-filled template

You can search for products that already exist in the Amazon catalog and then
list them using a pre-filled template. Minimal product details are required.

Follow these steps to list your products:  

  1. 1\. Go to **[Add Products](/product-search/bulk/generate/add-offer)** ; choose **Spreadsheet** ; click **Download a blank template** and use **List Products already in Amazon’s catalog** to search using product IDs.
  2. You can search for products using UPCs, EANs, ISBNs, or ASINs. You can enter multiple product IDs separated by a comma, space, or line break. Up to 500 products can be searched at once.
  3. After you click **Generate spreadsheet** , you'll be presented with a pre-filled spreadsheet under the **Downloads template** tab. This will have the details of products that you've searched. 
  4. Verify the products you want to sell and follow these steps:   

    1. If the returned result matches to the product you want to sell, add your offer details and the following information to the corresponding columns in the template:
       * Price 
       * Quantity 
       * Condition
       * Shipping options 
       * Any other optional columns that you want to provide
    2. Repeat the above step for all products in your list. If you don't want to add a particular product, you can either remove it from the list or change the **Action** for the template row to **Ignored**.
    3. Save the list as a tab-separated values (TSV) text file.
    4. Upload the completed spreadsheet by going to **[Add Products](/product-search/bulk/generate/add-offer)** and choosing **Spreadsheet**.
    5. You can check the processing summary for your SKUs by clicking on [Check Upload Status.](/product-search/status).

If you are unable to locate your product in the list, go to **[Add
Products](/product-search/bulk/generate/add-offer)** ; choose **Spreadsheet**
; click **Download a blank template** , to download a product template. You
can use the template to create new products in our catalog using product
attributes.

## Choose a file template

This table provides general guidelines for choosing the best type of inventory
file for your situation.

File type  |  Use case  |  File name  |  More info  |  Video tutorial   
---|---|---|---|---  
Product creation and matching  |  Page does not exist in the Amazon catalog.You have full product information. |  See the **Templates for Specific Categories** section below |  You can also use [UIEE files for Books](/help/hub/reference/G201576580).  |  [How do I fill out a template?](/gp/help/201467230)  
Product matching only  |  Page exists in the Amazon catalog.You do not have full product information. |  [Inventory Loader](https://sellercentral.amazon.com/listing/api/partner/template?feedVariant=inventoryloader&mkid=ATVPDKIKX0DER) |  [Upload inventory using Inventory Loader](/gp/help/201576540/) You can also use the [Listing Loader](/gp/help/201576570). (See discussion below for more information.) |  [ How do I use the Inventory Loader template?](/gp/help/201576540) **Note:** The video tutorial provides general guidance on how to fill out the Inventory Loader template. Actual column headers may vary within the template.  
Inventory updates  | For updates to price or quantity only. | [Price & Quantity](https://sellercentral.amazon.com/listing/api/partner/template?feedVariant=priceandqty&mkid=ATVPDKIKX0DER) |  [Update inventory with the Price and Quantity template](/gp/help/201576480/) |  No video tutorial is available. For more information, see **Update inventory with the Price and Quantity template**.   
See the **Templates for Specific Categories** section below  |  For non-media product files (Books, Music, Video and DVD), use the PartialUpdate option in the **Basic** attribute section in the templates.  |  [ How do I fill out a template?](/gp/help/201467230)  
Update listing data only. | 

  * [Inventory Loader](https://seller-templates.s3.amazonaws.com/xlsx/US/Flat.File.InventoryLoader.us.xlsx)

|  [Upload inventory using Inventory Loader](/gp/help/201576540/). You can also use the [Listing Loader](/gp/help/201576570). |  [ How do I use the Inventory Loader template?](/gp/help/201576540)  
Shipping options  | Update media shipping service options per listing or by using batch file settings.  | 

  * [Inventory Loader](https://sellercentral.amazon.com/listing/api/partner/template?feedVariant=inventoryloader&mkid=ATVPDKIKX0DER)
  * [Book Loader](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.BookLoader.xlsm)
  * [Music Loader](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Music.xlsm)
  * [Video Loader](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Video.xlsm)

|

  * [UIEE files for Books](/help/hub/reference/G201576580) allow batch updates only.
  * See [File Formats for Books, Music, Video and DVD](/help/hub/reference/G201576580).

|  [How do I use the Inventory Loader template?](/gp/help/201576540)  
Change shipping prices for specific products. |  [Shipping Override](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/ff/Flat.File.ShippingOverrides._TTH_.xls) |  [Customize shipping settings with the Shipping Overrides template](/gp/help/201576530/) Shipping overrides are not available for Books, Music, Video and DVD products.  |  [How do I change shipping settings?](/gp/help/13531)  
Product data changes  | Update data contributions to product pages. |  See the **Templates for Specific Categories** section below  |  For single products, use the [Add one product at a time](/gp/help/G200220550) tool.  |  [How do I fill out a template?](/gp/help/201467230)  
Delete product and catalog contributions.  |  Non-media inventory files  |  Use "Delete." |  [How do I fill out a template?](/gp/help/201467230)  
[Inventory Loader](https://sellercentral.amazon.com/listing/api/partner/template?feedVariant=inventoryloader&mkid=ATVPDKIKX0DER) |  Use "x." |  [ How do I use the Inventory Loader template?](/gp/help/201576540)  
  
## Inventory Loader and Listing Loader

The Inventory Loader and Listing Loader are similar templates with slightly
different uses:

  * The Inventory Loader allows you to enter media product (Books, Music, Video and DVD) shipping settings, with optional fields for expedited-shipping and will-ship-internationally.
  * The Listing Loader allows you to enter information for non-media product features, with optional fields such as sale-start-date and is-gift-wrap-available.

For basic matching, we recommend the Inventory Loader, but you can also use
the Listing Loader.

## Use Global SKUs

You can use inventory file templates to upload product data for multiple
countries using your North America unified account. To do so, prepare your
files separately using the browse tree guide and inventory file template for
each country.

Before you upload your file, verify that the **Quantity** value is greater
than 0 (zero) for listings that use a global SKU. If you change the quantity
to 0 (zero) in one country, we will remove the listing from all Amazon North
America countries. If you no longer want to list in a specific country, use
the **delete** field for your template.

When your file is ready to upload, check the website selected in the
**Marketplace Switcher** to make sure you upload inventory files to the
correct website. For more information, see [Share your available
inventory](/gp/help/G200663530).

## Templates, style guides, and BTG for specific categories

Use the following template versions.

File templates | Style guides | Browse Tree Guide (BTG) |  [Approval required](/gp/help/200333160)  
---|---|---|---  
[Automotive & Powersports (Parts & Accessories)](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.AutoAccessory_b2b.xlsm ) [Automotive & Powersports (Tires & Wheels)](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.TiresAndWheels_b2b.xlsm) |  [Automotive & Powersports (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainier/Style_guide_Automotive_Powersports_Final.pdf) [Motorcycles & ATVs (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/Motorcycle_ATV_Style_Guide.pdf) |  [Automotive and Powersports BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/automotive_browse_tree_guide.xls) |  [View requirements](/help/hub/reference/G200584550)  
[Baby](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Baby_b2b.xlsm) |  [Baby (PDF)](https://m.media-amazon.com/images/G/01/01/help/images/Baby.pdf) |  [Baby BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/baby-products_browse_tree_guide.xls) |  No   
[Beauty](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Beauty_b2b.xlsm ) |  [Beauty (PDF)](https://m.media-amazon.com/images/G/01/01/help/images/Beauty.pdf) |  [Beauty BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/beauty_browse_tree_guide.xls) |   
[Books](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.BookLoader_b2b.xlsm) |  [Use Book Loader](/help/hub/reference/G200390640) [Use UIEE Format to List Books](/gp/help/201576610) |  [Books BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/books_browse_tree_guide.xls) |  For Books, approval is required only for listing in "Collectible" condition.   
[Camera & Photo](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.CameraAndPhoto_b2b.xlsm) |  See Consumer Electronics.  |  See Consumer Electronics.  |  No   
[Cell Phones & Accessories (Wireless)](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Wireless_b2b.xlsm) |  See Consumer Electronics.  |  [Cell Phone & Accessories BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/cell-phones_browse_tree_guide.xls) |  No   
[Clothing & Accessories](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Clothing_b2b.xlsm) |  [Clothing & Accessories (PDF)](https://m.media-amazon.com/images/G/01/AMAZON_FASHION/ClothingStyleGuide.pdf) |  [Clothing & Accessories BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/fashion_browse_tree_guide.xls) |  No   
[Collectible Coins](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Coins_b2b.xlsm) |  [Collectible Coins (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainier/CoinsStyleGuide._V336345069_.pdf) |  There is no separate BTG available for this category.  |  [View requirements](/gp/help/201526800)  
[Computers](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Computers_b2b.xlsm) |  See Consumer Electronics.  |  See Consumer Electronics.  |  No   
[Consumer Electronics](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.ConsumerElectronics_b2b.xlsm) |  [Consumer Electronics (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/CEStyleGuide.pdf) [Consumer Electronics Store Style Guide](/gp/help/200288470) |  [Consumer Electronics BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/electronics_browse_tree_guide.xls) |  No   
[Entertainment Collectibles ](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.EntertainmentCollectibles_b2b.xlsm) |  [Entertainment Collectibles (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/EntertainmentCollectiblesStyleGuide.pdf) | BTG available upon approval to sell in this category.  |  [View requirements](/gp/help/200944120)  
Eyewear (See [Clothing & Accessories](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Clothing_b2b.xlsm))  |  [Eyewear](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/Eyewear_Style_Guide.pdf) |  [Clothing & Accessories BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/fashion_browse_tree_guide.xls) |  No   
Fine Art - Inventory File Template available upon approval to sell in this category.  |  [Fine Art (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/FineArtStyleGuide.pdf) |  BTG available upon approval to sell in this category.  |  [View requirements](/gp/help/201257400)  
[Gift Cards](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.GiftCards_b2b.xlsm) |  [Gift Cards (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainier/GiftCardStyleGuide512.pdf) |  BTG available upon approval to sell in this category.  |   
[Grocery & Gourmet Food](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.FoodAndBeverages_b2b.xlsm) |  [Grocery & Gourmet Food (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/SellerCentral/GroceryStyleGuide.pdf) |  [Grocery & Gourmet Food BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/grocery_browse_tree_guide._TTH_.xls) |  [View requirements](/gp/help/201511970)  
[Health & Personal Care](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Health_b2b.xlsm) |  [Health & Personal Care (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/SellerCentral/HPCStyleGuide.pdf) |  [Health & Personal Care BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/health_browse_tree_guide.xls) |  No  
[Home, Home Decor, Kitchen & Garden Furniture](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Home_b2b.xlsm) | [Furniture Home Kitchen (PDF)](https://m.media-amazon.com/images/G/01/Home_Image_Guide/Home_SG_Q3-2020_-_Draft_Finalized_-_seller_facing_-_1218.pdf) |  [Home & Kitchen BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/home-kitchen_browse_tree_guide._TTH_.xls) [Patio, Lawn & Garden BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/garden_browse_tree_guide.xls) [Arts, Crafts & Sewing BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/arts-and-crafts_browse_tree_guide._TTH_.xls) |  No   
[Industrial & Scientific (Fasteners)](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.MechanicalFasteners_b2b.xlsm) Industrial & Scientific (Food Service and Janitorial, Sanitation, & Safety) [Industrial & Scientific (Lab & Scientific Supplies)](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.LabSupplies_b2b.xlsm) [Industrial & Scientific (Power Transmission)](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.PowerTransmission_b2b.xlsm) [Industrial & Scientific (Raw Materials)](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.RawMaterials_b2b.xlsm) [Industrial & Scientific (Industrial and Other)](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Industrial_b2b.xlsm) |  [Industrial & Scientific (PDF)](https://m.media-amazon.com/images/G/01/01/help/images/Industrial__Scientific.pdf) |  [Industrial & Scientific BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/industrial_browse_tree_guide._TTH_.xls) |  [Selling Guidelines](/gp/help/201847780)  
[Jewelry](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Jewelry_b2b.xlsm) |  [Jewelry (PDF)](https://m.media-amazon.com/images/G/01/01/help/images/Jewelry.pdf) |  [Jewelry BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/jewelry_browse_tree_guide.xls) |  [View requirements](/gp/help/200332590)  
[Lighting](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Lighting_b2b.xlsm) |  [Lighting (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/LightingStyleGuide.pdf) |  See Tools & Home Improvement.  |  No   
[Luggage & Travel Accessories](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Clothing_b2b.xlsm) |  [Luggage & Travel Accessories](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/Luggage_Style_Guide.pdf) |  There is no separate BTG available for this category.  |   
Motorcycles & ATVs (See Automotive Parts & Accessories)  |  |  |  [View requirements](/help/hub/reference/G200584550)  
[Music](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Music_b2b.xlsm) |  [Music Loader Instructions](/help/hub/reference/G201576580) |  There is no separate BTG available for this category.  |  [View requirements ](/help/hub/reference/202188990)  
[Musical Instruments](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.MusicalInstruments_b2b.xlsm) |  See Consumer Electronics.  |  [Musical Instruments BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/musical-instruments_browse_tree_guide._TTH_.xls) |  No   
[Office Products](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Office_b2b.xlsm) |  See Consumer Electronics.  |  [Office Products BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/office-products_browse_tree_guide.xls) |  No   
[Outdoors (Outdoor Gear, Outdoor Sports Apparel, Cycling, and Action Sports)](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Outdoors_b2b.xlsm) |  [Outdoors (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainer/help/sportinggoods_style_guide.pdf) |  [Outdoors BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/sporting-goods_browse_tree_guide._TTH_.xls) |  No   
[Pet Supplies](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.PetSupplies_b2b.xlsm) |  [Home, Garden & Pets (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/help/Pets-Style_Guide.pdf) |  [Pet Supplies BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/pet-supplies_browse_tree_guide.xls) |  No   
[Shoes, Handbags & Sunglasses](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Shoes_b2b.xlsm) |  [Handbags](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/Handbags_Style_Guide.pdf) [Shoes & Accessories (PDF)](https://m.media-amazon.com/images/G/01/AMAZON_FASHION/SHOES/Shoes_StyleGuide.pdf) |  [Clothing & Accessories BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/fashion_browse_tree_guide.xls) |   
[Software & Video Games](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.SoftwareVideoGames_b2b.xlsm) |  [Software & Video Games](/help/hub/reference/G200390640) |  [Software BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/software_browse_tree_guide.xls) [Video Games BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/videogames_browse_tree_guide.xls) |  [View requirements ](/help/hub/reference/GP9BGQD68HQ5V4YF)  
[Sports (Exercise & Fitness, Hunting Accessories, Team Sports, Licensed Fan Shop, Athletic Apparel, Boating & Fishing, and Game Room)](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Sports_b2b.xlsm) |  [Sports (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainer/help/sportinggoods_style_guide.pdf) [Selling Sports Apparel](/gp/help/200626260) |  [Sports BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/sporting-goods_browse_tree_guide._TTH_.xls) |  No   
[Sports Collectibles](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.SportsMemorabilia_b2b.xlsm) [Trading Cards](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.TradingCards_b2b.xlsm) |  [Sports Collectibles](/gp/help/200800780) |  BTG available upon approval to sell in this category.  |  [View requirements](/gp/help/200800780)  
[Tools & Home Improvement](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.HomeImprovement_b2b.xlsm) |  [Tools & Home Improvement (PDF)](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/ToolsAndHomeImprovement_StyleGuide.pdf) [Reconditioned Tools & Hardware](/help/hub/reference/G200390640) |  [Tools & Home Improvement BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/home-improvement_browse_tree_guide.xls) |  No   
[Toys & Games](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Toys_b2b.xlsm) |  No specific style guide  |  [Toys & Games BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/toys-and-games_browse_tree_guide.xls) |  No   
[Video & DVD](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Video_b2b.xlsm) |  [Video Loader Instructions](/help/hub/reference/G200482410) |  There is no separate BTG available for this category.  |  [View requirements](/help/hub/reference/202188990)  
[Watches](https://s3.amazonaws.com/category-custom-templates/ff/na/us/Flat.File.Watches_b2b.xlsm) |  [Watches (PDF)](https://m.media-amazon.com/images/G/01/01/help/images/Watches.pdf) |  [Watches BTG](https://images-na.ssl-images-amazon.com/images/G/01/rainier/help/btg/watches_browse_tree_guide.xls) |   
  
## Troubleshooting

If you encounter a processing error after trying to upload your inventory file
templates, see the following pages to identify a solution:

  * [Review a Processing Report](/gp/help/G200194300)
  * [Review my inventory results](/gp/help/G611)
  * [Inventory file upload FAQ](/gp/help/G201201070)
  * [Error code explanations](/gp/help/G17781)

