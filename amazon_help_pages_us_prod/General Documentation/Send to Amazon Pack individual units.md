---
title: Send to Amazon: Pack individual units
url: https://sellercentral.amazon.com/help/hub/reference/GQ2HY393LHXF3GZN
section: General Documentation
---

## Create shipments and provide packing information

For eligible workflows, you can now create shipments based on SKUs and
quantities. If your workflow does not contain any SKU case packed or packed
with pallet template, if you have not chosen any cross-border transportation
programs (like Amazon Global Logistics), or your workflow is not for cross-
border shipments (refer to Frequently Asked Questions below), you can skip
providing the carton information in Step 1b and proceed to create shipments
based on the SKUs and quantities. If you choose to create shipments by
skipping Carton Level Information submission the existing Step 2 will change
to include 3 steps: Step 2a for confirming shipments; Step 2b for submitting
Carton Level Information for each shipment; Step 2c for confirming
transportation for each shipment.

After confirming your shipments splits in Step 2a, you will be able to proceed
to Step 2b. In Step 2b, you can submit Carton Level Information for each
shipment using excel sheet only. In Step 2b, you will not be able to edit SKU
quantities in shipments. You can edit the quantities as per the Edit policy in
Step 3.

**Note:** You will only be able to choose Freight for transportation if you’re
creating shipments before providing packing information. No Small Parcel
shipments are allowed, and we are working to enable additional functionality
in this flow.

## Provide packing information and Create shipments

In this step, you’ll provide box content information for the individual units
that you confirmed in the previous step, to be packed in mixed-SKU boxes.

  * Step 1 - [Choose inventory to send](/gp/help/G8SXKYFWPG6DAW6T)
  * **Step 1b - Pack individual units**
  * Step 2 - [Confirm shipping](/gp/help/GWC4BVUFCZ2FKHQW)
  * Step 3 - [Print box labels](/gp/help/GCUH6KKZA6PRA4E7)
  * Step 4 - [Confirm carrier and pallet information](/gp/help/GBJBZ65P2LHZM2DG) (for pallet shipments only) 
  * Step 5 - [Print pallet labels](/gp/help/GV42EVAG2U5ACZAQ) (for pallet shipments with an Amazon partnered carrier only)
  * Final step - [Tracking details](/gp/help/GWKTQ4PADXXT58JY) (for small parcel and pallet shipments not using an Amazon partnered carrier)

Watch the video for a quick overview, and read more information below.

Once you confirm the individual units of each SKU in step 1 of the workflow,
[Choose inventory to send](/gp/help/G8SXKYFWPG6DAW6T), we'll determine which
SKUs can be packed together and group them into pack groups.

Factors that determine which SKUs can be packed together include SKU weight
and dimensions, prep-and-labeling requirements and ownership, and whether the
SKUs are dangerous goods (hazmat) that require special handling at the
fulfillment center.

Once you pack your boxes according to the pack groups and provide box content
information for each pack group, we will determine the optimal shipment
destinations for your inventory. Placing your inventory closer to customers
can reduce the time to deliver orders for your products.

## Pack everything in one box

If all the SKUs in the pack group will fit into one box, follow these steps:

  1. Select **Everything will fit into one box** and click **Confirm**.

  2. Enter the **Box weight** , which is the total weight of a packed shipping box, including dunnage.

  3. Enter the **Box dimensions** , which is the outside dimensions of the shipping box.

  4. Click **Confirm packing information**.

**Note:** When you enter the box weight and dimensions, we compare those
figures with the units that you put into the box. We expect that the box
weight and volume will be no more than 10% less than the weight and volume of
all the units inside the box combined. If the figures aren’t as expected,
you’ll see a warning.

You can use this information to help prevent accidental errors, and to avoid
problems when you replenish your inventory. If you believe your input is
accurate and does not cause problems, you can ignore the warning.

## Pack in multiple boxes and submit box content information

If the SKUs in the pack group require more than one box, follow below steps to
provide box content information using either the web form or an Excel file or
Scan and Pack form:

