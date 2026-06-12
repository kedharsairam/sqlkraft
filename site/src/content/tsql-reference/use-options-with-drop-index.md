---
name: "Use options with DROP INDEX"
title: "Use options with DROP INDEX"
category: "statements"
description: "When indexes with 128 extents or more are dropped, the Database Engine defers the actual"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

When indexes with 128 extents or more are dropped, the Database Engine defers the actual

page deallocations, and their associated locks, until after the transaction commits. Indexes are

dropped in two separate phases: logical and physical. In the logical phase, the existing

allocation units used by the index are marked for deallocation and locked until the transaction

commits. In the physical phase, a background process removes the pages marked for

deallocation. This means that the space released by

might not be available for new

allocations immediately.

If

accelerated database recovery

is enabled, the separate logical and physical phases are used

regardless of the number of extents.

You can set the following index options when you drop a clustered index:

,

, and.

Use

to drop the clustered index and move the resulting table to another filegroup or

partition scheme in a single transaction.

When you specify

, queries and modifications to the underlying data and

associated nonclustered indexes aren't blocked by the

transaction. Only one

clustered index can be dropped online at a time. For a complete description of the

option, see

CREATE INDEX.

You can't drop a clustered index online if the index is disabled on a view, or contains

,

,

,

,

,

, or

columns in the leaf-level

data rows.

Using the

and

options requires more temporary disk space.

After an index is dropped, the resulting heap appears in the

catalog view with

in the

column. To view the table name, join

with

on. For an example query, see example D.

On multiprocessor computers that are running SQL Server 2005 Enterprise edition or later,

might use more processors to perform the scan and sort operations associated with

dropping the clustered index, just like other queries do. You can manually configure the

number of processors that are used to run the

statement by specifying the

index option. For more information, see

Configure Parallel Index Operations.

```sql
DROP INDEX
```

`MAXDOP`

`ONLINE`

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

`ONLINE`

```sql
ONLINE = ON
```

```sql
MOVE TO
```

`sys.indexes`

`NULL`

`name`

`sys.indexes`

`sys.tables`

`object_id`

```sql
DROP
INDEX
```

```sql
DROP INDEX
```

`MAXDOP`
