---
name: 'sys.availability_groups'
title: 'sys.availability_groups'
category: 'objects'
description: 'Specifies whether this is a contained'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
Specifies whether this is a contained

database.

The following table describes the possible failure condition levels for the

column.

Specifies that an automatic failover should be initiated when any of the following occurs:

- The SQL Server service is down.

- The lease of the availability group for connecting to the WSFC failover cluster expires because

no ACK is received from the server instance.

For more information, see

How It Works: SQL Server Always On Lease Timeout

.

Specifies that an automatic failover should be initiated when any of the following occurs:

- The instance of SQL Server doesn't connect to cluster, and the user-specified

threshold of the availability group is exceeded.

- The availability replica is in failed state.

Specifies that an automatic failover should be initiated on critical SQL Server internal errors, such

as orphaned spinlocks, serious write-access violations, or too much dumping.

This is the default value.

Specifies that an automatic failover should be initiated on moderate SQL Server internal errors,

such as a persistent out-of-memory condition in the SQL Server internal resource pool.

Specifies that an automatic failover should be initiated on any qualified failure conditions,

including:

- Exhaustion of SQL Engine worker-threads.

- Detection of an unsolvable deadlock.

Requires

permission on the server instance.

ﾉ

Expand table

sys.availability_replicas (Transact-SQL)

What is an Always On availability group?

Monitor Availability Groups (Transact-SQL)

Last updated on 12/29/2025

Related content

```sql
is_contained
```

```sql
failure_condition_level
```

```sql
1
```

```sql
2
```

```sql
health_check_timeout
```

```sql
3
```

```sql
4
```

```sql
5
```

```sql
VIEW ANY DEFINITION
```
