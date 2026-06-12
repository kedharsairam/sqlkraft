---
name: "sys.sp_change_feed_enable_db"
title: "sp_change_feed_enable_db"
category: "general"
description: "2022 (16.x) and later versions Mirrored databases in Microsoft SQL database in Microsoft Fabric SQL database in Microsoft Fabric Microsoft Fabric mirrored databases . Indicates the maximum number of transactions to process in each scan cycle."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  EXECUTE
      sys.sp_change_feed_enable_db
      [ [ @maxtrans ] ]
      [ , [ @pollinterval ]  ]
      [ , [ @destination_type ] ]
      GO
---

## Description

2022 (16.x) and later versions Mirrored databases in Microsoft SQL database in Microsoft Fabric SQL database in Microsoft Fabric Microsoft Fabric mirrored databases. Indicates the maximum number of transactions to process in each scan cycle. For Azure Synapse Link, the default value if not specified is For Fabric mirroring, this value is dynamically determined and automatically set.

## Syntax

```sql
EXECUTE sys.sp_change_feed_enable_db
[ [ @maxtrans ] ]
[ , [ @pollinterval ] ]
[ , [ @destination_type ] ]
GO
```
