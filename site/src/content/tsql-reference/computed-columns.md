---
name: "Computed columns"
title: "Computed columns"
category: "statements"
description: "columns that exceed the byte limit can be created if the existing"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

bytes.) Indexes on

columns that exceed the byte limit can be created if the existing

data in the columns don't exceed the limit at the time the index is created; however,

subsequent insert or update operations on the columns that cause the total size to be greater

than the limit fail. The index key of a clustered index can't contain

columns that have

existing data in the

allocation unit. If a clustered index is created on a

column and the existing data is in the

allocation unit, subsequent insert or

update operations on the column that would push the data off-row fail.

Nonclustered indexes can include non-key (included) columns in the leaf level of the index.

These columns are not considered by the Database Engine when calculating the index key size.

For more information, see

Create indexes with included columns

and the

index

architecture and design guide.

Indexes can be created on computed columns. In addition, computed columns can have the

property. This means that the Database Engine stores the computed values in the

table, and updates them when any other columns on which the computed column depends are

updated. The Database Engine uses these persisted values when it creates an index on the

column, and when the index is referenced in a query.

To index a computed column, the computed column must be deterministic and precise.

However, using the

property expands the type of indexable computed columns to

include:

Computed columns based on Transact-SQL and CLR functions and CLR user-defined type

methods that are marked deterministic by the user.

Computed columns based on expressions that are deterministic as defined by the

Database Engine but imprecise.

Persisted computed columns require the following

options to be set as shown in the

previous section

Required SET options for filtered indexes.

７

Note

When tables are partitioned, if the partitioning key columns are not already present in a

non-unique clustered index, they are added to the index by the Database Engine. The

combined size of the indexed columns (not counting included columns), plus any added

partitioning columns cannot exceed 1800 bytes in a non-unique clustered index.

### varchar(max)

### nvarchar(max)

### varbinary(max)

`ROW_OVERFLOW_DATA`

`IN_ROW_DATA`

`PERSISTED`

`PERSISTED`

`SET`
