---
name: "sys.sp_cdc_help_change_data_capture"
title: "sys.sp_cdc_help_change_data_capture"
category: "general"
description: "Returns the change data capture configuration for each table enabled for change data capture in the current database. Up to two rows can be returned for each source table, one row for each capture instance. Change data capture isn't available in every edition of SQL Server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_help_change_data_capture
  [ [ @source_schema = ]
  'source_schema'
  ]
  [ , [ @source_name = ]
  'source_name'
  ]
  [ ; ]
---

## Description

Returns the change data capture configuration for each table enabled for change data capture in the current database. Up to two rows can be returned for each source table, one row for each capture instance. Change data capture isn't available in every edition of SQL Server. For a list of features that are supported by the editions of SQL Server, see The name of the schema in which the source table belongs.

## Syntax

```sql
sys.sp_cdc_help_change_data_capture
[ [ @source_schema = ]
'source_schema'
]
[ , [ @source_name = ]
'source_name'
]
[ ; ]
```
