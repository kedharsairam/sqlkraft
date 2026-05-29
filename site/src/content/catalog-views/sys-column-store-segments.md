---
name: 'sys.column_store_segments'
title: 'sys.column_store_segments'
category: 'objects'
description: 'The columnstore segment encoding type is selected by the Database Engine by analyzing the'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

The columnstore segment encoding type is selected by the Database Engine by analyzing the

segment data with the goal of achieving the lowest storage cost. If data is mostly distinct, the

Database Engine uses value-based encoding. If data is mostly not distinct, the Database Engine

uses hash-based encoding. The choice between string-based and value-based encoding is

related to the type of data being stored, whether string data or binary data. All encodings take

advantage of bit-packing and run-length encoding when possible.

Columnstore segment elimination applies to numeric, date, and time data types, and the

data type with scale less than or equal to two. Beginning in SQL Server 2022

(16.x), segment elimination capabilities expand to string and binary data types, the

data type, and the

data type for scale greater than two.

Segment elimination does not apply to LOB data types such as

,

,

and

. For more information, see

What's new in columnstore indexes

.

The

permission on the view is required. The following columns return

unless the user also has the

permission:

,

,

,

,

, and

.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following query returns information about segments of a columnstore index.

SQL

Related content

Columnstore Indexes Guide

Performance tuning with ordered columnstore indexes

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

sys.columns (Transact-SQL)

sys.all_columns (Transact-SQL)

sys.computed_columns (Transact-SQL)

sys.column_store_dictionaries (Transact-SQL)

Last updated on 01/13/2026

```sql
VIEW DEFINITION
```

```sql
NULL
```

```sql
SELECT
```

```sql
has_nulls
```

```sql
base_id
```

```sql
magnitude
```

```sql
min_data_id
```

```sql
max_data_id
```

```sql
null_value
```

```sql
SELECT
i.name, p.object_id, p.index_id, i.type_desc,
COUNT
(*)
AS
number_of_segments
FROM
sys.column_store_segments
AS
s
INNER
JOIN
sys.partitions
AS
p
ON
s.hobt_id = p.hobt_id
INNER
JOIN
sys.indexes
AS
i
ON
p.object_id = i.object_id
WHERE
i.type = 5
OR
i.type = 6
GROUP
BY
i.name, p.object_id, p.index_id, i.type_desc;
```
