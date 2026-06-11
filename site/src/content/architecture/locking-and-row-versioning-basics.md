---
title: "Locking and row versioning basics"
topic: "locking"
description: ""
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

The Database Engine uses deferred name resolution, where object names are resolved at

execution time, not at compilation time. In the following example, the first two

statements are executed and committed, and those two rows remain in the

table after

the third

statement generates a run-time error by referring to a table that doesn't exist.

The Database Engine uses the following mechanisms to ensure the integrity of transactions and

maintain the consistency of databases when multiple users are accessing data at the same time:

Each transaction requests locks of different types on the resources, such as rows, pages, or

tables, on which the transaction is dependent. The locks block other transactions from

modifying the resources in a way that would cause problems for the transaction requesting

the lock. Each transaction frees its locks when it no longer has a dependency on the locked

resources.

When a row versioning based isolation level is used, the Database Engine maintains versions

of each row that is modified. Applications can specify that a transaction use the row

versions to view data as it existed at the start of the transaction or statement, instead of

### Lost updates

### Uncommitted dependency (dirty read)

`INSERT`

`TestBatch`

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
TestBatch
VALUES (1,
'ccc'
);
-- Duplicate key error.
GO
SELECT
*
FROM
TestBatch;
-- Returns rows 1 and 2.
GO
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
TestBch
VALUES (3,
'ccc'
);
-- Table name error.
GO
SELECT
*
FROM
TestBatch;
-- Returns rows 1 and 2.
GO
```
