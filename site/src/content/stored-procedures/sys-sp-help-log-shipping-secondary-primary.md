---
name: 'sys.sp_help_log_shipping_secondary_primary'
title: 'sp_help_log_shipping_secondary_primary'
category: 'general'
description: 'This stored procedure retrieves the settings for a given primary database on the secondary Transact-SQL syntax conventions The name of the primary instance of the SQL Server Database Engine in the log shipping The name of the database on the primary server. The result set contains the following columns from'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_log_shipping_secondary_primary
  [ @primary_server = ]
  N
  'primary_server'
  , [ @primary_database = ]
  N
  'primary_database'
  [ ; ]
---

## Description

This stored procedure retrieves the settings for a given primary database on the secondary Transact-SQL syntax conventions The name of the primary instance of the SQL Server Database Engine in the log shipping The name of the database on the primary server. The result set contains the following columns from

## Syntax

```sql
sp_help_log_shipping_secondary_primary
[ @primary_server = ]
N
'primary_server'
, [ @primary_database = ]
N
'primary_database'
[ ; ]
```

## Permissions

Description Available starting with SQL Server 2025 (17.x) and later versions. must be run from the database on the secondary server. Only members of the fixed server role can run this procedure. About log shipping (SQL Server) System stored procedures (Transact-SQL) Last updated on 09/16/2025 Related content sp_help_log_shipping_primary_secondary sp_help_log_shipping_secondary_database sp_help_log_shipping_secondary_primary sp_refresh_log_shipping_monitor About log shipping (SQL Server) System stored procedures (Transact-SQL) Related content Description Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. and use this column to control the display of monitor settings in SQL Server Management Studio. 0 = When invoking either of these two stored procedures, the user did not specify an explicit value for the parameter. 1 = An explicit value was specified by the user. Indicates whether the log shipping configuration overrides the server-level backup compression behavior. 0 = Disabled. Log backups are never compressed, regardless of the server-configured backup compression settings. 1 = Enabled. Log backups are always compressed, regardless of the server-configured backup compression settings. 2 = Uses the server configuration for the View or Configure the backup compression default Server Configuration Option server-configuration option. This is the default value. Backup compression is supported only in the Enterprise edition of SQL Server. Additional connection options for the connection made between the log shipping executable and the primary replica instance. Available starting with SQL Server 2025 (17.x) Preview RC 0 and later. Additional connection options for the connection made between the primary replica instance and the remote monitor. Available starting with SQL Server 2025 (17.x) Preview RC 0 and later.
