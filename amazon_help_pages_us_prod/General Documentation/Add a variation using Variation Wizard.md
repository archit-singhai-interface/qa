---
title: Add a variation using Variation Wizard
url: https://sellercentral.amazon.com/help/hub/reference/G202034620
section: General Documentation
---

The [Variation Wizard](/listing/varwiz?ref_=ag_varwiz_xx_prodsrch) is an
interactive tool that allows you to create parent-child variation
relationships in bulk using an automatically populated inventory file
template.

**Note:** Not all related products are valid variations. Amazon reserves the
right to remove the newly-created variations families or children that are
added to a variation family that do not comply with certain standards.
Variation families with more than 2000 child ASINs will not be displayed on
the detail page. To understand whether your products are good candidates for
variation or not and to get specific tips for creating variations, refer to
[Determine variations for your products](/gp/help/G201958220) and [Variation
Relationship FAQ](/gp/help/G201951410).  Go to [About parent-child
relationships](/gp/help/G8841) to understand how product variations work on
Amazon.

**Important:** Variation Wizard is only available for professional sellers. It
currently does not support ASINs in the Handmade category on Amazon.

To access the Variation Wizard, follow the steps below:

  * On the **Inventory** link in your Seller Central account, select **Manage All Inventory**.
  * On the **Manage Inventory** page, select **Add a Variation**.

## Add to or update an existing variation family via Variation Wizard

Follow the steps below to add a new child variation to an existing listing
that you or another seller created:  

  1. Select the option **Add to or update an existing variation family** and search for the ASIN for the parent-child listing in a variation family. The parent listing appears with **Parent** under the "parentage" column. If there are existing child variations, they appear with **Child** under the "parentage" column.
  2. For any existing child variations that you created, use **Edit** to edit information.
  3. If you searched for an ASIN created by another seller, click **Sell Yours** , if the child variation you want to add is already listed under the parent SKU. Provide the **Quantity** , **Price** and **Condition** to add your offer.
  4. Click **Add** to add a new child variation to the variation family, and use the editable columns to provide required information, and then click **Save**.
  5. Repeat step 4 to add more child variations.
  6. You can use **Edit** or **Delete** to edit or delete the newly added variation.
  7. Click **Generate Template** to get a pre-filled inventory file template, which you can modify to add the new variations.
  8. Once you have completed modifications to the inventory file, go to **Catalog** , **Add Products via Upload** , select **Upload your spreadsheet** , browse and select your file, and click **Submit products**.

**Note:** In the Excel template, delete the quantity amounts for any FBA SKUs
in your inventory. If you leave the quantities intact, it will convert any FBA
inventory to Merchant Fulfilled. Leave the **Update/Delete** column set to
**Partial Update**.

## Create a new variation family by combining existing standalone listings
within your catalog

  

  1. Download the appropriate category template for your category using the [Product Classifier](/hz/inventory/addproducts/download). Refer to the **Valid Values** tab in the template to see what variation themes are available.

**Note:** If no variation theme is listed, you cannot create a product with
variations in that category. Ensure you have downloaded any templates that
have been previously generated to avoid losing your variation family.

  2. In the inventory template, create parent and child SKUs.
  3. On the parent item:   

    1. Enter values for required fields, including SKU. This can be any alphanumeric string of 40 characters or less, but must be unique (that is, must not duplicate any of your other SKUs). Sellers often append "parent" to their base SKU as a reminder.
    2. Leave **Parent SKU** field blank.
    3. Enter a value of "parent" in **Parentage** and enter a valid value in **Variation Theme**.
    4. Leave **Relationship Type** and all other non-required fields blank.
  4. For each child item:   

    1. Enter values for required fields.
    2. Fill in the **Parent SKU** field using the value from the parent's SKU. This value will be the same for all child items.
    3. Enter a value of "child" in **Parentage** and enter "variation" in **Relationship Type**.
    4. Ensure that the **Product Type** is consistent across all child ASINs and the parent ASIN of the variation family.
    5. In the **Variation Theme** field, enter the same value that you entered for Variation Theme on the parent. This value will be the same for all child items.

