---
title: "Behavior when reading data"
topic: "io-fundamentals"
description: "Row versions are held long enough to satisfy the requirements of transactions running under row"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Row versions are held long enough to satisfy the requirements of transactions running under row

versioning-based isolation levels. The Database Engine tracks the earliest useful transaction

sequence number and periodically deletes all row versions stamped with transaction sequence

numbers that are lower than the earliest useful sequence number.

When both database options are set to

, only rows modified by triggers or MARS sessions, or

read by online index operations, are versioned. Those row versions are released when no longer

needed. A background process removes stale row versions.

When transactions running under row versioning-based isolation read data, the read operations

don't acquire shared (

) locks on the data being read, and therefore don't block transactions that

are modifying data. Also, the overhead of locking resources is minimized as the number of locks

acquired is reduced.

isolation using row versioning and

isolation are

designed to provide statement-level or transaction-level read consistency of versioned data.

All queries, including transactions running under row versioning-based isolation levels, acquire

schema stability (

) locks during compilation and execution. Because of this, queries are

blocked when a concurrent transaction holds a schema modification (

) lock on the table.

For example, a data definition language (DDL) operation acquires a

lock before it modifies

the schema information of the table. Transactions, including those running under a row

versioning-based isolation level, are blocked when attempting to acquire a

lock.

Conversely, a query holding a

lock blocks a concurrent transaction that attempts to

acquire a

lock.

When a transaction using the

isolation level starts, the instance of the Database Engine

records all of the currently active transactions. When the

transaction reads a row that

has a version chain, the Database Engine follows the chain and retrieves the row where the

transaction sequence number is:

Closest to but lower than the sequence number of the snapshot transaction reading the

row.

７

Note

For short-running transactions, a version of a modified row might get cached in the buffer

pool without getting written to the version store. If the need for the versioned row is short-

lived, the row gets dropped from the buffer pool and doesn't incur I/O overhead.

`OFF`

```sql
S
```

```sql
READ COMMITTED
```

`SNAPSHOT`

```sql
Sch-S
```

```sql
Sch-M
```

```sql
Sch-M
```

```sql
Sch-S
```

```sql
Sch-S
```

```sql
Sch-M
```

`SNAPSHOT`

`SNAPSHOT`
