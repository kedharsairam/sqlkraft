---
title: "Filtered index design guidelines"
topic: "index-architecture"
description: "constraint can't be created if duplicate"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

A unique index,

constraint, or

constraint can't be created if duplicate

key values exist in the data.

If the data is unique and you want uniqueness enforced, creating a unique index instead

of a nonunique index on the same combination of columns provides additional

information for the query optimizer that can produce more efficient execution plans.

Creating a

constraint or a unique index is recommended in this case.

A unique nonclustered index can contain included nonkey columns. For more

information, see

Use included columns in nonclustered indexes

.

Unlike a

constraint, a

constraint or a unique index can be created

with a nullable column in the index key. For the purposes of uniqueness enforcement, two

NULLs are considered equal. For example, this means that in a single-column unique

index, the column can be NULL for one row in the table only.

A filtered index is an optimized nonclustered index, especially suited for queries that require a

small subset of data in the table. It uses a filter predicate in the index definition to index a

portion of rows in the table. A well-designed filtered index can improve query performance,

reduce index update costs, and reduce index storage costs compared with a full-table index.

Filtered indexes can provide the following advantages over full-table indexes:

A well-designed filtered index improves query performance and execution plan quality

because it's smaller than a full-table nonclustered index. A filtered index has filtered

statistics

, which are more accurate than full-table statistics because they cover only the

rows in the filtered index.

An index is updated only when data manipulation language (DML) statements affect the

data in the index. A filtered index reduces index update costs compared with a full-table

nonclustered index because it's smaller and is only updated when the data in the index is

affected. It's possible to have a large number of filtered indexes, especially when they

contain data that is affected infrequently. Similarly, if a filtered index contains only the

frequently affected data, the smaller size of the index reduces the cost of updating

statistics.

### Reduced index storage costs

```sql
UNIQUE
```

```sql
PRIMARY KEY
```

```sql
UNIQUE
```

```sql
PRIMARY KEY
```

```sql
UNIQUE
```
