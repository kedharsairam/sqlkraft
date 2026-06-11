---
name: "sys.foreign_key_columns"
title: "sys.foreign_key_columns"
category: "objects"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each column, or set of columns, that comprise a foreign key."
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT
  fk.name
  AS
  ForeignKeyName
  , t_parent.name
  AS
  ParentTableName
  , c_parent.name
  AS
  ParentColumnName
  , t_child.name
  AS
  ReferencedTableName
  , c_child.name
  AS
  ReferencedColumnName
  FROM
  sys.foreign_keys fk
  INNER
  JOIN
  sys.foreign_key_columns fkc
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each column, or set of columns, that comprise a foreign key. ID of the FOREIGN KEY constraint. ID of the column, or set of columns, that comprise the FOREIGN KEY where n is the number of columns). ID of the parent of the constraint, which is the referencing object. ID of the parent column, which is the referencing column.

## Syntax

```sql
SELECT fk.name
AS
ForeignKeyName
, t_parent.name
AS
ParentTableName
, c_parent.name
AS
ParentColumnName
, t_child.name
AS
ReferencedTableName
, c_child.name
AS
ReferencedColumnName
FROM sys.foreign_keys fk
INNER
JOIN sys.foreign_key_columns fkc
```

## Examples

### Example 1

```sql
SELECT fk.name
AS
ForeignKeyName
, t_parent.name
AS
ParentTableName
, c_parent.name
AS
ParentColumnName
, t_child.name
AS
ReferencedTableName
, c_child.name
AS
ReferencedColumnName
FROM sys.foreign_keys fk
INNER
JOIN sys.foreign_key_columns fkc
```
