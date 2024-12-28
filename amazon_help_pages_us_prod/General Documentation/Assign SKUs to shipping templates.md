---
title: Assign SKUs to shipping templates
url: https://sellercentral.amazon.com/help/hub/reference/G201841600
section: General Documentation
---

You can assign SKUs to a shipping template, or change the shipping template
that was assigned to an existing SKU. Select from one of the following options
to assign SKUs to shipping templates:

  * Use **Manage All Inventory** tool in Seller Central **for up to 50 changes at a time** :

In [Manage All Inventory](/inventory), the shipping template name displays in
the **Price and shipping cost** column for each SKU, underneath the price.

**Note:** The shipping price will not display if the SKU is out of stock.

  

    1. Select one or more of the SKUs you want to update.
    2. Click **Action on X selected** in the top-left corner.
    3. Select **Change shipping template**.

**Note:**

The freight shipping template is only available for heavy and bulky items:

    * package weight >= 50 lb OR
    * package length >= 96 inches OR 
    * package length + 2 *(package width + package height) >= 130 inches

  * **Use feeds for bulk changes:**
    * Excel feed: The [Inventory Loader](/gp/help/201576540) has a column called **merchant_shipping_group_name**. Use this column to assign SKUs to Shipping Templates.
    * XML feeds: The product XML feed contains an attribute named **MerchantShippingGroupName**. Use this attribute to assign SKUs to Shipping Templates.
  * **Use the Manage SFP page:**

**Note:****Manage SFP** page is only available to sellers who participate in
the Seller Fulfilled Prime (SFP) program.

  

    1. Visit the [Manage SFP](/seller-fulfilled-prime/analytics) page under **Inventory** in Seller Central.
    2. On **Product List** tab, you can select one of the following options:
       * In **Shipping Template** column, change the shipping template to a Prime template at the SKU-level.
       * Select all the SKUs you want to assign to the Prime template, and then select **Prime template** from the **Change shipping template on # of selected** drop-down menu in the top left corner.

## Check the shipping template assigned to a SKU

You can select from the following options to verify which shipping template is
assigned to a SKU:

  * **From Manage All Inventory:**

In [Manage All Inventory](/inventory), the shipping template name displays in
the **Price and shipping cost** column for each SKU, underneath the price.  

    1. Select a SKU.
    2. Click **Edit**.
    3. Scroll down the **Offer** tab to find **Merchant Shipping Group** field, where you can check or change the shipping template assigned to the SKU.

**Note:** The shipping template field only displays if the ASIN is set to
"Fulfilled by Merchant."

  * **From the Active Listings report:**

Download the **Active Listings report** from [Inventory
Reports](/listing/reports), and open the file in Excel (or copy paste from
Notepad into Excel). Under the **merchant-shipping-group** column, you will
see the assigned SKUs to each template.

  * **From Manage SFP:**

**Note:****Manage SFP** page is only available to sellers who participate in
the Seller Fulfilled Prime (SFP) program.

Visit the [Manage SFP](/seller-fulfilled-prime/analytics) page. Your SFP SKUs
are listed on the **Product List** tab. In the right-hand column of the page,
you can see the shipping template assigned to each of the SKUs. To change the
shipping template, select one of the following options:

    * Select a new template from the dropdown menu at the SKU-level.
    * Select multiple SKUs and use the **Change shipping template on # of selected** drop-down menu.

## See also

[Create, edit, or delete shipping templates](/gp/help/201834090)

[Set your shipping rates](/gp/help/201841310)

[Set the Default Shipping Address](/gp/help/201841320)

[Modify handling time](/gp/help/200955560)

