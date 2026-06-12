---
title: "Outer and inner transactions"
topic: "io-fundamentals"
description: "An explicit inner transaction can be started within an explicit outer transaction. This is primarily"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

An explicit inner transaction can be started within an explicit outer transaction. This is primarily

intended to support transactions in stored procedures that can be called either from a process

already in a transaction or from processes that have no active transaction.

The following example shows the use of outer and inner transactions. If

is called when

a transaction is active, the outcome of the inner transaction in

is controlled by the

outer transaction, and its

statements are committed or rolled back based on the commit

or roll back of the outer transaction. If

is executed by a process that doesn't have an

outstanding transaction, the

at the end of the procedure commits the

statements.

Committing inner transactions is ignored by the Database Engine when an outer transaction is

active. The transaction is either committed or rolled back based on the commit or roll back at the

end of the outermost transaction. If the outer transaction is committed, the inner transactions are

also committed. If the outer transaction is rolled back, then all inner transactions are also rolled

back, regardless of whether or not the inner transactions were individually committed.

Each call to

or

applies to the last executed. If

there are multiple

statements, then a

statement applies only to the

last statement, in other words to the innermost transaction. Even if a

statement within an inner transaction refers to the transaction name of the

outer transaction, the commit applies only to the innermost transaction.

It isn't allowed for the

parameter of a

statement to refer

to the inner transaction in a set of named transactions.

can refer only to the

transaction name of the outermost transaction.

The

function records the current transaction nesting level. Each

statement increments

by one. Each

or

statement

decrements

by one. A

or a

statement that

doesn't have a transaction name rolls back the outer and all inner transactions and decrements

to 0. Similarly, a

that uses the transaction name of the

outermost transaction rolls back the outer and all inner transactions and decrements

to 0. To determine if you're already in a transaction,

to see if it's 1 or more. If

is 0, you're not in a transaction.

７

Note

### savepoint

`TransProc`

`TransProc`

`INSERT`

`TransProc`

```sql
COMMIT TRANSACTION
```

`INSERT`

```sql
SET
QUOTED_IDENTIFIER
OFF
;
GO
SET
NOCOUNT
OFF
;
GO
CREATE
TABLE
TestTrans (
ColA
INT
PRIMARY
KEY
,
ColB
CHAR (3)
NOT
NULL
);
GO
CREATE
PROCEDURE
TransProc
@PriKey
INT
,
@CharCol
CHAR (3)
AS
BEGIN
TRANSACTION
InProc;
INSERT
INTO
TestTrans
VALUES (@PriKey, @CharCol);
INSERT
INTO
TestTrans
VALUES (@PriKey + 1, @CharCol);
COMMIT
TRANSACTION
InProc;
GO
/* Start a transaction and execute TransProc. */
BEGIN
TRANSACTION
OutOfProc;
GO
EXEC TransProc 1, 'aaa';
GO
/* Roll back the outer transaction, this will roll back TransProc's inner transaction. */
ROLLBACK
TRANSACTION
OutOfProc;
```

```sql
COMMIT TRANSACTION
```

```sql
COMMIT WORK
```

```sql
BEGIN TRANSACTION
```

```sql
BEGIN TRANSACTION
```

`COMMIT`

```sql
COMMIT TRANSACTION transaction_name
```

`transaction_name`

```sql
ROLLBACK TRANSACTION
```

`transaction_name`

```sql
@@TRANCOUNT
```

```sql
BEGIN TRANSACTION
```

```sql
@@TRANCOUNT
```

```sql
COMMIT TRANSACTION
```

```sql
COMMIT WORK
```

```sql
@@TRANCOUNT
```

```sql
ROLLBACK WORK
```

```sql
ROLLBACK TRANSACTION
```

```sql
@@TRANCOUNT
```

```sql
ROLLBACK TRANSACTION
```

```sql
@@TRANCOUNT
```

```sql
SELECT @@TRANCOUNT
```

```sql
@@TRANCOUNT
```

```sql
GO
EXECUTE
TransProc 3,
'bbb'
;
GO
/*
The following SELECT statement shows only rows 3 and 4 are still in the table. This indicates that the commit of the inner transaction from the first EXECUTE statement of
TransProc was overridden by the subsequent roll back of the outer transaction.
*/
SELECT
*
FROM
TestTrans;
GO
```
