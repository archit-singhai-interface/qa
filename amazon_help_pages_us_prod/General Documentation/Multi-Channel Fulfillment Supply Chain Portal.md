---
title: Multi-Channel Fulfillment: Supply Chain Portal
url: https://sellercentral.amazon.com/help/hub/reference/GC2M7FXZ36SZG6K8
section: General Documentation
---

Supply Chain Portal (SCP) allows businesses to create listings and fulfill
orders with [Amazon Multi-Channel Fulfillment](/mcf) (MCF) for products that
are not intended to be listed for sale on Amazon.com. SCP gives you access to
inventory visibility, order management, reporting, and tracking for all your
MCF orders while bypassing many of the time-consuming requirements that are
specific to selling in the Amazon store.

**Note:** Supply Chain Portal listings or inventory will not appear in Seller
Central and cannot be used to fulfill orders in the Amazon store. To learn how
to use a consolidated pool of inventory for FBA and MCF orders, go to [Multi-
Channel Fulfillment: Fulfill orders for your sales
channels](/gp/help/G200332450).

## SCP benefits

There are fewer restrictions for creating listings with SCP than Seller
Central, which can potentially save you time, experience fewer enforcements,
and allow you to use MCF to fulfill a wider selection of your products, for
example:

  * SCP listings are proprietary to the seller that created them; sellers can use MCF to fulfill products without matching them to existing Amazon store listings
  * SCP listings do not have brand restrictions; sellers can use MCF to fulfill products without authorization from brand owners
  * SCP listings do not require a product identification code; sellers can use MCF to fulfill products that do not have a registered GTIN or UPC code
  * *[Dangerous goods](/gp/help/G201371860) (also referred to as hazmat) policies still apply for listings created in SCP

## SCP eligibility

Supply Chain Portal can be used by all sellers that do business in the US. If
you are an Amazon seller, you can use your same Seller Central or Vendor
Central account credentials to sign in to SCP at
<https://supplychain.amazon.com/login>.

If you are not an Amazon seller, you can sign-up for an SCP account by
following these steps:

  

  1. Go to <https://supplychain.amazon.com/sign-up>.
  2. Enter **Account Information** , **Primary contact** , and **Business address**.
  3. Click **Register**.
  4. You will receive an email with your approval status within 1 business day.
  5. If after 1 business day we are unable to verify the information provided in your business account registration, return to the sign up page to submit additional documentation.
  6. Click **Upload a document** , then upload the following two documents:  

    1. One: any of the following three documents that contain your business's valid/active Federal Tax ID or sole proprietor status:  

      1. EIN (Employee Verification Document) verification document from the US Internal Revenue Service (IRS)
      2. Business license
      3. State documents which contain state seal
    2. Two: A document from your business confirming employment.
  7. After submitting both documents you will receive an email confirming your approval status within 1 business day.
  8. If you require additional assistance while signing up for an SCP account, email [mcfonboarding@amazon.com](mailto:mcfonboarding@amazon.com).

## Create listings

