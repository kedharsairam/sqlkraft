---
name: 'sys.sp_help_change_feed_settings'
title: 'sys.sp_help_change_feed_settings'
category: 'general'
description: 'SQL Server 2022 (16.x) and later versions'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## Description
= Enabled

The autoreseed feature is disabled by default in SQL Server

2025. The autoreseed feature is enabled and can't be managed

or disabled in Azure SQL Database and Azure SQL Managed

Instance. For more information, see

Configure automatic

reseed for Fabric mirrored databases from SQL Server

.

If

is enabled, the transactions log usage

percentage at which to trigger automatic reseed. The default is

. For SQL Server 2025 (Preview), this must be configured

when

is enabled.

Whether or not the dynamic maximum transactions setting is

enabled. The dynamic maximum transactions feature is

enabled by default in SQL Server 2025 (Preview). The dynamic

maximum transactions feature is enabled and can't be

managed or disabled in Azure SQL Database and Azure SQL

Managed Instance. Fabric mirroring always follows a maximum

number of transactions to process in each scan cycle as

defined by the

setting. When

=

,

Fabric mirroring dynamically adjusts the number of

transactions to process per scan between configured values for

and

. For more

information,

Mirrored databases from SQL Server performance

.

The lower bound for dynamic maxtrans setting for Fabric

Mirroring. By default, the lower bound value is

but can be

modified by

sys.sp_change_feed_configure_parameters

.

A user with

database permissions,

database role membership, or

server role membership can execute this procedure.

sys.sp_change_feed_configure_parameters (Transact-SQL)

sys.sp_help_change_feed (Transact-SQL)

sys.sp_help_change_feed_table (Transact-SQL)

sys.sp_help_change_feed_table_groups (Transact-SQL)

sys.dm_change_feed_log_scan_sessions (Transact-SQL)

sys.dm_change_feed_errors (Transact-SQL)

Related content

Last updated on 12/17/2025

```sql
1
```

```sql
autoreseedthreshold
```

```sql
autoreseed
```

```sql
70
```

```sql
autoreseed
```

```sql
dynamicmaxtrans
```

```sql
maxtrans
```

```sql
dynamicmaxtrans
```

```sql
1
```

```sql
dynamicmaxtranslowerbound
```

```sql
maxtrans
```

```sql
dynamicmaxtranslowerbound
```

```sql
200
```

```sql
CONTROL
```
