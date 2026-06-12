---
title: "Shape XML with Nested FOR XML Queries"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The following example queries the

  table to retrieve the

  and

  values of a specific product.
tags:
  - "xml-data"
  - "shape-xml-with-nested-for-xml-queries"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The following example queries the

table to retrieve the

and

values of a specific product. To make the query interesting, both prices are

returned in a

element, and each

element has a

attribute.

This is the expected shape of the XML:

XML

This is the nested FOR XML query:

```sql
Production.Product
ListPrice
StandardCost
<Price>
<Price>
PriceType
<xsd:schema xmlns:schema
=
"urn:schemas-microsoft-com:sql:SqlRowSet2"
xmlns:xsd
=
"http://www.w3.org/2001/XMLSchema"
xmlns:sqltypes
=
"https://schemas.microsoft.com/sqlserver/2004/sqltypes"
targetNamespace
=
"urn:schemas-microsoft-com:sql:SqlRowSet2"
elementFormDefault
=
"qualified"
>
<xsd:import namespace
=
"https://schemas.microsoft.com/sqlserver/2004/sqltypes"
schemaLocation
=
"https://schemas.microsoft.com/sqlserver/2004/sqltypes/sqltypes.xsd"
/>
<xsd:element name
=
"Production.Product"
type
=
"xsd:anyType"
/>
</xsd:schema>
<Production.Product xmlns
=
"urn:schemas-microsoft-com:sql:SqlRowSet2"
ProductID
=
"520"
>
<Price xmlns
=
""
PriceType
=
"ListPrice"
>
133.34
</Price>
<Price xmlns
=
""
PriceType
=
"StandardCost"
>
98.77
</Price>
</Production.Product>
USE
AdventureWorks2022;
GO
SELECT
Product.ProductID,
(
SELECT
'ListPrice'
as
PriceType,
CAST (
CAST (ListPrice as
NVARCHAR (40)) as
XML
)
FROM
Production.Product Price
WHERE
Price.ProductID=Product.ProductID
FOR
XML
AUTO
,
TYPE
),
(
SELECT
'StandardCost'
as
PriceType,
CAST (
CAST (StandardCost as
NVARCHAR (40)) as
XML
)
FROM
Production.Product Price
WHERE
Price.ProductID=Product.ProductID
FOR
XML
AUTO
,
TYPE
)
FROM
Production.Product
```
