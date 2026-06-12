---
name: "sys.sp_help_log_shipping_monitor_secondary"
title: "sp_help_log_shipping_monitor_secondary"
category: "general"
description: "Returns information regarding a secondary database from the monitor tables."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_log_shipping_monitor_secondary
              [ @secondary_server = ]
              N
              'secondary_server'
              , [ @secondary_database = ]
              N
              'secondary_database'
              [ ; ]
---

## Description

Returns information regarding a secondary database from the monitor tables.

## Syntax

```sql
sp_help_log_shipping_monitor_secondary
[ @secondary_server = ]
N
'secondary_server'
, [ @secondary_database = ]
N
'secondary_database'
[ ; ]
```
