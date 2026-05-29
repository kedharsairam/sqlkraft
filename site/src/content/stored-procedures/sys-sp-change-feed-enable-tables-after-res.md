---
name: 'sys.sp_change_feed_enable_tables_after_res'
title: 'sys.sp_change_feed_enable_tables_after_res'
category: 'general'
description: 'SQL Server 2025 (17.x)'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2025 (17.x)

Azure SQL Database

Azure SQL Managed

Instance

Mirrored databases in Microsoft Fabric

SQL database in Microsoft Fabric

Enables tables after reseed within the current database context.

This system stored procedure is used for

Microsoft Fabric mirrored databases

and

SQL

database in Microsoft Fabric

.

Transact-SQL syntax conventions


## syntaxsql
None.

(success) or

(failure).

A user with

database permissions,

database role membership, or

server role membership can execute this procedure.

Ｕ

Caution

This system stored procedure is used internally and isn't recommended for direct

administrative use. Use Synapse Studio or the Fabric portal instead. Using this procedure

could introduce inconsistency.

sys.sp_help_change_feed (Transact-SQL)

sys.sp_help_change_feed_table (Transact-SQL)

sys.sp_help_change_feed_table_groups (Transact-SQL)

sys.sp_help_change_feed_settings (Transact-SQL)

sys.sp_change_feed_configure_parameters (Transact-SQL)

sys.dm_change_feed_log_scan_sessions (Transact-SQL)

sys.dm_change_feed_errors (Transact-SQL)

What is Mirroring in Fabric?

Monitor Fabric mirrored database replication

Explore data in your mirrored database using Microsoft Fabric

Last updated on 12/17/2025

Related content

```sql
0
```

```sql
1
```

```sql
CONTROL
```

```sql
sys.sp_change_feed_enable_tables_after_reseed
[ ; ]
```
