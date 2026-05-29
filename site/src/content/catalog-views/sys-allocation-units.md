---
name: 'sys.allocation_units'
title: 'sys.allocation_units'
category: 'objects'
description: '## Determine space used by object and type of an allocation unit'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Determine space used by object and type of an allocation unit


## Description
used_pages

Number of total pages actually in use.

data_pages

Number of used pages that have:

In-row data

LOB data

Row-overflow data

Note that the value returned excludes internal index pages and

allocation-management pages.

Requires membership in the

role. For more information, see

Metadata Visibility

Configuration

.

The following query returns all the user tables in a database and the amount of space used in

each, by allocation unit type.

SQL

７

Note

When you drop or rebuild large indexes, drop large tables, or truncate large tables or

partitions, the Database Engine defers the actual page deallocations, and their associated

locks, until after the transaction commits. Deferred drop operations do not release

allocated space immediately. Therefore, the values returned by sys.allocation_units

immediately after dropping or truncating a large object may not reflect the actual disk

space available.

When

is enabled, deferred drop is used regardless of

object size.

sys.partitions (Transact-SQL)

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Last updated on 11/18/2025

See Also

```sql
SELECT
t.object_id
AS
ObjectID,
OBJECT_NAME(t.object_id)
AS
ObjectName,
SUM
(u.total_pages) * 8
AS
Total_Reserved_kb,
SUM
(u.used_pages) * 8
AS
Used_Space_kb,
u.type_desc
AS
TypeDesc,
MAX
(p.rows)
AS
RowsCount
FROM
sys.allocation_units
AS
u
JOIN
sys.partitions
AS
p
ON
u.container_id = p.hobt_id
JOIN
sys.tables
AS
t
ON
p.object_id = t.object_id
GROUP
BY
t.object_id,
OBJECT_NAME(t.object_id),
u.type_desc
ORDER
BY
Used_Space_kb
DESC
,
ObjectName;
```
