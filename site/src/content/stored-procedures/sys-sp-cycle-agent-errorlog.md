---
name: "sys.sp_cycle_agent_errorlog"
title: "sp_cycle_agent_errorlog"
category: "general"
description: "Closes the current SQL Server Agent error log file and cycles the SQL Server Agent error log extension numbers just like a server restart. The new SQL Server Agent error log contains a line indicating that the new log was created."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_cycle_agent_errorlog"
---

## Description

Closes the current SQL Server Agent error log file and cycles the SQL Server Agent error log extension numbers just like a server restart. The new SQL Server Agent error log contains a line indicating that the new log was created.

## Syntax

`sp_cycle_agent_errorlog`

## Remarks

Closes the current SQL Server Agent error log file and cycles the SQL Server Agent error log

extension numbers just like a server restart. The new SQL Server Agent error log contains a line

indicating that the new log was created.

(success) or

Every time SQL Server Agent is started, the current SQL Server Agent error log is renamed to

, and so on.

enables you to cycle the error log files without stopping and starting

the server.

This stored procedure must be run from the

## Examples

### Example 1

`sp_cycle_agent_errorlog`

### Example 2

```sql
USE msdb;
GO
EXECUTE dbo.sp_cycle_agent_errorlog;
GO
```