**Important:**

  * When you enter the box weight and dimensions, we compare those figures with the units that you put into the box. We expect that the box weight and volume will be no more than 10% less than the weight and volume of all the units inside the box combined. If the figures aren’t as expected, you’ll see a warning. You can use this information to help prevent accidental errors, and to avoid problems when you replenish your inventory. If you believe your input is accurate and does not cause problems, you can ignore the warning.
  * For each pack group, keep track of which SKUs you pack into each box. Mark your boxes (for example, pack group 1–box 1, pack group 1–box 2) so that you can match the correct FBA box ID label to each box in step 3–[Print box labels](/gp/help/GCUH6KKZA6PRA4E7). Don’t mix SKUs from different pack groups into the same box.

**Provide box content information using the web form**

  1. Select **Multiple boxes will be needed** and click **Confirm**.

  2. Select **Enter through a web form** from the drop-down menu.

  3. Enter the estimated **number of boxes** that the SKUs in the pack group will fit into. This number will be used to generate a web form.

  4. Click **Open web form** and a pop-up window will open. In the top section of the pop-up, enter the number of units for each SKU per box. The total number of units you enter cannot exceed the number listed in the “Units boxed” column for that pack group. 

  5. You can update the box count in the web form by clicking on the plus/minus (+/-) icon at the top right.

  6. Below the SKUs, you’ll add information about box weight and dimensions.   

    1. First, enter the weights for each box in the pack group.
    2. Next, enter the box dimensions and mark the boxes that they apply to. If you are packing in boxes of different dimensions, you can click **Add another box dimension**. Enter the new dimensions and mark the boxes that the new dimensions apply to.

  7. Click **Confirm packing information**.

**Provide box content information using an Excel file**

  1. Select **Multiple boxes will be needed** and click **Confirm**.

  2. Select **Upload Excel file (.xlsx)** from the drop-down menu.

  3. Enter the estimated number of boxes required to fit all of the SKUs in the pack group. The estimate will be used to generate a pack-list spreadsheet. You can update the box count in the generated spreadsheet by up to 10 boxes.

  4. Click **Generate Excel file** to Download the pack-list template.

  5. Open the Excel spreadsheet and click **Enable editing**.    

    1. For each box, enter the number of units per SKU within each box. The **Boxed units** , which is the total number of units in each box, must not exceed the **Expected units** for a particular SKU in the pack group.
    2. Enter the weights and dimensions for each box in the pack group.

**Note:** The column headers and SKU details in the Excel file are password
protected, which means you cannot modify them. To enter box content
information, scroll to the right half of the page in the **Box packing
information** tab.

  6. Click **Upload and validate file**.

**Provide box content information as you pack using Scan and Pack**

You can provide the box content information as you pack using your barcode
scanner. Below are the steps for the same:

  1. Select **Multiple boxes will be needed** and click **Confirm**. 

  2. Select **Use Scan and Pack** from the drop-down menu.

  3. Enter the number of boxes required to pack contents in this pack group. You can add or remove boxes at a later point.

  4. Click **Open Scan and Pack** and a modal will open with the number of boxes you entered in previous step.

  5. On the modal, click the box that you are packing and the box will expand. 

  6. Scan the barcodes of the products in the expanded box. The SKUs and quantities will get added to the box.

  7. You can enter the weight and dimensions of the box next to the box title. Once you are done entering details of the current box, you can go to the next box by clicking on the new box or you can add a box by clicking on **Add a box**.

  8. You can either save the draft by **Save Form** or submit the details by clicking **Confirm packing details**.

**Note:**

  * You will be able to Confirm Packing details after submitting packing information for all SKUs in the pack group and submitting box weight dimensions for all boxes.
  * You can download the work-in-progress packing details through **Print Pick List**. You can use this as reference for reconciling your packing with the pack group SKUs.

## Pack in multiple boxes without providing box content information and pay
for Amazon to process the information

If the SKUs in the pack group require more than one box and you want Amazon to
manually process the contents of your box for a fee, follow these steps:

  1. Select **Multiple boxes will be needed** and click **Confirm**.

  2. Select **Amazon manually processes box content** from the drop-down menu.

  3. Enter **box count** , **dimensions** and **weight** for each box in the pack group.

  4. Review the **pack group manual processing fee**. For more information, go to [FBA manual processing fee](/gp/help/202061550).

  5. Click **Confirm manual processing**.

