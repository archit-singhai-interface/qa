---
title: CPSIA Choking Hazard Warnings and Material Content Limits
url: https://sellercentral.amazon.com/help/hub/reference/G200292910
section: General Documentation
---

The Consumer Product Safety Improvement Act of 2008 and the Federal Hazardous
Substances Act require the display of appropriate cautionary statements
relating to the choking hazards of toys and games intended for children 12 and
under on the product packaging and in certain advertisements.

These cautionary statements must be displayed in Internet advertisements for
applicable products. This includes all applicable product detail pages on
Amazon.

##  Lead and phthalates limits on all children’s products

The Consumer Product Safety Improvement Act also prescribes strict limits on
the content of certain materials in products intended for children, including
lead and phthalates. Sellers should familiarize themselves with the effective
dates of each applicable limit and work with their suppliers to ensure that
all products sold are compliant with the limits in force. Sellers are
responsible for tracking and complying with any regulations issued by the
CPSC.

Detailed information is available on the [Consumer Product Safety Commission
("CPSC") website](https://www.cpsc.gov/).

##  What the choking hazard warning requirement means to you

In order to add applicable choking hazard warnings to their product listing,
sellers on Amazon should do the following:

  

  1. Determine if a "cautionary statement" (choking hazard warning) applies to the products you sell on Amazon; and
  2. Provide such statements to Amazon as part of the product listing (product detail page) using our seller tools.

The cautionary statement(s) you choose for your product will appear on the
product's detail page in a yellow "Warning" box, located above the Product
Description.

Below is an example of how the warning will appear. The actual warnings on
your product detail pages will depend on the statements you choose.

![](https://images-na.ssl-images-
amazon.com/images/G/01/rainier/help/ToyWarningDetailPage_cpsia.gif)

##  How to verify & upload choking hazard warning information

**Step 1: Verify which of your products require a cautionary statement**

**A. Verification**

You will need to verify which (if any) of the products you sell on Amazon
require cautionary statements (choking hazard warnings) under the Consumer
Product Safety Improvement Act.

The cautionary statements apply to toys and games intended for children 12
years of age and under, regardless of the category in which these products are
listed.

You can verify which (if any) cautionary statements should be included for a
particular product by:

Contacting the product manufacturer OR checking the product's packaging for
the applicable choking hazard warnings.

If you are the manufacturer of a product, you are responsible for determining
whether the cautionary statements apply to your product. Amazon cannot verify
this information for you.

**B. The cautionary statements (choking hazard warnings)**

The following are the six cautionary statements (warnings) that may apply to
your products :

  * Choking Hazard - Small Parts 
    * WARNING: CHOKING HAZARD—Small parts
    * Not for children under 3 yrs.

  * Choking Hazard - Is a Small Ball 
    * WARNING: CHOKING HAZARD—This toy is a small ball.
    * Not for children under 3 yrs.

  * Choking Hazard - Contains Small Ball 
    * WARNING: CHOKING HAZARD—Toy contains a small ball.
    * Not for children under 3 yrs.

  * Choking Hazard - Balloon 
    * WARNING: CHOKING HAZARD--Children under 8 yrs. can choke or suffocate on uninflated or broken balloons.
    * Adult supervision required.
    * Keep uninflated balloons from children.
    * Discard broken balloons at once.

  * Choking Hazard - Is a Marble 
    * WARNING: CHOKING HAZARD—This toy is a marble.
    * Not for children under 3 yrs.

  * Choking Hazard - Contains a Marble 
    * WARNING: CHOKING HAZARD—Toy contains a marble
    * Not for children under 3 yrs.

You may select up to four of these six warnings. You should never need to
choose more than four warnings, as a warning that a product "contains" a small
ball or marble should not apply simultaneously with the corresponding warning
that a product "is" a small ball or marble.

**Step 2: Update your products with the required information**

After you have verified which of your products require cautionary statements
on their detail pages, and which values apply to each of those products, you
are ready to update your detail pages with those values. You can do this using
our updated seller tools.

**A. New data fields**

In order for you to provide the required information for your product
listings, we've created two additional data fields in our product information
feeds and seller tools. The new fields are listed below.

**Label Name** |  **Definition** |  **Values**  
---|---|---  
**cpsia-warning1 cpsia-warning4** |  Use this field to indicate if a cautionary statement relating to the choking hazards of children's toys and games applies to your product. Cautionary statements that you select will be displayed on the product detail page. If no cautionary statement applies to the product, select "no_warning_applicable." |  Select the appropriate statement from the following Valid Values:

  * choking_hazard_balloon
  * choking_hazard_contains_a_marble
  * choking_hazard_contains_small_ball
  * choking_hazard_is_a_marble
  * choking_hazard_is_a_small_ball
  * choking_hazard_small_parts
  * no_warning_applicable

  
**cpsia-warning-description** |  This field has been created for future use in the event that other product safety warnings (in addition to the six provided by the CPSIA) are later required to be displayed on the detail page. Do not use this field unless otherwise advised by Amazon.com. |   
  
Refer to Section B for information on how to use these fields in specific
tools.

**B. Using the new fields in tools**

After you have verified which of the products you sell on Amazon require
cautionary statements on their detail pages, and which of the 6 values listed
above apply to each of those products, you are ready to upload your
information.

Below are instructions for using seller tools to upload your CPSIA warning
information to your product details pages.

**Inventory file templates**

The new CPSIA columns have been added to all flat files for every category.
Because each product can have up to four values applicable to it, there are
four columns in the template.

![](https://images-na.ssl-images-
amazon.com/images/G/01/rainier/help/flatfile_cpsia.jpg)

To submit your information using inventory file templates:

  * Go to the [inventory file template](/gp/help/1641) page in Seller Central and download the updated templates.
  * Fill in these columns with the appropriate value(s) as they apply to your products. (Each column can have one value [cautionary statement] and each product can have up to four values.)
  * Upload the file as usual to Amazon.

**Note:** The cpsia_warning columns need only be filled out for those products
you sell on Amazon for toys and games for children under 12. The
cpsia_warning_description column should remain blank for all products, unless
you receive instruction otherwise by Amazon.

**Add A Product**

You can use the Add a Product tool to add the choking hazard warnings to your
applicable products one at a time.

  * On the Inventory link, click **Add A Product**. Enter your product's ISBN in the search box and scroll through the product information until you find the **CSPIA Cautionary Statement** selections. 
  * Select your values and click **Save & continue**.

![](https://images-na.ssl-images-
amazon.com/images/G/01/rainier/help/flatfile_cpsia.jpg)

**XML**

XML users need to know the following to update their product detail pages:

  * The Product.xsd has been amended to contain the following new fields: **CPSIAWarning** and the **CPSIAWarningDescription**.
  * Use the appropriate value(s) for your applicable product(s).
  * Remember that you should leave the **CPSIAWarningDescription** blank unless instructed otherwise by Amazon.

