---
name: "sys.sp_help_log_shipping_secondary_primary"
title: "sp_help_log_shipping_secondary_primary"
category: "general"
description: "This stored procedure retrieves the settings for a given primary database on the secondary The name of the primary instance of the SQL Server Database Engine in the log shipping The name of the database on the primary server."
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

This stored procedure retrieves the settings for a given primary database on the secondary The name of the primary instance of the SQL Server Database Engine in the log shipping The name of the database on the primary server.

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

Description Available starting with SQL Server 2025 (17.x) and later versions. must be run from the database on the secondary server. Only members of the fixed server role can run this procedure. About log shipping (SQL Server) System stored procedures (Transact-SQL)
