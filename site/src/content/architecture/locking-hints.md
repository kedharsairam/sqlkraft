---
title: "Locking hints"
topic: "locking"
description: "### Avoid locking hints with optimized locking"
tags: ["locking","architecture"]
pubDate: 2026-05-29
---

## Avoid locking hints with optimized locking

Locking hints can be specified for individual table references in the

,

,

,

and

statements. The hints specify the type of locking or row versioning the

instance of the Database Engine uses for the table data. Table-level locking hints can be used

when a finer control of the types of locks acquired on an object is required. These locking hints

override the current transaction isolation level for the session.

For more information about the specific locking hints and their behaviors, see

Table Hints

(Transact-SQL).

The Database Engine might have to acquire locks when reading metadata, even when processing

a statement with a locking hint that prevents requests for shared locks when reading data. For

example, a

statement running under the

isolation level or using the

hint doesn't acquire share locks when reading data, but might sometime request locks

when reading a system catalog view. This means it's possible for a

statement to be

blocked when a concurrent transaction is modifying the metadata of the table.

７

Note

Locking hints aren't recommended for use when optimized locking is enabled. While table

and query hints are honored, they reduce the benefit of optimized locking. For more

information, see.

７

Note

We recommend that table-level locking hints be used to change the default locking behavior

only when necessary. Forcing a locking level can adversely affect concurrency.

`SELECT`

`INSERT`

`UPDATE`

`DELETE`

`MERGE`

`SELECT`

```sql
READ UNCOMMITTED
```

`NOLOCK`

`SELECT`

```sql
dateformat mdy datefirst 7.
Isolation level repeatable read (14 row(s) affected)
DBCC execution completed. If DBCC printed error messages, contact your system administrator.
```
