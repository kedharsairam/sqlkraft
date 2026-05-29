---
name: "sys.sp_help_log_shipping_monitor_primary"
title: "sp_help_log_shipping_monitor_primary"
category: "general"
description: "Returns information regarding a primary database from the monitor tables. Transact-SQL syntax conventions The name of the primary instance of the SQL Server Database Engine in the log shipping The name of the database on the primary server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_log_shipping_monitor_primary
  [ @primary_server = ]
  N
  'primary_server'
  , [ @primary_database = ]
  N
  'primary_database'
  [ ; ]
---

## Description

Returns information regarding a primary database from the monitor tables. Transact-SQL syntax conventions The name of the primary instance of the SQL Server Database Engine in the log shipping The name of the database on the primary server.

## Syntax

```sql
sp_help_log_shipping_monitor_primary
[ @primary_server = ]
N
'primary_server'
, [ @primary_database = ]
N
'primary_database'
[ ; ]
```
