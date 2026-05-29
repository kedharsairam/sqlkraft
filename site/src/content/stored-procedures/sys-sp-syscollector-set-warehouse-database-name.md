---
name: 'sys.sp_syscollector_set_warehouse_database_name'
title: 'sp_syscollector_set_warehouse_database_name'
category: 'general'
description: '(with EXECUTE permission) fixed database role to The following example sets the name of the management data warehouse to System stored procedures (Transact-SQL)'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  USE
  msdb;
  GO
  EXECUTE
  sp_syscollector_set_warehouse_database_name N
  'RemoteMDW'
  ;
  GO
---

## Description

(with EXECUTE permission) fixed database role to The following example sets the name of the management data warehouse to System stored procedures (Transact-SQL)

## Syntax

```sql
USE
msdb;
GO
EXECUTE
sp_syscollector_set_warehouse_database_name N
'RemoteMDW'
;
GO
```

## Examples

### Example 1

```sql
RemoteMDW
```

### Example 2

```sql
USE
msdb;
GO
EXECUTE
sp_syscollector_set_warehouse_database_name N
'RemoteMDW'
;
GO
```
