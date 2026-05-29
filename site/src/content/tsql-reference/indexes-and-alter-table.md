---
name: "Indexes and ALTER TABLE"
title: "Indexes and ALTER TABLE"
category: "statements"
description: "statement requires changing a column used in a schema-bound view,"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

view. If the

statement requires changing a column used in a schema-bound view,

fails and the Database Engine raises an error message. For more information about

schema binding and indexed views, see

CREATE VIEW (Transact-SQL)

.

Adding or removing triggers on base tables isn't affected by creating a schema-bound view that

references the tables.

Indexes created as part of a constraint are dropped when the constraint is dropped. To drop

indexes that you created by using

, use

. Use the

statement

to rebuild an index that's part of a constraint definition. You don't need to drop and add the

constraint again by using

.

You must remove all indexes and constraints that are based on a column before you can remove

that column.

When you delete a constraint that created a clustered index, the data rows that were stored in

the leaf level of the clustered index are stored in a nonclustered table. You can drop the clustered

index and move the resulting table to another filegroup or partition scheme in a single

transaction by specifying the

option. The

option has the following restrictions:

isn't valid for indexed views or nonclustered indexes.

The partition scheme or filegroup must already exist.

If you don't specify

, the table is located in the same partition scheme or filegroup

as was defined for the clustered index.

When you drop a clustered index, specify the

option so the

transaction

doesn't block queries and modifications to the underlying data and associated nonclustered

indexes.

has the following restrictions:

isn't valid for clustered indexes that are also disabled. You must drop disabled

indexes by using

.

You can only drop one index at a time.

isn't valid for indexed views, nonclustered indexes, or indexes on local temp

tables.

isn't valid for columnstore indexes.

### ntext

### ntext

### ntext

```sql
ALTER TABLE
```

```sql
ALTER TABLE
```

```sql
CREATE INDEX
```

```sql
DROP INDEX
```

```sql
ALTER INDEX
```

```sql
ALTER TABLE
```

```sql
MOVE TO
```

```sql
MOVE TO
```

```sql
MOVE TO
```

```sql
MOVE TO
```

```sql
ONLINE = ON
```

```sql
DROP INDEX
```

```sql
ONLINE = ON
```

```sql
ONLINE = ON
```

```sql
ONLINE = OFF
```

```sql
ONLINE = ON
```

```sql
ONLINE = ON
```
