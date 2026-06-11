---
name: "Queues"
title: "Queues"
category: "statements"
description: "for parallelism depending on the subtree cost."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

for parallelism depending on the subtree cost. The target table referenced in the

clause isn't eligible for parallelism.

Columns returned from

reflect the data as it's after the

,

, or

statement completes, but before triggers are executed.

For

triggers, the returned results are generated as if the

,

, or

had actually occurred, even if no modifications take place as the result of the trigger operation.

If a statement that includes an

clause is used inside the body of a trigger, table aliases

must be used to reference the trigger inserted and deleted tables to avoid duplicating column

references with the

and

tables associated with

.

If the

clause is specified without also specifying the

keyword, the target of the

DML operation can't have any enabled trigger defined on it for the given DML action. For

example, if the

clause is defined in an

statement, the target table can't have any

enabled

triggers.

If the

option disallow results from triggers is set, an

clause without an

clause causes the statement to fail when it's invoked from within a trigger.

The

clause supports the large object data types:

,

,

,

,

,

, and

. When you use the

clause in the

statement to modify an

,

, or

column, the full

before and after images of the values are returned if they're referenced. The

function can't appear as part of an expression on a

,

, or

column in the

clause.

You can use

in applications that use tables as queues, or to hold intermediate result

sets. That is, the application is constantly adding or removing rows from the table. The

following example uses the

clause in a

statement to return the deleted row to

the calling application.

This example removes a row from a table used as a queue and returns the deleted values to

the processing application in a single action. Other semantics might also be implemented, such

as using a table to implement a stack. However, SQL Server doesn't guarantee the order in

which rows are processed and returned by DML statements using the

clause. It's up to

the application to include an appropriate

clause that can guarantee the desired

semantics, or understand that when multiple rows might qualify for the DML operation, there's

no guaranteed order. The following example uses a subquery and assumes uniqueness is a

characteristic of the

column in order to implement the desired ordering

semantics.

```sql
OUTPUT INTO
```

`OUTPUT`

`INSERT`

`UPDATE`

`DELETE`

```sql
INSTEAD OF
```

`INSERT`

`UPDATE`

`DELETE`

`OUTPUT`

`INSERTED`

`DELETED`

`OUTPUT`

`OUTPUT`

`INTO`

`OUTPUT`

`UPDATE`

`UPDATE`

`sp_configure`

`OUTPUT`

`INTO`

`OUTPUT`

```sql
.WRITE
```

`UPDATE`

`TEXTPTR()`

`OUTPUT`

`OUTPUT`

`OUTPUT`

`DELETE`

`OUTPUT`

`WHERE`

`DatabaseLogID`

```sql
USE
AdventureWorks2022;
GO
DELETE
TOP(1) dbo.DatabaseLog
WITH (READPAST)
OUTPUT
DELETED.*
WHERE
DatabaseLogID = 7;
GO
USE tempdb;
GO
CREATE
TABLE dbo.table1 (
id
INT
,
employee
VARCHAR (32)
);
GO
INSERT
INTO dbo.table1
VALUES (1,
'Fred'
),
(2,
'Tom'
),
(3,
'Sally'
),
(4,
'Alice'
);
GO
DECLARE
@MyTableVar
TABLE (
id
INT
,
employee
VARCHAR (32)
);
PRINT 'table1, before delete
';
SELECT *
FROM dbo.table1;
DELETE
FROM dbo.table1
OUTPUT DELETED.*
```
