---
name: "K. Use the HAVING clause"
title: "K. Use the HAVING clause"
category: "statements"
description: "The following example finds the average price of each type of product and orders the results"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

SQL

The following example finds the average price of each type of product and orders the results

by average price.

SQL

The first example that follows shows a

clause with an aggregate function. It groups the

rows in the

table by product ID and eliminates products whose average

order quantities are five or less. The second example shows a

clause without aggregate

functions.

SQL

```sql
HAVING
```

```sql
SalesOrderDetail
```

```sql
HAVING
```

```sql
USE
AdventureWorks2025;
GO
SELECT
AVG
(OrderQty)
AS
[Average Quantity],
NonDiscountSales = (OrderQty * UnitPrice)
FROM
Sales.SalesOrderDetail
GROUP
BY
(OrderQty * UnitPrice)
ORDER
BY
(OrderQty * UnitPrice)
DESC
;
GO
```

```sql
USE
AdventureWorks2025;
GO
SELECT
ProductID,
AVG
(UnitPrice)
AS
[Average Price]
FROM
Sales.SalesOrderDetail
WHERE
OrderQty > 10
GROUP
BY
ProductID
ORDER
BY
AVG
(UnitPrice);
GO
```

```sql
USE
AdventureWorks2025;
GO
SELECT
ProductID
FROM
Sales.SalesOrderDetail
GROUP
BY
ProductID
HAVING
AVG
(OrderQty) > 5
```
