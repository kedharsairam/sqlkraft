---
title: "Latch contention on page free space (PFS) pages"
topic: "io-fundamentals"
description: "The combination of a shallow B-Tree and random inserts across the index is prone to causing"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

The combination of a shallow B-Tree and random inserts across the index is prone to causing

page splits in the B-tree. In order to perform a page split, SQL Server must acquire shared (

)

latches at all levels, and then acquire exclusive (

) latches on pages in the B-tree that are

involved in the page splits. Also when concurrency is high and data is continually inserted and

deleted, B-tree root splits might occur. In this case, other inserts might have to wait for any

non-buffer latches acquired on the B-tree. This is manifested as a large number of waits on the

latch type observed in the

DMV.

The following script can be modified to determine the depth of the B-tree for the indexes on

the affected table.

SQL

PFS stands for Page Free Space, SQL Server allocates one PFS page for every 8088 pages

(starting with

=

) in each database file. Each byte in the PFS page records information

including how much free space is on the page, if it's allocated or not and whether the page

stores ghost records. The PFS page contains information about the pages available for

allocation when a new page is required by an insert or update operation. The PFS page must

be updated in several scenarios, including when any allocations or deallocations occur. Since

the use of an update (UP) latch is required to protect the PFS page, latch contention on PFS

```sql
SH
```

```sql
EX
```

```sql
ACCESS_METHODS_HOBT_VIRTUAL_ROOT
```

```sql
sys.dm_os_latch_stats
```

```sql
PageID
```

```sql
1
```

```sql
SELECT
o.name
AS
[
table
],
i.name
AS
[
index
],
indexProperty(object_id(o.name), i.name,
'indexDepth'
) +
indexProperty(object_id(o.name), i.name,
'isClustered'
)
AS
depth
,
--clustered
index depth reported doesn't count leaf level
i.[
rows
]
AS
[
rows
],
i.origFillFactor
AS
[fillFactor],
CASE
(indexProperty(object_id(o.name), i.name,
'isClustered'
))
WHEN
1
THEN
'clustered'
WHEN
0
THEN
'nonclustered'
ELSE
'statistic'
END
AS
type
FROM
sysIndexes
AS
i
INNER
JOIN
sysObjects
AS
o
ON
o.id = i.id
WHERE
o.type =
'u'
AND
indexProperty(object_id(o.name), i.name,
'isHypothetical'
) = 0
--filter
out hypothetical indexes
AND
indexProperty(object_id(o.name), i.name,
'isStatistics'
) = 0
--filter
out statistics
ORDER
BY
o.name;
```
