---
name: 'sys.partitions'
title: 'sys.partitions'
category: 'partitions'
description: '## Determine space used by object and show related partition'
tags: ["catalog-view", "partitions"]
pubDate: 2026-05-29
---

## Determine space used by object and show related partition

## information


## Description
Note:

Full text indexes are compressed in any edition of SQL

Server.

Indicates the state of compression for each partition. Possible

values for rowstore tables are

,

, and

. Possible

values for columnstore tables are

and

.

: SQL Server 2022 (16.x) and later versions.

Indicates the state of XML compression for each partition:

0 = OFF

1 = ON

: SQL Server 2022 (16.x) and later versions.

Indicates the state of XML compression for each partition.

Possible values are

and

.

: SQL Server 2012 (11.x) and later versions.

: SQL Server 2014 (12.x) and later versions.

Requires membership in the

role. For more information, see

Metadata Visibility

Configuration

.

The following query returns all the object in a database, the amount of space used in each

object, and partition information related to each object.

SQL

1

2

Object Catalog Views (Transact-SQL)

System catalog views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

Last updated on 11/18/2025

Related content

```sql
data_compression_desc
```

```sql
NONE
```

```sql
ROW
```

```sql
PAGE
```

```sql
COLUMNSTORE
```

```sql
COLUMNSTORE_ARCHIVE
```

```sql
xml_compression
```

```sql
xml_compression_desc
```

```sql
OFF
```

```sql
ON
```

```sql
SELECT
object_name(object_id)
AS
ObjectName,
total_pages / 128.
AS
SpaceUsed_MB,
p.partition_id,
p.object_id,
p.index_id,
```

```sql
p.partition_number,
p.rows,
p.data_compression_desc
FROM
sys.partitions
AS
p
INNER
JOIN
sys.allocation_units
AS
au
ON
p.partition_id = au.container_id
ORDER
BY
SpaceUsed_MB
DESC
;
```
