---
name: 'sys.sp_change_log_shipping_secondary_database'
title: 'sp_change_log_shipping_secondary_database'
category: 'general'
description: 'fixed server role can run this procedure. This example illustrates using database parameters for the database About log shipping (SQL Server) System stored procedures (Transact-SQL)'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_change_log_shipping_secondary_database'
---

## Description

fixed server role can run this procedure. This example illustrates using database parameters for the database About log shipping (SQL Server) System stored procedures (Transact-SQL)

## Syntax

```sql
sp_change_log_shipping_secondary_database
```

## Examples

### Example 1

```sql
sp_change_log_shipping_secondary_database
```

### Example 2

```sql
LogShipAdventureWorks
```

### Example 3

```sql
EXECUTE
master.dbo.sp_change_log_shipping_secondary_database
@secondary_database =
'LogShipAdventureWorks'
,
@restore_delay = 0,
@restore_all = 1,
@restore_mode = 0,
@disconnect_users = 0,
@threshold_alert = 14420,
@threshold_alert_enabled = 1,
@history_retention_period = 14420;
```
