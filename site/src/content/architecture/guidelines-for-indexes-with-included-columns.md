---
title: "Guidelines for indexes with included columns"
topic: "index-architecture"
description: "An index with included nonkey columns can significantly improve query performance when it"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

An index with included nonkey columns can significantly improve query performance when it

covers the query, that is, when all columns used in the query are in the index either as key or

nonkey columns. Performance gains are achieved because the Database Engine can locate all

the column values within the index; the base table isn't accessed, resulting in fewer disk I/O

operations.

If a column must be retrieved by a query, but isn't used in the query predicates, aggregations,

and sorts, add it as an included column and not as a key column. This has the following

advantages:

Included columns can use data types not allowed as index key columns.

Included columns aren't considered by the Database Engine when calculating the number

of index key columns or index key size. With included columns, you aren't limited by the

900-byte maximum key size. You can create wider indexes that cover more queries.

When you move a column from the index key to included columns, index build takes less

time because the index sort operation becomes faster.

If the table has a clustered index, the column or columns defined in the clustered index key are

automatically added to each nonunique nonclustered index on the table. It's not necessary to

specify them either in the nonclustered index key or as included columns.

Consider the following guidelines when you design nonclustered indexes with included

columns:

Included columns can only be defined in nonclustered indexes on tables or indexed views.

All data types are allowed except

,

, and

.

Computed columns that are deterministic and either precise or imprecise can be included

columns. For more information, see

Indexes on computed columns

.

As with key columns, computed columns derived from

,

, and

data types

can be included columns as long as the computed column data type is allowed in an

included column.

Column names can't be specified in both the

list and in the key column list.

Column names can't be repeated in the

list.

At least one key column must be defined in an index. The maximum number of included

columns is 1,023. This is the maximum number of table columns minus 1.

### Index Seek

```sql
INCLUDE
```

```sql
INCLUDE
```
