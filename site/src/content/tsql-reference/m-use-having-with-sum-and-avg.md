---
name: "M. Use HAVING with SUM and AVG"
title: "M. Use HAVING with SUM and AVG"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

This query uses the

clause in the

clause.

The following example shows using

,

,

, and

clauses in one

statement. It produces groups and summary values but does so after eliminating the

products with prices over $25 and average order quantities under 5. It also organizes the

results by

.

The following example groups the

table by product ID and includes only

those groups of products that have orders totaling more than

and whose average

order quantities are less than

.

`LIKE`

`HAVING`

```sql
GROUP BY
```

`HAVING`

`WHERE`

```sql
ORDER BY
```

`SELECT`

`ProductID`

`SalesOrderDetail`

```sql
$1000000.00
```

```sql
3
```

```sql
ORDER
BY
ProductID;
GO
USE
AdventureWorks2025;
GO
SELECT
SalesOrderID,
CarrierTrackingNumber
FROM
Sales.SalesOrderDetail
GROUP
BY
SalesOrderID, CarrierTrackingNumber
HAVING
CarrierTrackingNumber
LIKE
'4BD%'
ORDER
BY
SalesOrderID;
```

```sql
USE
AdventureWorks2025;
GO
SELECT
ProductID
FROM
Sales.SalesOrderDetail
WHERE
UnitPrice < 25.00
GROUP
BY
ProductID
HAVING
AVG (OrderQty) > 5
ORDER
BY
ProductID;
GO
```
