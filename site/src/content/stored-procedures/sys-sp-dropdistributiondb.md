---
name: "sys.sp_dropdistributiondb"
title: "sp_dropdistributiondb"
category: "general"
description: "Azure SQL Managed Instance Drops a distribution database. Drops the physical files used by the database if they aren't used by another database. This stored procedure is executed at the Distributor on any database. Transact-SQL syntax conventions The database to drop. , with no default. Specifies whether this node was previously part of an availability group for the distribution @former_ag_seconda"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_dropdistributiondb"
---

## Description

Azure SQL Managed Instance Drops a distribution database. Drops the physical files used by the database if they aren't used by another database. This stored procedure is executed at the Distributor on any database. Transact-SQL syntax conventions The database to drop. , with no default. Specifies whether this node was previously part of an availability group for the distribution @former_ag_secondary , with a default of is used in all types of replication.

## Syntax

```sql
sp_dropdistributiondb
```

## Permissions

This stored procedure must be executed before dropping the Distributor by executing . also removes a Queue Reader Agent job for the distribution database, if one exists. To disable distribution, the distribution database must be online. If a database snapshot exists for the distribution database, it must be dropped before disabling distribution. A database snapshot is a read-only offline copy of a database, and isn't related to a replication snapshot. For more information, see Database snapshots (SQL Server) . SQL Only members of the fixed server role can execute . Only members of the fixed server role can execute . Disable Publishing and Distribution sp_adddistributor (Transact-SQL) sp_changedistributor_property (Transact-SQL) sp_helpdistributor (Transact-SQL) Replication stored procedures (Transact-SQL) Related content

## Remarks

Applies to:

Azure SQL Managed Instance

Drops a distribution database. Drops the physical files used by the database if they aren't used

by another database. This stored procedure is executed at the Distributor on any database.

Transact-SQL syntax conventions

The database to drop.

, with no default.

Specifies whether this node was previously part of an availability group for the distribution

@former_ag_secondary

, with a default of

(success) or

is used in all types of replication.
