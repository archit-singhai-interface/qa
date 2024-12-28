---
title: Price per unit requirements
url: https://sellercentral.amazon.com/help/hub/reference/G201618190
section: General Documentation
---

We have implemented new data requirements that have to be followed regarding
price per unit (PPU) information to deliver an accurate and consistent
customer experience. This affects new as well as existing listings. Customers
use PPU information to compare and evaluate products during their shopping
experience. In addition, PPU information is required by law for many products.
Update the unit count information to comply with PPU requirements.

**Unit count** includes a value **unit_count** , such as,"5" and a type
**unit_count_type** , such as, "Count", "Foot", "Sq Ft", "Fl Oz" and, "Ounce".
On the basis of this unit count information, we will provide the PPU
information for certain products to customers.

  * New listings: Products sold within the product types listed in the [price per unit requirements table](https://m.media-amazon.com/images/G/01/PPU_US_HL/Table_US_v3.xlsx) will require new listings to include the unit count attributes.
  * Existing listings: Products sold within the product types listed in the [price per unit requirements table](https://m.media-amazon.com/images/G/01/PPU_US_HL/Table_US_v3.xlsx) will require existing ASINs without unit_count information or with incorrect values in the unit_count_type to provide the unit count attributes when the listings are updated. Product updates will show errors for ASINs that do not follow the new PPU requirements.

For certain product types, ASINs without unit_count information or with
incorrect values in the unit_count_type attribute have to be updated within a
certain time period that is shown in the [Listing Quality
Dashboard](/quality). After this period has passed, certain listings that do
not contain the above-mentioned attributes will no longer be shown in search.

For details, go to [price per unit requirements table](https://m.media-
amazon.com/images/G/01/PPU_US_HL/Table_US_v3.xlsx). These search-suppressed
ASINs will then be available under [Fix Your Product (FYP)](/fixyourproducts).

The scope of this change includes any product-level data submissions, whether
through excel templates, Seller Central (under **Manage Inventory** > **Edit**
> **Vital information**), or XSD feeds.

The unit of measure varies by item packaging and is restricted to the approved
values which includes Ounce, Fl Oz, Foot, Sq Ft, and Count.

Item Packaging | Unit of Measure | Example of products  
---|---|---  
If the product consists of a solid, semi-solid, powder, viscous substance, aerosol, or a mixture of solid and liquid, the unit of measure should always be "Ounce." | Ounce  |  chocolate (solid), face cream (semi-solid), protein powder (powder), honey (viscous substance) and, cooking spray (aerosol)  
If the product consists of a liquid, the unit of measure should always be "Fl Oz" (fluid ounce). | Fl Oz (fluid ounce)  |  juice, liquid detergent, soft drinks, liquid soap and, liquid foundation (makeup)  
If the product consists of a bi-directional commodity including roll-type commodities, continuous sheets, or other product commonly sold by area the unit of measure should be "Sq Ft" (square foot). | Sq Ft (square foot) |  aluminum foil, parchment paper, toilet paper, paper towels and,wax paper  
If the product consists of a unidimensional commodity such as a continuous tape, string, thread, or other product commonly sold by length the unit of measure should be "Foot." | Foot |  dental floss, athletes tape and, thread  
If the product consists of individually packaged, functional units, or units commonly sold by count, the unit of measure should always be the total "Count" of functional units. | Count |  laundry pods, coffee pods, protein bars, nutrition bars, snack bars, wipes, pills, vitamins, tablets, tea bags, dry balls, makeup brushes, hair ties, face masks, trash bags, tissues, napkins, plates, bandages, cups and, diapers  
  
The change applies to all product types mentioned in [price per unit
requirements table](https://m.media-
amazon.com/images/G/01/PPU_US_HL/Table_US_v3.xlsx).

## Frequently asked questions

#### What is price per unit (PPU)?

Price per unit (PPU) refers to the per unit price of a product. For example,
if you sell 16 ounces of coffee beans for $4.00, a PPU of $0.25 per ounce will
display in Search and on Detail page. Displaying PPU to customers facilitates
easy price comparison across products of different pack sizes.

#### What determines how PPU is displayed to customers?

To display PPU, it is important that **unit count** attributes are correctly
filled. Thereafter, an automated system decides whether PPU should be
displayed. For example, if the product is a "Car_seat", the system does not
display PPU. However, if the product is "Coffee", the system displays PPU. We
are constantly reviewing these rules based on customer feedback.

#### What should be done for bundles of different products or sets of products
such as, dishware sets, where PPU is not relevant?

For bundles of dissimilar items such as, a sample pack of ten wipes, two
makeup brushes, and one bottle of concealer, or a set of shampoo and
conditioner, set unit_count_type to "Count" and unit_count to "1".

When in doubt, check your product's image which is usually displayed as net
quantity, to determine which of the unit options is appropriate for the
product.

