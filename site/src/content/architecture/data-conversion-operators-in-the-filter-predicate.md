---
title: "Data conversion operators in the filter predicate"
topic: "io-fundamentals"
description: "A column in the filtered index expression should be a key or included column in the filtered"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

A column in the filtered index expression should be a key or included column in the filtered

index definition if the query predicate uses the column in a comparison that isn't equivalent to

the filtered index expression. For example,

is valid for the

following query because it selects a subset of rows from the filtered index. However, it doesn't

cover the following query because

is used in the comparison

,

which isn't equivalent to the filtered index expression. The query processor can't execute this

query without examining the values of. Therefore,

should be a key or

included column in the filtered index definition.

A column in the filtered index expression should be a key or included column in the filtered

index definition if the column is in the query result set. For example,

doesn't cover the following query because it returns the

column in the query results. Therefore,

should be a key or included column in

the filtered index definition.

The clustered index key of the table doesn't need to be a key or included column in the filtered

index definition. The clustered index key is automatically included in all nonclustered indexes,

including filtered indexes.

If the comparison operator specified in the filtered index expression of the filtered index results

in an implicit or explicit data conversion, an error occurs if the conversion occurs on the left

side of a comparison operator. A solution is to write the filtered index expression with the data

conversion operator (

or

) on the right side of the comparison operator.

`FIBillOfMaterialsWithEndDate`

`EndDate`

```sql
EndDate > '20040101'
```

`EndDate`

`EndDate`

`FIBillOfMaterialsWithEndDate`

`EndDate`

`EndDate`

`CAST`

`CONVERT`

```sql
FROM
Production.BillOfMaterials
WHERE
EndDate
IS
NOT
NULL
;
SELECT
ComponentID,
StartDate
FROM
Production.BillOfMaterials
WHERE
EndDate >
'20040101'
;
SELECT
ComponentID,
StartDate,
EndDate
FROM
Production.BillOfMaterials
WHERE
EndDate
IS
NOT
NULL
;
```
