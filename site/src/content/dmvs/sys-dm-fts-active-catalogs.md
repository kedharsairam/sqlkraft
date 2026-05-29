---
name: "sys.dm_fts_active_catalogs"
title: "sys.dm_fts_active_catalogs"
category: "full-text"
description: "SQL database in Microsoft Fabric Returns information on the full-text catalogs that have some population activity in progress on ID of the database that contains the active full-text ID of the active full-text catalog. Address of memory buffers allocated for the population activity related to this full-text catalog. Name of the active full-text catalog. Indicates whether the population of the acti"
tags: ["full-text", "dmv"]
pubDate: 2026-05-29
syntax: |
  dm_fts_active_catalogs.database_id
  dm_fts_index_population.database_id
---

## Description

SQL database in Microsoft Fabric Returns information on the full-text catalogs that have some population activity in progress on ID of the database that contains the active full-text ID of the active full-text catalog. Address of memory buffers allocated for the population activity related to this full-text catalog. Name of the active full-text catalog. Indicates whether the population of the active full-

## Syntax

```sql
dm_fts_active_catalogs.database_id
dm_fts_index_population.database_id
```
