---
title: "Use row versioning-based isolation levels"
topic: "io-fundamentals"
description: "isolation transactions isn't activated. No"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

## Description

The support for

isolation transactions isn't activated. No

isolation

transactions are allowed.

The support for

isolation transactions is in transition state (from

to

). Open transactions must complete.

No

isolation transactions are allowed.

The support for

isolation transactions is activated.

transactions are allowed.

The support for

isolation transactions is in transition state (from

to

).

transactions started after this time can't access this database. Existing

transactions can still access this database. Existing write transactions still

use versioning in this database. The state

doesn't become

until all

transactions that started when the database

isolation state was

finish.

Use the

catalog view to determine the state of both row versioning database

options.

All updates to user tables and some system tables stored in

and

generate row

versions.

The

option is automatically set to

in the

and

databases, and can't be disabled.

Users can't set the

option to

in

,

, or

.

The row versioning framework is always enabled and is used by multiple features. Besides

providing row versioning-based isolation levels, it's used to support modifications made in

triggers and multiple active result sets (MARS) sessions, and to support data reads for online

index operations.

Row versioning-based isolation levels are enabled at the database level. Any application

accessing objects from enabled databases can run queries using the following isolation levels:

that uses row versioning by setting the

database

option to

as shown in the following code example:

When the database is enabled for

, all queries running under the

isolation level use row versioning, which means that read operations don't

block update operations.

isolation by setting the

database option to

as

shown in the following code example:

When using cross-database queries, a transaction running under

isolation can

access tables in the database(s) that have the

database option

set to

. To access tables in databases that don't have the

database option set to

, the isolation level must be changed. For example, the following

code example shows a

statement that joins two tables while running under a

transaction. One table belongs to a database in which

isolation isn't

enabled. When the

statement runs under

isolation, it fails to execute

successfully.

The following code example shows the same

statement that has been modified to

change the transaction isolation level to

when accessing a specific table.

Because of this change, the

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
