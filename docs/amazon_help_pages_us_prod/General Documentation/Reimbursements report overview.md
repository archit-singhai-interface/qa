---
title: Reimbursements report (overview)
url: https://sellercentral.amazon.com/help/hub/reference/G200732720
section: General Documentation
---

The [Reimbursements](/gp/ssof/reports/search.html#recordType=REIMBURSEMENTS)
report provides itemized details for all reimbursements, including those
requested by you and those that are generated automatically.

Reimbursements appear in your account 4-5 business days after the
reimbursement is approved.

**Tip:** For information about FBA customer refunds, see [FBA customer
returns](/gp/help/200453320).

Reimbursements also appear in the **Payments** report. To locate a
reimbursement:

  

  1. In the **Payments** Dashboard, click **Transaction view**.
  2. In **Filter view by** , select **Other**.
  3. In the **Product Details** column, search for **Balance Adjustment** or **FBA Inventory Reimbursement**. 

For the reimbursements that you requested, use the case ID in the report to
view the details. For reimbursements associated with a customer refund, use
the Amazon order ID in the report to view the details.

Reimbursements can take up to five days to appear in the report after they
have been approved. When more than one reimbursement is processed on the same
day for the same issue, they may be combined into a single transaction.

##  Field Definitions

Online report header | Downloadable report header | Description  
---|---|---  
Date | approval-date | The date the reimbursement was approved.  
Reimbursement ID | reimbursement-id | The unique identifier for this reimbursement. Each reimbursement may include multiple line items.  
Case ID | case-id | The unique identifier assigned to the case when you request a reimbursement.  
Amazon Order ID | amazon-order-id | The unique identifier assigned to the customer order. This field is empty if the reimbursement is not associated with an order.  
Reason | reason | The reason for the reimbursement (for example, Damaged: Warehouse).  
Merchant SKU | Sku | The merchant SKU (stock keeping unit) is the unique identifier you assigned to your product.   
FNSKU | fnsku | The fulfillment network SKU (stock keeping unit) is the unique identifier Fulfillment by Amazon assigned to your product.  
ASIN | asin | An ASIN (Amazon Standard Identification Numbers) is a unique identifier assigned by Amazon to products in the Amazon product catalog. The ASIN can be found on the product detail page.  
Title | product-name | The name of your product.  
Condition | condition | The condition of your item (for example, New).  
Quantity | quantity | The total number of units reimbursed for this line item.  
[Does not appear in the online version] | currency-unit | The currency for the applicable marketplace.  
Amount Per Unit | amount-per-unit | The per-unit reimbursement amount for this line item.  
Quantity Reimbursed [Cash] | quantity-reimbursed-cash | The total number of units reimbursed with cash.  
Amount Total | amount-total | The total amount of the cash reimbursement for this line item.  
Quantity Reimbursed [Inventory] | quantity-reimbursed-inventory | The number of units reimbursed with inventory.  
Quantity Reimbursed [Total] | quantity-reimbursed-total | The total number of units reimbursed with either cash or inventory (Quantity Reimbursed [Cash] + Quantity Reimbursed [Inventory]).  
Original Reimbursement ID | original-reimbursement-id | The unique identifier for the original reimbursement request that is being adjusted, if present  
Original Reimbursement Type | original-reimbursement-type  | The type of transaction for the original reimbursement request that is being adjusted, if present

