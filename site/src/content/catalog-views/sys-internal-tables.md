---
name: 'sys.internal_tables'
title: 'sys.internal_tables'
category: 'objects'
description: 'System catalog views (Transact-SQL)'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

SQL

SQL

System catalog views (Transact-SQL)

Object catalog views (Transact-SQL)

Related content

```sql
SELECT
t.name
AS
parent_table,
t.object_id
AS
parent_table_id,
it.name
AS
internal_table_name,
it.object_id
AS
internal_table_id,
xi.name
AS
primary_XML_index_name,
xi.index_id
AS
primary_XML_index_id
FROM
sys.internal_tables
AS
it
INNER
JOIN
sys.tables
AS
t
ON
it.parent_id = t.object_id
INNER
JOIN
sys.xml_indexes
AS
xi
ON
it.parent_id = xi.object_id
AND
it.parent_minor_id = xi.index_id
WHERE
it.internal_type_desc =
'XML_INDEX_NODES'
;
GO
```

```sql
SELECT
q.name
AS
queue_name,
q.object_id
AS
queue_id,
it.name
AS
internal_table_name,
it.object_id
AS
internal_table_id
FROM
sys.internal_tables
AS
it
INNER
JOIN
sys.service_queues
AS
q
ON
it.parent_id = q.object_id
WHERE
it.internal_type_desc =
'QUEUE_MESSAGES'
;
GO
```

```sql
SELECT
*
FROM
tempdb.sys.internal_tables
WHERE
internal_type_desc =
'SERVICE_BROKER_MAP'
;
GO
```
