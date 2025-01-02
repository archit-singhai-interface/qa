---
title: Set up tax calculation services
url: https://sellercentral.amazon.com/help/hub/reference/G201706700
section: General Documentation
---

Before you set up tax calculation services, ensure the following:

  * You have obtained a state tax registration number for each state you intend to enable a tax calculation. Refer to [State Tax Registration Numbers](/gp/help/G201706660) for more information.
  * You have reviewed and understand how a product tax code impacts tax calculations on your orders. Refer to [Product Tax Codes](/gp/help/G200794510) for more information.
  * You understand the impact of downgrading from a Professional Selling plan or closing your account, as it will cancel your enrollment for tax collection services and your corresponding tax settings. Refer to [Downgrade or upgrade and tax calculation service](/gp/help/G202101950) for more information.

Follow the steps below to configure or modify your tax calculation settings:

  1. In Seller Central, go to the **Settings** drop-down menu and click **Tax Settings**.

  2. Skip Step 3 if you are a returning user.

  3. Before proceeding to Step 4, first-time users will want to do the following:    

    1. Review the Amazon tax methodology document. This document explains how Amazon will make your tax calculations.
    2. Review the available [Product Tax Codes](/gp/pipe/manager.html?ie=UTF8&pipe=TaxEdit&step=1). These are taxability rules that you can assign to individual products and use as a default on all calculations.

  4. Select a state:   

    1. To configure tax settings for a new state, add the state from the drop down box.
    2. To modify existing state configurations, locate the state in the configuration box.
    3. If the state you select shows 'For all shipments to this state, Amazon manages sales and use taxes', you will not be able to set jurisdictions. 
For additional information, see the [Marketplace Tax Collection
FAQ](https://sellercentral.amazon.com/gp/help/G7VYHGJ8ZT2M58CP).

  5. State Tax Registration Number - For each state you select, a valid state tax registration number is required to configuring taxing jurisdictions.   

    1. If you do not have a State Tax Registration Number for a state, you must obtain one prior to enabling calculation for that state. Refer to the [State Tax Registration Numbers](/gp/help/G201706660) for more information.

  6. Jurisdictions to tax - Jurisdiction selection tells the system what tax rates to look for when making calculations that Amazon supports.   

    1. The state jurisdiction is required to enable any other jurisdiction in a state.
    2. Select all the jurisdiction (state + county + city + district) that you want the system to make a calculation for once a rate is available from our third-party service. For example, if only state and city are selected, only the available state and city tax rate will be calculated.

  7. Shipping & Handling and Gift Wrap taxability - select the box to enable tax calculation.

  8. Optional Custom Rate assignment per state:    

    1. This feature overrides any jurisdiction tax rate supplied by our service provider and all product tax code rule assignments except A_GEN_NOTAX.
    2. All calculations using this option will be made at the state level only.
    3. To assign a custom rate to a state, enter a percentage value in the Custom Rate (%) text box.
Use this option only if required, refer to [Custom Rate](/gp/help/G202102080)
for more information.

  9. Configure a default Product Tax Code (PTC) - A PTC works with your jurisdiction settings and applies tax rules to the tax calculation. The default PTC is used when an offer does not have a PTC assigned to the item offer details. If you do not select a default PTC, an item offer level PTC should be assigned. If neither are assigned, the tax calculation result will be non-taxable using A_GEN_NOTAX value.   

    1. Select a default PTC from the drop-down menu. This will apply when a PTC is not assigned on the [item detail page](https://sellercentral.amazon.com/gp/help/201836910).
    2. If you do not want to configure a default PTC, select **Don’t use default PTC** from the drop-down menu and assign item offer level PTC to every listing.
    3. The item offer level PTC on the offer detail page applies to the item it is assigned.
    4. If a PTC assignment is not made at the default or item offer levels, Amazon will use the always nontaxable PTC A_GEN_NOTAX value resulting in a zero percent calculation. Refer to the [Product Tax Code (PTC)](/gp/help/G200794510) page for more information. 

  10. Amazon Tax Exemption Program - To enroll in the [Amazon Tax Exemption Program](/gp/help/G201707880), select the box next to ‘Enroll in the Amazon Tax-Exemption Program’.

  11. Once you have configured your tax settings, click **Save Settings**.

While Amazon’s tax calculation services provide a means to determine and apply
sales and use taxes to orders, sellers are responsible for reviewing and
determining the following:

  * The correct PTC
  * Calculation settings
  * All related information for their products
  * All tax documentation and payments to the appropriate taxing authorities for their transactions except where [Marketplace Facilitator](/gp/help/G7VYHGJ8ZT2M58CP) Legislation is in effect.

This applies to both Amazon-fulfilled and seller-fulfilled products. If you
have additional questions about tax calculation, we suggest seeking assistance
from your tax adviser.

