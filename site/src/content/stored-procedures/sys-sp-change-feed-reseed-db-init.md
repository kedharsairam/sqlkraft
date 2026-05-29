---
name: 'sys.sp_change_feed_reseed_db_init'
title: 'sys.sp_change_feed_reseed_db_init'
category: 'general'
description: 'SQL Server 2025 (17.x)'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## A. Initiate manual reseed event

(success) or non-zero (failure).

A reseed stops the current mirrored database and reinitializes the mirroring. This involves

generating a new initial snapshot of the tables configured for mirroring and then incremental

changes are replicated. During reseed, the old mirrored database item in Microsoft Fabric is still

available but doesn't receive incremental changes.

A user with

database permissions,

database role membership, or

server role membership can execute this procedure.

As a best practice, test manual reseed for a specific database to understand the impact before

turning on the automatic reseed functionality.

SQL

sys.sp_help_change_feed (Transact-SQL)

sys.sp_help_change_feed_table (Transact-SQL)

sys.sp_help_change_feed_table_groups (Transact-SQL)

sys.sp_help_change_feed_settings (Transact-SQL)

sys.sp_change_feed_configure_parameters (Transact-SQL)

sys.dm_change_feed_log_scan_sessions (Transact-SQL)

sys.dm_change_feed_errors (Transact-SQL)

What is Mirroring in Fabric?

Related content

Monitor Fabric mirrored database replication

Explore data in your mirrored database using Microsoft Fabric

Last updated on 12/17/2025

```sql
0
```

```sql
CONTROL
```

```sql
USE
<Mirrored
database
name
>
GO
EXECUTE
sp_change_feed_reseed_db_init @is_init_needed = 1;
```
