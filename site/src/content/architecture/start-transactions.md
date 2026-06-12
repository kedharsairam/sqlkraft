---
title: "Start transactions"
topic: "io-fundamentals"
description: "Using API functions and Transact-SQL statements, you can start transactions as explicit,"
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

Using API functions and Transact-SQL statements, you can start transactions as explicit,

autocommit, or implicit transactions.

An explicit transaction is one in which you explicitly define both the start and end of the

transaction through an API function or by issuing the Transact-SQL

,

,

,

, or

Transact-SQL statements.

When the transaction ends, the connection returns to the transaction mode it was in before the

explicit transaction was started, which might be the implicit or autocommit mode.

You can use all Transact-SQL statements in an explicit transaction, except for the following

statements:

Full-text system stored procedures

to set database options or any system procedure that modifies the

database inside explicit or implicit transactions.

７

Note

can be used inside an explicit transaction. However,

commits independently of the enclosing transaction and can't be rolled back.

### Implicit Transactions

### Batch-scoped Transactions

Autocommit mode is the default transaction management mode of the Database Engine. Every

Transact-SQL statement is committed or rolled back when it completes. If a statement completes

successfully, it's committed; if it encounters any error, it's rolled back. A connection to an instance

of the Database Engine operates in autocommit mode whenever this default mode hasn't been

overridden by either explicit or implicit transactions. Autocommit mode is also the default mode

for SqlClient, ADO, OLE DB, and ODBC.

When a connection is operating in implicit transaction mode, the instance of the Database Engine

automatically starts a new transaction after the current transaction is committed or rolled back.

You do nothing to delineate the start of a transaction; you only commit or roll back each

transaction. Implicit transaction mode generates a continuous chain of transactions. Set implicit

transaction mode on through either an API function or the Transact-SQL

statement. This mode is also known as Autocommit OFF, see

setAutoCommit Method (SQLServerConnection).

After implicit transaction mode is enabled for a connection, the instance of the Database Engine

automatically starts a transaction when it first executes any of these statements:

Applicable only to multiple active result sets (MARS), a Transact-SQL explicit or implicit

transaction that starts under a MARS session becomes a batch-scoped transaction. A batch-

scoped transaction that isn't committed or rolled back when a batch completes is automatically

rolled back by the Database Engine.

### Distributed transactions

### Prepare phase

### Commit phase

Distributed transactions span two or more servers known as resource managers. The

management of the transaction must be coordinated between the resource managers by a server

component called a transaction manager. Each instance of the Database Engine can operate as a

resource manager in distributed transactions coordinated by transaction managers, such as

Microsoft Distributed Transaction Coordinator (MS DTC), or other transaction managers that

support the Open Group XA specification for distributed transaction processing. For more

information, see the MS DTC documentation.

A transaction within a single instance of the Database Engine that spans two or more databases is

a distributed transaction. The instance manages the distributed transaction internally; to the user,

it operates as a local transaction.

In the application, a distributed transaction is managed much the same as a local transaction. At

the end of the transaction, the application requests the transaction to be either committed or

rolled back. A distributed commit must be managed differently by the transaction manager to

minimize the risk that a network failure can result in some resource managers successfully

committing while others roll back the transaction. This is achieved by managing the commit

process in two phases (the prepare phase and the commit phase), which is known as a two-phase

commit.

When the transaction manager receives a commit request, it sends a prepare command to

all of the resource managers involved in the transaction. Each resource manager then does

everything required to make the transaction durable, and all transaction log buffers for the

transaction are flushed to disk. As each resource manager completes the prepare phase, it

## returns success or failure of the phase to the transaction manager. SQL Server 2014 (12.x)

introduced delayed transaction durability. Delayed durable transactions commit before the

transaction log buffers on each resource manager are flushed to disk. For more information

on delayed transaction durability, see the article

Control Transaction Durability.

If the transaction manager receives successful prepares from all of the resource managers, it

sends commit commands to each resource manager. The resource managers can then

complete the commit. If all of the resource managers report a successful commit, the

transaction manager then sends a success notification to the application. If any resource

### Commit

### Roll back

```sql
BEGIN TRANSACTION
```

```sql
COMMIT
TRANSACTION
```

```sql
COMMIT WORK
```

```sql
ROLLBACK TRANSACTION
```

```sql
ROLLBACK WORK
```

```sql
CREATE DATABASE
ALTER DATABASE
DROP DATABASE
CREATE FULLTEXT CATALOG
ALTER FULLTEXT CATALOG
DROP FULLTEXT CATALOG
DROP FULLTEXT INDEX
ALTER FULLTEXT INDEX
CREATE FULLTEXT INDEX
BACKUP
RESTORE
RECONFIGURE
```

`sp_dboption`

`master`

```sql
UPDATE STATISTICS
```

```sql
UPDATE STATISTICS
```

```sql
SET
IMPLICIT_TRANSACTIONS ON
```

```sql
ALTER TABLE
CREATE
DELETE
DENY
DROP
FETCH
GRANT
INSERT
OPEN
REVOKE
SELECT
TRUNCATE
UPDATE
```
