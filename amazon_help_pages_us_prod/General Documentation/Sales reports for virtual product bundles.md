---
title: Sales reports for virtual product bundles
url: https://sellercentral.amazon.com/help/hub/reference/GG7X74YD2PZLZN9R
section: General Documentation
---

[Virtual product bundle](/gp/help/G87HAE6PMKKM23Z7) sales are not available in
most reports in Seller Central at this time. When a customer buys a virtual
bundle, the sales are passed through to each of the components in the bundle
and the bundle ASIN does not record a sale (according to most Seller Central
reports).

This allows you to easily manage your inventory without keeping track of new
ASINs or SKUs. However, you may wonder about the performance of your bundles

To help you measure bundle sales, the [default contact
email](/notifications/preferences/contacts) for your Seller Central account
will be sent a report about once a week with a link to download a CSV
breakdown of your bundle sales from the past 90 days. This email report will
be sent to you as long as you have had at least one bundle sale in the past 90
days. The report has one row for each day that a bundle ASIN was sold. It has
the following columns:

  * Date: Format is Year/Month/Day. If there is no row for a date, the bundle had no sales then.
  * Bundle ASIN
  * Bundle title: The first 100 characters of the bundle title.
  * Bundles sold: Units of your entire bundle (not components) ordered.
  * Total sales: Sum (bundle price * bundles sold). These are ordered product sales for your bundles.

The download link will expire about 6 days after the email is sent. After
that, you can wait for the following week’s email report which will contain
data for previous weeks. Note that anyone with the link can download the
report, so be careful about sharing it.

## FAQ

#### I did not receive my report emailed to me this week

Reports may be delayed occasionally due to increased data processing times or
other issues. Check your spam folder. If necessary, wait for the following
week or refer to the last FAQ to calculate your bundle sales.

Reports are only sent to sellers who have had a bundle sale in the past 90
days. Check your previous reports to make sure you have had a bundle sale in
the past 90 days.

#### I have never received a report

The Product Bundles Sales Report is only sent to sellers who have had a bundle
sale in the past 90 days. If the report was never sent to you, it may be
because you have not sold a bundle during that time frame. Otherwise, check
your spam folder, verify that your contact email is up-to-date in
[Notification Preferences](/notifications/preferences/), and make sure that
your email program is configured to accept emails from us. Our emails have the
following configuration:

  * Sender Name: Amazon Brand Services (Do Not Reply)
  * Sender Email Address: do-not-reply@amazon.com
  * Subject: Product Bundle Sales Report

#### How do I change the recipient of the Product Bundles Sales Report email?

Visit the [Notification Preferences](/notifications/preferences) page. Then
find the Product Bundles Sales Report and edit the email for that report.

#### Do bundle orders appear in Manage Orders?

Yes, bundle orders appear in [Manage Orders](/orders-v3/fba/all) > View FBA
orders.

You can look them up using order IDs. You cannot look them up by bundle ASIN
or SKU at this time, as bundle orders are passed through to the component
ASINs.

#### How do I see traffic for my bundle?

You can visit the **Detail Page Sales and Traffic by Child Item** report in
[Business Reports](/gp/site-metrics/report.html). This report will contain
traffic information, but it will not show sales or units.

#### How do returns and cancellations affect this report?

If a bundle order is canceled or returned, this report will not change, as the
report only reflects ordered product sales.

#### Can I calculate my total bundle sales using Order Reports?

In some instances, this can be done. If your bundles have discounts, you may
notice that some of the sales on component ASINs in bundles are recorded with
discounted sale prices, reflecting the bundle discount. You may be able to use
these to distinguish regular sales from bundle sales.

First, determine the discounted sale price of each component in the bundle.
You can do this by visiting your bundle’s detail page and looking at the sale
price shown on the widget that lists each component ASIN in the bundle. Then,
filter your **All Orders Report** to see which orders of component ASINs have
been recorded at those special prices. These may be bundle orders.

#### How can I get past reports of my virtual bundle sales?

The bundle email report will contain the past 90 days' data. At this time,
additional past data is not available.

#### How can I see canceled and returned orders for virtual bundles?

Customers are able to return and/or cancel individual components that are
ordered as part of the virtual bundle. You can see these returns and
cancellations like those of any other ASIN. At this time, you cannot look up
canceled and returned orders by bundle ASIN.

