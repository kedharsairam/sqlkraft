---
name: "sys.sp_delete_log_shipping_alert_job"
title: "sp_delete_log_shipping_alert_job"
category: "general"
description: "Removes an alert job from the log shipping monitor server if the job exists and there are no more primary or secondary databases to be monitored. Transact-SQL syntax conventions fixed server role can run this procedure."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_delete_log_shipping_alert_job"
---

## Description

Removes an alert job from the log shipping monitor server if the job exists and there are no more primary or secondary databases to be monitored. Transact-SQL syntax conventions fixed server role can run this procedure.

## Syntax

`sp_delete_log_shipping_alert_job`

## Permissions

SQL) 06/23/2025 Applies to: SQL Server Removes an alert job from the log shipping monitor server if the job exists and there are no more primary or secondary databases to be monitored. Transact-SQL syntax conventions syntaxsql None. (success) or (failure). None. must be run from the database on the monitor server. Only members of the fixed server role can run this procedure.

## Examples

### Example 1

`sp_delete_log_shipping_alert_job`

### Example 2

```sql
USE master
;
GO
EXECUTE sp_delete_log_shipping_alert_job;
GO
```
