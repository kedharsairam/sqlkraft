---
title: "Space used in tempdb"
topic: "query-processing"
description: "are detected, they're handled and retried"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Update conflict

detection

None.

If update conflicts

are detected, they're handled and retried

automatically.

Integrated support. Can't be disabled.

The row versioning framework supports the following Database Engine features:

Triggers

Multiple Active Results Sets (MARS)

Online indexing

The row versioning framework also supports the following row versioning-based transaction

isolation levels:

When the

database option is set to

,

transactions provide statement-level read consistency using row versioning.

When the

database option is set to

,

transactions

provide transaction-level read consistency using row versioning.

Row versioning-based isolation levels reduce the number of locks acquired by transaction by

eliminating the use of shared locks on read operations. This increases system performance by

reducing the resources used to manage locks. Performance is also increased by reducing the

number of times a transaction is blocked by locks acquired by other transactions.

Row versioning-based isolation levels increase the resources needed by data modifications.

Enabling these options causes all data modifications for the database to be versioned. A copy of

the data before modification is stored in the version store even when there are no active

transactions using row versioning-based isolation. The data after modification includes a pointer

to the versioned data in the version store. For large objects, only part of the object that changed

is stored in the version store.

For each instance of the Database Engine, the version store must have enough space to hold the

row versions. The database administrator must ensure that

and other databases (if ADR is

enabled) have ample space to support the version store. There are two types of version stores:

```sql
READ COMMITTED
```

`SNAPSHOT`

`READ_COMMITTED_SNAPSHOT`

`ON`

`READ_COMMITTED`

`ALLOW_SNAPSHOT_ISOLATION`

`ON`

`SNAPSHOT`

`tempdb`
