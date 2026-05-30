---
name: "N. Use the INDEX optimizer hint"
title: "N. Use the INDEX optimizer hint"
category: "statements"
description: "To see the products with total sales greater than"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

To see the products with total sales greater than

, use this query:

If you want to make sure the calculations for each product include at least 1,500 items, use

to eliminate the products that return totals for fewer than

items

sold. The query looks like this:

The following example shows two ways to use the

optimizer hint. The first example

shows how to force the optimizer to use a nonclustered index to retrieve rows from a table.

The second example forces a table scan by using an index of 0.

```sql
$2000000.00
```

```sql
HAVING COUNT(*) > 1500
```

```sql
1500
```

`INDEX`

```sql
USE
AdventureWorks2025;
GO
SELECT
ProductID,
AVG (OrderQty)
AS
AverageQuantity,
SUM (LineTotal)
AS
Total
FROM
Sales.SalesOrderDetail
GROUP
BY
ProductID
HAVING
SUM (LineTotal) > $1000000.00
AND
AVG (OrderQty) < 3;
GO
USE
AdventureWorks2025;
GO
SELECT
ProductID, Total =
SUM (LineTotal)
FROM
Sales.SalesOrderDetail
GROUP
BY
ProductID
HAVING
SUM (LineTotal) > $2000000.00;
GO
USE
AdventureWorks2025;
GO
SELECT
ProductID,
SUM (LineTotal)
AS
Total
FROM
Sales.SalesOrderDetail
GROUP
BY
ProductID
HAVING
COUNT (*) > 1500;
GO
```
