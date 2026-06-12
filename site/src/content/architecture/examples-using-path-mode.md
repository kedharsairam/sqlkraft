---
title: "Examples: Using PATH Mode"
topic: "xml-data"
description: |
  Article

  •

  08/10/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  The following examples illustrate the use of PATH mode in generating XML from a SELECT

  query. Many of
tags:
  - "xml-data"
  - "examples-using-path-mode"
pubDate: 2025-12-01
---

Article

•

08/10/2023

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The following examples illustrate the use of PATH mode in generating XML from a SELECT

query. Many of these queries are specified against the bicycle manufacturing instructions XML

documents that are stored in the Instructions column of the ProductModel table.

This query specifies a FOR XML PATH mode.

The following result is element-centric XML where each column value in the resulting rowset is

wrapped in an element. Because the

clause doesn't specify any aliases for the column

names, the child element names generated are the same as the corresponding column names

in the

clause. For each row in the rowset a

tag is added.

XML

The following result is the same as the

mode query with the

option specified. It

returns element-centric XML with a default

element for each row in the result set.

```sql
SELECT
SELECT
<row>
RAW
ELEMENTS
<row>
USE
AdventureWorks2022;
GO
SELECT
ProductModelID,
Name
FROM
Production.ProductModel
WHERE
ProductModelID=122
OR
ProductModelID=119
FOR
XML
PATH
;
GO
<row>
<ProductModelID>
122
</ProductModelID>
<Name>
All-Purpose Bike Stand
</Name>
</row>
<row>
<ProductModelID>
119
</ProductModelID>
<Name>
Bike Wash
</Name>
</row>
```
