---
title: 'Space used in large objects'
topic: 'query-processing'
description: 'If the size is large, the entire old row version is stored in a separate internal table.'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

If the size is large, the entire old row version is stored in a separate internal table.

The first two methods are called

version storage. The last method is called

version

storage. When in-row versions are no longer needed, they're removed to free up space on pages.

Similarly, pages in the internal table containing no longer needed off-row versions are removed

by the version cleaner.

Storing row versions as part of the row optimizes data retrieval by transactions that need to read

row versions. If a version is stored in-row, a separate read of an off-row PVS page isn't required.

The

sys.dm_db_index_physical_stats

DMV provides the number and type of versions stored in-

row and off-row for a partition of an index. The total size of version data stored in-row is

reported in the

column.

The size of the off-row version storage is reported in the

column in the

sys.dm_tran_persistent_version_store_stats

DMV.

The Database Engine supports several data types that can hold large strings up to 2 gigabytes

(GB) in length, such as:

,

,

,

,

, and

.

Large data stored using these data types are stored in a series of data fragments that are linked

to the data row. Row versioning information is stored in each fragment used to store these large

strings. Data fragments are stored in a set of pages dedicated to large objects in a table.

As new large values are added to a database, they're allocated using a maximum of 8040 bytes of

data per fragment. Earlier versions of the Database Engine stored up to 8,080 bytes of

,

, or

data per fragment.

Existing

,

, and

large object (LOB) data isn't updated to make space for the row

versioning information when a database is upgraded to SQL Server from an earlier version of SQL

Server. However, the first time the LOB data is modified, it's dynamically upgraded to enable

storage of versioning information. This happens even if row versions aren't generated. After the

LOB data is upgraded, the maximum number of bytes stored per fragment is reduced from 8,080

bytes to 8,040 bytes. The upgrade process is equivalent to deleting the LOB value and reinserting

the same value. The LOB data is upgraded even if only 1 byte is modified. This is a one-time

operation for each

,

, or

column, but each operation might generate a large

amount of page allocations and I/O activity depending upon the size of the LOB data. It might

also generate a large amount of logging activity if the modification is fully logged.

and

operations are minimally logged if the database recovery model isn't set to FULL.

```sql
total_inrow_version_payload_size_in_bytes
```

```sql
persistent_version_store_size_kb
```

```sql
nvarchar(max)
```

```sql
varchar(max)
```

```sql
varbinary(max)
```

```sql
ntext
```

```sql
text
```

```sql
image
```

```sql
ntext
```

```sql
text
```

```sql
image
```

```sql
ntext
```

```sql
text
```

```sql
image
```

```sql
ntext
```

```sql
text
```

```sql
image
```

```sql
WRITETEXT
```

```sql
UPDATETEXT
```
