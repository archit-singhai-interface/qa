---
title: Create parent-child relationships
url: https://sellercentral.amazon.com/help/hub/reference/G202135320
section: General Documentation
---

When you create parent-child relationships between products, you help
customers find different versions of the product they are viewing. To create a
parent-child relationship between products, you can use the [Add
Products](/product-search) tool or you can use product templates with [Add
Products via Upload](/listing).

**Note:** The option for creating variations using product templates is not
available to sellers with an Individual Selling Plan. Professional sellers can
avail both the option of **Add Products** and **Add Products via Upload**
(using product templates).

When creating parent-child relationships:

  * Do not include price and quantity values for parent products, as parent products are placeholders to establish relationships with child products and are not displayed on detail page. Including price and quantity for parent products would result into errors and can cause your products to disappear from the catalog.
  * Provide values to all child product’s attributes to describe and differentiate them with other child products.
  * Ensure that **Product Type** is consistent across all child SKUs and the parent SKU of the variation family being created.
  * Follow the recommendations in the [Product page style guides](/gp/help/G200270100) for each child SKU.

You can view the existing child ASINs for parent ASINs on the **Manage All
Inventory** page under the **Inventory** link in your seller account. If your
product is not in the Amazon catalog, you have to create a new ASIN. For more
information, go to [ASIN creation policy](/gp/help/G201844590).

## Create variations using Add Products

The **Add Products** tool offers the option to create variations, using a web-
based interface. Before you list a product variation, check whether the
variation of the product already exists in the Amazon catalog. To do this, go
to **Catalog** , and select **Add Products**. Search for the product variation
you want to sell. Results are more accurate if you search by product
identifiers (UPC, EAN, JAN, or ISBN).

To understand whether your products are good candidates for variation or not
and to get specific tips for creating variations, refer to [Determine
variations for your products](/gp/help/G201958220) and [Variation Relationship
FAQ](/gp/help/G201951410).

Based on the search results, there are two ways that you can use **Add
Products** to create variations:

  * Match your product variation to an existing variation listing: If you find the variation listing that corresponds to the product you want to list, you can match it to this existing variation listing 
  * Create a new variation listing: If you cannot find an existing variation listing that matches your product variation, you can create a new variation.

## Product templates: special considerations

There are a few special things to consider when you use product templates to
update, modify, or delete your inventory.

  * A child SKU cannot be assigned a new parent-SKU value without first removing the relationship to its original parent item. To remove the relationship, you can delete either the parent SKU or the child SKU.
  * When you delete a parent SKU, you remove the relationship between that parent SKU and all of its child SKUs. When you delete a child SKU, you only eliminate the relationship between that child SKU and its parent SKU.
  * After the original relationship is removed, you can re-assign the child item to a new parent item by entering that parent item's SKU in the child item's parent-SKU field.

## Setting up a parent-child relationship in the product template

The following table shows how you might use a product template to set up a
parent-child relationship for several t-shirts that come in 3 sizes and 2
colors.

**Note:**

  * The exact column headings in your product template might differ. Refer to the "Data Definitions" tab in your product template for the specific columns you use to establish relationships.
  * Some attribute fields in your template can be noted as optional, but they are required to describe your child SKUs accurately in relation to parent products.
  * The **variation theme** column indicates that products in this particular parent-child relationship differ from each other based on both color and size. The "Data Definitions" tab in the product template lists the terms you can use for variation themes. Amazon will remove product listings that do not correctly use established variation themes.
  * Use only SKUs for building variation relationships.
  * Do not include price and quantity values for parent products, as parent products are placeholders to establish relationships with child products and are not displayed on detail page. Including price and quantity for parent products would result into errors and can cause your products to disappear from the catalog.
  * When you list your child SKUs, completely describe each child SKU and include data for all of the variation attributes of the parent product, so that they are included in browse and search results and on product detail pages.
  * Ensure that **Product Type** is consistent across all child SKUs and the parent SKU of the variation family being created.
  * Follow the recommendations in the [Product page style guides](/gp/help/G200270100) when determining the variation attributes to use for each child SKU.

**Example** SKU  |  Title  | Size  | Color  | Parentage  | Parent SKU  | Relationship type  | Variation theme  | Price  | Quantity   
---|---|---|---|---|---|---|---|---|---  
101  |  T-Shirt  |  |  |  parent  |  |  |  SizeColor  |  |   
101MB  |  Royal Blue T-Shirt M  |  Medium  |  Royal Blue  |  child  |  101  |  variation  |  SizeColor  |  15.97  |  50   
101SB  |  Royal Blue T-Shirt S  |  Small  |  Royal Blue  |  child  |  101  |  variation  |  SizeColor  |  15.97  |  50   
101LB  |  Royal Blue T-Shirt L  |  Large  |  Royal Blue  |  child  |  101  |  variation  |  SizeColor  |  17.97  |  50   
101MR  |  English Red T-Shirt M  |  Medium  |  English Cherry Red  |  child  |  101  |  variation  |  SizeColor  |  15.97  |  50   
101SR  |  English Red T-Shirt S  |  Small  |  English Cherry Red  |  child  |  101 |  variation  |  SizeColor  |  15.97  |  50   
101LR  |  English Red T-Shirt L  |  Large  |  English Cherry Red  |  child  |  101  |  variation  |  SizeColor  |  17.97  |  50   
  
In the example above, SKU: 101 with "T-Shirt" is the parent product. Because
parent products are not offered for sale, fields such as size, color, price,
and quantity are irrelevant and should not be provided.

However, still describe other aspects of the parent product, including an
image that represents the generalized product. The only information to omit
relates specifically to price, availability, and shipping.

## Use XML for parent-child relationships

You can use XML uploads instead of product templates to create relationships
between products.

For more information go to [Establish product relationships - relationship
feed schema](/gp/help/G200386850).

## Delete parent-child relationships

For information about deleting relationships between products, see **Special
consideration** section under [Modify your inventory
file](/gp/help/G201576660).

## Best practices

For information about best practices to follow, go to [Variation
relationships](/gp/help/G8831).

## See also:

  * [About parent-child relationships](/gp/help/8841)
  * [Variation relationships overview](/gp/help/G8831)
  * [How variations appear on product detail pages](/gp/help/G202135360)
  * [Variation relationship FAQ](/gp/help/G201951410)
  * [How do I create variations?](/gp/help/UHKMBQ56WGQX9MM)

