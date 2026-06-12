---
name: "sys.sp_server_diagnostics"
title: "sp_server_diagnostics"
category: "general"
description: "Captures diagnostic data and health information about SQL Server to detect potential failures. The procedure runs in repeat mode and sends results periodically. It can be invoked from either a regular connection, or a Indicates the time interval at which the stored procedure runs repeatedly to send health . The valid parameter values are . The stored procedure has t"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_server_diagnostics [ @repeat_interval = ]
  'repeat_interval'
  [ ; ]
---

## Description

Captures diagnostic data and health information about SQL Server to detect potential failures. The procedure runs in repeat mode and sends results periodically. It can be invoked from either a regular connection, or a Indicates the time interval at which the stored procedure runs repeatedly to send health. The valid parameter values are. The stored procedure has to run at least 5 seconds to return

## Syntax

```sql
sp_server_diagnostics [ @repeat_interval = ]
'repeat_interval'
[ ; ]
```
