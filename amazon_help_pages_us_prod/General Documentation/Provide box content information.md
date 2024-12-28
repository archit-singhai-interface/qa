---
title: Provide box content information
url: https://sellercentral.amazon.com/help/hub/reference/G201967250
section: General Documentation
---

Amazon requires accurate box content information for each box sent to a
fulfillment center. This information allows the fulfillment center to receive
your shipment more quickly and make your inventory available for sale sooner.
If you do not provide box content information, Fulfillment by Amazon (FBA)
will assess a fee to manually process the contents of each box. For more
information, go to [FBA manual processing fee](/gp/help/G202061550).  
  
**Important:** Failure to provide accurate box content information might
result in blocking of future shipments, and a manual processing fee will be
applied.

**Note:** Accurate box weight and dimensions are required for all shipments,
even if you opt to not provide box content information in Seller Central.

You can provide box content information to Amazon during the shipment creation
process either through Seller Central or SP-API.

## How to provide box content information

The methods available for providing box content information depend on your
selected shipment creation workflow.

Workflow | Providing box content information   
---|---  
**Send to Amazon** | If you are packing single-SKU boxes or boxes that contain multiple units of the same SKU, select **create packing template** and enter **Box content information** including weights, dimensions, and prep and labelling instructions. Saving the SKU template enables you to reuse box content information whenever you replenish the SKU.  
**Send/replenish inventory** | After preparing your shipment on step five of the Send/Replenish workflow, click **Work on shipment**. For **Shipment packing options** , you will be prompted to choose one of the following methods to provide box content information:

  * [Provide box content information with the web form](/gp/help/GQEJBQMYP2BJ6K23)
  * [Provide box content information by uploading a file](/gp/help/GCZQGFX9HGFUWLKC)
  * [Provide 2D barcodes for box content information](/gp/help/G202049090)

  
**Amazon Selling Partner API (SP-API)** | For information about the fulfillment inbound API use case guide, go to [Provide box content information](https://developer-docs.amazon.com/sp-api/docs/fulfillment-inbound-api-v2024-03-20-use-case-guide#step-3-provide-box-content-information).  
  
## Frequently asked questions

#### How do I enter box content information for oversize units that I place
directly on a pallet?

If your shipment contains oversize products that you place directly on a
pallet instead of in a box, consider each oversize unit a single box with one
unit. If your shipment also contains boxes, continue to label those boxes as
you normally would. Place a pallet label on each of the four sides of your
pallet so your shipment is received properly.

**Note:** When you ship expiration-dated inventory to a fulfillment center,
only one expiration date per ASIN is allowed in the same shipping box.
Multiple ASINs with differing expiration dates can be shipped in the same box
only if all of the units of each ASIN have the same expiration date.

For more information, go to [Expiration dates on FBA
products](/gp/help/G201003420).

#### What if my shipping process does not support listing the contents in each
box?

Modifying your inventory fulfillment process to provide box content
information would allow fulfillment centers to receive your shipments more
quickly and make your inventory available for sale sooner. However, if your
shipping process doesn’t support providing this information, select one of the
multiple box options and select **Skip providing box contents** when asked how
you would like to provide box content information. Amazon will then manually
process your shipment for a fee.

#### What are the requirements for small parcel delivery (SPD) boxes?

All SPD boxes should:

  * Meet the [shipping and routing requirements](/gp/help/200141510)
  * The units inside each box must be prepped according to the [Packaging and prep requirements page](/gp/help/200141500)
  * Have an FBA shipment label and a carrier label 
  * Not weigh more than 50.00 lb unless they contain a single oversize item that weighs more than 50.00 lb 
  * Not exceed 25.00 inches on any side unless they contain a single oversize item that measures more than 25.00 inches 
  * Be properly packed to arrive at the fulfillment center intact 

**Important:** Box weight and dimension policies are strictly enforced.
Sending overweight or oversize boxes to the fulfillment center may lead to
blocking of future shipments. For more information, go to [Small parcel
delivery to Amazon](/gp/help/200280260).

**Tip:** There is a 1 lb minimum charge for partnered-carrier shipments. For
shipments that weigh less than 1 lb, the minimum charge applies.

#### What are the requirements for LTL or FTL delivery boxes?

Less than truckload (LTL) is for cases or boxes that are either secured on
pallets or sent on a trailer or container. For LTL, the truck might contain
shipments to other destinations. If your shipment qualifies for Full Truckload
(FTL), the shipment will go directly to the fulfillment center. LTL and FTL
shipments require an advance delivery appointment. For more information, go to
‘Scheduling delivery appointments’ at [Carrier requirements for LTL and FTL
deliveries](/gp/help/200978420).

For products shipped by truck:

  * Follow the [Packaging and prep requirements](/gp/help/200141500) and the [Seller requirements for LTL, FTL, and FCL deliveries](/gp/help/G200978400).
  * All boxes on a single pallet must belong to the same shipment ID. 
  * Every box on a pallet must have a unique FBA Box ID label. Do not photocopy, reuse, or modify labels for use on additional boxes. 
  * Total shipment weight must be no less than 150.00 lb. 
  * A single packed pallet must not exceed 1,500.00 lb for non-stackable pallets or 750.00 lb for stackable pallets. 
  * Pallets must be made of wood, GMA standard Grade B or higher, 40 x 48 inches, with 4-way access. 
  * Boxes on pallets must not overhang the pallet edge. 
  * Boxes must be secured to the pallet with plastic or stretch wrap. 
  * Single items weighing more than 100.00 lb, longer than 80.00 inches, or wider than 30.00 inches must be on their own pallet. 
  * Multiple boxes sold as a set that together weigh more than 100.00 lb must be on their own pallet. 
  * Pallets identified as stackable may be stacked by the carrier. 
  * Pallets are ideally 50 inches in height (45 inches for boxes and 5 inches for pallet) and stackable, as this is space efficient and maximizes trailer space. Non-stackable pallets cannot exceed 72 inches in height and are less space efficient. 

For more information, go to [Shipping and routing
requirements](/gp/help/200141510), [Shipment label
requirements](/gp/help/200178470), and [Seller requirements for LTL, FTL, and
FCL deliveries](/gp/help/200978400).

#### How many boxes can I send per shipment?

The maximum number of boxes you can send in a shipment varies depending on
your shipping method.

Shipping method | Box limit  
---|---  
SPD (partnered carrier) | 200  
SPD (non-partnered carrier) | 500  
LTL | 5,000

