---
name: "sys.sp_cycle_errorlog"
title: "sp_cycle_errorlog"
category: "general"
description: "Closes the current error log file and cycles the error log extension numbers just like a server restart. The new error log contains version and copyright information and a line indicating that Every time SQL Server is started, the current error log is renamed to you to cycle the error log files without stopping and starting the server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_cycle_errorlog
  [ ; ]
---

## Description

Closes the current error log file and cycles the error log extension numbers just like a server restart. The new error log contains version and copyright information and a line indicating that Every time SQL Server is started, the current error log is renamed to you to cycle the error log files without stopping and starting the server.

## Syntax

```sql
sp_cycle_errorlog
[ ; ]
```

## Permissions

06/23/2025 The new error log contains version and copyright information and a line indicating that the new log was created. syntaxsql None. (success) or (failure). None. Every time SQL Server is started, the current error log is renamed to ; becomes , becomes , and so on. enables you to cycle the error log files without stopping and starting the server.

## Examples

### Example 1

`sp_cycle_errorlog`

### Example 2

```sql
EXECUTE sp_cycle_errorlog;
GO
```
