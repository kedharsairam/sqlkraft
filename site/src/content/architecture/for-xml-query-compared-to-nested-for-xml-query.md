---
title: "FOR XML Query Compared to Nested FOR XML Query"
topic: "xml-data"
description: |
  Article

  •

  05/24/2024

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  This article compares a single-level

  query to a nested

  query. One of the

  benefits of using nested

  q
tags:
  - "xml-data"
  - "for-xml-query-compared-to-nested-for-xml-query"
pubDate: 2025-12-01
---

Article

•

05/24/2024

SQL Server

Azure SQL Database

Azure SQL Managed Instance

This article compares a single-level

query to a nested

query. One of the

benefits of using nested

queries is that you can specify a combination of attribute-

centric and element-centric XML for query results. The example demonstrates this benefit.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

The following

query retrieves product category and subcategory information in the

database. There's no nested

in the query.

Here's the partial result:

XML

```sql
FOR XML
FOR XML
FOR XML
AdventureWorks2022
AdventureWorksDW2022
SELECT
AdventureWorks2022
FOR XML
USE
AdventureWorks2022;
GO
SELECT
ProductCategory.ProductCategoryID,
ProductCategory.Name
AS
CategoryName,
ProductSubCategory.ProductSubCategoryID,
ProductSubCategory.Name
FROM
Production.ProductCategory,
Production.ProductSubCategory
WHERE
ProductCategory.ProductCategoryID = ProductSubCategory.ProductCategoryID
ORDER
BY
ProductCategoryID
FOR
XML
AUTO
,
TYPE
;
GO
<ProductCategory
ProductCategoryID
=
"1"
CategoryName
=
"Bike"
>
<ProductSubCategory
ProductSubCategoryID
=
"1"
Name
=
"Mountain Bike"
/>
<ProductSubCategory
ProductSubCategoryID
=
"2"
Name
=
"Road Bike"
/>
<ProductSubCategory
ProductSubCategoryID
=
"3"
Name
=
"Touring Bike"
/>
</ProductCategory>.
```
