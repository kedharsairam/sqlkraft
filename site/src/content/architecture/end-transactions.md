---
title: "End transactions"
topic: "io-fundamentals"
description: "manager reported a failure to prepare, the transaction manager sends a rollback command"
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

manager reported a failure to prepare, the transaction manager sends a rollback command

to each resource manager and indicates the failure of the commit to the application.

Database Engine applications can manage distributed transactions either through Transact-

SQL or through the database API. For more information, see

BEGIN DISTRIBUTED

TRANSACTION (Transact-SQL).

You can end transactions with either a COMMIT or ROLLBACK statement, or through a

corresponding API function.

If a transaction is successful, commit it. A

statement guarantees all of the

transaction's modifications are made a permanent part of the database. A commit also frees

resources, such as locks, used by the transaction.

If an error occurs in a transaction, or if the user decides to cancel the transaction, roll back

the transaction. A

statement backs out all modifications made in the transaction

by returning the data to the state it was in at the start of the transaction. Roll back also frees

resources held by the transaction.

If an error prevents the successful completion of a transaction, the Database Engine automatically

rolls back the transaction and frees all resources held by the transaction. If the client network

connection to an instance of the Database Engine is broken, any outstanding transactions for the

connection are rolled back when the network notifies the instance of the connection break. If the

client application fails or if the client computer goes down or is restarted, this also breaks the

connection, and the instance of the Database Engine rolls back any outstanding transactions

７

Note

On multiple active result sets (MARS) sessions, an explicit transaction started through an API

function can't be committed while there are pending execution requests. Any attempt to

commit this type of transaction while there are executing requests results in an error.

when the network notifies it of the connection break. If the client disconnects from the Database

Engine, any outstanding transactions are rolled back.

If a run-time statement error (such as a constraint violation) occurs in a batch, the default

behavior in the Database Engine is to roll back only the statement that generated the error. You

can change this behavior using the

statement. After

is

executed, any run-time statement error causes an automatic rollback of the current transaction.

Compile errors, such as syntax errors, aren't affected by. For more information,

see

SET XACT_ABORT (Transact-SQL).

When errors occur, the appropriate action (

or

) should be included in application

code. One effective tool for handling errors, including those in transactions, is the Transact-SQL

construct. For more information with examples that include transactions, see

TRY.CATCH (Transact-SQL). Beginning with SQL Server 2012 (11.x), you can use the

statement to raise an exception and transfers execution to a

block of a

construct. For more information, see

THROW (Transact-SQL).

In autocommit mode, it sometimes appears as if an instance of the Database Engine has rolled

back an entire batch instead of just one SQL statement. This happens if the error encountered is a

compile error, not a run-time error. A compile error prevents the Database Engine from building

an execution plan, hence nothing in the batch can be executed. Although it appears that all of the

statements before the one generating the error were rolled back, the error prevented anything in

the batch from being executed. In the following example, none of the

statements in the

third batch are executed because of a compile error. It appears that the first two

statements are rolled back when they're never executed.

In the following example, the third

statement generates a run-time duplicate primary key

error. The first two

statements are successful and committed, so they remain after the

run-time error.

Compile and run-time errors in autocommit mode

## Locking

## Row versioning

`COMMIT`

`ROLLBACK`

```sql
SET XACT_ABORT ON
```

```sql
SET XACT_ABORT ON
```

```sql
SET XACT_ABORT
```

`COMMIT`

`ROLLBACK`

`TRY.CATCH`

`THROW`

`CATCH`

`TRY.CATCH`

`INSERT`

`INSERT`

`INSERT`

`INSERT`

```sql
CREATE
TABLE
TestBatch (ColA
INT
PRIMARY
KEY
, ColB
CHAR (3));
GO
INSERT
INTO
TestBatch
VALUES (1,
'aaa'
);
INSERT
INTO
TestBatch
VALUES (2,
'bbb'
);
INSERT
INTO
TestBatch VALUSE (3,
'ccc'
);
-- Syntax error.
GO
SELECT
*
FROM
TestBatch;
-- Returns no rows.
GO
```
