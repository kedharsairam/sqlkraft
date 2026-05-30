---
title: "Query deprecated features"
topic: "query-processing"
description: "SQL Server 2019 (15.x)"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

SQL Server 2019 (15.x)

Applies to:

SQL Server 2019 (15.x)

SQL Server 2019 (15.x) deprecates:

Data Quality Services (DQS)

Master Data Services (MDS)

Features that were deprecated in prior releases are also deprecated in SQL Server 2019 (15.x).

For information about deprecated features in other versions of SQL Server, see:

Deprecated Database Engine features in SQL Server 2025 (17.x)

Deprecated Database Engine features in SQL Server 2022 (16.x)

Deprecated Database Engine features in SQL Server 2017 (14.x)

Deprecated Database Engine features in SQL Server 2016 (13.x)

When a feature is marked deprecated, it means:

The feature is in maintenance mode only. No new changes are added, including changes

related to addressing interoperability with new features.

We strive not to remove a deprecated feature from future releases to make upgrades

easier. However, under rare situations, we might choose to permanently discontinue

(remove) the feature from SQL Server if it limits future innovations.

For new development work, don't use deprecated features. For existing applications, plan

to modify applications that currently use these features as soon as possible.

You can monitor the use of deprecated features by using the SQL Server Deprecated Features

Object performance counter, or the

and

extended events. For more information, see

Use SQL Server Objects

.

The values of these counters are also available by executing the following statement:

SQL

Breaking changes to Database Engine features in SQL Server 2019

Discontinued Database Engine functionality in SQL Server

Last updated on 11/18/2025

Related content

```sql
deprecation_announcement
```

```sql
deprecation_final_support
```

```sql
SELECT
*
FROM
sys.dm_os_performance_counters
WHERE
object_name
LIKE
'%SQL%Deprecated Features%'
;
```