SCP can only be used to create listings for products dedicated for fulfillment
with MCF, for orders from non-Amazon sales channels. To create a SCP listing,
follow these steps:

  

  1. [Sign in to your SCP account](https://supplychain.amazon.com/login).
  2. Navigate to the **Inventory** tab in the main menu.
  3. Click **Add product** , then **Add a product by category**.
  4. **Search** or **Browse** for the product type that you would like to list.
  5. Enter the product identity details (Name, Brand, Product ID, Manufacturer, and so on).  

    1. Select **n/a** for Product ID if you do not have a registered GTIN or UPC
  6. Enter the selling details (SKU and Item Value)
  7. Enter the product description (Description, Bullet Point, Color, and so on).
  8. Enter product safety and compliance details (Battery, Hazmat, Country/Region of Origin).
  9. Upload product image
  10. Enter shipping details (Package Length, Package Width, Package Height, Package Weight, and so on).
  11. Click **Submit** to create listing.
  12. Once processed, listing details and status will be available in **Inventory** , then **All Inventory** from the side menu.  

    1. If an “issue found” message is shown in the **Status** column, select **Edit listing** to correct the listing or provide additional documents.

**Note:** It may take up to 24 hours for newly submitted SCP listings to be
processed and appear on the Inventory page. The ability to create listings
with bulk upload will be available as soon as the feature is visible on the
Add Products page.

## Dangerous goods

Dangerous goods (also referred to as hazmat) policies apply to all listings
created in Supply Chain Portal. Amazon will internally classify your product
into the correct regulatory control classes based on the product information
provided. Failing to provide the correct hazmat information may cause your
product to be delayed or denied to be received by Amazon's fulfillment
network. For more information go to [Dangerous goods required information and
documentation (hazmat)](/gp/help/G201371860).

SCP listings that require additional documentation or corrections will display
an “issue found” message. To resolve this, follow these steps:

  

  1. Navigate to the **Inventory** tab in the main menu.
  2. Click **All inventory** , then locate the **Listing** with an “issue found” in the **Status** column.
  3. Select **Edit listing**.
  4. Upload missing **Dangerous goods classification documents**.
  5. Click **Save product**.
  6. If you require additional assistance, navigate to the **Support** tab in the main menu and select **Contact Us**.

## Restricted products

Any items that cannot be listed on Seller Central because they are included on
Amazon's [restricted products](/gp/help/G200164330) list, such as weapons,
offensive material, and controlled substances, are also not allowed to be
listed using SCP.

Additionally, any items that are not eligible for to be Fulfilled by Amazon
due to [FBA product restrictions](/gp/help/G200140860), such as alcoholic
beverages, gift cards, and counterfeit items, are also not allowed to be
listed using SCP.

## Send inventory

When you’re ready to send inventory to Amazon, initiate the [Send to
Amazon](/gp/help/G6925SDD66GDLXJW) process in SCP by following these steps:

  

  1. [Sign in to your SCP account](https://supplychain.amazon.com/login).
  2. Navigate to the **Shipments** tab in the main menu.
  3. Click **New shipment** and select **Supply Chain Portal listing** from the window.
  4. Complete the Send to Amazon workflow for your shipment. For step by step instructions, go to [Create shipment with Send to Amazon](/gp/help/G6925SDD66GDLXJW).  

    1. All SCP items are currently required to be labeled with an [Amazon barcode](/gp/help/G200141490) so that they can be tracked throughout the fulfillment process.
  5. You can view in progress, in transit, or completed Send to Amazon workflows by returning to the **Shipments** tab.

**Note:** If you sell on Amazon, you can initiate a shipment for FBA inventory
in SCP by selecting Seller Central listing in step 3, but combined inbound
shipments for Seller Central listings and Supply Chain Portal listings is not
currently supported.

## Create orders

You can create MCF orders in SCP through the [quick order
form](/mcf/orders/create-order), [bulk order upload](/mcf/orders/bulk-orders),
or [API integrations](https://supplychain.amazon.com/integrations). The [quick
order form](/mcf/orders/create-order) allows you to place a single MCF order
against available SCP inventory by entering your customer's shipping address,
items, and delivery speed. To create or cancel multiple orders at once, upload
a completed template to the [MCF bulk orders form](/mcf/orders/bulk-orders).

In the quick order form, if you select **Create hold order** , an order will
be planned and placed on hold, reserving your inventory. These hold orders
must be activated on the MCF order details page to initiate the delivery. The
order will meet the expected delivery date only if activated before the
expected ship date. If the hold order isn't activated within 14 days, the
order will be canceled automatically.

To activate a hold order, follow these steps:

  

  1. [Sign in to your SCP account](https://supplychain.amazon.com/login).
  2. Go to [Manage orders](https://supplychain.amazon.com/orders).
  3. **Select a time frame** or in the search box, enter the MCF order ID and click **Search**.
  4. Click the order ID link in the **Order details** column.
  5. On the MCF order details page, click **Ship this order**.

## Track orders

To track MCF orders in SCP, follow these steps:

  

  1. [Sign in to your SCP account](https://supplychain.amazon.com/login).
  2. Go to [Manage orders](https://supplychain.amazon.com/orders).
  3. **Select a time frame** or in the search box, enter the MCF order ID and click **Search**.
  4. Click the order ID link in the **Order details** column.
  5. On the MCF order details page, click the **Shipment** tab to view the details for the order.

For each delivery, the send date, delivery estimate, tracking number, and
carrier information will be available, along with the package contents.

Click the tracking number to view tracking details on
[Swiship](https://www.swiship.com/track/), our tracking website. Swiship
provides real-time status updates for packages, which can be shared with
buyers. Alternatively, to view the tracking details on your selling account,
click the **Shipment** tab on the MCF order details page and click **Shipping
event details**. For more information, go to [How to track your Multi-Channel
Fulfillment orders](/learn/how-to-track-your-mcf-orders).

Tracking numbers generated by our system expire after 90 days. If a tracking
number has expired, the tracking details may not be available on Swiship.

## Cancel orders

To request an order cancellation in SCP, follow these steps:

  

  1. [Sign in to your SCP account](https://supplychain.amazon.com/login).
  2. Go to [Manage orders](https://supplychain.amazon.com/orders).
  3. **Select a time frame** or in the search box, enter the MCF order ID and click **Search**.
  4. Click the order ID link in the **Order details** column.
  5. On the MCF order details page, click **Cancel this order** , if available.

**Note:** Clicking **Cancel this order** only submits a request and doesn’t
guarantee a cancellation. Cancellation success depends on how far an order has
progressed in the fulfillment process and will be confirmed by email. If there
are multiple deliveries in an order, the cancellation request for each
delivery will be treated independently.

**Cancel this order** may not appear in certain cases. For example, it may not
appear if the order was already packed, or if a tracking number was generated
and the order was sent. In these cases, the order can't be canceled.

You aren't charged for MCF orders that are successfully canceled before being
sent for delivery. If some items in an order have been sent, or have returned
to Amazon before reaching the buyer, fees for those items will apply. MCF
doesn’t offer the option to intercept an order after it’s been sent.

Once an MCF order has been submitted, the order details can’t be changed,
including the products, quantity, recipient name, and delivery address. Before
you place an order, make sure that you confirm with the buyer that the address
provided is accurate. Amazon is not responsible for any delivery failures that
result from incorrect information submitted during order creation. Such orders
are ineligible for reimbursement.

For additional Supply Chain Portal information, including fulfillment fees,
order management, and reimbursements, go to [Supply Chain Portal: Fees,
settings, and support](/gp/help/GYRBCGWNF66MHL7G).

