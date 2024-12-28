---
title: Location based Shipping Settings
url: https://sellercentral.amazon.com/help/hub/reference/G4LD7W2EKPFK2ULE
section: General Documentation
---

With Location based Shipping Settings you can create new locations, edit
existing ones, and manage your order-fulfillment preferences separately for
each of your locations or fulfillment centers, rather than at an account
level. In the Location based Shipping Settings you will be able to:

  * Define if a location has fulfillment capabilities to ship from only, or if you also allow for in-store or curb-side pickup by enrolling into [Buy-Online Pickup in Store](https://sell.amazon.com/programs/local-selling) (BOPIS).
  * Update the address and contact information of each location.
  * Assign a location’s time-zone.
  * Set cut-off times:
    * If you manually calculate Transit Time on your shipping templates, you can only edit the operating days and cut-off times for your default location, and it will apply this to all of your locations (Note: you can’t set these differently per location).
    * If you have upgraded your shipping templates by enabling [Shipping Settings Automation (SSA)](/gp/help/G8WRJF2N5B787XKQ) to automatically calculate Transit Time for you, you can also set the cut-off time and last pick-up time for each carrier you use, per day of the week, and per location.
  * Use [Multi-location inventory](/gc/multi-location-inventory) APIs to automatically sync your available inventory of each SKU per location.

## Benefits of Location based Shipping Settings

  * Show buyers more accurate delivery dates which adapt based on each location’s fulfillment capabilities.
  * If you are using shipping templates with [Shipping Settings Automation (SSA)](/gp/help/G8WRJF2N5B787XKQ?) enabled, and have connected to the [Multi-location inventory](/gc/multi-location-inventory) APIs, your delivery promise will be more accurate, which is typically shorter and typically leads to more sales. Your delivery promise will be more accurate because it will automatically calculate the transit time based on: a) The buyer’s location, b) the closest warehouse/location to that buyer with inventory available, c) up-to-date estimations of the delivery capabilities of the carriers you use, and d) each location’s order fulfillment settings.

## How to create a new location

  1. Go to **Settings** and click **Shipping Settings**.

  2. Go to **Locations**.

  3. Click **Create a new Location**.

  4. Give this location a unique name and fill in address and contact info.

  5. Choose **Fulfillment Capabilities** (Shipping or In-store Pickup). This option will only be shown to sellers enrolled in the BOPIS program.

  6. Click **Create Location**.

## How to deactivate an existing location

  1. Go to **Settings** and click **Shipping Settings**.

  2. Go to **Locations**.

  3. Next to the location you want to deactivate, click the **drop-down arrow next to Edit**.

  4. Select **Deactivate all operations**.

## How to edit your Order Fulfillment Settings per location for Locations
where you Ship from

  

  1. Go to **Settings** and click **Shipping Settings**.
  2. Go to **Locations**.
  3. Identify the location you want to update and click **Edit**.
  4. Under the fulfillment capabilities for **Shipping** , click edit toupdate your operating days, delivery days, and order cut off times for each location:  

    1. If you manually calculate Transit Time on your shipping templates, you can only edit the operating days and cut-off times for your default location, and it will apply this to all of your locations.

**Note:** You can’t set these differently per location.

    2. If you have upgraded your shipping templates by enabling [Shipping Settings Automation (SSA)](/gp/help/G8WRJF2N5B787XKQ?) to automatically calculate Transit Time for you, you can also set the cut-off time and last pick-up time for each carrier you use, per day of the week, and per location.
  5. Click **Save order fulfillment settings**.

## How to edit your order fulfillment settings per location for locations
where you do in-store pickup

  

  1. Go to **Settings** and click **Shipping Settings**.
  2. Go to **Locations**.
  3. Identify the location you want to update and click **Edit**.
  4. Under the fulfillment Capabilities for **In-store Pickup** , click edit toupdate your Pickup handling time, inventory hold period and your pickup and curbside delivery hours:  

    1. Handling time is the time taken by your business to process the orders received online till they are received by customers. We recommend that you keep handling time under two hours to meet our customers’ expectations. Pickup cut-off times will be calculated based on the handling time and the store hours.
    2. Inventory hold period is the number of days you will hold the item for the customer before considering the order as expired and issue a refund. We recommend that you keep inventory hold period as five days. 

**Note:** This field is read-only in Seller Central, editing is available
through BOPIS API.

    3. Pickup methods allow you to determine if customers can pick-up in-store by walking inside to pick-up their online order, or curbside by parking in a designated parking space and the store associate will bring the order to them.
    4. Pickup hours allow you to set per day of the week if this location is open for pickup, and the start and end time of the day where you allow pickup or curbside delivery.

For more information, go to [Location based Shipping Settings frequently asked
questions](/gp/help/GPGZ78ZWVG42M4CW).

