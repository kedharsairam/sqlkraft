---
name: "Nonclustered indexes on separate filegroups"
title: "Nonclustered indexes on separate filegroups"
category: "queries"
description: "of every table and indexed view in the filegroup."
tags: ["tsql","queries"]
pubDate: 2026-05-29
---

DBCC CHECKTABLE

of every table and indexed view in the filegroup.

Running

or

separately from

isn't

required.

uses an internal database snapshot to provide the transactional

consistency that it must have to perform these checks. For more information, see

View the Size

of the Sparse File of a Database Snapshot (Transact-SQL)

and the

DBCC internal database

snapshot usage

section in

DBCC (Transact-SQL).

If a snapshot can't be created, or the

option is specified,

acquires

locks to obtain the required consistency. In this case, an exclusive database lock is required to

perform the allocation checks, and shared table locks are required to perform the table checks.

causes

to run faster on a database under heavy load, but

decreases the concurrency available on the database while

is running.

By default,

performs parallel checking of objects. The degree of

parallelism is automatically determined by the query processor. The maximum degree of

parallelism is configured just like parallel queries. To restrict the maximum number of

processors available for DBCC checking, use

sp_configure. For more information, see

Configure

the max degree of parallelism Server Configuration Option.

Parallel checking can be disabled by using Trace Flag 2528. For more information, see

Trace

Flags (Transact-SQL).

７

Note

Running

against

does not perform any allocation checks and

must acquire shared table locks to perform table checks. This is because, for performance

reasons, database snapshots are not available on. This means that the required

transactional consistency cannot be obtained.

#### State

```sql
DBCC CHECKALLOC
```

```sql
DBCC CHECKTABLE
```

```sql
DBCC CHECKFILEGROUP
```

```sql
DBCC CHECKFILEGROUP
```

`TABLOCK`

```sql
DBCC CHECKFILEGROUP
```

`TABLOCK`

```sql
DBCC CHECKFILEGROUP
```

```sql
DBCC CHECKFILEGROUP
```

```sql
DBCC CHECKFILEGROUP
```

```sql
DBCC CHECKFILEGROUP
```

`tempdb`

`tempdb`
