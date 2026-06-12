---
name: "Table fragmentation"
title: "Table fragmentation"
category: "data-types"
description: "performance. A fast scan doesn't read the leaf or data level pages of the index. The"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

performance. A fast scan doesn't read the leaf or data level pages of the index. The

option doesn't apply to a heap.

doesn't display data with

,

, and

data types. This is because

text indexes that store text and image data no longer exist.

Also,

doesn't support some new features. For example:

If the specified table or index is partitioned,

only displays the first

partition of the specified table or index.

doesn't display row-overflow storage information and other new off-row

data types, such as

,

,

, and.

Spatial indexes aren't supported by.

All new features are fully supported by the

sys.dm_db_index_physical_stats (Transact-SQL)

dynamic management view.

determines whether the table is heavily fragmented. Table fragmentation

occurs through the process of data modifications (INSERT, UPDATE, and DELETE statements)

made against the table. Because these modifications aren't ordinarily distributed equally

among the rows of the table, the fullness of each page can vary over time. For queries that

scan part or all of a table, such table fragmentation can cause additional page reads. This

hinders parallel scanning of data.

When an index is heavily fragmented, the following choices are available for reducing

fragmentation:

Drop and re-create a clustered index.

Re-creating a clustered index reorganizes the data, and causes full data pages. The level

of fullness can be configured by using the

option in. The

drawbacks of this method are that the index is offline during the drop or re-create cycle,

and that the operation is atomic. If the index creation is interrupted, the index isn't re-

created.

Reorder the leaf-level pages of the index in a logical order.

### Avg. Bytes free per page

### Avg. Page density (full)

### Avg. Bytes free per page

### Avg.

### Page density (full)

### Extent Switches

### Extents Scanned

### Extent Switches

### Extents Scanned

### Scan Density

### Logical Scan Fragmentation

### Extent Scan Fragmentation

### Logical Scan Fragmentation

### Extent Scan Fragmentation

Use

to reorder the leaf-level pages of the index in a logical

order. Because this operation is an online operation, the index is available when the

statement is running. The operation is also interruptible without loss of completed work.

The drawback of this method is that the method doesn't do as good a job of reorganizing

the data as a clustered index drop or re-create operation.

Rebuild the index.

Use

with

to rebuild the index. For more information, see

ALTER

INDEX (Transact-SQL).

The

and

statistic in the result set indicate the

fullness of index pages. The

number should be low and the

number should be high for an index that won't have many random inserts.

Dropping and re-creating an index with the

option specified can improve the

statistics. Also,

with

will compact an index, taking into account its

, and will improve the statistics.

The fragmentation level of an index can be determined in the following ways:

By comparing the values of

and.

The value of

should be as close as possible to that of.

This ratio is calculated as the

value. This value should be as high as possible,

and can be improved by reducing index fragmentation.

By understanding

and

values.

and, to a lesser extent,

values

are the best indicators of the fragmentation level of a table. Both these values should be

as close to zero as possible, although a value from 0 through 10 percent may be

acceptable.

７

Note

An index that has many random inserts and very full pages will have an increased number

of page splits. This causes more fragmentation.

７

Note

This method does not work if the index spans multiple files.

### sysadmin

### db_owner

### db_ddladmin

### Extent Scan Fragmentation

```sql
WITH FAST
```

```sql
DBCC SHOWCONTIG
```

```sql
DBCC SHOWCONTIG
```

```sql
DBCC SHOWCONTIG
```

```sql
DBCC SHOWCONTIG
```

```sql
DBCC SHOWCONTIG
```

```sql
DBCC SHOWCONTIG
```

`FILLFACTOR`

```sql
CREATE INDEX
```

```sql
ALTER INDEX.REORGANIZE
```

```sql
ALTER INDEX
```

`REBUILD`

`FILLFACTOR`

```sql
ALTER INDEX
```

`REORGANIZE`

`FILLFACTOR`
