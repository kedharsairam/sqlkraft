---
name: "Check objects in parallel"
title: "Check objects in parallel"
category: "predicates"
description: ""
tags: ["tsql", "predicates"]
pubDate: 2026-05-29
---

If a snapshot can't be created, or

is specified,

acquires a shared table

lock to obtain the required consistency.

When FILESTREAM is enabled for a database and table, you can optionally store

binary large objects (BLOBs) in the file system. When using

on

a table that stores BLOBs in the file system, DBCC checks link-level consistency between the file

system and database.

For example, if a table contains a

column that uses the FILESTREAM attribute,

will check that there is a one-to-one mapping between file system directories

and files and table rows, columns, and column values.

can repair corruption if

you specify the

option. To repair FILESTREAM corruption, DBCC will

delete any table rows that are missing file system data and will delete any directories and files

that don't map to a table row, column, or column value.

By default,

performs parallel checking of objects. The degree of parallelism is

automatically determined by the query processor. The maximum degree of parallelism is

configured in the same manner as that of parallel queries. To restrict the maximum number of

processors available for DBCC checking, use

sp_configure

. For more information, see

Configure

the max degree of parallelism Server Configuration Option

.

Parallel checking can be disabled by using Trace Flag 2528. For more information, see

Trace

Flags (Transact-SQL)

.

７

Note

If

is run against

, it must acquire a shared table lock. This is

because, for performance reasons, database snapshots are not available on

. This

means that the required transactional consistency cannot be obtained.

７

Note

During a

operation, the bytes that are stored in a byte-ordered user-

defined type column must be equal to the computed serialization of the user-defined type

value. If this is not true, the

routine will report a consistency error.

#### State

### RDBMS manageability

### Editions and

### supported features of SQL Server 2022

`TABLOCK`

```sql
DBCC CHECKTABLE
```

```sql
DBCC CHECKTABLE
```

```sql
DBCC CHECKTABLE
```

```sql
DBCC CHECKTABLE
```

`REPAIR_ALLOW_DATA_LOSS`

```sql
DBCC CHECKTABLE
```

```sql
DBCC CHECKTABLE
```

`tempdb`

`tempdb`

```sql
DBCC CHECKTABLE
```

```sql
DBCC CHECKTABLE
```
