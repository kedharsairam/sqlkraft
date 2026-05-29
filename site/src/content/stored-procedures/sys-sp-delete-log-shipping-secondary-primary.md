---
name: 'sys.sp_delete_log_shipping_secondary_primary'
title: 'sp_delete_log_shipping_secondary_primary'
category: 'general'
description: 'removes the information about the specified primary server from the secondary server, and removes the copy job and restore job from the Transact-SQL syntax conventions The name of the primary instance of the SQL Server Database Engine in the log shipping The name of the database on the primary server.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_delete_log_shipping_secondary_primary'
---

## Description

removes the information about the specified primary server from the secondary server, and removes the copy job and restore job from the Transact-SQL syntax conventions The name of the primary instance of the SQL Server Database Engine in the log shipping The name of the database on the primary server.

## Syntax

```sql
sp_delete_log_shipping_secondary_primary
```

## Permissions

None. must be run from the database on the secondary server. This stored procedure does the following: 1. Deletes the copy and restore jobs for the secondary ID. 2. Deletes the entry in . 3. Calls on the monitor server. Only members of the fixed server role can run this procedure. About log shipping (SQL Server) System stored procedures (Transact-SQL) Related content
