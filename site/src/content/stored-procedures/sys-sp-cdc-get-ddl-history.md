---
name: 'sys.sp_cdc_get_ddl_history'
title: 'sys.sp_cdc_get_ddl_history'
category: 'general'
description: 'Returns the data definition language (DDL) change history associated with the specified capture instance since change data capture was enabled for that capture instance. Change data capture isn''t available in every edition of SQL Server. For a list of features that are supported by the editions of SQL Server, see Editions and supported features of SQL Server 2022 Transact-SQL syntax conventions Th'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_get_ddl_history [ @capture_instance = ]
  'capture_instance'
  [ ; ]
---

## Description

Returns the data definition language (DDL) change history associated with the specified capture instance since change data capture was enabled for that capture instance. Change data capture isn't available in every edition of SQL Server. For a list of features that are supported by the editions of SQL Server, see Editions and supported features of SQL Server 2022 Transact-SQL syntax conventions The name of the capture instance associated with a source table.

## Syntax

```sql
sys.sp_cdc_get_ddl_history [ @capture_instance = ]
'capture_instance'
[ ; ]
```
