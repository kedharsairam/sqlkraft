---
name: "sys.sp_cdc_enable_table"
title: "sys.sp_cdc_enable_table"
category: "general"
description: "Enables change data capture for the specified source table in the current database. When a table is enabled for change data capture, a record of each data manipulation language (DML) operation applied to the table is written to the transaction log."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_enable_table
  [ @source_schema = ]
  'source_schema'
  , [ @source_name = ]
  'source_name'
  [ , [ @capture_instance = ]
  'capture_instance'
  ]
  [ , [ @supports_net_changes = ] supports_net_changes ]
  , [ @role_name = ]
  'role_name'
  [ , [ @index_name = ]
  'index_name'
  ]
  [ , [ @captured_column_list = ]
  N
  'captured_column_list'
  ]
  [ , [ @filegroup_name = ]
  'filegroup_name'
  ]
  [ , [ @allow_partition_switch = ]
  'allow_partition_switch'
  ]
  [ ; ]
---

## Description

Enables change data capture for the specified source table in the current database. When a table is enabled for change data capture, a record of each data manipulation language (DML) operation applied to the table is written to the transaction log. The change data capture process retrieves this information from the log and writes it to change tables that are accessed Change data capture isn't available in every edition of SQL Server. For a list of features that are

## Syntax

```sql
sys.sp_cdc_enable_table
[ @source_schema = ]
'source_schema'
, [ @source_name = ]
'source_name'
[ , [ @capture_instance = ]
'capture_instance'
]
[ , [ @supports_net_changes = ] supports_net_changes ]
, [ @role_name = ]
'role_name'
[ , [ @index_name = ]
'index_name'
]
[ , [ @captured_column_list = ]
N
'captured_column_list'
]
[ , [ @filegroup_name = ]
'filegroup_name'
]
[ , [ @allow_partition_switch = ]
'allow_partition_switch'
]
[ ; ]
```
