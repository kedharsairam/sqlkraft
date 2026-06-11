---
name: "E. Use correlated subqueries"
title: "E. Use correlated subqueries"
category: "statements"
description: "A correlated subquery is a query that depends on the outer query for its values."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

A correlated subquery is a query that depends on the outer query for its values. This query can

be executed repeatedly, one time for each row that the outer query selects.

The first example shows queries that are semantically equivalent to illustrate the difference

between using the

keyword and the

keyword. Both are examples of a valid

subquery that retrieves one instance of each product name for which the product model is a

long sleeve logo jersey, and the

numbers match between the

and

tables.

The next example uses

and retrieves one instance of the first name and family name of each

employee for which the bonus in the

table is

, and for which the

employee identification numbers match in the

and

tables.

The previous subquery in this statement can't be evaluated independently of the outer query. It

requires a value for

, but this value changes as the SQL Server Database

Engine examines different rows in

.

You can also use a correlated subquery in the

clause of an outer query. This example

finds the product models for which the maximum list price is more than twice the average for

the model.

`EXISTS`

`IN`

`ProductModelID`

`Product`

`ProductModel`

```sql
USE
AdventureWorks2025;
GO
IF OBJECT_ID('dbo.NewProducts', 'U') IS NOT NULL
DROP
TABLE dbo.NewProducts;
GO
ALTER
DATABASE
AdventureWorks2025
SET
RECOVERY
BULK_LOGGED;
GO
SELECT
*
INTO dbo.NewProducts
FROM
Production.Product
WHERE
ListPrice > $25
AND
ListPrice < $100;
GO
ALTER
DATABASE
AdventureWorks2025
SET
RECOVERY
FULL
;
GO
```

```sql
USE
AdventureWorks2025;
GO
SELECT
DISTINCT
Name
FROM
Production.Product
AS p
WHERE
EXISTS (
SELECT
*
FROM
Production.ProductModel
AS pm
WHERE p.ProductModelID = pm.ProductModelID
AND pm.Name
LIKE
'Long-Sleeve Logo Jersey%'
);
GO
-- OR
```

`IN`

`SalesPerson`

```sql
5000.00
```

`Employee`

`SalesPerson`

`Employee.EmployeeID`

`Employee`

`HAVING`

```sql
USE
AdventureWorks2025;
GO
SELECT
DISTINCT
Name
FROM
Production.Product
WHERE
ProductModelID
IN (
SELECT
ProductModelID
FROM
Production.ProductModel
AS pm
WHERE p.ProductModelID = pm.ProductModelID
AND
Name
LIKE
'Long-Sleeve Logo Jersey%'
);
GO
USE
AdventureWorks2025;
GO
SELECT
DISTINCT p.LastName,
p.FirstName
FROM
Person.Person
AS p
INNER
JOIN
HumanResources.Employee
AS e
ON e.BusinessEntityID = p.BusinessEntityID
WHERE
5000.00
IN (
SELECT
Bonus
FROM
Sales.SalesPerson
AS sp
WHERE e.BusinessEntityID = sp.BusinessEntityID
);
GO
USE
AdventureWorks2025;
GO
SELECT p1.ProductModelID
FROM
Production.Product
AS p1
GROUP
BY p1.ProductModelID
```
