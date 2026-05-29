---
title: "Example: Specifying XSINIL with the ELEMENTS Directive"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The following query specifies the

  directive to generate element-centric XML from the

  query
tags:
  - "xml-data"
  - "example-specifying-xsinil-with-the-elements-directive"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The following query specifies the

directive to generate element-centric XML from the

query result.

SQL

This is the partial result.

XML

Because the

column has null values for some products, the resulting XML won't

generate the corresponding

element. By adding the

directive with

,

you can generate the

element even for NULL color values in the result set.

SQL

```sql
ELEMENTS
Color
<Color>
XSINIL
ELEMENTS
<Color>
USE
AdventureWorks2022;
GO
SELECT
ProductID,
Name
, Color
FROM
Production.Product
FOR
XML
RAW
, ELEMENTS;
GO
<row>
<ProductID>
1
</ProductID>
<Name>
Adjustable Race
</Name>
</row>
...
<row>
<ProductID>
317
</ProductID>
<Name>
LL Crankarm
</Name>
<Color>
Black
</Color>
</row>
USE
AdventureWorks2022;
GO
SELECT
ProductID,
Name
, Color
```
