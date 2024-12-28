---
title: Dimensional weight
url: https://sellercentral.amazon.com/help/hub/reference/G53Z9EKF8VVZVH29
section: General Documentation
---

**Definition** | Dimensional weight is a calculation of the volumetric weight of a package, using the package’s length, width, and height.   
---|---  
**Using this article** | Dimensional weight is used to determine your item’s product size tier and shipping weight in certain instances. After reading this article, you'll be able to determine whether dimensional weight is used to calculate fees for your item and how to calculate the dimensional weight for your product. To accomplish these tasks, first know the unit weight, product volume, and product dimensions.  
**Fees that use this attribute** |  [FBA fulfillment fees](/gp/help/GPDC3KPYAGDTVDJP) [FBA removal order fees](/gp/help/G9W7FVTLY343ZBKN) [FBA disposal order fees](/gp/help/G5FKTA8LXU4TZPD5) [Fulfillment fees for Multi-Channel Fulfillment orders](/gp/help/201112650) [FBA inbound placement service fees](/gp/help/GC3Q44PBK8BXQW3Z)  
**Related terms and articles** |  [Product dimensions and volume](/gp/help/G37G73BJXHF75ACH) [Shipping weight](/gp/help/GEVWP48HPBLEFJEY) [Product size tier](/gp/help/GG5KW835AHDJCH8W) [Unit weight](/gp/help/GE3VC5FGJE9TYJKM) [FBA fees reimbursement policy: Weight and dimensions](/gp/help/GL7U4JFSDXUTQAJ)  
  
## Determine if dimensional weight is used to calculate fees

Dimensional weight is calculated using your item package’s dimensions. For
more information, go to the **Calculate dimensional weight** section below.

A **small standard-size** item meets all of the following criteria when fully
packaged:

  * Unit weight is less than or equal to 1 lb
  * Longest side (length) is less than or equal to 15 inches
  * Median side (width) is less than or equal to 12 inches
  * Shortest side (height) is less than or equal to 0.75 inches

A **large standard-size** item is not **small standard-size** and meets all of
the following criteria when fully packaged:

  * Greater of unit or dimensional weight is less than or equal to 20 lb
  * Longest side (length) is less than or equal to 18 inches
  * Median side (width) is less than or equal to 14 inches
  * Shortest side (height) is less than or equal to 8 inches

From now through February 4, 2024, items that don’t meet the **standard-size**
criteria indicated above are considered **oversize**.

A **special oversize** tier applies to products that must be delivered using
special delivery options due to their size, weight, special handling
requirements, or other restrictions. Products are classified and charged as
special oversize if any of the following applies:

  * Greater of unit or dimensional weight is more than 150 lb
  * Longest side (length) is greater than 108 inches
  * Girth plus length is greater than 165 inches. To calculate girth plus length:
    * Measure the length, height, and width of the packaged unit.
    * Calculate the girth by adding the shortest and median sides and multiplying by 2.
    * Add the longest side and girth.
  * Product requires special handling
  * If your oversize item didn’t meet any of these criteria, the item isn’t special oversize and the greater of dimensional weight or unit weight is used to calculate fees. If it met all of the criteria, the item is considered special oversize, and only unit weight is used instead to calculate fees.

Starting on February 5, 2024, we’ll introduce the **large bulky size tier**
and **extra-large size tiers** to replace the **oversize size tiers**. A
**large bulky-size** item is not **small standard-size** , is not **large
standard-size,** and meets all of the following criteria when fully packaged:

  * Greater of unit or dimensional weight is less than or equal to 50 lb
  * Longest side (length) is less than or equal to 59 inches
  * Median side (width) is less than or equal to 33 inches
  * Shortest side (height) is less than or equal to 33 inches
  * Girth plus length is less than or equal to 130 inches

Starting on February 5, 2024, items that exceed the limits for **large bulky-
size** are considered **extra-large** , which require using special delivery
options due to their size, weight, special handling requirements, or other
restrictions.

## Calculate dimensional weight

The dimensional weight is equal to the unit volume (length x width x height)
divided by 139. The dimensional weight for oversize, large bulky, and extra-
large items assume a minimum width and height of 2 inches.

**Important:** If an FBA product is sold as a set, the weight and dimensions
used are the weight and dimensions of the set packaged together. For Multi-
Channel Fulfillment, the dimensional weight is calculated for all large
standard, oversize (except special oversize), large bulky, and extra-large
items (except for extra-large 150+ lb).

You can look up product dimensions for your existing FBA inventory using the
[Monthly Storage Fees report](/reportcentral/STORAGE_FEE_CHARGES/1).

To look up dimensions:  

  1. Download the report.
  2. Identify the product of interested by its FNSKU.
  3. View the product dimensions on the **longest-side** , **median-side** , and **shortest-side** fields.
  4. Use the formula above to calculate the product volume and convert to dimensional weight.

For products that are already being sold in Amazon stores but you do not sell,
you can look up the product dimensions to calculate volume by using the
[Revenue calculator](/fba/profitabilitycalculator/index).

To calculate the volume:  

  1. Search for the product of interest.
  2. View the **Package Dimensions** values.
  3. Use the formula above to calculate the product volume and convert to dimensional weight.

For products you currently have in FBA inventory, you can look up the size
tier using the [Fee Preview](/reportcentral/ESTIMATED_FBA_FEES/1) report.

To look up the size tier:  

  1. Download the report.
  2. Identify the product of interested by its FNSKU.
  3. View the product size tier in the **product-size-tier** field.

**Note:** Amazon may verify the weight and dimensions of a product using
representative samples. Amazon’s information about a product’s weight and
dimensions will be used to calculate fees if there is a difference between
Amazon’s information and a seller’s information. Amazon may change its
information about a product’s weight and dimensions from time to time to
reflect updated measurements. Fees based on the weight and dimensions of a
product are calculated using Amazon’s information about the weight and
dimensions of that product at the time the fee is calculated.

## Dimensional weight example

Dimensional weight with a 2-inch minimum  
---  
![](https://m.media-amazon.com/images/G/01/fba-help/fees//Whiteboard_v2._CB1555700111_.png) | **White dry erase board** Dimensions: 40 x 1 x 25 inches Unit weight: 4.5 lb Dimensional weight: 14.4 lb, 2-inch minimum applied (40 x 2 x 25 inches, divided by 139) 2023: Item is oversized, but not special oversized, so dimensional weight is used for fee calculations. 2024: Item is large bulky, so dimensional weight is used for fee calculations.  
  
## Frequently asked questions

#### How is [unit weight](/gp/help/GE3VC5FGJE9TYJKM) different from
dimensional weight?

Unit weight is the scale weight of the product when fully packaged.
Dimensional weight is an estimate of what the weight will be based on the
product’s dimensions. Depending on the size tier of the product, either the
unit weight or the dimensional weight will be used to calculate the shipping
weight. For more information, go to [Shipping
weight](/gp/help/GEVWP48HPBLEFJEY).

