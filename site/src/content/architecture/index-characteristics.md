---
title: 'Index characteristics'
topic: 'index-architecture'
description: 'Examine column uniqueness. A unique index instead of a nonunique index on the same'
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

Examine column uniqueness. A unique index instead of a nonunique index on the same

key columns provides additional information for the query optimizer that makes the index

more useful. For more information, see

Unique index design guidelines

in this guide.

Examine data distribution in the column. Creating an index on a column with many rows

but few distinct values might not improve query performance even if the index is used by

the query optimizer. As an analogy, a physical telephone directory sorted alphabetically

on family name doesn't expedite locating a person if all people in the city are named

Smith or Jones. For more information about data distribution, see

Statistics

.

Consider using filtered indexes on columns that have well-defined subsets, for example

columns with many NULLs, columns with categories of values, and columns with distinct

ranges of values. A well-designed filtered index can improve query performance, reduce

index update costs, and reduce storage costs by storing a small subset of all rows in the

table if that subset is relevant for many queries.

Consider the order of the index key columns if the key contains multiple columns. The

column that is used in the query predicate in an equality (

), inequality (

,

,

,

), or

expression, or participates in a join, should be placed first. Additional columns

should be ordered based on their level of distinctness, that is, from the most distinct to

the least distinct.

For example, if the index is defined as

,

, the index is useful when the

query predicate in the

clause is

or

. However, the query optimizer wouldn't use the index for

a query that searched only on

, or the index wouldn't improve

the performance of such a query.

Consider indexing computed columns if they are included in query predicates. For more

information, see

Indexes on computed columns

.

After you determine that an index is appropriate for a query, you can select the type of index

that best fits your situation. Index characteristics include:

Clustered or nonclustered

Unique or nonunique

Single column or multicolumn

Ascending or descending order for the key columns in the index

All rows or filtered, for nonclustered indexes

Columnstore or rowstore

```sql
=
```

```sql
>
```

```sql
>=
```

```sql
<
```

```sql
<=
```

```sql
BETWEEN
```

```sql
LastName
```

```sql
FirstName
```

```sql
WHERE
```

```sql
WHERE LastName = 'Smith'
```

```sql
WHERE LastName =
Smith AND FirstName LIKE 'J%'
```

```sql
WHERE FirstName = 'Jane'
```
