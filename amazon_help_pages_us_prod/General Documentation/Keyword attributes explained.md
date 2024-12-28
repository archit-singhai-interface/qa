---
title: Keyword attributes explained
url: https://sellercentral.amazon.com/help/hub/reference/GF2C2L6RCFZGWBXC
section: General Documentation
---

## Overview

The table below explains the keyword attributes that sellers encounter when
managing product listings. Most of the keyword attributes require valid
values, which can be found in [Browse Tree Guides (BTGs)](/gp/help/G1641). The
attributes specific_uses_keywords, thesaurus_attribute_keywords and
target_audience_keywords are primarily used in the U.S., and are being phased
out. Free text can be input for generic_keywords and subject_keywords.
Subject_keywords should only be used for Media products. You don’t have to
populate platinum_keywords as they are now redundant.

Field Name | Attribute Name | Description | Values | Length Limit (Bytes) | Indexed by Search? | Used by Browse?  
---|---|---|---|---|---|---  
**Intended Use** | specific_uses_keywords | Describe the context the product is used in, which can be an activity or location e.g. gaming, bedroom. This attribute is primarily used in the US and is being phased out. | N/A (being phased out) | 150 | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png) | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png)  
**Item Type Keywords (ITK)** | item_type_keyword | ITKs automatically assign products to browse nodes and are primarily used in the US. | See valid values in BTGs. | 250 | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png) | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png)  
**Other Attributes** | thesaurus_attribute_keywords | Describe features of a product e.g. waterproof, glow-in-the-dark. This attribute is primarily used in the US and is being phased out. | N/A (being phased out) | N/A | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/No._CB1198675309_.png) | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png)  
**Platinum Keywords** | platinum_keywords | No longer used. Previously used to populate platinum sellers storefronts, this attribute is redundant. | N/A (phased out) | N/A | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/No._CB1198675309_.png) | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/No._CB1198675309_.png)  
**Search Terms** | generic_keywords | Describe products. [See help page](/gp/help/23501). | Free text. | 249 | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png) | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png)  
**Style-specific Terms** | style_keywords | Describe apparel items e.g. ankle-boots, fur-lined. | See valid values in BTGs. | 100 | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png) | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png)  
**Subject Keywords** | subject_keywords | Subject Keywords should only be used to describe Media products. | Free text. | 210 | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png)Media only | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png)  
**Subject Matter** | thesaurus_subject_keywords | Describe what is depicted on a product e.g. a poster depicting horses. | See valid values in BTGs. | 250 | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png) | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png)  
**Target Audience** | target_audience_keywords | Describe target end users e.g. women, children, dogs. This attribute is primarily used in the US and is being phased out. | N/A (being phased out) | N/A | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/No._CB1198675309_.png) | ![](https://images-na.ssl-images-amazon.com/images/G/31/rainer/help/Yes._CB1198675309_.png)  
  
#### How is this data used?

Sellers populate attributes and Amazon uses the data to help customers find
products. For example, Amazon uses the data to generate search results for
customers keyword searches. The data is also used to automatically assign
products to browse navigation, another way in which customers find products.
For example, the browse assignment query of “style_keywords:sport-sandals”
assigns products that have a style_keywords value of sport-sandals to the
Sports Sandals browse node.

#### Should I use the drop-down list or free text?

On the Keywords tab that sellers see when adding or editing listings in Seller
Central, sellers can either select a drop-down value or enter free text. Free
text must match a valid value listed in the BTGs, so that it is possible to
use the data in browse queries. Amazon does not publish the full list of valid
values; rather, we direct sellers to the BTG that corresponds to the product
category in which they sell, in order to ensure that they focus on the values
that are relevant to them.

#### Length Limits

Search Terms (generic_keywords) should be less than 250 bytes long ([read
more](/gp/help/G23501)). If it exceeds the limit, the attribute is completely
ignored by Amazon Search.

For other length limits in the table above, if limit exceeds, Amazon Search
indexes up until the length limit and ignores any excess.

