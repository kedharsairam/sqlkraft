---
name: "I. Use GROUP BY with an expression"
title: "I. Use GROUP BY with an expression"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Because of the

clause, the query returns only one row containing the sum of all sales

for each sales order.

The following example finds the average price and the sum of year-to-date sales, grouped by

product ID and special offer ID.

The following example puts the results into groups after retrieving only the rows with list prices

greater than.

The following example groups by an expression. You can group by an expression if the

expression doesn't include aggregate functions.

```sql
GROUP BY
```

```sql
$1000
```

```sql
USE
AdventureWorks2025;
GO
SELECT
ProductID,
SpecialOfferID,
AVG (UnitPrice)
AS
[Average Price],
SUM (LineTotal)
AS
SubTotal
FROM
Sales.SalesOrderDetail
GROUP
BY
ProductID,
SpecialOfferID
ORDER
BY
ProductID;
GO
```

```sql
USE
AdventureWorks2025;
GO
SELECT
ProductModelID,
AVG (ListPrice)
AS
[Average
List
Price]
FROM
Production.Product
WHERE
ListPrice > $1000
GROUP
BY
ProductModelID
ORDER
BY
ProductModelID;
GO
```
