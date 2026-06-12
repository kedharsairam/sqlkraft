---
name: "Set options"
title: "Set options"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Row and page locks options

Disabling an index prevents user access to the index, and for clustered indexes, to the

underlying table data. The index definition remains in the system catalog. Disabling a

nonclustered index or clustered index on a view physically deletes the index data. Disabling a

clustered index prevents access to the data, but the data remains unmaintained in the B-tree

until the index is dropped or rebuilt. To see if an index is disabled, use the

column

in the

catalog view.

If a table is in a transactional replication publication, you can't disable an index that is

associated with a primary key constraint. These indexes are required by replication. To disable

such an index, you must first drop the table from the publication. For more information, see

Publish Data and Database Objects.

Use the

statement or the

statement to

enable the index. Rebuilding a disabled clustered index can't be performed with the

option set to. For more information, see

Disable indexes and constraints.

You can set the options

,

,

,

, and

for a specified index without rebuilding or

reorganizing that index. The modified values are immediately applied to the index. To view

these settings, use. For more information, see

Set Index Options.

When

and

, row-level, page-level, and table-level

locks are allowed when you access the index. The Database Engine chooses the appropriate

lock and can escalate the lock from a row or page lock to a table lock.

When

and

, only a table-level lock is allowed

when you access the index.

７

Note

Documentation uses the term B-tree generally in reference to indexes. In rowstore

indexes, the Database Engine implements a B+ tree. This does not apply to columnstore

indexes or indexes on memory-optimized tables. For more information, see the.

#### Option

#### Applies to

`is_disabled`

`sys.indexes`

```sql
ALTER INDEX REBUILD
```

```sql
CREATE INDEX WITH DROP_EXISTING
```

`ONLINE`

`ON`

`ALLOW_ROW_LOCKS`

`ALLOW_PAGE_LOCKS`

`OPTIMIZE_FOR_SEQUENTIAL_KEY`

`IGNORE_DUP_KEY`

`STATISTICS_NORECOMPUTE`

`sys.indexes`

```sql
ALLOW_ROW_LOCKS = ON
```

```sql
ALLOW_PAGE_LOCK = ON
```

```sql
ALLOW_ROW_LOCKS = OFF
```

```sql
ALLOW_PAGE_LOCK = OFF
```
