---
title: 'Use included columns in nonclustered indexes'
topic: 'index-architecture'
description: 'Nonclustered indexes have one row in'
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

Nonclustered indexes have one row in

sys.partitions

for each partition used by the index, with

. By default, a nonclustered index has a single partition. When a nonclustered

index has multiple partitions, each partition has a B+ tree structure that contains the index

rows for that specific partition. For example, if a nonclustered index has four partitions, there

are four B+ tree structures, one in each partition.

Depending on the data types in the nonclustered index, each nonclustered index structure has

one or more allocation units in which to store and manage the data for a specific partition. At a

minimum, each nonclustered index has one

allocation unit per partition that

stores the index B+ tree pages. The nonclustered index also has one

allocation unit

per partition if it contains large object (LOB) columns such as

. Additionally, it

has one

allocation unit per partition if it contains variable length columns

that exceed the 8,060-byte row size limit.

The following illustration shows the structure of a nonclustered index in a single partition.

In addition to key columns, a nonclustered index can also have nonkey columns stored in the

leaf level. These nonkey columns are called included columns and are specified in the

clause of the

statement.

### text

### ntext

### image

### image

### ntext

### text

```sql
index_id > 1
```

```sql
IN_ROW_DATA
```

```sql
LOB_DATA
```

```sql
ROW_OVERFLOW_DATA
```

```sql
INCLUDE
```

```sql
CREATE INDEX
```
