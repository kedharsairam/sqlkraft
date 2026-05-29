---
name: 'sys.sp_syscollector_set_warehouse_instance_name'
title: 'sp_syscollector_set_warehouse_instance_name'
category: 'general'
description: '(with EXECUTE permission) fixed database role to The following example illustrates how to configure the data collector to use a management data warehouse instance on a remote server. In this example, the remote server is named and the database is installed on the default instance. Data collector stored procedures (Transact-SQL) syscollector_config_store (Transact-SQL)'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  USE
  msdb;
  GO
  EXECUTE
  sp_syscollector_set_warehouse_instance_name N
  'RemoteSERVER'
  ;
  -- the
  default instance is assumed on the remote server
  GO
---

## Description

(with EXECUTE permission) fixed database role to The following example illustrates how to configure the data collector to use a management data warehouse instance on a remote server. In this example, the remote server is named and the database is installed on the default instance. Data collector stored procedures (Transact-SQL) syscollector_config_store (Transact-SQL)

## Syntax

```sql
USE
msdb;
GO
EXECUTE
sp_syscollector_set_warehouse_instance_name N
'RemoteSERVER'
;
-- the
default instance is assumed on the remote server
GO
```

## Examples

### Example 1

```sql
RemoteSERVER
```

### Example 2

```sql
USE
msdb;
GO
EXECUTE
sp_syscollector_set_warehouse_instance_name N
'RemoteSERVER'
;
-- the
default instance is assumed on the remote server
GO
```
