---
title: Valid tracking rate (VTR)
url: https://sellercentral.amazon.com/help/hub/reference/G201817070
section: General Documentation
---

Valid tracking rate (VTR) measures how often you use valid tracking
information for your packages. VTR measures the percentage of seller-fulfilled
packages that have a valid tracking ID. Amazon customers depend on tracking ID
to find out where their orders are and when they can expect to receive them.
VTR is a performance metric that reflects those expectations.

## VTR policy requirements

All non-FBA sellers must maintain a VTR greater than or equal to 95% at a
product category level. VTR below 95% in a product category can result in:

  * Suspension of your seller-fulfilled listings within the category or categories with low VTR. Note that other seller-fulfilled listings in product categories where VTR is above threshold of 95% and your FBA listings will not be impacted. Negative impacts to your eligibility to participate in premium shipping and guaranteed delivery.
  * If, for any category, your VTR is below threshold and any of your listings are suspended, you can submit an appeal by clicking on **Appeal** next to the impacted categories on the Account health page in [Seller Central](https://sellercentral.amazon.com/performance/detail/shipping?t=vtr&ref=sp_st_dash_csp_vtr). If your appeal is approved, your seller-fulfilled listings in the affected product category will be restored. In case your appeal is denied, you will receive an email confirming the same and you will be required to furnish more information.

**Note:** For Seller Fulfilled Prime, 99% or more of Prime packages must have
valid tracking in aggregate across all product categories. Learn more at
[Seller Fulfilled Prime performance requirements](/gp/help/G202072550).

## How to maintain a healthy VTR

  * Select carriers that are integrated with Amazon from the drop-down menu on the Order Details page, as these carriers provide real-time tracking status to Amazon.
  * Verify that the carrier name, shipping service, and tracking ID combination are entered correctly and belong to the same carrier.
  * In case of an error while entering tracking information, update the package tracking ID within 24 hours of ship-confirmation. Tracking information confirmed or updated after the package is delivered implies that the customer was not able to track the package and it will impact your VTR metric negatively.
  * Consider purchasing shipping labels through Amazon’s [Buy Shipping services](/gp/help/hub/reference/G200202220).

Visit the [How to confirm a shipment](/gp/help/G200197960) page for more
information.

**Note:** Using **Chinese characters** or **special characters** to manually
enter tracking information is considered **invalid** as Amazon currently does
not support these.

## Tracking ID validation

Amazon validates tracking details (including carrier name and tracking ID) for
all seller-fulfilled packages and shows warnings for invalid tracking details.
However, this policy does not apply to items excluded from the VTR
calculation.

You will have to provide the following information when confirming a shipment:

  * The name of the carrier from the drop-down list on the Ship Confirmation page of Seller Central
  * The specific delivery service used for each of the seller-fulfilled orders
  * The tracking ID for seller-fulfilled orders that are shipped with a tracking method

##  How VTR is calculated

VTR is the percentage of total packages with valid tracking ID for which
Amazon receives a scan event from the carrier. The VTR calculation is based on
the country of origin of a package. To calculate VTR, we take the number of
packages you ship with a valid tracking ID and divide it by the total number
of packages you have shipped and confirmed over a 30-day period. Note that
exempted packages are not considered in this calculation. We use the promised
delivery date to determine which orders are included in the performance
metric.

Given below is the VTR calculation logic based on ship origin country:

  * For packages shipped from US, we consider a valid tracking ID if Amazon records at least _one physical carrier scan_.
  * For packages shipped from China, we will consider a valid tracking based on following criteria:
    * Packages with a value below USD 5 (including shipping fee) must use an integrated carrier and trackable ship method that provides at least _one physical carrier scan_ *.
    * Packages with a value equal to or above USD 5 (including shipping fee) must use an integrated carrier and fully trackable ship method that can provide at least _two physical =carrier scans_ (including a delivery scan or delivery attempt).
  * We require at least two carrier scans in order for tracking to be valid, one of which must be a **Delivery scan** by the carrier.
  * Items delivered 17+ days past the Promised Delivery date will be considered invalid tracking.

*A carrier scan is a scan the carrier performs to show the package is in transit.

##  Which carriers are Amazon-integrated?

At Amazon, carrier integration is an ongoing process to increase integrated
carrier coverage and ensure that our customers are able to track their
packages throughout the order journey. The list of integrated carriers is
updated on the Ship Confirmation page. To ensure that sellers maintain a good
VTR, they are encouraged to use carriers in the drop-down list on Ship
Confirmation page on Seller Central.

**Note:** If you manually add a carrier name in the free-form text field
**“Other”** and that carrier is integrated with Amazon, your tracking will be
marked as **invalid**. You must use the drop-down menu to select carriers who
are integrated with Amazon.

##  Exemptions from VTR calculation

The following items are exempted from VTR and will not be included in the VTR
calculation.

**Note:** For Seller Fulfilled Prime packages, there are no exemptions for the
VTR calculation. For more information, go to [Seller Fulfilled Prime
performance requirements](/gp/help/G202072550).

  * **Heavy/Bulky shipments:** Domestic packages shipped by the following heavy/bulky freight carriers:  Alliance Air Freight | Dayton | LTL | Priority1  
---|---|---|---  
AJL Transport | Dependable Highway Express | Metropolitan Warehouse | QuadExpress  
Central Freight | Dohrn | Midwest Motor Express | Trend Transport  
CEVA | Forward Air | New Penn | Truck  
CRST | Geodis | Old Dominion | Unified  
Custom Companies | Holland | Personal |  Conway  
Custom Global Logistics | IT Worldwide | Pitt Ohio |   
  * Domestic small and flat shipments that meet all of the following criteria:
    * Small and flat packages, such as screen protectors and greeting cards, that cost less than USD 10 (including shipping charges). 
    * Shipped by USPS.
    * The shipping service is "**USPS Standard Mail envelopes** ” or “**USPS First Class Mail envelopes** " from the drop down in the shipping service field in Seller Central.
  * **Digital products** such as audio books.
  * Packages shipped from outside of the US and China into the US are exempted from VTR calculation.

## Tracking details for multiple packages of same order

For orders with multiple units (same ASIN or different ASIN), you can ship
confirm the order in a single package or more. If you are shipping the order
via multiple packages, then perform the following:  

  1. On the **Order details** page, select **Add a Package**.
  2. Select the quantity per ASIN and enter the tracking details correctly for each package. This will ensure that customers are able to track all the packages.

##  How to view the VTR metric and report

You can view your VTR metric on the [Shipping
Performance](/performance/detail/shipping?t=vtr&ref=sp_st_dash_csp_vtr) page.

Following is the path to Shipping Performance page for VTR:  

  1. From the **Performance** menu, select **Account health**.
  2. Click the **Shipping performance** section and click **View details**.

Only orders included in your current VTR defect report count against your
metric. If the report contains no orders, it means all of your orders have a
valid tracking.

To download the VTR defect report:  

  1. Click **Download Report** in the **Valid Tracking Rate** section of the Shipping Performance page.
  2. Filter by carrier or product category.

Allow 72 hours for the report and metrics to reflect any updates.

**Note:** For more information about Seller Fulfilled Prime VTR performance,
go to [Seller Fulfilled Prime defects report](/gp/help/G202072570).

##  Fields on the report and what they mean

  * **Tracking ID** : The tracking number or ID you entered on Seller Central. 
  * **Has valid tracking** : If the order has a valid tracking “Yes”, if not “No”.

**Note:** If you entered tracking information or edited this after the
delivery was made, it will say “No”.

  * **Has tracking ID** : If you entered a tracking number or ID it will say “Yes”, if you left this field blank on Seller Central, it will say “No”.
  * **Package value** : Price of the package (including shipping charges), which will help you know if your package was exempted from VTR calculation or requirements of carrier scans.
  * **Any physical scan from carrier** : Check the “How VTR is Calculated” section above for more details on the requirements. “Yes” if scans are present, “No” if they aren’t.

**Note:** If you entered tracking information or edited this after the
delivery was made, it will say “No”.

  * **Delivery scan or attempt** : Check the “How VTR is Calculated” section above for more details on the requirements. “Yes” if scans are present. If not, “No”.

**Note:** If you entered tracking information or edited this after the
delivery was made, it will say “No”.

  * **Origin country** : The country that the package was shipped from.

## Important resources for Valid tracking rates

[Valid Tracking Rate FAQ](/gp/help/202014610)

[How to confirm shipping](/gp/help/G200197960)

