---
title: "Example: Retrieving Product Model Information as XML"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The following query returns product model information.

  mode is specified in the

  clause.

  SQ
tags:
  - "xml-data"
  - "example-retrieving-product-model-information-as-xml"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The following query returns product model information.

mode is specified in the

clause.

This is the partial result:

XML

You can retrieve element-centric XML by specifying the

directive.

This is the result:

XML

```sql
RAW
FOR XML
ELEMENTS
USE
AdventureWorks2022;
GO
SELECT
ProductModelID,
Name
FROM
Production.ProductModel
WHERE
ProductModelID
IN (122, 119)
FOR
XML
RAW
;
GO
<row
ProductModelID
=
"122"
Name
=
"All-Purpose Bike Stand"
/>
<row
ProductModelID
=
"119"
Name
=
"Bike Wash"
/>
USE
AdventureWorks2022;
GO
SELECT
ProductModelID,
Name
FROM
Production.ProductModel
WHERE
ProductModelID
IN (122, 119)
FOR
XML
RAW
, ELEMENTS;
GO
<row>
<ProductModelID>
122
</ProductModelID>
```
