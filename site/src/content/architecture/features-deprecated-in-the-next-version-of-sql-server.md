---
title: "Features deprecated in the next version of SQL Server"
topic: "io-fundamentals"
description: "2016 (13.x) and later versions"
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

2016 (13.x) and later versions

2016 (13.x) deprecates:

Data Quality Services (DQS)

Master Data Services (MDS)

For information about deprecated features in other versions of SQL Server, see:

Deprecated Database Engine features in SQL Server 2025 (17.x)

Deprecated Database Engine features in SQL Server 2022 (16.x)

Deprecated Database Engine features in SQL Server 2019 (15.x)

Deprecated Database Engine features in SQL Server 2017 (14.x)

This article describes the deprecated SQL Server Database Engine features that are still available in SQL Server 2016 (13.x). Deprecated features

shouldn't be used in new applications.

When a feature is marked deprecated, it means:

The feature is in maintenance mode only. No new changes are added, including changes related to addressing interoperability with new

features.

We strive not to remove a deprecated feature from future releases to make upgrades easier. However, under rare situations, we might

choose to permanently discontinue (remove) the feature from SQL Server if it limits future innovations.

For new development work, don't use deprecated features. For existing applications, plan to modify applications that currently use these

features as soon as possible.

For SQL Server 2017 (14.x), see

Deprecated Database Engine features in SQL Server 2017 (14.x).

You can monitor the use of deprecated features by using the SQL Server Deprecated Features Object performance counter and trace events. For

more information, see

Use SQL Server Objects.

The value of these counters is also available by executing the following statement:

The following SQL Server Database Engine features aren't supported in a future version of SQL Server. Don't use these features in new

development work, and modify applications that currently use these features as soon as possible. The

Feature name

value appears in trace events

as the ObjectName and in performance counters and

as the instance name. The

Feature ID

value appears in

trace events as the ObjectId.

Category

Deprecated feature

Replacement

Feature name

Feature

ID

Backup and

Restore

{

|

}

[MEDIA]

continues to be

deprecated.

{

|

}

and

{

|

}

are discontinued.

None

or

or

104

103

Compatibility

levels

Upgrade from version 100 (SQL Server 2008

(10.0.x) and SQL Server 2008 R2 (10.50.x)).

When a SQL Server version goes out of

support

, the

associated database compatibility level will be marked

deprecated. However, we continue to support

applications certified on any supported Database

Database compatibility

level 100

108

ﾉ

Expand table

`sys.dm_os_performance_counters`

`RESTORE`

`DATABASE`

`LOG`

`WITH`

`PASSWORD`

`BACKUP`

`DATABASE`

`LOG`

```sql
WITH
PASSWORD
```

`BACKUP`

`DATABASE`

`LOG`

```sql
WITH
MEDIAPASSWORD
```

```sql
BACKUP DATABASE
```

```sql
LOG
WITH PASSWORD
BACKUP DATABASE
```

```sql
LOG
WITH MEDIAPASSWORD
```

```sql
SELECT
*
FROM sys.dm_os_performance_counters
WHERE object_name
LIKE
'%SQL%Deprecated Features%'
;
```
