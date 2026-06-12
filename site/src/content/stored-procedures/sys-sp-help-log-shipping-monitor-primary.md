---
name: "sys.sp_help_log_shipping_monitor_primary"
title: "sp_help_log_shipping_monitor_primary"
category: "general"
description: "Returns information regarding a primary database from the monitor tables."
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

Returns information regarding a primary database from the monitor tables.

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
