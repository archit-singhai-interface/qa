---
title: Send to Amazon: Tracking details
url: https://sellercentral.amazon.com/help/hub/reference/GWKTQ4PADXXT58JY
section: General Documentation
---

In this step, you can provide tracking information for your shipments if
you’re using a non-partnered carrier.

  * Step 1 – [Choose inventory to send](/gp/help/G8SXKYFWPG6DAW6T)
  * Step 1b – [Pack individual units](/gp/help/GQ2HY393LHXF3GZN)
  * Step 2 – [Confirm shipping](/gp/help/GWC4BVUFCZ2FKHQW)
  * Step 3 – [Print box labels](/gp/help/GCUH6KKZA6PRA4E7)
  * Step 4 – [Confirm carrier and pallet information](/gp/help/GBJBZ65P2LHZM2DG) (for pallet shipments only) 
  * Step 5 – [Print pallet labels](/gp/help/GV42EVAG2U5ACZAQ) (for pallet shipments with an Amazon partnered carrier only)
  * **Final step – Tracking details** (and delivery window updates for small parcel and pallet shipments that aren’t using an Amazon partnered carrier)

##

If you’re using an Amazon partnered carrier, we’ll generate the carrier
tracking ID information for you, which you can review in this step. No action
is required by you.

If you’re using a non-partnered carrier, and the carrier shares the
information with you, provide the tracking IDs for all of the boxes in your
shipments. You can provide details either in the Send to Amazon **Tracking
details** step or in the **Track shipment** tab of the **shipment summary**
page.

To provide carrier tracking IDs using Send to Amazon, follow these steps:

  1. In the final step of the workflow, **Tracking details** , select the shipment that you want to provide tracking details for.

  2. Use one of the following methods to provide tracking IDs:
     * Type the tracking IDs individually.
     * Use a barcode scanner to scan shipping barcodes from the box label. 
     * Upload the tracking IDs for a shipment in bulk by selecting **Upload tracking IDs in bulk** and then following the steps on the **Tracking details** page.

  3. Ensure that the tracking IDs are mapped to the correct FBA box ID label on each box.

**Note:** To avoid errors when updating tracking ID information, follow all
alerts and prompts to validate your entries.

Once you’ve entered valid tracking details, the status of your shipment will
change from **Ready to ship** to **Shipped**.

##  Pallet shipments using a non-partnered carrier

If your non-partnered carrier shares the freight bill (PRO) number with you,
provide this information on the **Tracking details** page by following these
steps:

  1. In the final step of the workflow, **Tracking details** , select the shipment that you want to provide tracking details for.

  2. Enter the **PRO/freight bill number** for the shipment in the text box.

**Note:** To avoid errors when updating tracking ID information, follow all
alerts and prompts to validate your entries.

Once you’ve entered valid tracking details, the status of your shipment will
change from **Ready to ship** to **Shipped**.

## Delivery windows

If you ship with a non-partnered carrier, you must provide a delivery window
in step 2 for small parcel delivery or step 4 for less-than-truckload
shipments. You can update the delivery window in the **Track details** step up
to the start of the window. Once your window starts, it’s locked so that we
can use the information for planning purposes.

## Frequently asked questions

#### Why is it important to provide tracking details?

With the carrier name, shipping method, and tracking information that you
provide, we can pass any scan events that the carrier made available along to
our fulfillment centers. This will help us plan efficiently for receiving your
inventory, minimizing delays, and making in-transit inventory available sooner
for sale to your customers.

#### How do I edit my carrier name or tracking ID?

You can update your carrier name and tracking information any time before your
shipment is delivered to our fulfillment center by following these steps:  

  1. Access your shipment from the Shipping Queue through one of the following methods:
     * If the shipment hasn’t shipped yet, select it from the list. This will bring you to the final step of the Send to Amazon workflow, **Tracking details**. 
     * If the shipment has shipped, click **Track shipment** for the shipment that you want to update. This will bring you to the shipment summary page. Click the **Tracking events** tab. 
  2. Click **Change carrier**.
  3. Select a new carrier from the list, or select **Other** if your carrier isn’t listed. We’ll add more carriers to the list over time.
  4. Click **Update**.

**Note:** If you use integrators such as Amazon Marketplace Web Service APIs,
you must submit updated tracking information.

#### Why did I receive an error message that a unique tracking ID is required?

This error message occurs when you enter the same tracking IDs for different
boxes in a small-parcel shipment. We require a unique tracking ID per box for
these shipments. Some carriers provide a master tracking ID, however they
should also provide a unique ID per box. If you did not receive all of the
tracking IDs from your carrier, visit the carrier’s website or contact the
carrier to get a full list of box tracking IDs.

#### What should I do if my carrier does not provide a tracking ID?

We encourage you to use carriers who provide tracking information for
delivering shipments. These carriers provide real-time status to Amazon and
can help minimize receive delays and avoid out of stock risk.

#### Why did I receive an error message about an invalid tracking ID?

This error message appears when the tracking ID that you provided is either
invalid or does not match the carrier that you selected. To fix this error,
make sure that you’re not entering any blank spaces before or after the
tracking ID, and that the carrier that you selected matches the tracking ID.

You can change your carrier in the final step of Send to Amazon, **Tracking
details**. To navigate to this step, click the shipment name link on the
Shipping Queue page. If the shipment is in **Working** or **Ready to ship**
status, you’ll be directed to Send to Amazon and you can navigate to the final
step. If your shipment is in a different status, you’ll be directed to the
shipment summary page. At the top of the page, click the **Send to Amazon
(view)** link and navigate to the final step of the workflow.

#### For international shipments, it can take more than a month for my freight
forwarder to provide tracking information. Is that too late?

No. Enter the tracking information for the shipment as soon as your carrier
shares it with you, before your inventory is delivered to our fulfillment
center.

#### Is Amazon going to monitor my performance? If yes, where will I see it?

Yes. We evaluate your defect rate for missing tracking information at the
shipment level, for all shipments that you send to us using non-partnered
carriers. You’ll be able to view defects in the **Problems** tab of the
**shipment summary** page.

Initially, only the defect information will be shown. In the future, you may
be required to acknowledge each defect before you can create new shipments.

We may reach out to you for one-on-one seller coaching if your coaching defect
level reaches **Elevated**. We may restrict you from creating new shipments to
Amazon for 24 to 72 hours if your coaching defect level reaches **Critical**.

For more information, go to [Resolving inbound performance
alerts](/gp/help/G3FFQ2AHWU69GTDW) and [Performance
coaching](/gp/help/G5H26MCVJG4B82ST).

#### How do I update my delivery window information if it has changed?

You can edit your delivery window in this step up to the start of the window.
Once your window starts, it’s locked so that we can use the information for
planning purposes.

#### What happens if I provide an inaccurate delivery window?

If the window hasn't started yet, you can update the date range. If you miss a
delivery window, we’ll notify you in the Shipping Queue so you can work with
your carrier to provide more accurate estimates for future shipments. There is
no penalty or enforcement.

