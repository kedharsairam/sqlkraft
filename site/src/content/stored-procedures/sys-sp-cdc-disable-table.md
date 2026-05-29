---
name: 'sys.sp_cdc_disable_table'
title: 'sys.sp_cdc_disable_table'
category: 'general'
description: 'Disables change data capture for the specified source table and capture instance in the current database. Change data capture isn''t available in every edition of SQL Server. For a list of features that are supported by the editions of SQL Server, see Editions and supported features Transact-SQL syntax conventions The name of the schema in which the source table is contained. must exist in the curr'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_disable_table
  [ @source_schema = ]
  'source_schema'
  , [ @source_name = ]
  'source_name'
  [ , [ @capture_instance = ] {
  'capture_instance'
  |
  'all'
  } ]
  [ ; ]
---

## Description

Disables change data capture for the specified source table and capture instance in the current database. Change data capture isn't available in every edition of SQL Server. For a list of features that are supported by the editions of SQL Server, see Editions and supported features Transact-SQL syntax conventions The name of the schema in which the source table is contained. must exist in the current database.

## Syntax

```sql
sys.sp_cdc_disable_table
[ @source_schema = ]
'source_schema'
, [ @source_name = ]
'source_name'
[ , [ @capture_instance = ] {
'capture_instance'
|
'all'
} ]
[ ; ]
```
