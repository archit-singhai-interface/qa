---
title: Reconcile your shipment
url: https://sellercentral.amazon.com/help/hub/reference/G201214140
section: General Documentation
---

This page explains how to use the shipment reconciliation tool to identify and
resolve any discrepancies between what is listed in your shipping plan and
what is received at the fulfillment center.

Follow these steps to navigate to the shipment reconciliation tool:  

  1. From the drop-down menu in Seller Central, select **Inventory** , and then select [Shipments](/gp/fba/inbound-queue/index.html/ref=ag_xx_cont_fbashipq).
  2. Find your shipment and click **Track shipment**.
  3. In the shipment summary, click the **Contents** tab.

After your shipment has arrived at an Amazon fulfillment center, the
**Contents** tab on the **Shipment summary** page will display the status of
the units as they are received. If there are any differences between what you
have sent in the shipment and what is received, use the tools within the
**Contents** tab for the following:

  * Get detailed information about discrepancies between your shipping plan and what the fulfillment center received
  * Provide more information about the shipment contents
  * Request an investigation into missing or unexpected items

Reconciliation of shipped inventory usually takes 2 to 30 days. In some cases,
it will take up to 60 days. You can track the status of your shipment in the
**Shipping Queue** with the status cycling through In Transit, Delivered,
Checked-In, Receiving, and finally Closed. To learn more, go to [How Amazon
receives and stores your inventory](/gp/help/G201081250).

## Is your shipment eligible for investigation?

[Sign in](/gp/sign-in/sign-
in.html?destination=/gp/help/201214140?ref=efph_login_wf_201214140) to use the
tool below to check if your shipment is eligible for investigation and get
personalized help (desktop browser required).

A shipment can only be eligible for reconciliation when the status is
**Closed**. The eligibility date shown in the shipment reconciliation tool is
an estimated date for when your shipment will be ready for investigation. If
your shipment is not eligible for reconciliation, it may be for one of several
reasons:

  * The shipment is still being processed by the fulfillment center.
  * The shipment has not been delivered to the fulfillment center.
  * Pending confirmation on the final unit counts during receiving stage of your shipment.
  * Additional units found that may be part of your shipment requiring extra time to process.
  * The shipment contents have been received in full or have been reconciled.

To get tips for avoiding discrepancies and ensuring that your FBA shipments
are eligible for reconciliation, view the following tutorial:

## Steps for shipment reconciliation

To reconcile your shipment, take the following steps on the **Contents** tab.
For details of each step, refer to the sections below.

  * **Step 1: View discrepancies and request research**
    * View the Units located messages
    * View the Status messages
    * Request research
  * **Step 2: Upload documents**
  * **Step 3: Provide additional information**
  * **Step 4: Preview and submit your request**

## View the Units located messages

The discrepancy column shows the difference between the units expected and the
units located, which can be found under the **Units expected/Units located**
column. By hovering over the units located number, you will be able to find
additional information about the received and reconciled units.

Units Located Messages | Description  
---|---  
Received | These products are accounted for through the standard receiving process. The received quantity is displayed on the **Contents** tab.  
Reconciled | When possible, we investigate product discrepancies automatically and add or remove the reconciled units from your shipment.  
Reimbursed | If Amazon accepts responsibility for lost or damaged products, they are accounted for as reimbursements. Reimbursement amounts are listed on the **Transactions View** tab of the **Payments** report.  
Units located | Units located are units that Amazon has already received and units updated during reconciliation. All located units are available for sale.  
Units not shipped | Units that have not shipped.  
Acknowledged fewer units were sent | Seller acknowledged they sent fewer units than they originally put when creating the shipment.  
Acknowledged extra units were sent | Seller acknowledged they sent more units than they originally put when creating the shipment.  
Not eligible for reimbursement | Units that were deemed ineligible for reimbursements.  
Inventory adjusted due to a receive error | Inventory transferred back to the seller as an ownership transfer adjustment in place of a receive.  
Received on shipment FBAXXXXXX | Units that have been reallocated from a different shipment for the same seller.  
Different item received on shipment FBAXXXXXX as FNSku BXXXXXXXX |  Extra units of a different item received on the same shipment. or Extra units of same item but with different SKU received on the same/different shipment  or A different shipment that corresponds to the shortage on this shipment (a.k.a, item substitution).  
  
## View the Status messages

The status column is used to understand the state of each product in your
shipment to Amazon.

Status Messages | Description  
---|---  
Receiving | The product is being received.  
Action required | The product has a discrepancy that is eligible for research. Every product with this status must have an option selected from the dropdown menu before you can preview and submit the research request.   
Units located. No action required | The product does not have a discrepancy, since it was received in full or has been reconciled automatically. No action is necessary.  
Pending dangerous goods (hazmat) review | To ensure that the inventory in our fulfillment centers is safe for customers and transport, your products may be reviewed for compliance with our requirements for dangerous goods. While these products are under review, they cannot be received at the fulfillment center. Learn more about the [FBA dangerous goods review process](/gp/help/G201749580).  
Investigation completed - shipment contents counted and confirmed |  Amazon has investigated the delivered boxes or pallets and associated units. When you see your items marked as **Investigation completed** , it means Amazon physically counted the units upon receipt. In these scenarios, when the receiving process starts at our fulfillment centers, Amazon first matches all the received boxes with the boxes expected according to your shipping plan. Amazon then proceeds to physically count all the units being stored. When all the boxes are successfully matched and the physical count is completed, that's when items are marked **Investigation Completed – shipment contents counted and confirmed** in Seller Central. These products are no longer eligible for research. If you have information that will help locate any of these missing units, contact Selling Partner Support. If we locate the missing units, we will add them to your inventory. Otherwise, we will deem the units short-shipped and a reimbursement cannot be issued.   
Case submitted | The product has already been submitted for research using the **Contents** tab, so no further action is required.  
Claim window expired | The claim window has expired for the shipment per the [FBA inventory reimbursement policy](/gp/help/G200213130).  
Automatically closed after 45 days (domestic shipment) and 75 days (international shipment) for all shipments created after February 1, 2024. | The shipment was automatically closed. For more information, go to [Track your shipment: Shipping Queue and Shipment Summary](/gp/help/G201022330).  
  
