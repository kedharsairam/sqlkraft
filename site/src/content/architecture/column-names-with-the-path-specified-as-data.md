---
title: "Column Names with the Path Specified as data()"
topic: "xml-data"
description: ""
tags: ["xml-data","column-names-with-the-path-specified-as-data"]
pubDate: "2025-12-01"
---

If the path specified as column name is

, the value is treated as an atomic value in the

generated XML. A space character is added to the XML if the next item in the serialization is

also an atomic value. This is useful when you're creating list typed element and attribute values.

The following query retrieves the product model ID, name, and list of products in that product

model.

The nested SELECT retrieves a list of product IDs. It specifies "data()" as the column name for

product IDs. Because PATH mode specifies an empty string for the row element name, there's

no row element generated. Instead, the values are returned as assigned to a ProductIDs

attribute of the

row element of the parent SELECT. This is the result:

XML

Use PATH Mode with FOR XML

```sql
data()
<ProductModelData>
USE
AdventureWorks2022;
GO
SELECT
ProductModelID
AS
"@ProductModelID"
,
Name
AS
"@ProductModelName"
,
(
SELECT
ProductID
AS
"data()"
FROM
Production.Product
WHERE
Production.Product.ProductModelID =
Production.ProductModel.ProductModelID
FOR
XML
PATH (
''
))
AS
"@ProductIDs"
FROM
Production.ProductModel
WHERE
ProductModelID = 7
FOR
XML
PATH (
'ProductModelData'
);
<ProductModelData
ProductModelID
=
"7"
ProductModelName
=
"HL Touring Frame"
ProductIDs
=
"885 887 888 889 890 891 892 893"
/>
```
