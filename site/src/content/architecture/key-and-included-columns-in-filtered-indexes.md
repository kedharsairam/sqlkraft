---
title: 'Key and included columns in filtered indexes'
topic: 'index-architecture'
description: 'covers the following query because the query results'
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

The filtered index

covers the following query because the query results

are contained in the index and the query plan doesn't require accessing the base table. For

example, the query predicate expression

is a subset of the filtered

index predicate

and

, the

and

columns in the query predicate are both key columns in

the index, and name is stored in the leaf level of the index as an included column.

SQL

It's a best practice to add a small number of columns in a filtered index definition, only as

necessary for the query optimizer to choose the filtered index for the query execution plan. The

query optimizer can choose a filtered index for the query regardless of whether it does or

doesn't cover the query. However, the query optimizer is more likely to choose a filtered index

if it covers the query.

In some cases, a filtered index covers the query without including the columns in the filtered

index expression as key or included columns in the filtered index definition. The following

guidelines explain when a column in the filtered index expression should be a key or included

column in the filtered index definition. The examples refer to the filtered index,

that was created previously.

A column in the filtered index expression doesn't need to be a key or included column in the

filtered index definition if the filtered index expression is equivalent to the query predicate and

the query doesn't return the column in the filtered index expression with the query results. For

example,

covers the following query because the query

predicate is equivalent to the filter expression, and

isn't returned with the query

results. The

index doesn't need

as a key or included

column in the filtered index definition.

SQL

```sql
FIProductAccessories
```

```sql
ProductSubcategoryID = 33
```

```sql
ProductSubcategoryID >= 27
```

```sql
ProductSubcategoryID <= 36
```

```sql
ProductSubcategoryID
```

```sql
ListPrice
```

```sql
FIBillOfMaterialsWithEndDate
```

```sql
FIBillOfMaterialsWithEndDate
```

```sql
EndDate
```

```sql
FIBillOfMaterialsWithEndDate
```

```sql
EndDate
```

```sql
SELECT
Name
,
ProductSubcategoryID,
ListPrice
FROM
Production.Product
WHERE
ProductSubcategoryID = 33
AND
ListPrice > 25.00;
```

```sql
SELECT
ComponentID,
StartDate
```
