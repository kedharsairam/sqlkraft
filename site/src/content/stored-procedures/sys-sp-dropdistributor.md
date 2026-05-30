---
name: "sys.sp_dropdistributor"
title: "sp_dropdistributor"
category: "general"
description: "Uninstalls the Distributor. This stored procedure is executed at the Distributor on any database except the distribution database. Transact-SQL syntax conventions Indicates whether to check for dependent objects before dropping the Distributor. checks to make sure that all publishing and distribution objects were dropped, in addition to the Distributor. drops all the publishing and distribution ob"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropdistributor
  [ [ @no_checks = ] no_checks ]
  [ , [ @ignore_distributor = ] ignore_distributor ]
  [ ; ]
---

## Description

Uninstalls the Distributor. This stored procedure is executed at the Distributor on any database except the distribution database. Transact-SQL syntax conventions Indicates whether to check for dependent objects before dropping the Distributor. checks to make sure that all publishing and distribution objects were dropped, in addition to the Distributor. drops all the publishing and distribution objects before

## Syntax

```sql
sp_dropdistributor
[ [ @no_checks = ] no_checks ]
[ , [ @ignore_distributor = ] ignore_distributor ]
[ ; ]
```

## Permissions

This stored procedure must be executed before dropping the Distributor by executing . also removes a Queue Reader Agent job for the distribution database, if one exists. To disable distribution, the distribution database must be online. If a database snapshot exists for the distribution database, it must be dropped before disabling distribution. A database snapshot is a read-only offline copy of a database, and isn't related to a replication snapshot. For more information, see Database snapshots (SQL Server) . SQL Only members of the fixed server role can execute . Only members of the fixed server role can execute . Disable Publishing and Distribution sp_adddistributor (Transact-SQL) sp_changedistributor_property (Transact-SQL) sp_helpdistributor (Transact-SQL) Replication stored procedures (Transact-SQL) Related content View and Modify Distributor and Publisher Properties sp_adddistributor (Transact-SQL) sp_dropdistributor (Transact-SQL) sp_helpdistributor (Transact-SQL) Replication stored procedures (Transact-SQL) Last updated on 11/18/2025 Related content
