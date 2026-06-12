---
name: "sys.securable_classes"
title: "sys.securable_classes"
category: "compatibility"
description: "Returns a list of securable classes Numerical designation of the class. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see The following example returns the securable classes supported by this instance of SQL Ser"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT
  *
  FROM
  sys.securable_classes
  ORDER
  BY
  class
  ;
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns a list of securable classes Numerical designation of the class. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see The following example returns the securable classes supported by this instance of SQL Server.

## Syntax

```sql
SELECT
*
FROM sys.securable_classes
ORDER
BY class
;
```

## Examples

### Example 1

```sql
SELECT
*
FROM sys.securable_classes
ORDER
BY class
;
```
