---
title: Using XML
url: https://sellercentral.amazon.com/help/hub/reference/G200374090
section: General Documentation
---

**Important:** You must be an Amazon SP-API developer in order to send a Feeds
request.

**Individual sellers:** This feature is only available to sellers with a
Professional selling plan. Learn more by visiting [Selling plan
comparison](/gp/help/64491).

## What is XML?

XML (Extensible Markup Language) is a markup language for documents containing
structured information. It defines a generic syntax used to mark up data with
simple, human-readable tags. Data is included in XML documents as strings of
text. The data is surrounded by text markup that describes the data. XML's
basic unit of data and markup is called an element. The XML specification
defines the exact syntax this markup must follow:

  * how elements are delimited by tags 
  * what a tag looks like 
  * what names are acceptable for elements 
  * where attributes are placed and more 

The markup in an XML document looks a lot like the markup in an HTML
(Hypertext Markup Language) document, but there are some crucial differences.
Most importantly, XML is a meta markup language. This means that it does not
have a fixed set of tags and elements that are meant to work for everybody.

The X in XML stands for Extensible, which means that the language can be
extended and adapted to meet many different needs. XML allows developers to
define elements appropriate to a specific field or type of business. For
example, chemists can define elements for molecules and atoms, real-estate
agents can define elements for apartments and rents, and musicians can define
elements for quarter notes and lyrics.

XML was developed at the World Wide Web Consortium (W3C) by a group of people
who wanted to improve on HTML and SGML (Standard Generalized Markup Language).

**Note:** This is not a tutorial on using or understanding XML. For more
information about using XML, see the [W3C XML
Tutorial](http://www.w3schools.com/xml/).

## Why Use XML?

XML allows you to integrate your systems with Amazon's systems. Your systems
can communicate with our systems using predefined APIs (Application
Programming Interfaces) to post documents to and pull documents from the
Amazon systems. When working with large amounts of data, it can be convenient
to send and receive data using XML. Once XML integration is fully implemented
and tested, little or no manual intervention is required. For more information
about systems integration, go to [Selling Partner API
Overview](/gp/help/GGE2PFUPLTR6J8FX).

## Prerequisites

Before you decide to implement XML, make sure you meet these prerequisites.
Ask yourself, do I have development resources who can create an XML feed based
on an XSD (XML Schema Document)? Also, make sure that you are registered for a
Professional seller account. Individual sellers do not have access to Amazon's
systems and APIs for XML integration.

##  Using XML to send catalog information

You will use up to six files to upload and manage your products on Amazon.

#### Product file:

Contains descriptive information about the products in your catalog.
Establishes the mapping between your unique identifier (the SKU) and the
Amazon unique identifier (the ASIN: Amazon Standard Identification Number).
This is always the first feed to send when listing a new product.

#### Inventory file:

Communicates the current stock levels of the products you are listing on
Amazon. Includes values for restock dates as well as your fulfillment latency
(the time it will take you to process the order before shipping it).

#### Pricing file:

Sets the current prices for your products, whether the regular (standard)
prices or temporary (sale) prices.

#### Image file:

Supplies URLs (on your server) from which Amazon can pull images to associate
with your products.

#### Relationship file:

(not always applicable) - Defines relationships between different products in
your catalog. There are two types of relationships:

  * **Variation** (the most common type of relationship): Allows customers to select from a list of variations of the same product, such as different sizes and colors.
  * **Accessory** : Allows customers to select products classified as accessories to the main product on a product detail page. For example, a portable radio might have batteries and external speakers listed as accessories. 

#### Overrides feed

(not always applicable) - Allows you to override the account-level shipping
settings with SKU-level shipping settings. This can work well for heavy or
oversized products.

## Using XML to process orders

When a customer places an order on Amazon, the quantity ordered decreases the
quantity available in your seller account. The order is placed into a
90-minute holding period while we validate the transaction. During this time,
we authorize the customer's payment method and send the customer an order
confirmation email. Also during this time, the customer can modify or cancel
the order from within their Amazon account. If the payment is declined or the
customer cancels the order, we add the quantity back into the quantity
available in your seller account. We also send the customer an order
cancellation email.

  

  1. **Receiving the order:** Once the holding period has expired, Amazon generates an order report.

**Note:** XML is not the default format for order reports. Contact [Selling
Partner Support](/hz/contact-us/) to have this option configured for your
account.

  2. **Acknowledging receipt of the order:** The Order Acknowledgment feed allows you to associate your own internal order IDs and order item IDs with Amazon's order IDs and order item IDs, if desired. Additionally, you can use this feed to cancel the entire order (see [Acknowledge Receipt of Orders](/gp/help/200387140) for more information). 
  3. **Shipping the order and confirming the shipment:** Once you have picked, packed, and shipped the order let Amazon know by sending a shipping confirmation. This step is important because it signals Amazon to complete the financial transaction (so you can be paid). Amazon also notifies the buyer that the order is on the way. If we do not receive the shipping confirmation within 30 days after the order was placed, we will automatically cancel the order and you will not be paid for the order. 
  4. **Adjusting the order:** Process refunds and returns as needed. 
  5. **Being paid:** After you confirm shipment of an order, Amazon completes the buyer payment transaction and credits your seller account. Settlement reports are generated showing all financial transactions for each settlement period. For information about disbursements to your bank account, see the[Getting Paid FAQ](/gp/help/18841).

## XML Overview

[Maximize Inventory File Upload Performance](/gp/help/200894980)

