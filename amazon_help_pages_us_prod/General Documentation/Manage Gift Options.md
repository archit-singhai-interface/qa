---
title: Manage Gift Options
url: https://sellercentral.amazon.com/help/hub/reference/G571
section: General Documentation
---

If you have a Professional selling plan you can use **Gift Options** to offer
gift-wrapping, gift messaging, or both to customers. These services can help
increase your sales conversion rates by offering an enhanced buying
experience.

Gift Options allows customers to indicate an order is a gift. By default, when
customers indicate that an order is a gift, the product prices will not appear
on the packing slip. However, customers can elect to include prices. The
buyer's choices will show on the packing slip available in the **Manage
Orders** page. If you create your own packing slips, you will need to manage
the messaging and product price display.

By default, neither gift messaging nor gift-wrap options are enabled. To allow
customers to access your gift-wrap and gift messaging options, you must enable
Gift Options in your seller account and add fields to your inventory file to
indicate whether gift-wrap, gift messaging, or both are available for each
product in your inventory.

**Note:**

  * Gift Options are not available for Books, Music, Video, and DVD products. 
  * Fulfillment by Amazon (FBA) offers gift-wrap services for eligible items, at no extra cost to sellers. 
  * We charge on a per-item basis for gift-wrapping. You cannot charge a flat fee for gift-wrapping a buyer's entire order. 

##  Configure gift options

By default, neither gift messaging nor gift-wrap services are enabled. To
enable Gift Options, you perform two tasks:

  * Set up and configure Gift Options in your seller account.   

    1. Go to **Settings** , then click **Gift Options**.
    2. Click **Edit** next to **Gift Messaging** or **Gift-Wrap** , then enable the service for individual order items.
    3. Click **Continue** to save the setting.
  * Modify and upload your inventory files to enable Gift Options. 

If you upload your inventory using text files or XML, you can use the **is-
gift-message-available** field, or **is-gift-wrap-available** field, or both
to control which products are eligible for these options.

If you download Order reports and Adjustment reports, you will want to adapt
your integration method to process the Gift Options information that appears
in those reports. See the Integration requirements section below for more
information.

Changes to Gift Options appear within 4 hours.

##  Disable gift options

To stop offering a particular type of gift wrap, follow one of these two
methods:

  * If you never plan to offer this gift wrap option in the future:   

    1. Go to **Gift Options** and click **Edit** in the section that displays your gift-wrap images.
    2. Check **Remove** next to the gift wrap option you no longer want to offer. 
    3. Click **Submit** to save your changes.
  * If you want to temporarily stop offering a gift option:   

    1. Go to **Gift Options** and click **Edit** in the section that displays your gift-wrap images. 
    2. Click **Disabled** next to the gift wrap option you want to temporarily disable.
    3. Click **Submit** to save your changes. The gift wrap option will remain in your account, but its status will change from **Enabled** to **Disabled**.
To resume offering a disabled gift-wrap option, click **Enabled** next to the
gift wrap, and click **Submit** to save your changes.

##  Customize help pages

To communicate information to buyers about your Gift Options, you can create
custom Help pages. For more information, see [Create custom help
pages](/gp/help/201716580).

To update your customer-facing Help pages, follow these steps:

  

  1. On the **Settings** link, select **Your Info & Policies**.
  2. Select **Gift Services** to create help content about your gift-wrap and messaging options.
  3. Enter your help content in the **Gift Messaging** field, **Gift-Wrap** field, or both.
  4. Click **Save**.
  5. Select **Custom Help Pages** to create more generalized help content about your gift options.
  6. Add a title and help content.
  7. Click **Save**.

##  Integration requirements

You might be using an inventory file to create new items and adjust inventory
levels for existing listings. This file contains the core information about
each product (such as the title, SKU, description, etc.).

Once you enable and configure your Gift Options, you will want to modify and
upload your inventory files to identify products that are eligible for gift-
wrap, gift messaging, or both.

