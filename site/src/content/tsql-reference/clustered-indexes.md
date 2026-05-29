---
name: "Clustered indexes"
title: "Clustered indexes"
category: "statements"
description: "You can also specify the"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

You can also specify the

option more than once, for example:

SQL

When creating the query plan for the

statement, the query optimizer might

choose to scan another index instead of performing a table scan. The sort operation might be

eliminated in some situations. On multiprocessor computers,

can use parallelism

for the scan and sort operations associated with creating the index, in the same way that other

queries do. For more information, see

Configure parallel index operations

.

The

operation might be minimally logged if the database recovery model is set

to either bulk-logged or simple.

Indexes can be created on a temporary table. When the table is dropped or goes out of scope,

the indexes are dropped.

A clustered index is built on a table variable when a primary key constraint is added. Similarly, a

nonclustered index is built on a table variable when a unique constraint is added. When the

table variable goes out of scope, the indexes are dropped.

Indexes support extended properties.

is not supported in Microsoft Fabric.

Creating a clustered index on a table (heap) or dropping and re-creating an existing clustered

index requires additional workspace to be available in the database to accommodate data

```sql
XML_COMPRESSION
```

```sql
CREATE INDEX
```

```sql
CREATE INDEX
```

```sql
CREATE INDEX
```

```sql
CREATE INDEX
```

```sql
REBUILD
WITH
(
DATA_COMPRESSION =
NONE
ON
PARTITIONS
(1),
DATA_COMPRESSION =
ROW
ON
PARTITIONS
(2, 4, 6
TO
8),
DATA_COMPRESSION = PAGE
ON
PARTITIONS
(3, 5)
);
REBUILD
WITH
(
XML_COMPRESSION =
OFF
ON
PARTITIONS
(1),
XML_COMPRESSION =
ON
ON
PARTITIONS
(2, 4, 6
TO
8),
XML_COMPRESSION =
OFF
ON
PARTITIONS
(3, 5)
);
```
