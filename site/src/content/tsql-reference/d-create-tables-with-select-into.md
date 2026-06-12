---
name: "D. Create tables with SELECT INTO"
title: "D. Create tables with SELECT INTO"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

The following example uses

to prevent the retrieval of duplicate titles.

The following first example creates a temporary table named

in.

This second example creates the permanent table.

`DISTINCT`

```sql
#Bicycles
```

`tempdb`

`NewProducts`

```sql
USE
AdventureWorks2025;
GO
SELECT
'Total income is'
,
((OrderQty * UnitPrice) * (1.0 - UnitPriceDiscount)),
' for '
,
p.Name
AS
ProductName
FROM
Production.Product
AS p
INNER
JOIN
Sales.SalesOrderDetail
AS sod
ON p.ProductID = sod.ProductID
ORDER
BY
ProductName
ASC
;
GO
```

```sql
USE
AdventureWorks2025;
GO
SELECT
DISTINCT
JobTitle
FROM
HumanResources.Employee
ORDER
BY
JobTitle;
GO
```

```sql
USE tempdb;
GO
IF OBJECT_ID(N'#Bicycles', N'U') IS NOT NULL
DROP
TABLE
#Bicycles;
GO
SELECT
*
INTO
#Bicycles
FROM
AdventureWorks2025.Production.Product
WHERE
ProductNumber
LIKE
'BK%'
;
GO
```
