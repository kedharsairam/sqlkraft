---
title: "Database Engine"
topic: "query-processing"
description: "Starting with SQL Server 2005 (9.x), the Database Engine offers an implementation of an existing"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

SQL

Starting with SQL Server 2005 (9.x), the Database Engine offers an implementation of an existing

transaction isolation level,

, that provides a statement level snapshot using row

versioning. Database Engine also offers a transaction isolation level,

, that provides a

transaction level snapshot also using row versioning.

Row versioning is a general framework in SQL Server that invokes a copy-on-write mechanism

when a row is modified or deleted. This requires that while the transaction is running, the old

version of the row must be available for transactions that require an earlier transactionally

consistent state. Row versioning is used to implement the following features:

Build the

and

tables in triggers. Any rows modified by the trigger are

versioned. This includes the rows modified by the statement that launched the trigger, as

well as any data modifications made by the trigger.

Support Multiple Active Result Sets (MARS). If a MARS session issues a data modification

statement (such as

,

, or

) at a time there's an active result set, the rows

affected by the modification statement are versioned.

Support index operations that specify the

option.

Support row versioning-based transaction isolation levels:

A new implementation of the

isolation level that uses row versioning to

provide statement-level read consistency.

A new isolation level,

, to provide transaction-level read consistency.

Row versions are stored in a version store. If

accelerated database recovery (ADR)

is enabled on a

database, the version store is created in that database. Otherwise, the version store is created in

the

database.

The database must have enough space for the version store. When the version store is in

,

and the

database is full, update operations stop generating versions but continue to

succeed, but read operations might fail because a particular row version that is needed doesn't

exist. This affects operations like triggers, MARS, and online indexing.

When ADR is used and the version store is full, read operations continue to succeed but write

operations that generate versions, such as

and

fail.

operations continue to

succeed if the database has sufficient space.

Using row versioning for

and

transactions is a two-step process:

1. Set either or both the

and

database

options to

.

2. Set the appropriate transaction isolation level in an application:

When the

database option is

, transactions setting the

isolation level use row versioning.

When the

database option is

, transactions can set the

isolation level.

When either

or

database option is set to

,

the Database Engine assigns a transaction sequence number (XSN) to each transaction that

manipulates data using row versioning. Transactions start at the time a

statement is executed. However, the transaction sequence number starts with the first read or

write operation after the

statement. The transaction sequence number is

incremented by one each time it's assigned.

When either the

or

database options are set

to

, logical copies (versions) are maintained for all data modifications performed in the

database. Every time a row is modified by a specific transaction, the instance of the Database

Engine stores a version of the previously committed image of the row in the version store. Each

version is marked with the transaction sequence number of the transaction that made the

change. The versions of modified rows are chained using a link list. The newest row value is

always stored in the current database and chained to the versioned rows in the version store.

７

Note

For modification of large objects (LOBs), only the changed fragment is copied to the version

store.

```sql
READ COMMITTED
```

```sql
SNAPSHOT
```

```sql
inserted
```

```sql
deleted
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
ONLINE
```

```sql
READ COMMITTED
```

```sql
SNAPSHOT
```

```sql
tempdb
```

```sql
tempdb
```

```sql
tempdb
```

```sql
BEGIN
TRANSACTION
;
SELECT
col1
FROM
TestTable
WITH
(TABLOCKX, HOLDLOCK);
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
INSERT
```

```sql
READ COMMITTED
```

```sql
SNAPSHOT
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
ALLOW_SNAPSHOT_ISOLATION
```

```sql
ON
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
ON
```

```sql
READ COMMITTED
```

```sql
ALLOW_SNAPSHOT_ISOLATION
```

```sql
ON
```

```sql
SNAPSHOT
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
ALLOW_SNAPSHOT_ISOLATION
```

```sql
ON
```

```sql
BEGIN TRANSACTION
```

```sql
BEGIN TRANSACTION
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
ALLOW_SNAPSHOT_ISOLATION
```

```sql
ON
```
