---
title: Selling Partner API Overview
url: https://sellercentral.amazon.com/help/hub/reference/GGE2PFUPLTR6J8FX
section: General Documentation
---

## Overview

Selling Partner Application Programming Interface (SP-API) is the next
generation suite of API-based automation functionality for Amazon’s selling
partners.

SP-API is a modernized suite of REST APIs with current standards, OAuth2.0
selling partner authorization using Login with Amazon (LWA), a test endpoint.
SP-API is available for all registered developers worldwide.

As an SP-API developer, you receive an authorization token, such as LWA, that
is used for the following:

  * Sending requests to SP-API for your own seller account
  * Sending requests to SP-API on behalf of other sellers

**Note:** To send requests on behalf of other sellers, you must receive the
authorization token from the seller in order to make the connection.

As a registered developer, you can do the following with SP-API:

  * Create or authorize applications that help manage selling in the Amazon store.
  * Upload product and inventory information.
  * Get product information.
  * Receive notifications.
  * Download orders for fulfillment.
  * Schedule and retrieve reports.

## Register as a SP-API developer

You must register as a developer to create apps with SP-API. To register as a
SP-API developer, you must create a developer profile. If you decide to
develop an application for your own selling account, Amazon selling partners
(the appstore), or vendors, you also must have a Professional selling plan.

TThe developer profile, formerly the Developer Registration and Assessment
form, allows you to submit information about your organization and
applications. Amazon uses this information to assess compliance with our SP-
API [Acceptable Use Policy](/mws/static/policy?documentType=AUP&locale=en_US)
and the [Data Protection
Policy](/mws/static/policy?documentType=DPP&locale=en_US) requirements and to
ensure that we provide the appropriate level of access. All new and existing
developers who require changes to their data access have to submit their
responses to the developer profile.

To get started with SP-API, fill out your [developer
profile](/developer/register).

If you are completing your developer profile for the first time, you can save
a draft and return to complete it later. If you are modifying an existing
developer profile, updates are saved only after you submit it for review. When
you submit the developer profile for review, a support case is automatically
created for you. We will contact you with any next steps.

## Sellers who work with developers

SP-API provides secure authentication of API callers. Sellers with a
Professional plan can delegate calling rights to developers using LWA
authorization.

**Note:** When authorizing a developer to access selling data on your behalf,
that developer can view or edit your information pertaining to product
listing, order management, shipping, pricing, performance, and financial
information.

The SP-API functions are designed to facilitate and automate the stages of the
business process for selling in Amazon’s stores.

SP-API provides the following major features:

  * **Inventory management.** You can perform batch uploads of inventory, add products, check inventory levels, examine pricing information, and perform other inventory management tasks. 
  * **Order management.** You can download order information, obtain payment data, acknowledge orders, and schedule reports. 
  * **Reports management.** You can use SP-API to request generation of a variety of reports, query their status, and then download them. 
  * **Shipping management.** You can buy shipping services or create and manage Fulfillment by Amazon shipments. 

For more information on SP-API, visit these resources:

  * [SP-API Documentation on GitHub](https://github.com/amzn/selling-partner-api-docs)
  * [Amazon Selling Partner API Developer Agreement](/mws/static/agreement?locale=en_US)
  * [Acceptable Use Policy](/mws/static/policy?documentType=AUP&locale=en_US)
  * [Data Protection Policy](/mws/static/policy?documentType=DPP&locale=en_US)

