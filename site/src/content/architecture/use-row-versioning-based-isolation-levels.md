---
title: "Use row versioning-based isolation levels"
topic: "io-fundamentals"
description: "isolation transactions isn't activated. No"
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

## Description

isolation transactions isn't activated. No

isolation

transactions are allowed.

isolation transactions is in transition state (from

to

). Open transactions must complete.

No

isolation transactions are allowed.

isolation transactions is activated.

transactions are allowed.

isolation transactions is in transition state (from

to

).

transactions started after this time can't access this database. Existing

transactions can still access this database.

use versioning in this database.

doesn't become

transactions that started when the database

finish.

catalog view to determine the state of both row versioning database

options.

and

versions.

The

and

databases, and can't be disabled.

in

,

, or.

The row versioning framework is always enabled and is used by multiple features. Besides

triggers and multiple active result sets (MARS) sessions, and to support data reads for online

index operations.

Row versioning-based isolation levels are enabled at the database level. Any application

accessing objects from enabled databases can run queries using the following isolation levels:

database

as shown in the following code example:

isolation level use row versioning, which means that read operations don't

block update operations.

as

shown in the following code example:

database option

set to.

, the isolation level must be changed. For example, the following

code example shows a

statement that joins two tables while running under a

transaction.

isolation isn't

enabled.

isolation, it fails to execute

successfully.

when accessing a specific table.

statement executes successfully.

`SNAPSHOT`

`OFF`

`SNAPSHOT`

`SNAPSHOT`

`PENDING_ON`

`SNAPSHOT`

`OFF`

`ON`

`SNAPSHOT`

`ON`

`SNAPSHOT`

`SNAPSHOT`

`PENDING_OFF`

`SNAPSHOT`

`ON`

`OFF`

`SNAPSHOT`

`SNAPSHOT`

`PENDING_OFF`

`OFF`

`SNAPSHOT`

`SNAPSHOT`

`ON`

`sys.databases`

`master`

`msdb`

`ALLOW_SNAPSHOT_ISOLATION`

`ON`

`master`

`msdb`

`READ_COMMITTED_SNAPSHOT`

`ON`

`master`

`tempdb`

`msdb`

```sql
READ COMMITTED
```

`READ_COMMITTED_SNAPSHOT`

`ON`

`READ_COMMITTED_SNAPSHOT`

```sql
READ COMMITTED
```

`SNAPSHOT`

`ALLOW_SNAPSHOT_ISOLATION`

`ON`

`SNAPSHOT`

`ALLOW_SNAPSHOT_ISOLATION`

`ON`

`ALLOW_SNAPSHOT_ISOLATION`

`ON`

`SELECT`

`SNAPSHOT`

`SNAPSHOT`

`SELECT`

`SNAPSHOT`

`SELECT`

```sql
READ COMMITTED
```

`SELECT`

```sql
ALTER
DATABASE
AdventureWorks2022
SET
READ_COMMITTED_SNAPSHOT
ON
;
ALTER
DATABASE
AdventureWorks2022
SET
ALLOW_SNAPSHOT_ISOLATION
ON
;
SET
TRANSACTION
ISOLATION
LEVEL
SNAPSHOT
;
BEGIN
TRANSACTION
;
SELECT t1.col5, t2.col5
FROM
Table1 as t1
INNER
JOIN
SecondDB.dbo.Table2 as t2
ON t1.col1 = t2.col2;
```
