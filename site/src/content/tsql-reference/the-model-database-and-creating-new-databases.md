---
name: 'The model database and creating new databases'
title: 'The model database and creating new databases'
category: 'operators'
description: 'Every database has at least two files, a'
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

Every database has at least two files, a

primary file

and a

transaction log file

, and at least one

filegroup. A maximum of 32,767 files and 32,767 filegroups can be specified for each database.

When you create a database, make the data files as large as possible based on the maximum

amount of data you expect in the database.

We recommend that you use a Storage Area Network (SAN), iSCSI-based network, or locally

attached disk for the storage of your SQL Server database files, because this configuration

optimizes SQL Server performance and reliability.

You can use the

statement to create a read-only, static view, a

database

snapshot

of the

source database

. A database snapshot is transactionally consistent with the

source database as it existed at the time when the snapshot was created. A source database

can have multiple snapshots.

If creating a database snapshot fails, the snapshot becomes suspect and must be deleted. For

more information, see

DROP DATABASE

.

Each snapshot persists until it's deleted by using

.

For more information, see

Database snapshots (SQL Server)

and

Create a database snapshot

.

Several database options are automatically set whenever you create a database. For a list of

these options, see

ALTER DATABASE SET options

.

All user-defined objects in the

model database

are copied to all newly created databases. You

can add any objects, such as tables, views, stored procedures, data types, and so on, to the

７

Note

When you create a database snapshot, the

statement can't reference log

files, offline files, restoring files, and defunct files.

### true

```sql
CREATE DATABASE
```

```sql
DROP DATABASE
```

```sql
CREATE DATABASE
```
