---
title: Fix a "no listing" error
url: https://sellercentral.amazon.com/help/hub/reference/G200252930
section: General Documentation
---

A "no listing" error means that your listing cannot be viewed on Amazon. The
listing must be fixed to make your product available for purchase.

The following error messages indicate that a listing is not available for your
product:

  * No listing exists for this inventory item
  * Item not in catalog
  * No Amazon-fulfilled listing exists for this inventory item

"No listing" errors are often the result of incorrect feeds. If you use feeds
and have received a large number of "no listing" errors, confirm that your
feed is correct. For more information, see [List FBA products in
bulk](/gp/help/200327780).

You can also use the **Fix Stranded Inventory** report to help resolve "no
listing" errors. If the report is not available, you do not have stranded
inventory. For more information, see [Fix stranded
inventory](/gp/help/201436600).

If your feed is correct and your inventory is not stranded, the questions to
consider when you receive a "no listing" error are:

  * Is your listing active?
  * Is your listing accurate?
  * Is your product restricted or reserved?
  * Is the start selling date accurate?
  * Is your product a variation of another ASIN?
  * Are your account settings current?

## Is your listing active?

Your listing may be inactive or you may need to create a new listing.

  

  1. On the [Manage Inventory](/hz/inventory) page, type the product MSKU in the **Search** box, and click "Search".
  2. If the status is **Active** , continue to the section entitled "Is your listing inaccurate."
  3. If the status is **Inactive** , review the note in parentheses to determine next steps. For example: 
     * For **Inactive (Blocked)** items, review any communication you may have received for next steps.
     * For **Inactive (Out of Stock)** items, replenish your inventory.
     * For **Inactive (Closed)** items, click **Relist**.
  4. If you can't find the listing, click the **Add a product** button at the top right corner of the page and create a new listing. For more information, see [Add One Product at a Time](/gp/help/200220550).

**Tip:** Make sure that the ASIN, merchant SKU (MSKU), and condition match the
items in your inventory. If they don't match, a second item will be added to
your inventory list, and the first listing will not be fixed.

##  Is your listing accurate?

If your listing is not accurate, it may not be associated with the product
that you have sent to the fulfillment center.

  * Are the **Merchant SKU** and **ASIN/ISBN** the same as the product causing the error? If the **Merchant SKU** , **ASIN** , or **ISBN** don't match, click the **Add a product** button and create a new listing with the same merchant SKU as the product causing the error.
  * Is a price listed for the product (**Your Price + Shipping**)? If the price is missing, click **Edit** in the far right column of the inventory listing that you want to modify. In the **Your Price** field, type the price, and then click **Save and finish**.
  * Is the condition the same as the product causing the error? If the condition is different, click **Add another condition** in the far right column of the inventory listing that you want to modify. Edit the condition, and then click **Save and finish**.
  * Is the **Fulfilled by** column set to **Amazon** for that product? If it is set to **Merchant** , select the listing for that product and, on the **Action on selected** menu, click **Change to Fulfilled by Amazon**.

If you answered Yes to all of the above, continue to the section entitled "Is
your product restricted or reserved."

## Is your product restricted or reserved?

Amazon regularly reviews and occasionally removes product listings as a result
of product restrictions, selling restrictions, or finding duplicate detail
pages, and then sends an email regarding these changes.

  

  1. Check your email to see if you have received any communications from Amazon regarding this product.
  2. If you have not received any communication, continue to the section entitled **Is the Start selling date accurate**.
  3. If you have received communication regarding this product, follow the instructions you received.

## Is the Start selling date accurate?

If you set a **Start selling date** that is in the future, Amazon will not
make those products available for sale until that date.

  

  1. On the **Manage Inventory** page, click **Edit** in the far right column of the inventory listing that you want to modify. Locate the **Start selling date** field.
  2. If the **Start selling date** field is blank or if the date occurs in the past, continue to the section entitled **Is your product a variation of another ASIN**.
  3. If the **Start selling date** field is in the future, delete the date and click **Save and finish**.

## Is your product a variation of another ASIN?

You can create variations on a parent ASIN. For example, a T-shirt may be
available in different sizes and colors. The T-shirt is the parent ASIN, and
the listings for different sizes and colors are the product variations, also
called child ASINs. If the parent-child ASIN relationship is incorrect, it may
cause a "no listing" error.

For more information about parent-child relationships, see [Creating Parent-
Child Variation Relationships](/gp/help/8841).

  

  1. In [All Inventory view](/myi/search/DefaultView.amzn), click the **ASIN/ISBN** for the product.
  2. If there are no color and/or size options, continue to the section entitled "Are your account settings current."
  3. If there are color and/or size options, your listing is a variation of another ASIN. Select the color and/or size of the product that you are offering. Scroll down the page and select and copy (Ctrl+C) the ASIN for this listing.
  4. In [All Inventory view](/myi/search/DefaultView.amzn), paste the ASIN that you copied into the **Search** box and click **Search**.
  5. On the left side of the page, click **All Inventory**. In the **Status** column, look for **Variation Parent**.
  6. If **Variation Parent** appears in the **Status** column, continue to the section entitled "Are your account settings current."
  7. If **Variation Parent** does not appear in the **Status** column, click the **Add a product** button, paste the ASIN that you copied into the **Find it on Amazon** search box and click **Search**. Click **Sell yours** to create a new listing with the correct parent-child relationship.

## Are your account settings current?

If every item in your inventory is displaying a "no listing" error, there may
be an issue with your account. Check your account settings and make sure that:

  * You have entered the tax information for your account. For more information, see [Tax Collection Services](/gp/help/200787660).
  * Your selling privileges have not been suspended or removed. For more information, see [Appeal the removal of selling privileges](/gp/help/200370560).

