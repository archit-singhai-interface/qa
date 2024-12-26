# Get started with Multi-Location Inventory

Section: Seller Flex and Alternative Fulfillment
Original URL: https://sellercentral.amazon.com/help/hub/reference/GYCAQ9XRL273EVDX

Multi-Location Inventory (MLI) is a feature for your account that synchronizes
your inventory per location in real time to make more accurate delivery
promises and simplify order fulfillment.

Follow these steps to get started:

  1. Enroll through our automated onboarding tool.
     * Fill the [Multi-Location Inventory Sign-up Form](https://amazonexteu.qualtrics.com/jfe/form/SV_4IY1OG3g51fE3L8) so we can prepare your selling account to use MLI. We will notify you within 15 business days when your account is ready to start integrating.

  2. Create locations and synchronize your inventory by location.
     * View our MLI API integration instructions to learn how to set up locations (also known as Supply Sources), and sync inventory per location. You can use MLI to sync your inventory for as many ASINs as you like.
     * [View Integration Instructions](https://developer-docs.amazon.com/sp-api/docs/mli-integration-guide)

  3. Enable Shipping Setting Automation (SSA) on your Shipping Template, and assign ASINs synced with MLI to this template. Follow these steps to enable Shipping Settings Automation (SSA):  

    1. From the **Settings** drop-down menu on the top right of Seller Central, click **Shipping Settings**.
    2. Go to the **Shipping Templates** tab.
    3. On the **Shipping Templates** tab, you can enable Shipping Settings Automation on the following:  

      1. Click **Create New Shipping Template** and select new ****shipping templates****.
      2. Choose **Existing shipping templates** and click **Edit**.
    4. Turn on the **Shipping Settings Automation** option.
    5. Select one or more of your **Ship-from location** , and click **Next**. These locations should match your inventory locations.
    6. Choose from a Prime or non-Prime Shipping Template and click **Next**.
    7. On the **Standard Shipping Automation Preferences** page, enable automated transit time for Standard Shipping by following these steps:  

      1. Under **Region Preferences** section, click **Edit** to manage your standard shipping regions.
      2. Select the carriers and shipping services you currently use in the **Carrier Preferences** section and click **Next**.
    8. If you are shipping from domestic fulfillment center, you can enable Premium Shipping region automation for Self-Fulfilled One-Day Delivery and Two-Day Delivery. Select the carriers and shipping services you use in the **Carrier Preferences** section on the **Premium Shipping Automation Preferences** page and click **Next**.
    9. Review your shipping settings automation preferences and click **Confirm**.
    10. Review and edit the **shipping fee** for your shipping regions.
    11. Click **Save** template.
    12. Assign your MLI SKUs to the shipping template.

MLI is available for sellers with multiple locations who provide their
inventory via SP-API, Feeds API, and Listing Loader feed file upload in Seller
Central or using a Multi-channel integrator. You can add as many or as few
ASINs as you would like. To get the benefits of MLI, we recommend adding all
of your ASINs.

Currently, Shipping Templates are limited to 10 locations. Your ASINs synced
with MLI can be on the same Shipping Template as ASINs not synced with MLI.
However, this Shipping Template should be enabled with Shipping Settings
Automation (SSA), and must include all of your inventory locations.

You can use MLI for Seller Fulfilled Prime and have your MLI inventory on as
many Shipping Templates as you would like.

If SSA on a Shipping Template that has ASINs synced with MLI is disabled, your
customers will still be able to place orders. However, your delivery promise
will be based off of your manual estimation and you will not get the benefits
of MLI and SSA.

In case of further assistance, write to us at
[multilocationteam@amazon.com](mailto:multilocationteam@amazon.com).

