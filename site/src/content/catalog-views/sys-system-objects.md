---
name: "sys.system_objects"
title: "sys.system_objects"
category: "objects"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains one row for all schema-scoped system objects that are included with Microsoft SQL Server. All system objects are contained in the schemas named sys or INFORMATION_SCHEMA."
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  UNION
  SELECT
  'XML SCHEMA COLLECTION'
  AS
  entity_type,
  COALESCE
  (USER_NAME(xsc.principal_id), USER_NAME(s.principal_id))
  AS
  owner_name,
  xsc.name
  FROM
  sys.xml_schema_collections
  AS
  xsc
  INNER
  JOIN
  sys.schemas
  AS
  s
  ON
  s.schema_id = xsc.schema_id
  WHERE
  s.name =
  '<schema_name>'
  ;
  GO
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains one row for all schema-scoped system objects that are included with Microsoft SQL Server. All system objects are contained in the schemas named sys or INFORMATION_SCHEMA. Object identification number. Is unique within a database. ID of the individual owner if different from the schema owner. By default, schema-contained objects are owned by the schema

## Syntax

```sql
UNION
SELECT
'XML SCHEMA COLLECTION'
AS entity_type,
COALESCE (USER_NAME(xsc.principal_id), USER_NAME(s.principal_id))
AS owner_name,
xsc.name
FROM sys.xml_schema_collections
AS xsc
INNER
JOIN sys.schemas
AS s
ON s.schema_id = xsc.schema_id
WHERE s.name =
'<schema_name>'
;
GO
```
