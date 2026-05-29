---
title: "Locking overview"
topic: "locking"
description: "Optimized locking is enabled per database. Connect to your database, then use the following"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

SQL

Optimized locking is enabled per database. Connect to your database, then use the following

query to check if optimized locking is enabled:

SQL

## Description

Optimized locking is disabled.

Optimized locking is enabled.

Optimized locking isn't available.

You can also use the

sys.databases

catalog view. For example, to see if optimized locking is

enabled for all databases, execute the following query:

SQL

This is a short summary of the behavior when optimized locking isn't enabled. For more

information, review the

Transaction locking and row versioning guide

.

ﾉ

Expand table

```sql
0
```

```sql
1
```

```sql
NULL
```

```sql
SELECT
database_id,
name
,
is_accelerated_database_recovery_on,
is_read_committed_snapshot_on,
is_optimized_locking_on
FROM
sys.databases
WHERE
name
= DB_NAME();
```

```sql
SELECT
DATABASEPROPERTYEX(DB_NAME(),
'IsOptimizedLockingOn'
)
AS
is_optimized_locking_enabled;
```

```sql
SELECT
database_id,
name
,
is_optimized_locking_on
FROM
sys.databases;
```
