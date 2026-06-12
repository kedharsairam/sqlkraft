---
title: "Database snapshots"
topic: "collation"
description: "A database snapshot is a read-only, static view of a SQL Server database (the source database). It's transactionally consistent with the source databa"
tags: ["collation","database-snapshots"]
pubDate: "2025-12-01"
---

A database snapshot is a read-only, static view of a SQL Server database (the source database).

It's transactionally consistent with the source database as of the snapshot's creation and always

resides on the same server instance as its source database. While database snapshots provide a

read-only view of the data in the same state as when the snapshot was created, the size of the

snapshot file grows as changes are made to the source database.

While database snapshots can be beneficial during major schema upgrades and allow for

reverting to a previous state, it's crucial to understand that snapshots don't replace the need

for regular backups. You can't back up or restore database snapshots, which means they should

be used with a robust backup strategy to ensure data protection and recovery if there is data

loss or corruption.

Database snapshots are created with the

CREATE DATABASE

T-SQL syntax, using the

syntax.

Multiple snapshots can exist on a given source database. Each database snapshot persists until

the database owner explicitly drops it.

Database snapshots operate at the data page level. Before a page of the source database is

modified for the first time, the original page is copied from the source database to the

snapshot. The snapshot stores the original page, preserving the data records as they existed

when the snapshot was created. The same process is repeated for every page being modified

for the first time. To the user, a database snapshot appears never to change because read

operations on a database snapshot always access the original data pages, regardless of where

they reside.

The snapshot stores the copied original pages using one or more

sparse files. Initially, a sparse

file is an empty file that contains no user data and hasn't yet been allocated disk space for user

data. The file size grows as more pages are updated in the source database. The following

７

Note

Database snapshots are unrelated to snapshot backups, Transact-SQL snapshot backups,

snapshot isolation of transactions, or snapshot replication.

```sql
AS
SNAPSHOT OF
```
