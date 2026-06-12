---
name: "sys.types"
title: "sys.types"
category: "compatibility"
description: "Contains a row for each system and user-defined type."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  INNER
  JOIN
  sys.types t
  ON
  c.user_type_id = t.user_type_id
  WHERE
  object_id = object_id(
  'dbo.sample'
  );
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each system and user-defined type.

## Syntax

```sql
INNER
JOIN sys.types t
ON c.user_type_id = t.user_type_id
WHERE object_id = object_id(
'dbo.sample'
);
```

## Permissions
