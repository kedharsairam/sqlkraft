---
name: "sys.sp_dropdistpublisher"
title: "sp_dropdistpublisher"
category: "general"
description: "Drops a distribution Publisher. This stored procedure is executed at the Distributor on any checks that the Publisher has uninstalled the server as , replication verifies that the remote Publisher has uninstalled the local server as the Distributor. If the Publisher is local, replication verifies that there are no publication or Using a custom port for the SQL Serve"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropdistpublisher
              [ @publisher = ]
              N
              'publisher'
              [ , [ @no_checks = ] no_checks ]
              [ , [ @ignore_distributor = ] ignore_distributor ]
              [ ; ]
---

## Description

Drops a distribution Publisher. This stored procedure is executed at the Distributor on any checks that the Publisher has uninstalled the server as , replication verifies that the remote Publisher has uninstalled the local server as the Distributor. If the Publisher is local, replication verifies that there are no publication or Using a custom port for the SQL Server publisher was introduced in SQL Server 2019

## Syntax

```sql
sp_dropdistpublisher
[ @publisher = ]
N
'publisher'
[ , [ @no_checks = ] no_checks ]
[ , [ @ignore_distributor = ] ignore_distributor ]
[ ; ]
```

## Permissions

Only members of the fixed server role can execute. Disable Publishing and Distribution sp_adddistpublisher (Transact-SQL) sp_changedistpublisher (Transact-SQL) sp_helpdistpublisher (Transact-SQL) Replication stored procedures (Transact-SQL)
