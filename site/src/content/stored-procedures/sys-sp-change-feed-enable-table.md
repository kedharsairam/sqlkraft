---
name: "sys.sp_change_feed_enable_table"
title: "sp_change_feed_enable_table"
category: "general"
description: "2022 (16.x) and later versions Mirrored databases in Microsoft SQL database in Microsoft Fabric Stored procedure to enable the creation of a new table to an existing table group. This system stored procedure is used for: SQL database in Microsoft Fabric Microsoft Fabric mirrored databases The unique identifier of the table group. This system stored proced"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_change_feed_enable_table
              @table_group_id
              , @table_id
              , @source_schema
              , @source_name
              [ ; ]
---

## Description

2022 (16.x) and later versions Mirrored databases in Microsoft SQL database in Microsoft Fabric Stored procedure to enable the creation of a new table to an existing table group. This system stored procedure is used for: SQL database in Microsoft Fabric Microsoft Fabric mirrored databases The unique identifier of the table group. This system stored procedure is used internally and isn't recommended for direct

## Syntax

```sql
sys.sp_change_feed_enable_table
@table_group_id
, @table_id
, @source_schema
, @source_name
[ ; ]
```
