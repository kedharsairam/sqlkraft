---
title: "Isolation levels in the Database Engine"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

When multiple transactions attempt to modify data in a database at the same time, a system of

controls must be implemented so that modifications made by one transaction don't adversely

affect those of another transaction. This is called concurrency control.

Concurrency control theory has two classifications for the methods of instituting concurrency

control:

concurrency control

A system of locks prevents transactions from modifying data in a way that affects other

transactions. After a transaction performs an action that causes a lock to be applied, other

transactions can't perform actions that would conflict with the lock until the owner releases

it. This is called pessimistic control because it's typically used in systems where there's high

contention for data, where the cost of protecting data with locks is less than the cost of

rolling back transactions if concurrency conflicts occur.

concurrency control

In optimistic concurrency control, transactions don't lock data when they read it. However,

when a transaction updates data, the system checks to see if another transaction changed

the data after it was read. If another transaction updated the data, an error is raised.

Typically, the transaction receiving the error rolls back and starts over. This is called

optimistic because it's typically used in systems where there's low contention for data, and

where the cost of occasionally rolling back a transaction is lower than the cost of locking

data when read.

The Database Engine supports both concurrency control methods. Users specify the type of

concurrency control by selecting transaction isolation levels for connections or concurrency

options on cursors. These attributes can be defined using Transact-SQL statements, or through

the properties and attributes of database application programming interfaces (APIs) such as ADO,

ADO.NET, OLE DB, and ODBC.

Transactions specify an isolation level that defines the degree to which one transaction must be

isolated from the resource or data modifications made by other transactions. Isolation levels are

described in terms of which concurrency side-effects, such as dirty reads or phantom reads, are

allowed.

Transaction isolation levels control:

Whether locks are acquired when data is read, and what type of locks are requested.

How long the read locks are held.

Whether a read operation referencing rows modified by another transaction:

Blocks until the exclusive lock on the row is freed.

Retrieves the committed version of the row that existed at the time the statement or

transaction started.

Reads the uncommitted data modification.

A lower isolation level increases the ability of many transactions to access data at the same time,

but also increases the number of concurrency effects (such as dirty reads or lost updates)

transactions might encounter. Conversely, a higher isolation level reduces the types of

concurrency effects that transactions might encounter, but requires more system resources and

increases the chances that one transaction blocks another. Choosing the appropriate isolation

level depends on balancing the data integrity requirements of the application against the

overhead of each isolation level. The highest isolation level,

, guarantees that a

transaction retrieves exactly the same data every time it repeats a read operation, but it does this

by performing a level of locking that's likely to impact other transactions in multi-user systems.

The lowest isolation level,

, might retrieve data that has been modified but not

committed by other transactions. All of the concurrency side effects can happen in

, but there's no read locking or versioning, so overhead is minimized.

The ISO standard defines the following isolation levels, all of which are supported by the

Database Engine:

）

Important

Choosing a transaction isolation level doesn't affect the locks acquired to protect data

modifications. A transaction always holds an exclusive lock to perform data modification,

and holds that lock until the transaction completes, regardless of the isolation level set for

that transaction. For read operations, transaction isolation levels primarily define the level of

protection from the effects of modifications made by other transactions.

Database Engine isolation levels

ﾉ

Expand table

The lowest isolation level where transactions are isolated only enough to ensure that

physically inconsistent data isn't read. In this level, dirty reads are allowed, so one

transaction might see not-yet-committed changes made by other transactions.

Allows a transaction to read data previously read (not modified) by another transaction

without waiting for the first transaction to complete. The Database Engine keeps write locks

(acquired on selected data) until the end of the transaction, but read locks are released as

soon as the read operation is performed. This is the Database Engine default level.

The Database Engine keeps read and write locks that are acquired on selected data until

the end of the transaction. However, because range-locks aren't managed, phantom reads

can occur.

The highest level where transactions are completely isolated from one another. The

Database Engine keeps read and write locks acquired on selected data until the end of the

transaction. Range-locks are acquired when a SELECT operation uses a range WHERE clause

to avoid phantom reads.

Note:

DDL operations and transactions on replicated tables might fail when the

