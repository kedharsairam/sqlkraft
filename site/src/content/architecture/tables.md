---
title: "tables"
topic: "query-processing"
description: "The performance of a hash index is:"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

The performance of a hash index is:

Excellent when the predicate in the

clause specifies an

exact

value for each column

in the hash index key. A hash index reverts to a scan given an inequality predicate.

Poor when the predicate in the

clause looks for a

range

of values in the index key.

Poor when the predicate in the

clause stipulates one specific value for the

first

column of a two column hash index key, but doesn't specify a value for

other

columns of

the key.

If a hash index is used, and the number of unique index keys is more than 100 times smaller

than the row count, consider either increasing to a larger bucket count to avoid large row

chains, or use a

nonclustered index

instead.

When creating a hash index, consider:

A hash index can exist only on a memory-optimized table. It can't exist on a disk-based

table.

A hash index is nonunique by default, but can be declared as unique.

The following example creates a unique hash index:

In a memory-optimized table, when a row is affected by an

statement, the table creates

an updated version of the row. During the update transaction, other sessions might be able to



Tip

The predicate must include

all

columns in the hash index key. The hash index requires the

entire key to seek into the index.

`WHERE`

`WHERE`

`WHERE`

`UPDATE`

```sql
ALTER
TABLE
MyTable_memop
ADD
INDEX ix_hash_Column2
UNIQUE
HASH (Column2)
WITH (BUCKET_COUNT = 64);
```
