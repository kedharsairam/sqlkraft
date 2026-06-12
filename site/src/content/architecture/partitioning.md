---
title: "Partitioning"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  You can use partitioning on both the current and the history
tags:
  - "tables"
  - "partitioning"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

You can use partitioning on both the current and the history table independently. However,

partitioning can't be used to change the content of the data without system-versioning.

Partitioning is an Enterprise edition feature in SQL Server 2016 (13.x) before Service Pack 1 and

earlier versions. Partitioning is supported in all editions in SQL Server 2016 (13.x) with Service

Pack 1, and later versions.

This section describes how to use

and

with temporal tables.

to the current table can be used to facilitate data loading and querying while

is.

isn't permitted while

is.

You can run

from the history table while

is

, to purge

portions of history data that is no longer relevant.

isn't allowed while

is

, since it can invalidate temporal data

consistency.

Temporal tables

Get started with system-versioned temporal tables

Temporal table system consistency checks

Temporal table considerations and limitations

Temporal table security

Manage retention of historical data in system-versioned temporal tables

System-versioned temporal tables with memory-optimized tables

Temporal table metadata views and functions

```sql
SWITCH IN
SWITCH OUT
SWITCH IN
SYSTEM_VERSIONING
ON
SWITCH OUT
SYSTEM_VERSIONING
ON
SWITCH OUT
SYSTEM_VERSIONING
ON
SWITCH IN
SYSTEM_VERSIONING
ON
```
