---
title: Amazon Bulk Services: Creating a package hierarchy
url: https://sellercentral.amazon.com/help/hub/reference/GQ4S7SV9K4GXH3WX
section: General Documentation
---

## Create a package hierarchy

Before you get started, identify products for which you sell or want to sell 2
or more package configurations: unit, case pack, or pallet. For example, if
you sell a box of 10 pens (unit) and a case of 10 boxes (case pack) or you
sell a box of 10 pens (unit) and want to sell a pallet with 100 boxes, you can
use package hierarchy to link those configurations. Note that selling a pallet
is not a must to participate. As long as you offer 2 or more package
configurations, package hierarchy is available to you.

Then follow these 4 steps to create package hierarchy.

## Step 1: Download the template

  

  1. In Seller Central go to **Inventory** > **Add Products via Upload** > [Download an Inventory file](/listing/download).
  2. Download the template:   

    1. Select the right product type. You can select multiple product types.
    2. Select the store.
    3. When selecting the type of template, select either **Advanced** mode.
    4. Click **Generate Template**.

The template will have multiple tabs: “Instructions”, “Images”, “Example”,
“Data Definitions”, “Valid Values” to help you to fill out the template. The
“Template” tab is where you have to input information.

## Step 2: Fill Template

There are two possible scenarios as you fill the template:

  * **Product is already listed on Amazon** : For example, unit and case of pens are already listed on Amazon. In this case, you only need to fill the template with information to create a package hierarchy:  

    1. Fill **item_sku** and **external_product_id**. Each configuration (unit, case, pallet) of a product should have distinct external product IDs (such as GTIN or UPC, extra).
    2. Fill the package hierarchy attributes as illustrated below in the **Filling package hierarchy attributes** in the variation section of the template.
    3. Set the update_delete attribute to **PartialUpdate**.
  * **Product is not listed on Amazon** : For example, a unit of pens is already listed on Amazon but a pallet isn’t. In this case, in addition to providing information to create a package hierarchy, you also need to provide information to create a listing for the pallet:  

    1. Fill at least all the mandatory fields in the first section, including **item_sku** and **external_product_id**. Each configuration (unit, case, pallet) of a product should have distinct external product IDs (such as GTIN or UPC).
    2. Fill the package hierarchy attributes as illustrated below in the **Filling package hierarchy attributes** in the variation section.
    3. Set the update_delete attribute to **Update**.

## Filling package hierarchy attributes

The following table outlines how to fill out the package hierarchy attributes
in Seller Central templates for a unit, case, and pallet:

| relationship type | package_level | package_contains_quantity | package_contains_identifier  
---|---|---|---|---  
| relationship_type | package_level | package_contains_quantity | package_contains_identifier   
**For a Unit** |  | unit |  |   
**For a Case** | package_contains | case | Quantity of the seller SKU contained in the case | Seller SKU contained in the case  
**For a Pallet** | package_contains | pallet | Quantity of the seller SKU contained in the pallet | Seller SKU contained in the pallet  
  
**Examples:**

| Relationship Type | package_level | package_contains_quantity | package_contains_identifier  
---|---|---|---|---  
**Case_SKU containing 5 Unit_SKU** | package_contains | case | 5 | Unit_SKU  
**Case1_SKU containing 10 Case2_SKU** | package_contains | case | 10 | Case2_SKU  
**Pallet_SKU containing fifteen Unit_SKU** | package_contains | pallet | 15 | Unit_SKU  
**Pallet_SKU containing ten Case_SKU** | package_contains | pallet | 10 | Case_SKU  
  
## Step 3: Upload the template

  

  1. In Seller Central, go to **Inventory** > **Add Products via Upload** > **Upload your Inventory file**.
  2. Upload the completed template from Step 3.

## Step 4: Confirm in the processing report

Once you have uploaded the template, download the processing report by going
to **Inventory** > **Add Products via Upload** > **Monitor Upload Status**.
Check and correct any errors in the processing report. Error messages related
to package hierarchy are provided in the **Error Messages** section. If there
are no errors, the package hierarchy was successfully created.

**Note:** It might take some time before the status changes to “Upload Status
Done.”

## Frequently asked questions

#### 1\. What is package hierarchy?

Package hierarchy is at the core of the [Amazon Bulk Services
(ABS)](/gp/help/GXNDQS697S3JVFK6) program. Once multiple package
configurations of a product are linked using package hierarchy, you will
receive enhanced seller and customer experience features. The hierarchy can
consist of units, cases, and pallets, defined as follows:

  * Unit (also Each, Item): Smallest saleable package of a product, for example a “box” of 10 pens.
  * Case (also Case pack): Package containing multiple units, for example a “case” of 10 “boxes”.
  * Pallet: Stacked units or cases on a wooden or plastic frame to facilitate shipping and storage. For example, a “pallet” of 100 “cases”.

Different package configurations - unit, case, pallet - of a product can be
represented in a package hierarchy with multiple levels of parent-child
relationships. The following are the most common types of package hierarchies:

