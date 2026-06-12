---
name: "A. Use SELECT to retrieve rows and columns"
title: "A. Use SELECT to retrieve rows and columns"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

This article provides examples of using the

SELECT

statement.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

The following example shows three code examples. The first code example returns all rows (no

clause is specified) and all columns (using the

) from the

table in the

database.

This example returns all rows (no

clause is specified), and only a subset of the columns

(

,

,

) from the

table in the

database.

Additionally, a column heading is added.

`AdventureWorks2025`

`AdventureWorksDW2025`

`WHERE`

```sql
*
```

`Product`

`AdventureWorks2025`

`WHERE`

`Name`

`ProductNumber`

`ListPrice`

`Product`

`AdventureWorks2025`

```sql
USE
AdventureWorks2025;
GO
SELECT
*
FROM
Production.Product
ORDER
BY
Name
ASC
;
-- Alternate way.
USE
AdventureWorks2025;
GO
SELECT p.*
FROM
Production.Product
AS p
ORDER
BY
Name
ASC
;
GO
USE
AdventureWorks2025;
GO
SELECT
Name
,
ProductNumber,
ListPrice
AS
Price
```
