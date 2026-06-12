---
name: "sys.service_queues"
title: "sys.service_queues"
category: "compatibility"
description: "Contains a row for each object in the database that is a service queue, with For a list of columns that this view inherits, see Maximum number of the concurrent readers Three-part name of the activation procedure."
tags: ["compatibility","catalog-view"]
pubDate: 2026-05-29
syntax: |
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
---

## Description

Contains a row for each object in the database that is a service queue, with For a list of columns that this view inherits, see Maximum number of the concurrent readers Three-part name of the activation procedure.

## Syntax

```sql
SELECT t.name
AS parent_table,
t.object_id
AS parent_table_id,
it.name
AS internal_table_name,
it.object_id
AS internal_table_id,
xi.name
AS primary_XML_index_name,
xi.index_id
AS primary_XML_index_id
FROM sys.internal_tables
AS it
INNER
JOIN sys.tables
AS t
ON it.parent_id = t.object_id
INNER
JOIN sys.xml_indexes
AS xi
ON it.parent_id = xi.object_id
AND it.parent_minor_id = xi.index_id
WHERE it.internal_type_desc =
'XML_INDEX_NODES'
;
GO
```

## Permissions

Article • 02/28/2023 Description For a list of columns that this view inherits, see sys.objects (Transact-SQL). Maximum number of the concurrent readers allowed in the queue. Three-part name of the activation procedure. ID of the EXECUTE AS database principal. NULL by default or if EXECUTE AS CALLER. ID of the specified principal if EXECUTE AS SELF EXECUTE AS <principal>. -2 = EXECUTE AS OWNER. 1 = Activation is enabled. 1 = Receive is enabled. 1 = Enqueue is enabled. 1 = Messages are retained until dialog end. : SQL Server 2012 (11.x) and later. 1 = Poison message handling is enabled. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. ﾉ Expand table
