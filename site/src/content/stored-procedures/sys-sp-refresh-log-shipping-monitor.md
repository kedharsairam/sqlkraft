---
name: "sys.sp_refresh_log_shipping_monitor"
title: "sp_refresh_log_shipping_monitor"
category: "general"
description: "This stored procedure refreshes the remote monitor tables with the latest information from a given primary or secondary server for the specified log shipping agent. The procedure is invoked on the primary or secondary server. Transact-SQL syntax conventions The primary ID for backup or the secondary ID for copy or restore. , with no default, and can't be"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_refresh_log_shipping_monitor
  [ @agent_id = ]
  'agent_id'
  , [ @agent_type = ] agent_type
  [ , [ @database = ]
  N
  'database'
  ]
  , [ @mode = ] mode
  [ ; ]
---

## Description

This stored procedure refreshes the remote monitor tables with the latest information from a given primary or secondary server for the specified log shipping agent. The procedure is invoked on the primary or secondary server. Transact-SQL syntax conventions The primary ID for backup or the secondary ID for copy or restore. , with no default, and can't be

## Syntax

```sql
sp_refresh_log_shipping_monitor
[ @agent_id = ]
'agent_id'
, [ @agent_type = ] agent_type
[ , [ @database = ]
N
'database'
]
, [ @mode = ] mode
[ ; ]
```

## Permissions

must be run from the database on the primary or secondary server. Only members of the fixed server role can run this procedure. About log shipping (SQL Server) System stored procedures (Transact-SQL) Related content
