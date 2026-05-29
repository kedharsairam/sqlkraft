---
title: "Avoid locking hints"
topic: "locking"
description: "enabled, and the number of queries where LAQ wasn't used for various reasons. This"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

enabled, and the number of queries where LAQ wasn't used for various reasons. This

event fires even if optimized locking is disabled.

In SQL Server and Azure SQL Managed Instance, the

event fires for

every database every several minutes and provides the

skip index locks

and

LAQ

heuristics

statistics for the time interval.

To maximize the benefits of optimized locking, it's recommended to enable

read committed

snapshot isolation (RCSI)

on the database and use

isolation as the default

isolation level.

In Azure SQL Database and SQL database in Microsoft Fabric, RCSI is enabled by default and

is the default isolation level. With RCSI enabled and when using

isolation level, readers read a version of the row from the snapshot taken at the start

of the statement. With LAQ, writers qualify rows per the predicate based on the latest

committed version of the row and without acquiring

locks. With LAQ, a query waits only if

the row qualifies and there's an active write transaction on that row. Qualifying based on the

latest committed version and locking only the qualified rows reduces blocking and increases

concurrency.

While

table and query hints

such as

,

,

,

, etc. are

honored when optimized locking is enabled, they reduce the benefit of optimized locking. Lock

hints force the database engine to take row or page locks and hold them until the end of the

transaction, to honor the intent of the lock hints. Some applications have logic where lock hints

are needed, for example when reading a row with the

hint and then updating it later.

We recommend using lock hints only where needed.

With optimized locking, there are no restrictions on existing queries and queries don't need to

be rewritten. Queries that aren't using hints benefit from optimized locking most.

A table hint on one table in a query doesn't disable optimized locking for other tables in the

same query. Further, optimized locking only affects the locking behavior of tables being

updated by a DML statement such as

,

,

, or

. For example:

SQL

```sql
locking_stats2
```

```sql
READ COMMITTED
```

```sql
READ COMMITTED
```

```sql
READ
COMMITTED
```

```sql
U
```

```sql
UPDLOCK
```

```sql
READCOMMITTEDLOCK
```

```sql
XLOCK
```

```sql
HOLDLOCK
```

```sql
UPDLOCK
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
MERGE
```
