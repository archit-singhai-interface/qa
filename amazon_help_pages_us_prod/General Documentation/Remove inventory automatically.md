---
title: Remove inventory automatically
url: https://sellercentral.amazon.com/help/hub/reference/G200678710
section: General Documentation
---

You can set up automatic removals for your inventory at Amazon fulfillment
centers. You can enable automatic removals for the following:

  * [Unfulfillable inventory](/recoveryui/removal-setting/automated-unfulfillable?)

**Note:** Amazon has enabled the automated unfulfillable settings and grayed-
out the **Disable** option. It is not possible to opt out of the automated
unfulfillable settings.

  * [Fulfillable inventory](/recoveryui/removal-setting/automated-lts): 
    * Inventory that is subject to 365+ days aged inventory surcharge

**Note:** Inventory that has been in a fulfillment center for 181 to 365 days
will still be subject to the 181-365 aged inventory surcharge. For more
information about inventory cleanup dates and surcharges, go to [Aged
inventory
surcharge](https://www.sellercentral.amazon.dev/gp/help/GJQNPA23YWVA4SBD). To
avoid this surcharge, create a removal order using the standard process on the
[Create removal
order](https://www.sellercentral.amazon.dev/recoveryui/removal-
order/create?requestId=d7ef9d43-d5b7-40b1-b6e2-b278e8bd8603) page. For more
information, go to [Remove inventory
(overview)](https://www.sellercentral.amazon.dev/gp/help/200280650).

    * Units of ASINs that have not sold in six or more consecutive months and that have been in fulfillment centers for more than 180 days

Per-item removal fees are applicable. For more information, go to [FBA removal
order fees](/gp/help/200685050) and [FBA disposal order
fees](/gp/help/5FKTA8LXU4TZPD5).

We fulfill orders using inventory based on its location, to quickly deliver
products to buyers. We don't fulfill inventory in the order that it was
received in our facilities. For more information, go to [Expiration dates on
FBA products](/gp/help/G201003420).

## Remove unsellable inventory automatically

When inventory that is in a fulfillment center is not in sellable condition,
its status changes to **Unfulfillable** and it is set aside. This inventory
must be removed from the FBA network. You may configure your removal
preferences using Automated unfulfillable settings. If you do not configure a
removal preference, your items will be Disposed at Amazon’s earliest
discretion based on capacity, including immediately after returns evaluation.
For more information, go to [Required removals](/gp/help/202000820).

You can remove unsellable inventory at any time by submitting a removal order.
For more information, go to [Remove inventory from a fulfillment
center](/gp/help/201436560).

You can also choose to have unsellable inventory refurbished, liquidated, or
returned to you automatically by enabling the service in your seller account.

  1. Go to [Automated unfulfillable settings](/recoveryui/removal-setting/automated-unfulfillable?), optionally select one or more of the following value-recovery services for unsellable inventory:
     * **Refurbishment** to have eligible unsellable inventory refurbished for sale. For more information, go to [FBA repackaging and refurbishment services](/gp/help/G201505310).
     * **Grade and resell** to have enrolled ASINs automatically graded and relisted as **Used**. For more information, go to [FBA Grade and resell](/help/hub/reference/GUA6RV6UA4DR2MFK).
     * **Liquidate** to have unsellable inventory liquidated. For more information, go to [FBA Liquidations](/gp/help/GYVCG5Q3BEJ6MLMF).

  2. Select one of the following required removal options:
     * **None** (available only if you did not enable automated removals when you signed up for refurbishment)
     * **Return** to have unsellable inventory returned to you
     * **Dispose** to have unsellable inventory disposed of

  3. If you selected **Return** , select your preferred schedule:
     * **Weekly (on the 8th, 15th, 22nd, and 28th)**
     * **Twice a month (on the 5th and 20th)**

  4. If you selected **Return** or **Dispose** , provide your preferred email address.

  5. If you selected **Return** , provide the address and phone number for the delivery destination.

  6. Click **Update**.

**Note:**

  * Immediate removal is the default schedule for Disposal and Liquidation. If you enroll in these removal options, you will not be able to place manual removal orders for your unfulfillable inventory.
  * If you select immediate removal, unsellable customer returns will be disposed of at Amazon’s earliest discretion based on capacity, including immediately after returns evaluation.
  * Items that are immediately removed will be reported in the [FBA Customer Returns report](/reportcentral/CUSTOMER_RETURNS/0). Immediate removals will not be available in the Removal Order Detail Report.
  * Some items may not be eligible for immediate disposal. If you use the [FBA repackaging and refurbishment services](/gp/help/201505310), we will evaluate customer returns, repackage eligible items, and return them to sellable inventory. If an item is not eligible for repackaging and sale, it will be removed in accordance with your Automated unfulfillable settings. The usual storage and removal fees will apply.

##  Remove fulfillable inventory automatically

You can choose to have aging and slow-moving inventory removed through the
[automated fulfillable inventory settings](/recoveryui/removal-
setting/automated-lts). Once you’ve enabled automated removals, we’ll return,
liquidate, or dispose of the following:

  * Fulfillable inventory that has been in a fulfillment center for more than 365 days
  * Units of ASINs that have not sold for six or more consecutive months and that have been in a fulfillment center for more than 180 days

**Important:** Removal orders will be created one to two weeks after the
inventory cleanup date. For more information about cleanup dates and fees, go
to [Aged inventory surcharge](/gp/help/GJQNPA23YWVA4SBD).

  1. Under **Settings** in Seller Central, select [Fulfillment by Amazon](/gp/ssof/configuration/index.html/ref=xx_fbasettings_dnav_xx). 

  2. Locate **Automated fulfillable inventory settings** , and click **Edit**.

  3. Enable **Automated long-term storage removals settings** , **Automated removal of ASINs with no sale** , or both.

  4. Optionally enable **Liquidations** to recover value from eligible units. To learn more about product eligibility, go to [FBA Liquidations](/gp/help/GYVCG5Q3BEJ6MLMF).

**Note:** Once enabled, you can exclude ASINs from liquidation by entering
them as a comma-separated list.

  5. Select either **Return** or **Dispose** as your removal preference.
     * If you select **Return** :  

       1. In the **Email address** text box, enter your preferred email address.
       2. Provide the address and phone number for the delivery destination.

**Note:** To avoid errors when saving information in your seller account, the
full name and address fields cannot be longer than 50 characters, and the
return address must be a physical street address.

       3. Click **Update**.
     * If you select **Dispose** : In the **Email address** text box, enter your preferred email address.

  6. Click **Update**.

**Note:** Once a removal order is successfully created, we do not charge
storage fees on the units during the processing period until its completion.