Why do I see my product being received as merchant SKU
“Amazon.Found.Bxxxxxxxxx”?

When your product is not labeled correctly is received as non-labeled
inventory for the same ASIN with merchant SKU as Amazon.Found.Bxxxxxxxxx Or,
if you ship a different product than what we expected to receive and it is not
the same ASIN, the received product is assigned to you as merchant SKU
Amazon.Found.Bxxxxxxxxx. These merchant SKUs are created so that your product
can be assigned back to your account. Since these are your products, you can
sell them to customers by creating an offer listing for the
Amazon.Found.Bxxxxxxxxx merchant SKU. These products will appear in Stranded
inventory report if you do not have an active listing for
Amazon.Found.Bxxxxxxxxx. If you create a listing for the
Amazon.Found.Bxxxxxxxxx merchant SKU, your inventory for this merchant SKU
will be subject to virtual tracking. Rest of your labeled inventory is not
affected.

## Request research

Products in the shipment that are eligible for additional research will have
"Action required" options for you to select from in the **Status** column.
Every product with a status of "Action required" must have an option selected
from the dropdown menu before you can preview and submit the research request.

Action required options | Description  
---|---  
Units not shipped | You have confirmed that you or your supplier did not ship these units or shipped a different product instead.  
Research missing units | You have confirmed that these units were included in your shipment, and you need Amazon to research further.  
Extra units shipped | You have confirmed that you or your supplier included extra units or a different product than was originally recorded on your shipment.  
Research extra units | You have confirmed that these units were not included in your shipment, and you need Amazon to research further.  
  
**Note:** Before submitting a request for research, reconcile any
discrepancies in your shipment by confirming if units were not shipped or
extra units were shipped. After a research request has been submitted, Amazon
will confirm the quantities received and attempt to reconcile units not
shipped with extra units shipped. These reconciliations will not affect your
available inventory.

## Upload documents

Click **Choose File** to select all documents and **Upload** to attach
documents to the research request. Certain documents are required for Amazon
to research the discrepancies; uploading them will help Amazon work on the
research request.

Amazon requires both proof of inventory ownership and proof of delivery to be
submitted with the research request:

  * Proof of inventory ownership: this will help identify any potential discrepancies that may have occurred. Examples of acceptable documents for proof of inventory ownership include an invoice from a supplier, receipt from another seller, or signed packing slip only if you are a manufacturer.
    * If you use an invoice as the proof of inventory ownership, the following information must be provided:
      * Date of purchase
      * Product names matching the missing products
      * Quantity purchased
    * If you are the manufacturer, you can send a copy of the signed packing slip as proof of ownership. The packing slip must include the following information:
      * Packing list date
      * Shipment or purchase order ID
      * Product names of the missing items
      * Quantity shipped
      * Manufacturer signature or stamp
  * Proof of delivery: For LTL or FTL shipments, a bill of lading showing the number of boxes in the shipment and the total weight when it was picked up by the carrier. The document must be stamped by Amazon confirming that the shipment was received and signed for at the fulfillment center. Your carrier should have a copy of this document. This information helps verify that the entire shipment was picked up and shipped as expected. 

**Tip:**

If you provided a receipt or invoice as proof of inventory ownership, the
price you paid for the items is not required and may be hidden or obscured.

We do not accept pro forma invoices or similar contracts as proof of ownership
because they don’t demonstrate a completed purchase.

Invoices and packing slips must be in a non-editable format. Invoices must be
clearly created by a supplier or manufacturer. Please note that we do not
accept documents in Excel, Word, or other editable formats. We therefore ask
you to provide us with a scanned copy or picture of the original invoice in
PDF, JPG, JPEG, PNG, or TIFF format.

## Provide additional information

For any additional discrepancies, you can ask Selling Partner Support to
investigate. Describe the discrepancy in the form provided. This information
helps Amazon complete the research and resolve issues as quickly as possible.

Information type example | Description  
---|---  
Any known discrepancies  | Did you or your supplier ship more or fewer units than you originally expected? Did you or your supplier ship the wrong product?  
A description of the shipping boxes  | Amazon does a physical check at the fulfillment center, so information about the color, size, or any distinguishing marks on your shipping boxes can help us find them more quickly.  
Product codes  | Verify the UPC, EAN, or JAN on your products. Does it match the product code shown in Seller Central?   
Any prep activity that was missed  | An item that was not properly prepped before being shipped can cause delays in the receiving process, as we must prep the item for you.   
  
## Preview and submit your request

After you have classified the discrepancies remaining on your shipment, click
**Preview your request** , review the information, and, if everything is
correct, click **Submit Request**. The submission will create a case with
Selling Partner Support for the products that require research.

After submitting the request, you will be provided with a case number, which
will also be shown in the **Contents** tab when you next visit the page. You
can watch for status updates and communications by clicking on the case number
or going directly to your [Case Log](/cu/case-
lobby?ref=xx_caselog_count_home).