To enable Gift Options, add two fields —both are Boolean fields— to the
product feeds:

#### Is_Gift_Wrap_Available or IsGiftWrapAvailable

  * **true** : Item can be gift-wrapped.
  * **false** : Item cannot be gift-wrapped.

#### Is_Gift_Message_Available or IsGiftMessageAvailable

  * **true** : Item can have a gift message.
  * **false** : Item cannot have a gift message.

**Notes:**

  * "true" and "false" are case-sensitive. Make sure to use all lower-case letters.
  * Field naming conventions vary across templates. Depending on your template, you either use a single phrase with no spaces (IsGiftWrapAvailable) or you use hyphens (Is-Gift-Wrap-Available). Use the convention shown in your template.
  * For variation product relationships, setting Gift Options for a parent product does not mean that all children associated with that parent are gift-enabled. To enable Gift Options for one child product, you must set a value for each child product.

##  Reports

If you enable Gift Options and use a parsing program to process your Order
reports, you might need to change your back-end system to accept all new
orders.

#### Orders

Order reports for Gift Options-enabled sellers contain the following fields:

  * **gift-wrap-type:** The gift-wrap identifier you specified during Gift Options configuration. The limit is 40 characters long.
  * **gift-message-text:** The text that the buyer entered as the gift message for an item. The limit is what you set during configuration. The message text appears in the Order report as a single line of text.
  * **gift-wrap-price:** The charge applied for gift-wrapping.
  * **gift-wrap-tax:** The tax on the gift wrap price. You can choose to apply the same tax rates on both your gift wrap products.

If you collect tax through Amazon, you can customize your gift wrap tax
preferences. By default, the tax settings for gift wrap are identical to the
tax settings for your products. For more information, see the Amazon Services
Business Solutions Agreement.

#### Adjustments (Refunds)

You must add these fields to your Adjustments files to process adjustments for
gift services:

  * **gift-wrap-price-adj:** The gift-wrap price you charged and now want to refund.
  * **gift-wrap-tax-adj:** The gift wrap tax you charged and now want to refund.

Append these two fields as the right-most two columns in your Adjustments file
in the order listed above.

##  Gift messaging

The Gift Messaging option is free to both you and the buyer. When you enable
Gift Messaging for a product, you offer buyers the ability to create one gift
message for each item in the order. Messages appear on the packing slip
produced using **Manage Orders**.

For the gift message, you can use the system defaults, or you can configure
your gift messaging as follows:

#### Maximum gift message length

The maximum number of characters in a gift message. You can set the limit from
1 to 255 characters. The default is 255.

####  Maximum lines in gift message

The number of lines in a gift message. You can set the limit from 1 to 10
lines. The default is 10.

To improve the buying experience, we recommend offering the maximum number of
characters your business can support. Customers appreciate flexibility in
creating personalized messages.

##  Gift-wrap

You can offer up to four different Gift-Wrap options. You are not able to
specify which gift-wrap options are eligible for which products. All gift-wrap
options are available for every product you specify as eligible for gift wrap.

For each gift-wrap option, you can provide the following information:

#### Gift-wrap name:

The name the buyer sees for a specific gift-wrap option. Each gift-wrap option
must have a description. The limit is 50 characters.

#### Gift-wrap identifier:

The name you see for a specific gift-wrap option in the order reports. It
might or might not match the name the buyer sees. The limit is 40 characters.

#### Gift-wrap charge:

The price you charge the buyer to gift-wrap an item. If the order is tax-
enabled, we will charge tax against this amount. If you want to offer free
gift wrapping, set the price to 0.

**Note:** You can charge only a single price per gift-wrap option. You cannot
charge different prices for different size or type of packages.

#### Gift-wrap image:

The image buyers see when making their gift wrap selection. If you do not
provide an image, a placeholder image appears. Images must be a minimum of 71
x 71 pixels, in either a .gif or .jpg format.

