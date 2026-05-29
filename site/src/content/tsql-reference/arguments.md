---
name: 'Arguments'
title: 'Arguments'
category: 'statements'
description: 'Specifies that statements can read rows that were modified by other transactions but not yet'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## READ UNCOMMITTED

## READ COMMITTED

Specifies that statements can read rows that were modified by other transactions but not yet

committed.

Transactions running at the

level don't issue shared locks to prevent other

transactions from modifying data read by the current transaction.

transactions are also not blocked by exclusive locks that would prevent the current transaction

from reading rows that were modified but not committed by other transactions. When this

option is set, it's possible to read uncommitted modifications, which are called dirty reads.

Values in the data can be changed and rows can appear or disappear in the data set before the

end of the transaction. This option has the same effect as setting

on all tables in all

statements in a transaction. This is the least restrictive of the isolation levels.

In SQL Server, you can also minimize locking contention while protecting transactions from

dirty reads of uncommitted data modifications using either:

The

isolation level with the

database option set

to

.

The

isolation level. For more information about snapshot isolation, see

Snapshot Isolation in SQL Server

.

Specifies that statements can't read data that was modified but not committed by other

transactions. This prevents dirty reads. Data can be changed by other transactions between

individual statements within the current transaction, resulting in nonrepeatable reads or

phantom data. This option is the SQL Server default.

The behavior of

depends on the setting of the

database option:

If

is set to

(the default on SQL Server), the Database Engine

uses shared locks to prevent other transactions from modifying rows while the current

transaction is running a read operation. The shared locks also block the statement from

reading rows modified by other transactions until the other transaction is completed. The

shared lock type determines when it is released. Row locks are released before the next

### Transaction Locking and Row

### Versioning Guide

## REPEATABLE READ

row is processed. Page locks are released when the next page is read, and table locks are

released when the statement finishes.

If

is set to

, the Database Engine uses row versioning to

present each statement with a transactionally consistent snapshot of the data as it existed

at the start of the statement. Locks aren't used to protect the data from updates by other

transactions.

is the default on Azure SQL Database and SQL database

in Microsoft Fabric.

Snapshot isolation supports FILESTREAM data. Under snapshot isolation mode, FILESTREAM

data read by any statement in a transaction is the transactionally consistent version of the data

that existed at the start of the transaction.

When the

database option is

, you can use the

table hint to request shared locking instead of row versioning for individual statements in

transactions running at the

isolation level.

）

Important

Choosing a transaction isolation level doesn't affect the locks acquired to protect data

modifications. A transaction always gets an exclusive lock on any data it modifies, and

holds that lock until the transaction completes, regardless of the isolation level set for that

transaction. Additionally, an update made at the

isolation level uses

update locks on the data rows selected, whereas an update made at the

isolation level uses row versions to select rows to update. For read operations, transaction

isolation levels primarily define the level of protection from the effects of modifications

made by other transactions. For more information, see

.

７

Note

When you set the

option, only the connection executing the

command is allowed in the database. There must be no other open

connection in the database until

is complete. The database doesn't have

to be in single-user mode.

## SNAPSHOT

Specifies that statements can't read data that was modified but not yet committed by other

transactions, and that no other transactions can modify data that was read by the current

transaction until the current transaction completes.

Shared locks are placed on all data read by each statement in the transaction and are held until

the transaction completes. This prevents other transactions from modifying any rows that were

read by the current transaction. Other transactions can insert new rows that match the search

conditions of statements issued by the current transaction. If the current transaction then

retries the statement, it retrieves the new rows, which results in phantom reads. Because shared

locks are held to the end of a transaction instead of being released at the end of each

statement, concurrency is lower than the default

isolation level. Use this option

only when necessary.

Specifies that data read by any statement in a transaction is the transactionally consistent

version of the data that existed at the start of the transaction. The transaction can only

recognize data modifications that were committed before the start of the transaction. Data

modifications made by other transactions after the start of the current transaction aren't visible

to statements executing in the current transaction. The effect is as if the statements in a

transaction get a snapshot of the committed data as it existed at the start of the transaction.

Except when a database is being recovered,

transactions don't request locks when

reading data.

transactions reading data don't block other transactions from writing

data. Transactions writing data don't block

transactions from reading data.

During the roll-back phase of a database recovery,

transactions request a lock if an

attempt is made to read data that is locked by another transaction that is being rolled back.

The

transaction is blocked until that transaction is rolled back. The lock is released

immediately after it is granted.

The

database option must be set to

before you can start a

transaction that uses the

isolation level. If a transaction using the

isolation

level accesses data in multiple databases,

must be set to

in each

database.

A transaction can't be set to

isolation level that started with another isolation level;

doing so causes the transaction to abort. If a transaction starts in the

isolation level,

you can change it to another isolation level and then back to

. A transaction starts the

first time it accesses data.

## SERIALIZABLE

```sql
READ UNCOMMITTED
```

```sql
READ UNCOMMITTED
```

```sql
NOLOCK
```

```sql
SELECT
```

```sql
READ COMMITTED
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
ON
```

```sql
SNAPSHOT
```

```sql
READ COMMITTED
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
OFF
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
ON
```

```sql
READ_COMMITTED_SNAPSHOT
ON
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
ON
```

```sql
READCOMMITTEDLOCK
```

```sql
READ COMMITTED
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
ALTER DATABASE
```

```sql
ALTER DATABASE
```

```sql
READ COMMITTED
```

```sql
SNAPSHOT
```

```sql
SNAPSHOT
```

```sql
SNAPSHOT
```

```sql
SNAPSHOT
```

```sql
SNAPSHOT
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
SNAPSHOT
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
SNAPSHOT
```

```sql
SNAPSHOT
```
