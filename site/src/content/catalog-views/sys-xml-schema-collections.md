---
name: "sys.xml_schema_collections"
title: "sys.xml_schema_collections"
category: "xml"
description: "Returns a row per XML schema collection. An XML schema collection is a named set of XSD definitions. The XML schema collection itself is contained in a relational schema, and it is identified by a schema-scoped Transact-SQL name. The following tuples are unique: xml_collection_id, and schema_id and name."
tags: ["xml", "catalog-view"]
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

Returns a row per XML schema collection. An XML schema collection is a named set of XSD definitions. The XML schema collection itself is contained in a relational schema, and it is identified by a schema-scoped Transact-SQL name. The following tuples are unique: xml_collection_id, and schema_id and name.

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

## Permissions
