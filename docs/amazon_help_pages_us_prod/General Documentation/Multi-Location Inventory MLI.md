---
title: Multi-Location Inventory (MLI)
url: https://sellercentral.amazon.com/help/hub/reference/GJTDKPYEPQCXNS6M
section: General Documentation
---

Multi-Location Inventory (MLI) is a feature for your account that synchronizes
your inventory per location in real time to make more accurate delivery
promises and simplify order fulfillment.

## Benefits of Multi-Location Inventory

  * Accurate and automated deliveries: Delivery dates are calculated using the location with available inventory that is closest to the customer zip code, and the ship capabilities within the shipping template you already use. This will result in more accurate and automated delivery promises in combination with Shipping Setting Automation (SSA).
  * Simplify shipping templates: The simplification of managing multiple Shipping Templates for combinations of locations and inventory, but with MLI you can configure a single shipping template for all of your locations and simplify the process.
  * Increase available inventory: To avoid out-of-stock inventory at a location, you can configure inventory based on the location with the lowest stock. By doing this, customers may see products out-of-stock, when there is actually inventory available. MLI allows you to show customers the most accurate available inventory from the closest available fulfillment center.
  * Automated inventory updates: MLI automatically synchronizes your inventory count per location so you don't have to update manually.

**Note:** MLI is currently only available through SP-API, Feeds API, and
Listing Loader feed file upload in Seller Central. MLI is only available on
orders Fulfilled By Merchant (FBM), not on orders Fulfilled by Amazon (FBA).

## Without MLI

You may be overestimating your delivery promise when setting it manually
because you haven't considered your customer's location in relation to your
available inventory. For example, your actual days to deliver are 4, but the
delivery promise shown to customers is 10.

## With MLI

Your delivery Promise will be more accurate by using the closest location to
the customer that has inventory. Using the previous example, your actual days
to deliver are 4 and your delivery promise shown to customers is also 4.

