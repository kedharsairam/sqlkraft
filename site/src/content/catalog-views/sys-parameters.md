---
name: "sys.parameters"
title: "sys.parameters"
category: "compatibility"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each parameter of an object that accepts parameters. If the object is a scalar function, there's also a single row describing the return value. That row has a ID of the object to which this parameter belongs. Name of the parameter. Is unique within the If the object is a scalar function, the parameter name is an em"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT
  name
  ,
  TYPE_NAME(user_type_id)
  FROM
  sys.parameters
  WHERE
  object_id = OBJECT_ID(
  'dbo.to_upper'
  );
  GO
  SELECT
  dbo.to_upper(
  'abcdefgh'
  );
  -- Fails because of truncation
  GO
  EXECUTE
  sys.sp_refreshsqlmodule
  'dbo.to_upper'
  ;
  SELECT
  name
  ,
  TYPE_NAME(user_type_id)
  FROM
  sys.parameters
  WHERE
  object_id = OBJECT_ID(
  'dbo.to_upper'
  );
  GO
  SELECT
  dbo.to_upper(
  'abcdefgh'
  );
  GO
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each parameter of an object that accepts parameters. If the object is a scalar function, there's also a single row describing the return value. That row has a ID of the object to which this parameter belongs. Name of the parameter. Is unique within the If the object is a scalar function, the parameter name is an empty string in the row representing

## Syntax

```sql
SELECT
name
,
TYPE_NAME(user_type_id)
FROM
sys.parameters
WHERE
object_id = OBJECT_ID(
'dbo.to_upper'
);
GO
SELECT
dbo.to_upper(
'abcdefgh'
);
-- Fails because of truncation
GO
EXECUTE
sys.sp_refreshsqlmodule
'dbo.to_upper'
;
SELECT
name
,
TYPE_NAME(user_type_id)
FROM
sys.parameters
WHERE
object_id = OBJECT_ID(
'dbo.to_upper'
);
GO
SELECT
dbo.to_upper(
'abcdefgh'
);
GO
```