**Important:** If you choose not to provide box content information, Amazon
will manually process your boxes at the fulfillment center and a fee will
apply. Shipments that are manually processed may be received much slowly than
shipments with box content information.

## Pack in multiple boxes and use 2D barcodes to provide box content
information

If the SKUs in the pack group require more than one box, follow these steps to
provide box content information using 2D barcodes:

  1. Select **Multiple boxes will be needed** and click **Confirm**.

  2. Select **Use 2D barcodes** from the drop-down menu.

  3. Enter box count, dimensions, and weight for each box in the pack group.

  4. Click **Confirm 2D barcodes.**

If your product requires expiration dates, you can provide this information
the following ways:

  * If you choose **Select from list** as your SKU selection method, you can enter expiration dates in step 1.
  * If you choose **File upload** as your SKU selection method, you can provide expiration dates within your file. 

2D barcodes require shipment ID as a mandatory value. You could find shipment
IDs after shipment creation. If you need to change the contents for a shipment
after shipment creation, go to [Send to Amazon: Change or cancel your
shipment](/gp/help/GP29SYECJZGJ9XMR).

To learn more about using 2D barcodes, go to [Send to Amazon: 2D barcodes for
box content information](/gp/help/GJWALJCN6JKWJX5A).

## Pick List

You will find the pick lists in Step 1b- Pack individual units. Click View
contents link in upper right corner of each pack group. There you will find
the option to download Pick list as a .csv. Pick lists indicate which items
should be taken from the fulfillment center to fulfill the Send To Amazon
(STA) workflow. A fulfillment center associate will use this list to pick the
SKUs and bring them over for packing. You can access the box content details
either saved or submitted on Scan and Pack form and on the Web Form through
the pick list at any point in time.

## Confirm and continue to next step

After providing box content information for all pack groups, proceed to Step
2- [Confirm shipping](/gp/help/GWC4BVUFCZ2FKHQW).

## Frequently asked questions

#### What are pack groups?

Pack groups are groups of SKUs that can be packed together. For example, SKUs
that are classified as dangerous goods (hazmat) cannot be packed with SKUs
that are not dangerous goods. That's because dangerous goods are shipped to
special fulfillment centers that can receive them safely. Other factors that
determine which SKUs can be packed together include SKU weights and
dimensions, and prep and labeling requirements and ownership.

#### Are pack groups same as shipments?

No, pack groups are not the same as shipments. The pack group determines which
SKUs can be packed together in a box, based on the factors outlined above.
Once you have provided box content information for all of your pack groups, we
will determine the optimal shipment destinations for your boxes.

#### What is the benefit of packing before shipment destinations are known?

In addition to allowing Amazon to determine the optimal destinations for your
inventory, you can make quantity adjustments as you pack before you confirm
the shipment destinations.

#### What if I want to make changes to the SKUs that I want to ship when
packing?

We understand that as you pack your boxes, you might want to make changes to
the quantity of certain SKUs either to account for damaged inventory or to
optimize space in the boxes. Packing before you confirm shipments allows you
to make quantity adjustments as you pack without any limitations. You can do
so by going back to the previous step where you entered the quantities,
**choose inventory to send** , and updating the quantity of SKUs that you want
to change. When you are done, continue to step 1b by selecting **Pack
individual units**.

**Note:** Pack groups can change if you add or remove SKUs, or if there are
changes to an existing SKU’s weight, dimensions, prep or labeling
requirements, or dangerous goods classification. Make sure that you provide
updated box content information for the updated pack groups.

#### Why do I see “Skip packing and continue to shipment creation” in Step 1b
of certain workflows?

We have launched this feature only on workflows that satisfy the following
conditions:  

  1. Workflow contains only “Individual units”. The workflow does not contain a single case packed box or packed using case/pallet template.
  2. Amazon Global Logistics was not chosen in Step 1.
  3. Workflow will not proceed if any of the following Ship From and Ship To address combinations: VN-US;UK-US;TW-US;TH-US;MX-US;KR-US;DE-US;CN-US;US-UK;CN-SA;CN-JP;US-DE;CN-AU;CN-AE