isolation level is requested. This is because replication queries use hints that

might be incompatible with the

isolation level.

The Database Engine also supports two additional transaction isolation levels that use row

versioning. One is an implementation of

isolation level, and one is the

transaction isolation level.

When the

database option is set

, which is the default setting in

, the

isolation level uses row versioning to provide

statement-level read consistency. Read operations require only the schema stability (

)

table level locks and no page or row locks. That is, the Database Engine uses row versioning

to present each statement with a transactionally consistent snapshot of the data as it existed

at the start of the statement. Locks aren't used to protect the data from updates by other

transactions. A user-defined function can return data that was committed after the time the

statement containing the UDF began.

When the

database option is set

, which is the default setting in

and Azure SQL Managed Instance,

isolation uses shared locks to

prevent other transactions from modifying rows while the current transaction is running a

ﾉ

Expand table

read operation. The shared locks also block the statement from reading rows modified by

other transactions until the other transaction is completed. Both implementations meet the

ISO definition of

isolation.

The snapshot isolation level uses row versioning to provide transaction-level read

consistency. Read operations acquire no page or row locks; only the schema stability (

)

table locks are acquired. When reading rows modified by another transaction, read

operations retrieve the version of the row that existed when the transaction started. You can

only use

isolation when the

database option is set to.

By default, this option is set to

for user databases in SQL Server and Azure SQL Managed

Instance, and set to

for databases in Azure SQL Database.

Note:

The Database Engine doesn't support versioning of metadata. For this reason, there are

restrictions on what DDL operations can be performed in an explicit transaction that's

running under snapshot isolation. The following DDL statements aren't permitted under

snapshot isolation after a

statement:

,

,

,

,

,

,

,

, or any common language runtime (CLR) DDL statement. These statements

are permitted when you're using snapshot isolation within implicit transactions. An implicit

transaction, by definition, is a single statement that makes it possible to enforce the

semantics of snapshot isolation, even with DDL statements. Violations of this principle can

cause error 3961:

The following table shows the concurrency side effects enabled by the different isolation levels.

Yes

Yes

Yes

No

Yes

Yes

No

No

Yes

No

No

No

No

No

No

ﾉ

Expand table

## Transact-SQL

## ADO

## ADO.NET

## OLE DB

## ODBC

`SERIALIZABLE`

```sql
READ UNCOMMITTED
```

```sql
READ
UNCOMMITTED
```

```sql
READ
UNCOMMITTED
```

```sql
READ
COMMITTED
```

```sql
REPEATABLE
READ
```

`SERIALIZABLE`

`SERIALIZABLE`

`SERIALIZABLE`

```sql
READ COMMITTED
```

`SNAPSHOT`

```sql
Read
Committed
Snapshot (RCSI)
```

`READ_COMMITTED_SNAPSHOT`

`ON`

```sql
READ COMMITTED
```

```sql
Sch-S
```

`READ_COMMITTED_SNAPSHOT`

`OFF`

```sql
READ COMMITTED
```

```sql
READ COMMITTED
```

`SNAPSHOT`

```sql
Sch-S
```

`SNAPSHOT`

`ALLOW_SNAPSHOT_ISOLATION`

`ON`

`OFF`

`ON`

```sql
BEGIN TRANSACTION
```

```sql
ALTER TABLE
```

```sql
CREATE INDEX
```

```sql
CREATE
XML INDEX
```

```sql
ALTER INDEX
```

```sql
DROP INDEX
```

```sql
DBCC REINDEX
```

```sql
ALTER PARTITION FUNCTION
```

```sql
ALTER
PARTITION SCHEME
```

```sql
Snapshot isolation transaction failed in database '%.*ls' because the object accessed by the statement has been modified by a DDL statement in another concurrent transaction since the start of this transaction. It is not allowed because the metadata is not versioned. A concurrent update to metadata could lead to inconsistency if mixed with snapshot isolation.
```

```sql
READ UNCOMMITTED
```

```sql
READ COMMITTED
```

```sql
REPEATABLE READ
```

`SNAPSHOT`

`SERIALIZABLE`
