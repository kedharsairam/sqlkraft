---
name: "sys.sp_cleanup_log_shipping_history"
title: "sp_cleanup_log_shipping_history"
category: "general"
description: "This stored procedure cleans up history locally, and on the monitor server, based on retention Transact-SQL syntax conventions The primary ID for backup or the secondary ID for copy or restore. , with no default, and can't be , with no default, and must be one of these"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_cleanup_log_shipping_history
  [ @agent_id = ]
  'agent_id'
  , [ @agent_type = ] agent_type
  [ ; ]
---

## Description

This stored procedure cleans up history locally, and on the monitor server, based on retention Transact-SQL syntax conventions The primary ID for backup or the secondary ID for copy or restore. , with no default, and can't be , with no default, and must be one of these

## Syntax

```sql
sp_cleanup_log_shipping_history
[ @agent_id = ]
'agent_id'
, [ @agent_type = ] agent_type
[ ; ]
```
