---
title: "Clustered index design guidelines"
topic: "index-architecture"
description: "If a disk-based rowstore index is created with key columns that match those in the"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

If a disk-based rowstore index is created with key columns that match those in the

clause in the query, the

operator in the query plan is eliminated, making query plan more

efficient.

SQL

After the query is executed again, the following execution plan shows that the

operator is

no longer present and the newly created nonclustered index is used.

The Database Engine can scan an index in either direction. An index defined as

can still be used for a query in which the sort directions of the columns in

the

clause are reversed. For example, a query with the

clause

can use the same index.

Sort order can be specified only for the key columns in index. The

sys.index_columns

catalog

view reports whether an index column is stored in ascending or descending order.

The clustered index stores all rows and all columns of a table. Rows are sorted in the order of

index key values. There can only be one clustered index per table.

The term

can refer either to a clustered index or to a heap. A heap is an

unsorted

data structure on disk that contains all rows and all columns of a table.

### int

### bigint

### uniqueidentifier

### int

### bigint

### ever-increasing

With a few exceptions, every table should have a clustered index. The desirable properties of

the clustered index are:

## Description

The clustered index key is a part of any nonclustered index on the same base table. A

narrow key, or a key where the total length of key columns is small, reduces the storage,

I/O, and memory overhead of all indexes on a table.

To calculate the key length, add up the storage sizes for the data types used by key

columns. For more information, see

Data type categories

.

If the clustered index isn't unique, a 4-byte internal uniqueifier column is automatically

added to the index key to ensure uniqueness. Adding an existing unique column to the

clustered index key avoids the storage, I/O, and memory overhead of the uniqueifier

column in all indexes on a table. Additionally, the query optimizer can generate more

efficient query plans when an index is unique.

In an ever-increasing index, data is always added on the last page of the index. This

avoids page splits in the middle of the index, which reduce

page density

and decrease

performance.

The clustered index key is a part of any nonclustered index. When a key column of a

clustered index is modified, a change must also be made in all nonclustered indexes,

which adds a CPU, logging, I/O, and memory overhead. The overhead is avoided if the

key columns of the clustered index are immutable.

If a row has nullable columns, it must include an internal structure called a

NULL block

,

which adds 3-4 bytes of storage per row in an index. Making all columns of the

clustered index not nullable avoids this overhead.

Columns using variable width data types such as

or

use an additional

2 bytes per value compared to fixed width data types. Using fixed width data types such

as

avoids this overhead in all indexes on the table.

Satisfying as many of these properties as possible when designing a clustered index makes not

only the clustered index, but also all nonclustered indexes on the same table more efficient.

Performance is improved by avoiding storage, I/O, and memory overheads.

For example, a clustered index key with a single

or

not nullable column has all of

these properties if it's populated by an

clause or a default constraint using a

sequence

and isn't updated after a row is inserted.

Conversely, a clustered index key with a single

column is wider because it uses

16 bytes of storage instead of 4 bytes for

and 8 bytes for

, and doesn't satisfy the

property unless the values are generated sequentially.

ﾉ

Expand table

### nvarchar(max)

```sql
ORDER BY
```

```sql
RejectedQty
DESC, ProductID ASC
```

```sql
ORDER BY
```

```sql
ORDER BY
```

```sql
ORDER BY
RejectedQty ASC, ProductID DESC
```

```sql
CREATE
NONCLUSTERED
INDEX
IX_PurchaseOrderDetail_RejectedQty
ON
Purchasing.PurchaseOrderDetail
(RejectedQty
DESC
, ProductID
ASC
, DueDate, OrderQty);
```

```sql
IDENTITY
```
