---
name: "sys.sp_cleanup_log_shipping_history"
title: "sp_cleanup_log_shipping_history"
category: "general"
description: "This stored procedure cleans up history locally, and on the monitor server, based on retention The primary ID for backup or the secondary ID for copy or restore."
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

This stored procedure cleans up history locally, and on the monitor server, based on retention The primary ID for backup or the secondary ID for copy or restore.

## Syntax

```sql
sp_cleanup_log_shipping_history
[ @agent_id = ]
'agent_id'
, [ @agent_type = ] agent_type
[ ; ]
```
