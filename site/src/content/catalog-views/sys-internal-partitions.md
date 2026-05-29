---
name: 'sys.internal_partitions'
title: 'sys.internal_partitions'
category: 'partitions'
description: '## A. View all of the internal rowsets for a table'
tags: ["catalog-view", "partitions"]
pubDate: 2026-05-29
---

## A. View all of the internal rowsets for a table

Requires membership in the

role. For more information, see

Metadata Visibility

Configuration

.

The Database Engine re-creates new columnstore internal indexes each time it creates or

rebuilds a columnstore index.

This example returns all of the internal columnstore rowsets for a table. You can also use the

column to join with other system views and functions and find more information

about the specific rowset.

SQL

Object catalog views (Transact-SQL)

System catalog views (Transact-SQL)

Querying the SQL Server system catalog FAQ

Last updated on 11/18/2025

Related content

```sql
public
```

```sql
hobt_id
```

```sql
SELECT
i.object_id,
i.index_id,
i.name,
p.hobt_id,
p.internal_object_type_id,
p.internal_object_type_desc
FROM
sys.internal_partitions
AS
p
INNER
JOIN
sys.indexes
AS
i
ON
i.object_id = p.object_id
WHERE
p.object_id = OBJECT_ID(
'<table name>'
);
```
