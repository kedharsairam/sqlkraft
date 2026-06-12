---
name: "F. Use GROUP BY"
title: "F. Use GROUP BY"
category: "statements"
description: "This example uses two correlated subqueries to find the names of employees who sold a"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

This example uses two correlated subqueries to find the names of employees who sold a

particular product.

The following example finds the total of each sales order in the database.

```sql
HAVING
MAX (p1.ListPrice) >= (
SELECT
AVG (p2.ListPrice) * 2
FROM
Production.Product
AS p2
WHERE p1.ProductModelID = p2.ProductModelID
);
GO
USE
AdventureWorks2025;
GO
SELECT
DISTINCT pp.LastName,
pp.FirstName
FROM
Person.Person pp
INNER
JOIN
HumanResources.Employee e
ON e.BusinessEntityID = pp.BusinessEntityID
WHERE pp.BusinessEntityID
IN (
SELECT
SalesPersonID
FROM
Sales.SalesOrderHeader
WHERE
SalesOrderID
IN (
SELECT
SalesOrderID
FROM
Sales.SalesOrderDetail
WHERE
ProductID
IN (
SELECT
ProductID
FROM
Production.Product p
WHERE
ProductNumber =
'BK-M68B-42'
)
)
);
GO
```

```sql
USE
AdventureWorks2025;
GO
SELECT
SalesOrderID,
SUM (LineTotal)
AS
SubTotal
FROM
Sales.SalesOrderDetail
GROUP
BY
SalesOrderID
ORDER
BY
SalesOrderID;
GO
```
