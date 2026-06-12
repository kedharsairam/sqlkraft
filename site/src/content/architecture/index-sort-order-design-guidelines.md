---
title: "Index sort order design guidelines"
topic: "index-architecture"
description: ""
tags: ["index-architecture","architecture"]
pubDate: "2026-05-29"
---

For more information, see

Partitioned tables and indexes.

When defining indexes, consider whether each index key column should be stored in

ascending or descending order. Ascending is the default. The syntax of the

,

, and

statements supports the keywords

(ascending) and

(descending) on individual columns in indexes and constraints.

Specifying the order in which key values are stored in an index is useful when queries

referencing the table have

clauses that specify different directions for the key column

or columns in that index. In these cases, the index can remove the need for a

operator

in

the query plan.

For example, the buyers in the Adventure Works Cycles purchasing department have to

evaluate the quality of products they purchase from vendors. The buyers are most interested in

finding products sent by vendors with a high rejection rate.

As shown in the following query against the

AdventureWorks sample database

, retrieving the

data to meet this criteria requires the

column in the

table to be sorted in descending order (large to small) and

the

column to be sorted in ascending order (small to large).

The following

execution plan

for this query shows that the query optimizer used a

operator to return the result set in the order specified by the

clause.

２

Warning

Partitioning rarely improves query performance in OLTP systems, but it can introduce a

significant overhead if a transactional query must access many partitions.

### Sort

### Sort

### base table

```sql
CREATE INDEX
```

```sql
CREATE TABLE
```

```sql
ALTER TABLE
```

`ASC`

`DESC`

```sql
ORDER BY
```

`RejectedQty`

`Purchasing.PurchaseOrderDetail`

`ProductID`

```sql
ORDER BY
```

```sql
SELECT
RejectedQty,
((RejectedQty / OrderQty) * 100)
AS
RejectionRate,
ProductID,
DueDate
FROM
Purchasing.PurchaseOrderDetail
ORDER
BY
RejectedQty
DESC
, ProductID
ASC
;
```