| **Parent** | **Child**  
---|---|---  
Case containing multiple Units | ![](https://m.media-amazon.com/images/G/01/rainier/help/casetounit.png) | Case | Unit  
Case contains Unit  
Pallet containing multiple Units | ![](https://m.media-amazon.com/images/G/01/rainier/help/pallettounit.png) | Pallet | Unit  
Pallet contains Unit  
Pallet containing multiple Cases and each Case containing multiple Units | ![](https://m.media-amazon.com/images/G/01/rainier/help/pallettocasetounit.png) |  Pallet Case |  Case Unit  
Pallet contains Case contains Unit  
  
Many other hierarchies are possible, such as:

  * Case 1 containing Case 2 containing Unit
  * Pallet containing Case 1 containing Case 2 containing Unit
  * Case 1 containing 10 Units and Case 2 containing 20 Units

#### 2\. What is the difference between Package hierarchy and Variation?

Package hierarchy is different from variation relationships.
[Variations](/gp/help/8831) are sets of products that are related to one
another in terms of size, color, flavor, and so on. With package hierarchy,
different package configurations (unit, case, pallet) are linked to each other
through an established hierarchy. Features for better seller and customer
experience, including the referral fee discount launched as part of the ABS
program, are applicable for products linked using package hierarchy but do not
apply to variations. Package hierarchy and variation relationships can co-
exist, that is a product can be part of a variation relationship and also a
package hierarchy at the same time.

Variation | Package hierarchy  
---|---  
| Parent |  | ![](https://m.media-amazon.com/images/G/01/rainier/help/pallettocasetounit.png)  
![](https://m.media-
amazon.com/images/G/01/rainier/help/parenttovariations.png)  
Green color product | Blue color product | Yellow color product |  Pallet contains Case contains Unit  
  
#### 3\. Which mechanisms on Seller Central can I use to create or change a
package hierarchy?

Package hierarchy can be created:

  * for products already listed on Amazon, or
  * while creating new listings

Currently, you can create a package hierarchy using templates on Seller
Central. Support for a web-based interface and API integration will be
introduced later down the line.

#### 4\. What are the new attributes to create a package hierarchy?

The three new attributes used to enable package hierarchy, which have been
implemented into existing Seller Central templates, are:

  * Package level: Indicates whether a product is a unit, case or pallet
  * Package contains identifier: Indicates the SKU of the product contained in the package. This field is left blank if the package level is “unit”.
  * Package contains quantity: Indicates the number of SKUs contained in the package. This field is left blank if the package level is “unit”.

For example:

Case containing 10 units  
---  
case seller SKU: Case_SKU unit seller SKU: Unit_SKU |  **For Case** : 

  * Package level = case
  * Package contains identifier = Unit_SKU
  * Package contains quantity = 10

  
**For Unit** :

  * Package level = unit
  * Package contains identifier = _blank_
  * Package contains quantity = _blank_

  
Pallet containing 5 cases and each case containing 20 units  
---  
pallet seller SKU: Pallet_SKU case seller SKU: Case_SKU unit seller SKU: Unit_SKU |  **For Pallet** : 

  * Package level = pallet
  * Package contains identifier = Case_SKU
  * Package contains quantity = 5

  
**For Case** :

  * Package level = case 
  * Package contains identifier = Unit_SKU
  * Package contains quantity = 20

  
**For Unit** :

  * Package level = unit
  * Package contains identifier = _blank_
  * Package contains quantity = _blank_

  
  
#### 5\. How do I change package hierarchy attributes if I input an attribute
incorrectly while submitting the template?

If you have already created a package hierarchy and want to change any of the
package hierarchy attributes, fill the template as follows:  

  1. Fill all mandatory fields including **item_sku** and **external_product_id**.
  2. Fill all package hierarchy attributes to reflect the desired change.
  3. Set **update_delete** attribute to **Update**.

#### 6\. How do I delete ASINs in a package hierarchy?

Deleting an ASIN in a package hierarchy will remove the ASIN and the
corresponding package hierarchy relationships. For example, if there is a
hierarchy pallet–case–unit and you delete the case ASIN, case ASIN will be
removed. Additionally, the package hierarchy relationship with the pallet and
the unit will also be removed.

To delete, fill the template as follows:  

  1. Fill the **item_sku** and **external_product_id**.
  2. Set **update_delete** attribute to **Delete**.

#### 7\. I received error messages when I uploaded my template. What do they
mean?

The following table lists the errors you may encounter while creating package
hierarchy:

Error code and message | Reason for error  
---|---  
**99010:** A value is missing from one or more required columns from this group: [Relationship Type], [package_level], [package_contains_identifier], [package_contains_quantity]. | When **Relationship type** is set as “package_contains” and **package_level** is set as "case" or "pallet", then **package_contains_identifier** and **package_contains_quantity** are required fields.  
**99008** : The value in the "Relationship Type" (Variation) field conflicts with the value in the "package_contains_identifier" field. | The **package_contains_identifier** attribute can have a value only when **Relationship type** is **package_contains**.  
**99008** : The value in the "Relationship Type" (package_contains) field conflicts with the value in the "package_level" (unit) field. | For **package_level** "unit", **package_contains_identifier** should be blank.  
**99008:** The value in the "Relationship Type" (Variation) field conflicts with the value in the "package_level" (case/unit) field. | The **package_contains_identifier** attribute can have a value only when **Relationship type** is **package_contains**.  
**990101** : The ${relationship_type} relationship from parent SKU ${sku} to child SKU ${child_id} was refused because one or more GTIN values on the parent (${duplicate_gtins}) are duplicated on a descendent (SKU: ${duplicate_gtin_child_id}). | Each SKU in the hierarchy must have a unique external product ID (such as GTIN or UPC).  
**990100** : We have detected a potential error with “package_contains_identifier” attribute. If you see other errors or warnings related to “package_contains_identifier”, correct and resubmit. Otherwise your request may still be processing and this error will resolve itself. | If there are no other error or warning messages related to **package_contains_identifier** , then this error will resolve itself. Otherwise, the error or warning needs to be fixed.  
  
## Additional resources

[Amazon Bulk Services](/gp/help/GXNDQS697S3JVFK6)

