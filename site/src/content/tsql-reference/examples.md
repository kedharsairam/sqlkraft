---
name: "Examples"
title: "Examples"
category: "statements"
description: "To view the current setting for this setting, run the following query."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

To view the current setting for this setting, run the following query.

The following code example causes a foreign key violation error in a transaction that has other

Transact-SQL statements. In the first set of statements, the error is generated, but the other

statements execute successfully and the transaction is successfully committed. In the second

set of statements,

is set to. This causes the statement error to terminate the

batch and the transaction is rolled back.

THROW (Transact-SQL)

BEGIN TRANSACTION (Transact-SQL)

COMMIT TRANSACTION (Transact-SQL)

ROLLBACK TRANSACTION (Transact-SQL)

SET Statements (Transact-SQL)

@@TRANCOUNT (Transact-SQL)

See Also

```sql
SET XACT_ABORT
```

`ON`

```sql
DECLARE
@XACT_ABORT
VARCHAR (3) =
'OFF'
;
IF ( (16384 & @@OPTIONS) = 16384 )
SET
@XACT_ABORT =
'ON'
;
SELECT
@XACT_ABORT
AS
XACT_ABORT;
```

```sql
IF OBJECT_ID(N't2', N'U') IS NOT NULL
DROP
TABLE t2;
GO
IF OBJECT_ID(N't1', N'U') IS NOT NULL
DROP
TABLE t1;
GO
CREATE
TABLE t1 (a
INT
NOT
NULL
PRIMARY
KEY
);
CREATE
TABLE t2 (a
INT
NOT
NULL
REFERENCES t1(a));
GO
INSERT
INTO t1
VALUES (1);
INSERT
INTO t1
VALUES (3);
INSERT
INTO t1
VALUES (4);
INSERT
INTO t1
VALUES (6);
GO
SET
XACT_ABORT
OFF
;
GO
BEGIN
TRANSACTION
;
INSERT
INTO t2
VALUES (1);
INSERT
INTO t2
VALUES (2);
-- Foreign key error.
INSERT
INTO t2
VALUES (3);
COMMIT
TRANSACTION
;
GO
SET
XACT_ABORT
ON
;
GO
BEGIN
TRANSACTION
;
INSERT
INTO t2
VALUES (4);
INSERT
INTO t2
VALUES (5);
-- Foreign key error.
INSERT
INTO t2
VALUES (6);
COMMIT
TRANSACTION
;
```

```sql
GO
-- SELECT shows only keys 1 and 3 added.
-- Key 2 insert failed and was rolled back, but
-- XACT_ABORT was OFF and rest of transaction
-- succeeded.
-- Key 5 insert error with XACT_ABORT ON caused
-- all of the second transaction to roll back.
SELECT
*
FROM t2;
GO
```
