---
name: "calculations"
title: "calculations"
category: "statements"
description: "This example returns only the rows for"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

This example returns only the rows for

that have a product line of

and that have

days to manufacture that's less than

.

SQL

The following examples return all rows from the

table. The first example returns total

sales and the discounts for each product. In the second example, the total revenue is calculated

for each product.

SQL

This query calculates the revenue for each product in each sales order.

SQL

```sql
Product
```

```sql
R
```

```sql
4
```

```sql
Product
```

```sql
FROM
Production.Product
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
FROM
Production.Product
WHERE
ProductLine =
'R'
AND
DaysToManufacture < 4
ORDER
BY
Name
ASC
;
GO
```

```sql
USE
AdventureWorks2025;
GO
SELECT
p.Name
AS
ProductName,
NonDiscountSales = (OrderQty * UnitPrice),
Discounts = ((OrderQty * UnitPrice) * UnitPriceDiscount)
FROM
Production.Product
AS
p
INNER
JOIN
Sales.SalesOrderDetail
AS
sod
ON
p.ProductID = sod.ProductID
ORDER
BY
ProductName
DESC
;
GO
```
