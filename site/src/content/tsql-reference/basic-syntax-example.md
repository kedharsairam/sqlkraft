---
name: "Basic syntax example"
title: "Basic syntax example"
category: "statements"
description: "You can't change the compression setting of a single partition if the table has nonaligned"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

You can't change the compression setting of a single partition if the table has nonaligned

indexes.

The

## syntax

rebuilds the specified partition of the index with the specified compression option. If the

clause is omitted, the existing compression option is used.

The

## syntax rebuilds all partitions of

the index using the existing compression options.

The

## syntax rebuilds all

partitions of the index. You can choose different compression for different partitions

using the

clause.

To evaluate how changing

and

compression affects a table, an index, or a partition,

use the

sp_estimate_data_compression_savings

stored procedure.

When you rebuild an index, the statistics on the index are updated with full scan for non-

partitioned indexes, and with the default sampling ratio for partitioned indexes. No other

statistics on the table are updated as a part of index rebuild.

The

permission on the table or view is required.

Azure SQL Database doesn't support filegroups other than

.

Azure SQL Database and Azure SQL Managed Instance don't support

options.

Columnstore indexes aren't available before SQL Server 2012 (11.x).

Resumable index operations are available in SQL Server 2017 (14.x) and later versions,

Azure SQL Database, and Azure SQL Managed Instance.

```sql
ALTER INDEX <index> ... REBUILD PARTITION ... WITH DATA_COMPRESSION = ...
```

```sql
WITH DATA_COMPRESSION
```

```sql
ALTER INDEX <index> ... REBUILD PARTITION = ALL
```

```sql
ALTER INDEX <index> ... REBUILD PARTITION = ALL (WITH ...)
```

```sql
DATA_COMPRESSION = ... ON PARTITIONS ( ...)
```

`PAGE`

`ROW`

`ALTER`

`PRIMARY`

`FILESTREAM`

```sql
ALTER
INDEX index1
ON table1
REBUILD
;
ALTER
INDEX
ALL
ON table1
REBUILD
;
ALTER
INDEX
ALL
ON dbo.table1
REBUILD
;
```
