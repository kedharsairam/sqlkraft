---
name: 'sys.sp_change_feed_configure_parameters'
title: 'sys.sp_change_feed_configure_parameters'
category: 'general'
description: 'SQL Server 2022 (16.x) and later versions'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## A. Enable automatic reseed

## B. Disable automatic reseed

: Fabric Mirroring only

The lower bound for dynamic maxtrans setting for Fabric Mirroring. By default, the lower

bound value is

.

(success) or

(failure).

A user with

database permissions,

database role membership, or

server role membership can execute this procedure.

: Fabric Mirroring only

Use the following T-SQL sample to enable automatic reseed on the current mirrored database.

Specify a log usage percentage threshold to trigger an autoreseed event, for example 70%. For

more information, see

Configure automatic reseed for Fabric mirrored databases

.

SQL

: Fabric Mirroring only

Use the following T-SQL sample to disable automatic reseed on the current mirrored database.

SQL

## C. Enable dynamic maximum transactions

## D. Configure the dynamic maximum transactions maximum

## and lower bound

: Fabric Mirroring only

To enable the dynamic maximum transactions feature, set

to

. For example:

SQL

To disable the dynamic maximum transactions feature, set

to

. For example:

SQL

Verify the setting of the dynamic maximum transactions feature with

sys.sp_help_change_feed_settings

.

: Fabric Mirroring only

To modify the maximum and lower bounds for the dynamic maximum transactions feature, use

and

respectively. For example:

SQL

sys.sp_help_change_feed (Transact-SQL)

sys.sp_help_change_feed_table (Transact-SQL)

sys.sp_help_change_feed_table_groups (Transact-SQL)

sys.sp_help_change_feed_settings (Transact-SQL)

sys.dm_change_feed_log_scan_sessions (Transact-SQL)

sys.dm_change_feed_errors (Transact-SQL)

Last updated on 12/17/2025

Related content

```sql
200
```

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
USE
<Mirrored
database
name
>
GO
EXECUTE
sys.sp_change_feed_configure_parameters
@autoreseed = 1
, @autoreseedthreshold = 70;
```

```sql
@dynamicmaxtrans
```

```sql
1
```

```sql
@dynamicmaxtrans
```

```sql
0
```

```sql
@maxtrans
```

```sql
@dynamicmaxtranslowerbound
```

```sql
USE
<Mirrored
database
name
>
GO
EXECUTE
sys.sp_change_feed_configure_parameters @autoreseed = 0;
```

```sql
USE
<Mirrored
database
name
>
GO
EXECUTE
sys.sp_change_feed_configure_parameters
@dynamicmaxtrans=1;
USE
<Mirrored
database
name
>
GO
EXECUTE
sys.sp_change_feed_configure_parameters
@dynamicmaxtrans=0;
```

```sql
USE
<Mirrored
database
name
>
GO
EXECUTE
sys.sp_change_feed_configure_parameters
@dynamicmaxtrans=1
, @dynamicmaxtranslowerbound=5
, @
maxtrans
=5000;
```
