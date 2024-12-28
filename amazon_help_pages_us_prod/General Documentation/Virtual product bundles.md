---
title: Virtual product bundles
url: https://sellercentral.amazon.com/help/hub/reference/G87HAE6PMKKM23Z7
section: General Documentation
---

The [virtual product bundles tool](/bundles/create) for FBA allows [Brand
Representatives](/gp/help/GJ84K745AL3R5N3Q) to create 'virtual' bundles made
up of two to five complementary ASINs that are bought together from a single
detail page. This allows Brand Representatives to offer bundles without
packaging items together or changing FBA inbound inventory.

The virtual product bundles tool works best with Firefox or Chrome.

#### Seller eligibility

This feature is only available to sellers who has a Brand Representative role
assigned to a brand in Brand Registry. The seller must be internal to the
brand and responsible for selling the brand in the Amazon store. If you do not
have access to this feature, you have not been identified as a Brand
Representative. Visit the [Brand Benefit Eligibility](/brands/brand-
relationships?ref=brnd_bndl_bssi_help) page to identify as Brand
Representative and gain access to virtual product bundles and your other
brand-exclusive benefits.

#### Requirements

The following requirements must be met to be eligible to be added to a virtual
product bundle:

  * ASINs must belong to a brand that you own and that is registered in [Brand Registry](https://brandservices.amazon.com/).
  * ASINs must have active FBA inventory in the 'New' condition.
  * Virtual product bundles can be created only in the US Amazon store.

The following items cannot be included in virual product bundles:

  * Gift cards
  * Electronically delivered products (such as digital music, video, and books)
  * Renewed or used ASINs

#### Number of ASINs

Virtual product bundles must contain two to five ASINs. Each component ASIN
must be buyable on its own. This means that
[multipacks](/gp/help/94GSFMC79RSLDBY) and "multi-box" items (single ASINs
that ship in parts in multiple boxes) cannot be created with this tool.

Examples of eligible and ineligible virtual product bundles:

  * Red pen (2) - This cannot be a bundle because there is only one ASIN.
  * Red pen (1) + blue pen (1) - This can be a bundle because there are two unique ASINs.
  * Red pen (4) + blue pen (7) - This can be a bundle because there are two unique ASINs.

To include multiple units of an ASIN in your virtual product bundle, add the
ASIN to your bundle. Then, click number "1" next to **Quantity in bundle** to
share quantity from available FBA in-stock inventory for ASIN components.

#### Pricing

Virtual product bundle price is the sum of prices of the products in the
bundle, and this will update dynamically as price change. Virtual product
bundles have the option to apply an "always-on" percentage discount to the
current price.

#### Dynamic pricing example:

ASIN A: $100

ASIN B: $50

Bundle ASIN (A+B): $150

ASIN A: $100 -> component level discount -> $90

ASIN B: $50

Bundle ASIN (A+B): $140

#### 'Always-on' percentage discount example:

ASIN A: $100

ASIN B: $50

Bundle ASIN (A+B): $150

ASIN A: $100

ASIN B: $50

Bundle ASIN (A+B): $150 -> 5% bundle discount applied -> $142.50

#### Dynamic pricing + 'Always-on' percentage discount example:

ASIN A: $100

ASIN B: $50

Bundle ASIN (A+B): $150

ASIN A: $100 -> component level discount -> $90

ASIN B: $50

Bundle ASIN (A+B): $140 -> 5% bundle discount applied -> $133

#### Main component in a virtual product bundle

You may choose any ASIN in your virtual product bundle to be its main
component. The main component helps determine the search and browse
categorization of the bundle. A bundle ASIN inherits search keywords from its
main component ASIN.

Once a virtual product bundle is created, the main component cannot be
changed. If you have to do so, delete your bundle and re-create it. Use a
different SKU or ensure to wait 24 hours before reusing the same SKU.

#### Discoverability

On mobile and desktop, the detail page of the main component in your bundle
may show the Bundles with this item widget which shows up to six bundles that
share the same main component ASIN

**Note:** It is prohibited to create a bundle that has the exact same
components as an existing bundle but a different designated main component.

#### Editing a bundle

The following attributes of a virtual product bundle ASIN are editable after
the bundle has been saved:

  * Title
  * Description
  * Bullet points
  * Price
  * Images

However, the products that make up the bundle, the main component, and the
bundle’s SKU cannot be edited once saved. If these attributes are wrong,
delete the bundle, wait 24 hours, then re-create it. If you re-create it, use
a different SKU or make sure to wait 24 hours before reusing the same SKU.

#### API integration or Feeds

Virtual product bundles can only be created and edited in Seller Central.
There is no API or feed integration available. Do not try to edit a bundle
using a feed or any means other than the bundles tool.

If you do this, your virtual product bundle may stop being buyable. To fix
this, first remove the bundle ASIN from your API integration or third-party
tool. Then, edit and re-submit the bundle.

#### Variations

At this time, virtual product bundles may not be part of variation families.

#### Deals, Coupons, and A+ content

Virtual product bundles must meet [all standard criteria](/gp/help/202111490)
to be eligible for Deals. Note that adding a bundle discount does **not**
affect the price history of its component ASINs or their eligibility for
Deals.

Virtual product bundles are compatible with
[coupons](/gp/help/GJHCPEFJ5JJQD52D) and [A+ content](/gp/help/G202102960).

#### Advertising

Virtual product bundles are compatible with [Sponsored
Brands](/gp/help/G202144300) ads. They are **not** compatible with [Sponsored
Products](/gp/help/G202145370) at this time.

#### Reviews and ratings

Virtual product bundle ASINs have separate reviews and ratings from those of
the component ASINs in the bundle.

#### Orders and Returns

Orders are recorded as if each component of the virtual product bundles was
bought as part of the same order. In most Seller Central reports, the bundle
ASIN or SKU does not record an order, only the components do. Components can
be returned separately. If your bundle had a discount, customers will receive
a prorated refund upon return.

#### Fees

Since all the products are fulfilled separately just as if they were bought
separately, there are no changes to fulfillment fees; all standard selling
fees will apply.

## Additional Links

  * [Sales reports for virtual product bundles](/gp/help/GG7X74YD2PZLZN9R)
  * [Troubleshooting FAQ for virtual product bundles](/gp/help/G2BTQWUUDS3RV7WB)

