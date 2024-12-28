---
title: Deleted, misrouted, and incomplete shipments
url: https://sellercentral.amazon.com/help/hub/reference/GLMEBQLNBY97ANYY
section: General Documentation
---

To deliver your products as quickly as possible to customers, we distribute
your inventory across our network of fulfillment centers based on your
shipment volume and customer demand. As a result, when you create a shipping
plan, your shipment may be divided into multiple shipments, each directed to a
different receive center or fulfillment center (a process called distributed
inventory placement).

Once you approve a shipping plan on your **Review shipments** page, we begin
preparing for the arrival of your inventory, and we rely on your approved plan
to coordinate our operations.

The following actions lead to additional processing, handling, and rerouting,
which can delay the receipt of your inventory and its availability for sale:

  * Deleting or canceling shipments from shipping plans after you've approved them.
  * Misrouting shipments where some or all items are received at the wrong Amazon facility.
  * Abandoning shipments, such as failing to complete all shipments or sending incomplete shipments where item quantities differ significantly from your shipping plan.
  * Delivering shipments after they were automatically closed, canceled, or deleted.
  * Delivering shipments in a multi-destination shipping plan after 30 days from when the first shipment was received.

To avoid these risks and any associated [inbound defect
fees](/gp/help/GL5XA3MNXAJKJE8E) or [inbound placement service
fees](/gp/help/GC3Q44PBK8BXQW3Z), adhere to the shipment policies below. These
requirements apply to all product sizes.

##  FBA shipment requirements

Once you approve a shipping plan, you are required to ship your products to
Amazon as stated in that plan, including sending the stated quantity of each
product in that plan to the assigned Amazon facility.

Shipments that deviate from an approved shipping plan, like sending to the
wrong facility or sending significantly different item quantities, are non-
compliant.

You can’t abandon shipments after you approve the shipping plan. If your
domestic shipments don’t arrive within 45 days of shipment creation and your
international shipments don’t arrive within 75 days of shipment creation, we
will notify you that your shipments aren't compliant with the policy and the
shipments will close automatically. If your shipments are in transit and are
delayed due to unforeseen circumstances such as weather events and severe
events impacting logistic services, they will remain open.

**Note:** Shipments created after February 1, 2024, and arriving 45 days
(domestic shipment) and 75 days (international shipment) after shipment
creation will close automatically.

You may not delete some of the shipments in a multi-destination shipping plan
after you approve that plan. If you delete portions of a shipping plan, or if
we don't receive all of the shipments in your approved multi-destination plan
within 30 days after the first shipment in that plan arrives at our
facilities, we will notify you that your shipments aren't compliant with this
policy. (The exception is if one or more of your shipments is delayed solely
because of the action or omission of an Amazon partnered carrier).

Make sure that you and your carrier are aware of the requirements for shipping
to Amazon, including the need to schedule delivery appointments. To learn
more, go to [Carrier requirements for LTL and FTL
deliveries](/gp/help/G200978420).

If you want to change a shipping plan after you approve it, you must delete
all of the shipments in that plan before you begin shipping any portion of it.

**Note:** We understand that small changes in shipment quantity can happen due
to normal business fluctuations. You can edit the number of units in a
shipment by up to 5% above or below the original amount, up to six units. You
will not be able to remove the units from your plan once you have approved it.

If you continue to send shipments that aren't compliant with this policy after
we send an initial notice, we may suspend your ability to send additional
shipments to us until you acknowledge this policy and provide us with an
acceptable [plan of action](/gp/help/201623610) to ensure that your future
shipments to us will be compliant with this policy.

**Note:** Effective April 1, 2022, if you continue to send canceled or deleted
shipments to Amazon fulfillment centers, your shipments may be rejected and we
may suspend your ability to send us additional shipments.

## Amazon Selling Partner API (SP-API)

[Amazon SP API](https://developer-docs.amazon.com/sp-api/docs/fulfillment-
inbound-api-v2024-03-20-use-case-guide) may group items that you want to send
to Amazon’s fulfillment network into multiple shipments based on specific
criteria. For example, products that you prep yourself must be sent in a
separate shipment from products that are prepped using the [FBA Prep
service](/gp/help/G201023020).

When you call [createInboundPlan](https://developer-docs.amazon.com/sp-
api/docs/fulfillment-inbound-api-v2024-03-20-use-case-guide#step-1-create-an-
inbound-plan), you provide Amazon with key information that we use to create
shipping plans for your items. Multiple shipping plans might be required to
increase the availability of items across Amazon's fulfillment network. We
recommend that you create listings for all of the items that you want to
include in a shipping plan before using [createInboundPlan](https://developer-
docs.amazon.com/sp-api/docs/fulfillment-inbound-api-v2024-03-20-use-case-
guide#step-1-create-an-inbound-plan).

Shipments that comply with FBA policy can be received at fulfillment centers
more quickly, and your inventory can be made available for sale sooner. When
multiple shipping plans are created, you must approve all shipments in the
plan, then ship inventory according to each shipping plan. You cannot ignore,
delete, or abandon units in any shipping plan.

If you delete parts of a shipping plan, or if we don’t receive every shipment
in your multi-destination plan within 30 days after the first shipment arrives
at Amazon, you will be notified by email. (The exception is if one or more of
your shipments is delayed solely because of an action or omission by an Amazon
partnered carrier.)

To make changes to the shipments, you must delete each shipment in the plan
before you begin shipping any part of it.

**Note:** We realize that small changes in shipment quantity can occur. You
can edit the number of units within a shipment by up to 5% above or below the
original amount, up to 10 units. You cannot remove units from your plan once
you have approved it.

If you continue to send noncompliant shipments after your first email
notification, we may suspend your ability to send more shipments until you
take the following steps:  

  1. Acknowledge FBA policy in an email to us.
  2. Provide an acceptable plan of action to ensure that future shipments comply with Amazon policy.

**Note:** Effective April 1, 2022, if you continue to send canceled or deleted
shipments to Amazon fulfillment centers, your shipments may be rejected and we
may suspend your ability to send us additional shipments.

