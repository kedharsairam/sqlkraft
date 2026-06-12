---
title: "Locking overview"
topic: "locking"
description: "Optimized locking is enabled per database. Connect to your database, then use the following"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Optimized locking is enabled per database. Connect to your database, then use the following

query to check if optimized locking is enabled:

## Description

Optimized locking is disabled.

Optimized locking is enabled.

Optimized locking isn't available.

sys.databases

catalog view.

enabled for all databases, execute the following query:

This is a short summary of the behavior when optimized locking isn't enabled.

Transaction locking and row versioning guide.

ﾉ

```sql
0
```

```sql
1
```

`NULL`

```sql
SELECT database_id,
name
,
is_accelerated_database_recovery_on,
is_read_committed_snapshot_on,
is_optimized_locking_on
FROM sys.databases

= DB_NAME();
```

```sql
SELECT
DATABASEPROPERTYEX(DB_NAME(),
'IsOptimizedLockingOn'
)
AS is_optimized_locking_enabled;
```

```sql
SELECT database_id,
name
,
is_optimized_locking_on
FROM sys.databases;
```
