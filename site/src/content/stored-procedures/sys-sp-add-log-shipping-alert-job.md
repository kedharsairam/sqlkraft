---
name: "sys.sp_add_log_shipping_alert_job"
title: "sp_add_log_shipping_alert_job"
category: "general"
description: "This stored procedure checks to see if an alert job has been created on this server. If an alert job doesn't exist, creates the alert job, and adds its job ID to table. The alert job is enabled by default, and runs on a schedule of once every two minutes. Transact-SQL syntax conventions The SQL Server Agent job ID of the log shipping alert job. must be run from the database on the monitor server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_add_log_shipping_alert_job"
---

## Description

This stored procedure checks to see if an alert job has been created on this server. If an alert job doesn't exist, creates the alert job, and adds its job ID to table. The alert job is enabled by default, and runs on a schedule of once every two minutes. Transact-SQL syntax conventions The SQL Server Agent job ID of the log shipping alert job. must be run from the database on the monitor server.

## Syntax

`sp_add_log_shipping_alert_job`

## Remarks

Applies to:

This stored procedure checks to see if an alert job has been created on this server. If an alert

job doesn't exist,

creates the alert job, and adds its job ID to

table. The alert job is enabled by default, and runs on a

schedule of once every two minutes.

Transact-SQL syntax conventions

The SQL Server Agent job ID of the log shipping alert job.

(success) or

must be run from the

database on the monitor server.

## Examples

### Example 1

`sp_add_log_shipping_alert_job`

### Example 2

```sql
USE master
;
GO
EXECUTE sp_add_log_shipping_alert_job;
```
