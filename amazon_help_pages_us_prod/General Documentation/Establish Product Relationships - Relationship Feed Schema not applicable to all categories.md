---
title: Establish Product Relationships - Relationship Feed Schema (not applicable to all categories)
url: https://sellercentral.amazon.com/help/hub/reference/G200386850
section: General Documentation
---

![](https://d1n436oh1t0g4d.cloudfront.net/GWRSWEQJ49XZZB7U_Global_en-US.png)

## Description

The Relationship feed allows you to set up optional relationships between
items in your catalog. There are two types of relationships:  

  1. **Variation** : This is the most common type of relationship. It allows customers to select from a list of variations of the same product. For example, a shirt might come in a variety of sizes and colors. The main item (parent SKU) is the type of shirt in general. It does not have a size, color, price, or quantity and is not buyable. The variations (child SKUs) are all of the different size and color combinations of the shirt, and are buyable. (See the diagram below.) 

Before uploading a relationship feed for a new parent/child relationship,
upload the product feed for the SKUs. In that feed, designate the parent SKU
as "parent" using the <em>Parentage</em> element, and designate how the child
SKUs will vary (for example, Size or SizeColor) using the
<em>VariationTheme</em> element. Likewise, designate each child SKU as "child"
using the <em>Parentage</em> element, and designate the same VariationTheme as
for the parent SKU.

Note that VariationTheme as well as its associated attributes (for example,
Size and Color for the VariationTheme SizeColor) are defined in your product
feed. The Relationship feed only builds the actual relationships between the
parent and child items.

**Note:** Each category has individual specific requirements for variations.
See the product XSD for a specific category to learn how to set up a variation
relationship for that category.

![](https://d1n436oh1t0g4d.cloudfront.net/G4ZF4MEGW8Y6TPZ4_Global_en-US.png)

  2. **Accessory** : Some items can be classified as accessories for other items. For example, a portable radio electronics item might have batteries and external speakers as accessories. Similarly, a pair of gloves might be designated as accessories for a hat. 

![](https://d1n436oh1t0g4d.cloudfront.net/GEBFKMQEBMWT76VJ_Global_en-US.png)

## Dictionary

**Element** | **Description**  
---|---  
**ParentSKU** | The master SKU for a product with variations  
**Relation** |  Child SKU and type of relationship information, broken into the following components: **SKU** – Used to identify an individual product, one (child) variation of the parent SKU **Type –** Type of relationship, variation or accessory  
  
## XSD

<https://images-na.ssl-images-
amazon.com/images/G/01/rainier/help/xsd/release_1_9/Relationship.xsd>

<!- Revision="$Revision: #1 $"

\-->

<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"

elementFormDefault="qualified">

<xsd:include schemaLocation="amzn-base.xsd" />

<xsd:element name="Relationship">

<xsd:complexType>

<xsd:sequence>

<xsd:element name="ParentSKU" type="SKUType" />

<xsd:element name="Relation" maxOccurs="unbounded">

<xsd:complexType>

<xsd:sequence>

<xsd:element ref="SKU" />

<xsd:element name="Type">

<xsd:simpleType>

<xsd:restriction base="xsd:string">

<xsd:enumeration value="Variation" />

<xsd:enumeration value="DisplaySet" />

<xsd:enumeration value="Collection" />

<xsd:enumeration value="Accessory" />

<xsd:enumeration value="Customized" />

<xsd:enumeration value="Part" />

<xsd:enumeration value="Complements" />

<xsd:enumeration value="Piece" />

<xsd:enumeration value="Necessary" />

<xsd:enumeration value="ReplacementPart" />

<xsd:enumeration value="Similar" />

<xsd:enumeration value="Episode" />

<xsd:enumeration value="Season" />

</xsd:restriction>

</xsd:simpleType>

</xsd:element>

</xsd:sequence>

</xsd:complexType>

</xsd:element>

</xsd:sequence>

</xsd:complexType>

</xsd:element>

</xsd:schema>

## Example (Variation)

<?xml version="1.0" encoding="utf-8" ?>

<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:noNamespaceSchemaLocation="amzn-envelope.xsd">

<Header>

<DocumentVersion>1.01</DocumentVersion>

<MerchantIdentifier>M_SELLER_354577</MerchantIdentifier>

</Header>

<MessageType>Relationship</MessageType>

<Message>

<MessageID>1</MessageID>

<OperationType>Update</OperationType>

<Relationship>

<ParentSKU>5555_5556</ParentSKU>

<Relation>

<SKU>555540352</SKU>

<Type>Variation</Type>

</Relation>

<Relation>

<SKU>555685952</SKU>

<Type>Variation</Type>

</Relation>

<Relation>

<SKU>555690352</SKU>

<Type>Variation</Type>

</Relation>

<Relation>

<SKU>555690552</SKU>

<Type>Variation</Type>

</Relation>

<Relation>

<SKU>555690752</SKU>

<Type>Variation</Type>

</Relation>

<Relation>

<SKU>555690952</SKU>

<Type>Variation</Type>

</Relation>

</Relationship>

</Message>

</AmazonEnvelope>

## Example (Accessory)

<?xml version="1.0" encoding="utf-8" ?>

<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:noNamespaceSchemaLocation="amzn-envelope.xsd">

<Header>

<DocumentVersion>1.01</DocumentVersion>

<MerchantIdentifier>M_SELLER_354577</MerchantIdentifier>

</Header>

<MessageType>Relationship</MessageType>

<Message>

<MessageID>1</MessageID>

<OperationType>Update</OperationType>

<Relationship>

<ParentSKU>ASUSVNA1</ParentSKU>

<Relation>

<SKU>ASUSVNA198714G</SKU>

<Type>Accessory</Type>

</Relation>

</Relationship>

</Message>

<Message>

<MessageID>2</MessageID>

<OperationType>Update</OperationType>

<Relationship>

<ParentSKU>FUJI32XD </ParentSKU>

<Relation>

<SKU>ALPSCARD0024</SKU>

<Type>Accessory</Type>

</Relation>

</Relationship>

</Message>

</AmazonEnvelope>

