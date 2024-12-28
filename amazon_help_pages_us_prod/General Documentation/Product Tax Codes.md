---
title: Product Tax Codes
url: https://sellercentral.amazon.com/help/hub/reference/G200794510
section: General Documentation
---

**Important:** Information on this page does not constitute tax, legal, or
other professional advice and must not be used as such. You should consult
your professional advisers if you have questions.

Tax Calculation Services require both [Product Tax
Code](/tax/nexus/settings/ptc) (PTC) and [ jurisdiction
settings](/tax/nexus/settings) to be configured for calculations to take
effect.

Product taxability rules are applied by PTC and are specific to jurisdictions,
as outlined in the [Amazon Product Tax Code list](/tax/nexus/settings/ptc). A
PTC can be assigned at the item or default level.

If a PTC assignment is not assigned to the default or item levels, the tax
calculation result will be non-taxable for the item(s) in the transaction
using the "Always Non-taxable" A_GEN_NOTAX product tax code, resulting in a
zero percent calculation.

**Default level** : The default PTC is set in your [Tax
Settings](/tax/nexus/settings) and is used to apply a single PTC assignment to
multiple offers that do not have a specific item level PTC already assigned.
If you use a [custom rate](/gp/help/G202102080), your PTC rule and rate will
be overridden with your custom rate. Custom rate is not available in Canada.

To view or edit Default Product Tax Code:

  

  1. In Seller Central, go to **Settings.**
  2. Click **Tax Settings**.
  3. Under **Tax Calculation Rules** use the drop-down next to **Default Product Tax Code**.
  4. Select your **Default Product Tax Code**
     * Use the [View Product Tax Codes link](/tax/nexus/settings/ptc) next to the drop down to review a complete list of PTC’s and associated rules for each
  5. Read the **Tax Methodology** and **Service Terms** and **check acknowledgment** box
  6. Click **Save Settings**

**Item level** : Your item level PTC is set in the items inventory page and is
used to designate a specific PTC to the specific item it is assigned to. The
item level PTC will be used before your default PTC assignment. Also, if you
use a [custom rate](/gp/help/G202102080), your PTC rule and rate will be
overridden with your custom rate. Custom rate is not available in Canada.

To view or edit item level product tax code:

  

  1. Go to **Manage Inventory**
  2. Click **Edit** for the individual product
  3. This will take you to the**Edit Product Info** page
  4. In the **Offer tab** locate the Tax Code field
  5. Click into the field and select your **item level product tax code** from the drop down list
  6. Click **Save and finish**

The following tools are available to assist with updating individual product
detail pages:

  * To edit multiple listings in bulk use [Inventory file upload](/hz/inventory/addproducts).
  * To add a new listing use [ Add a Product tool](/productsearch).

##  How a Product Tax Code (PTC) is determined at the time of tax calculation

When a PTC is assigned at the seller-defined default level AND the item level,
Amazon will use the item level tax code.

When a PTC is assigned at the default level but not at the item level, Amazon
will use the seller-defined default PTC.

When a PTC is not assigned at the item or default level, a calculation will be
made using the nontaxable PTC
[A_GEN_NOTAX](/tax/nexus/settings/ptc/general#A_GEN_NOTAX).

**Note:** Custom Rate, if configured, will override the taxability rules of
PTCs except for A_GEN_NOTAX. To learn more, see[ Custom
Rates](/gp/help/G202102080). Custom rate is not available in Canada.

Tax Calculation Setting updates will typically become effective within 15-20
minutes and do not apply to orders retroactively. If you notice unexpected tax
calculations, check your settings (tax settings and item level) and inventory
file upload for errors (if you used an inventory file upload). If the
calculation issue persists, please contact seller support.

You are responsible for identifying your Tax obligations in addition to the
calculation, remittance, and reporting of all taxes within your obligation,
regardless of your participation in Amazon’s Tax Calculation Service. For more
information, see our [Tax Policies](/gp/help/G200405820).

##  Related Pages

[Set up tax calculation services](/gp/help/201706700)

[Tax Calculation Services](/gp/help/200787660)

