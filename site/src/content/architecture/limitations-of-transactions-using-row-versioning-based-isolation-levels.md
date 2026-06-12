---
title: "Limitations of transactions using row versioning-based isolation levels"
topic: "io-fundamentals"
description: "Consider the following limitations when working with row versioning-based isolation levels:"
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

Consider the following limitations when working with row versioning-based isolation levels:

can't be enabled in

,

, or.

Global temp tables are stored in. When accessing global temp tables inside a

transaction, one of the following must happen:

Set the

database option to

in.

Use an isolation hint to change the isolation level for the statement.

transactions fail when:

A database is made read-only after the

transaction starts, but before the

transaction accesses the database.

If accessing objects from multiple databases, a database state was changed in such a way

that database recovery occurred after a

transaction starts, but before the

transaction accesses the database. For example: the database was set to

and then to

, database was automatically closed and reopened due to

the

option set to

, or database was detached and reattached.

Distributed transactions, including queries in distributed partitioned databases, aren't

supported under

isolation.

The Database Engine doesn't keep multiple versions of system metadata. Data definition

language (DDL) statements on tables and other database objects (indexes, views, data

types, stored procedures, and common language runtime functions) change metadata. If a

DDL statement modifies an object, any concurrent reference to the object under

isolation causes the

transaction to fail.

transactions don't have

this limitation when the

database option is set to.

For example, a database administrator executes the following

statement.

`READ_COMMITTED_SNAPSHOT`

`tempdb`

`msdb`

`master`

`tempdb`

`SNAPSHOT`

`ALLOW_SNAPSHOT_ISOLATION`

`ON`

`tempdb`

`SNAPSHOT`

`SNAPSHOT`

`SNAPSHOT`

`SNAPSHOT`

`SNAPSHOT`

`OFFLINE`

`ONLINE`

`AUTO_CLOSE`

`ON`

`SNAPSHOT`

`SNAPSHOT`

`SNAPSHOT`

```sql
READ COMMITTED
```

`READ_COMMITTED_SNAPSHOT`

`ON`

```sql
ALTER INDEX
```

```sql
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
WITH (READCOMMITTED)
INNER
JOIN
SecondDB.dbo.Table2 as t2
ON t1.col1 = t2.col2;
```
