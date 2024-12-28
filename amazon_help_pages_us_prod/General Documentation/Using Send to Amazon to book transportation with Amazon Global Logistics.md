---
title: Using Send to Amazon to book transportation with Amazon Global Logistics
url: https://sellercentral.amazon.com/help/hub/reference/GV6DMTQ3AKGYUWWN
section: General Documentation
---

**Overview**

Use [Send to
Amazon](https://sellercentral.amazon.com/fba/sendtoamazon/confirm_shipping_step?wf=wff802f775-42ef-48db-9055-9bd8898730b3),
a streamlined shipment creation workflow that replaces the Send/replenish
inventory workflow, to replenish your Fulfillment by Amazon (FBA) Inventory.

With Send to Amazon, you can:

  * **Save time creating shipments** with simplified process steps.
  * **Create reusable case pack templates** to provide box content information, box weight and dimensions, and prep and labeling details for shipments of single-SKU boxes. The templates are ideal when you use the same box configuration for a SKU because you won't have to re-enter the details each time you replenish inventory.
  * **Pack single-SKU and mixed-SKU boxes** before you create shipments, and update quantities as you pack, before you confirm your shipment destinations.
  * **Compare and choose the best shipping mode and shipping speed**. Based on your inventory and expected in-stock date, you can select shipping mode (Ocean FCL, Ocean LCL, Air freight) and shipping speed (standard, fast) based on your inventory and expected in-stock date.

## Book shipments using Send to Amazon

**There are two ways you can access the Send to Amazon workflow:**

  

  1. Navigate to **Inventory** , then select **Manage FBA Inventory** in Seller Central.
  2. Or select **Send to Amazon** in the upper left hand corner on the Shipping Queue page.

**Step 1 - Choose inventory to send**

  

  1. **Select your Ship from address.** This is the address from where you’ll send your inventory. By default, the last address you shipped from will appear. You can change this address by clicking **Ship from another address**.

**Tip:** Amazon requires an accurate **Ship from** address to ensure proper
placement of your inventory and accurate shipping charges. Please be sure to
double-check your **Ship from** address as you will not be able to change it
once you confirm your shipments in **Step 2**.

  2. Make sure you have checked the “I want to ship with Amazon Global Logistics program” checkbox.
  3. **Choose inventory to send.** You can add inventory by either selecting from a list of available Fulfillment by Amazon (FBA) SKUs or by uploading SKUs in bulk using a template.  

    1. **Select from list:** If the contents, weights, and dimensions for your single-SKU boxes don’t change frequently, we recommend choosing this option to create case-pack templates for those SKUs that you want to send to Amazon. If you are shipping mixed-SKU boxes (boxes that contain more than one SKU), or single-SKU boxes that change from shipment to shipment, you can select **Individual units** from the **Packing details drop-down menu.**   

      1. **Add single-SKU boxes to a workflow.** If the contents, weights, and dimensions for your single-SKU boxes don’t change frequently, we recommend that you create case pack templates for those SKUs that you want to send to Amazon.

Create a case pack template:  

        1. From the Packing details drop-down menu, select **Create new case pack template** for the SKU you want to work on.
        2. Enter the following information into the template:  

          1. Packing template name: Name the template so that you can tell it apart from others you may create for the same SKU.
          2. Units per box: The number of sellable units in each shipping box. A sellable unit is the item that a customer can buy. For example, a pack of ten pens sold together is one sellable unit.
          3. Box dimensions: The outside dimensions of the shipping box.
          4. Box weight: The total weight of a packed shipping box, including dunnage.
          5. Prep for each unit: The packaging and prep requirements for your SKU.
          6. Who preps units (if required): Choose By seller if your units will be prepped before they arrive at the fulfillment center. Choose By Amazon to opt in to the FBA Prep Service.
          7. Who labels units (if required): Choose By seller if your units will be labeled before they arrive at the fulfillment center. Choose By Amazon to opt in to the FBA Label Service. Labeling with an Amazon barcode may not be required if your inventory is tracked with FBA virtual tracking.
        3. Select **Save**.
        4. Once you have created a case pack template for a SKU, enter the number of boxes that you want to send. With the correct case pack template selected under Packing details, enter the Number of boxes to send for the SKU that you want to send.
        5. If an expiration date is required for your product, you will be prompted to enter it. For more information, go to [Expiration dates on FBA products](https://sellercentral.amazon.com/help/hub/reference/201003420).
        6. Select **Ready to send**.

If you have more than one box configuration for a SKU, you can add a second
packing line by following the steps below:  

        1. Select Additional inputs in the Information/action column to expand it.
        2. Select Add packing line.
        3. From the Packing detail drop-down menu, select either a case-pack template or individual units.
        4. Enter the Quantity to send and confirm.

**Note:** Each pack line can have different expiration dates. Currently, there
is a maximum of two packing lines per SKU.

      2. **Add individual units to a workflow.** If you are shipping mixed-SKU boxes (boxes that contain more than one SKU), or single-SKU boxes that change from shipment to shipment, follow the steps below:  

        1. From the Packing details drop-down menu, select Individual units for the SKU you want to work on.
        2. Enter the following information into the template:  

          1. Prep for each unit: The packaging and prep requirements for your SKU.
          2. Who preps units (if required): Choose By seller if your units will be prepped before they arrive at the fulfillment center. Choose By Amazon to opt in to the FBA Prep Service.
          3. Who labels units (if required): Choose By Seller if your units will be labeled before they arrive at the fulfillment center. Choose By Amazon to opt in to the FBA Label Service. Labeling with an Amazon barcode may not be required if your inventory is tracked with FBA virtual tracking.
        3. Select **Save**.
        4. When you are done, enter the number of units for each SKU that you want to send to Amazon.
        5. If an expiration date is required for your product, you will be prompted to enter it. For more information, go to [Expiration dates on FBA products](https://sellercentral.amazon.com/help/hub/reference/201003420).
        6. Select **Ready to pack**.
    2. **File upload.** If you have hundreds of SKUs, we recommend choosing this option to upload a file with dimensions and weights.x  

      1. **Add inventory in bulk using a template file.** If you have hundreds of SKUs, we recommend choosing this option to upload a file with dimensions and weights. To add inventory to a workflow in bulk using a template, choose **File upload** as your SKU selection method. To create and upload the file, follow the steps below:  

        1. **Generate and download the template.**   

          1. Choose optional columns to add to your template:  

            1. Choose **Case pack information** if one or more of your SKUs will be packed in single-SKU shipping boxes. You can enter box content information, weights, and dimensions in the template so that you won't need to re-enter this information during the workflow.
            2. Choose **Expiration date** if one or more of your SKUs require an expiration date. You can enter the expiration date information for your inventory in the Excel template.
          2. Select **Generate and download file**.
  

      1. **List your SKUs in the spreadsheet.** The downloaded template has tabs with instructions, data definitions, examples, and a blank spreadsheet to create your workflow.  

        1. Review the instructions and data definitions.
        2. Fill out the spreadsheet and list your SKUs in the **Create workflow – template** tab. Individual units and case packed SKUs can be listed together in the **Create workflow – template** tab. The spreadsheet will include the optional columns that you selected when you generated the template.
      2. **Upload your completed file.** After you have filled out all of the required information, choose one of the following save options:  

        1. Save the entire spreadsheet in .xlsx format. Do not rename the tabs or change the structure of the cells in the spreadsheet.
        2. Save the **Create workflow – template** tab in .txt format. Do not change the structure of the cells in the tab.
      3. Select **Upload completed file** and choose your file. 

This can take a few minutes depending on file size. Don’t refresh or leave the
page while the upload is in progress.

**Note:** If the information is accurate, the **SKUs ready to send** tab opens
for you to review all the SKUs. If there are errors, they will appear in the
**SKUs requiring attention** tab. You must either resolve the error or remove
the SKU from the workflow before you can proceed to the next step.

  4. **Label your units.** If you selected **Seller as the labeling owner** and your SKU requires Amazon barcodes (FNSKU labels), select **Print SKU labels** in the **Information/action** column, and then apply the printed labels. You can also print all of the unit labels for a shipment by selecting **Print all SKU labels** at the end of this step.

Each item that you send to a fulfillment center requires a barcode, which we
use to identify and track inventory throughout the fulfillment process. For
more information, go to [FBA product barcode
requirements](https://sellercentral.amazon.com/gp/help/G201100910).

  5. After you have chosen which inventory to send, select Confirm and continue to book your transportation with Amazon Global Logistics.

**Step 2 - Confirm shipping**

  

  1. **Make sure you’ve selected Amazon Global Logistics (recommended) to confirm shipping through the Send to Amazon workflow on Seller Central.** If you want to book transportation on Shipper Central, you can select **Book transportation through Shipper Central?** In the popup window, select **Confirm booking through Shipper Central**.

Why confirm shipping through STA on Seller Central?

     * Seller Central is a one-stop shop that allows you to manage your inventory and book transportation in one portal.

Why confirm shipping through Shipper Central?

     * Shipper Central is open to both FBA sellers and individuals who do not manage the inventory, but assist with the booking, invoicing, and shipment tracking. Shipper Central users can create Amazon Global Logistics bookings that consolidate multiple FBA shipments, including those from different seller accounts. Also unlike Seller Central, where sellers need to create separate accounts for each marketplace and country, Shipper Central allows sellers to book transportation for all countries using a single account.

  2. **Under Shipping mode and details, choose your preferred shipping mode to see typical transit times.** Then enter or select the following:
     * Origin city
     * Cargo ready date
     * Incoterms (see “Booking terms” below for more information)
     * Any value-added services (optional)
     * Your preferred currency to make payments: US dollars (USD), Chinese yuan (CNY), British pounds (GBP), or Euros (EUR).
  3. **After you’ve entered all the info above, select** **Update shipping cost**. An estimated delivery date and estimated cost for each shipping speed will be provided. You will also see a cost breakdown.
  4. After obtaining a quote, go to Shipping parties and product description and provide the following information:
     * Shipper
     * Importer of record (IOR)
     * Destination contact
     * Select **Who will act as the primary contact for your booking?**
     * Provide the product description. The description will be used to generate the bill of lading.

**Tip:** Make sure the information that you provide does not include
nicknames, slang, abbreviations, or other unclear references.

  5. After entering all the information for Shipping parties and product description, review the Total estimated shipping fees. Then select Accept charges and confirm shipping.

**Your booking has been submitted.** You can select Shipping queue to track
your shipments or select **New shipment** to start a new shipment.

**Step 3: Add customs information and print box labels**

Before printing box labels, you will need to provide transportation and
[compliance
documentation](https://sellercentral.amazon.com/help/hub/reference/G63ELGKVHKN2NPTF?ref_=xx_swlang_head_xx&mons_sel_locale=en_US&languageSwitched=1&).
Note: If you confirmed shipping in Shipper Central, you need to return to Send
to Amazon in Seller Central to print your box labels.  

  1. Provide the required transportation and compliance documentation to ship your goods.  

    1. **You can upload required transportation and compliance documentation by downloading the templates and then uploading them back into the system.** Alternatively, our operations team will send you an email asking for the required transportation and compliance documentation, where you can directly provide documentation.
    2. **If using Customs Document automation, you will be prompted to enter the customs compliance linformation.** After you enter in that information, your commercial invoice and packing list will be automatically generated instead of having to manually upload them as mentioned in Step 3.1.
  2. Select Print box label format and select Print.

**Step 4: Print pallet labels (optional)**

  

  1. Select Continue to print pallet labels—only if you will be packing your inventory on pallets for shipment.
  2. Enter how many pallets you will be sending, select the format, and then select Print.

## Booking terms

Before you book your first shipment with Amazon Global Logistics, make sure
that you understand these terms:

#### Cargo ready date

The date your cargo is ready to ship from your supplier or shipper. This date
may differ from the date that your cargo is shipped or picked up.

#### Shipping mode

The method that you choose for shipping freight: ocean less-than-container
load (LCL) or air.

#### Port of departure

The port of origin from which your cargo departs.

#### Container freight station (CFS)

The location where ocean freight is consolidated, processed, and readied for
transfer to a container yard.

#### Container yard (CY)

The location within a port where ocean freight is staged for shipment.

#### Shipping order

A document provided by the carrier confirming that a shipment has been
received.

#### Port delivery date

The date your cargo needs to be delivered to the port of departure.

#### Incoterms

Commercial terms published by the [International Chamber of Commerce
(ICC)](https://iccwbo.org/resources-for-business/incoterms-
rules/incoterms-2020/) that are used widely for global trade. A description of
each is available on the [ICC website](https://iccwbo.org/resources-for-
business/incoterms-rules/incoterms-rules-2010/) (note that the 2010 edition of
incoterms remains valid).

## Frequently asked questions

#### Who can use Send to Amazon now?

Currently all Amazon Global Logistics sellers are able to use [Send to
Amazon](https://sellercentral.amazon.com/fba/sendtoamazon/)as of January 2022.

#### If I have questions specifically for Amazon Global Logistics when I book
transportation in Send to Amazon, how can I get help?

You can contact the Amazon Global Logistics customer support team by
submitting a ticket. To submit a ticket, you can select **Help** at the top-
right corner of any page on Seller Central. Then select **Get Support** at the
bottom of page. Then select **Selling on Amazon** and enter in the details of
your issue. Or select **Or, browse for your issue in the menu link** and
select the topic related to your question.

#### If a booking created in Send to Amazon workflow is canceled, will the FBA
shipment be canceled?

Yes, once your booking is cancelled, the system will automatically cancel the
FBA shipment.

#### Are the rates for air and ocean transportation the same in both the Send
to Amazon workflow and the old Send/replenish workflows?

Yes, the rates for all shipping modes and ship options are the same in both
workflows.

#### How can I provide feedback to Amazon?

You can provide feedback in two ways.

  * You can select **Your feedback is important** that appears at each step of the Send to Amazon workflow. There you can provide a rating and more detailed feedback.
  * After you submit a booking, a popup window will appear. Select a star rating on a scale from 1-5 and provide text feedback.

