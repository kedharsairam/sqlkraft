---
name: "sys.sp_change_feed_create_table_group"
title: "sp_change_feed_create_table_group"
category: "general"
description: "SQL Server 2022 (16.x) and later versions Mirrored databases in Microsoft SQL database in Microsoft Fabric Creates a source to maintain metadata specific to each table group. A table group represents the container for all the individual tables that will be replicated. This system stored procedure is used for: SQL database in Microsoft Fabric Microsoft Fabric mirrored databases Transact-SQL syntax"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  EXECUTE
  sys.sp_change_feed_create_table_group
  @table_group_id
  , @table_group_name
  , @workspace_id
  , @destination_location
  , @destination_credential
  [ ; ]
---

## Description

SQL Server 2022 (16.x) and later versions Mirrored databases in Microsoft SQL database in Microsoft Fabric Creates a source to maintain metadata specific to each table group. A table group represents the container for all the individual tables that will be replicated. This system stored procedure is used for: SQL database in Microsoft Fabric Microsoft Fabric mirrored databases Transact-SQL syntax conventions

## Syntax

```sql
EXECUTE sys.sp_change_feed_create_table_group
@table_group_id
, @table_group_name
, @workspace_id
, @destination_location
, @destination_credential
[ ; ]
```
