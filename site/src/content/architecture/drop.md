---
title: "Drop"
topic: "collation"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Dropping a database snapshot deletes the database snapshot from SQL Server and deletes the

  sparse files that are used by the snapshot. When you drop a
tags:
  - "collation"
  - "drop"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Dropping a database snapshot deletes the database snapshot from SQL Server and deletes the

sparse files that are used by the snapshot. When you drop a database snapshot, all user

connections to it are terminated.

Any user with DROP DATABASE permissions can drop a database snapshot.

1. Identify the database snapshot that you want to drop. You can view the snapshots on a

database in SQL Server Management Studio. For more information, see

View a Database

Snapshot (SQL Server)

.

2. Issue a

DROP DATABASE

statement, specifying the name of the database snapshot to be

dropped. The syntax is as follows:

DROP DATABASE

database_snapshot_name

[

...

n

]

Where

database_snapshot_name

is the name of the database snapshot to be dropped.

This example drops a database snapshot named SalesSnapshot0600, without affecting the

source database.

SQL)

```sql
DROP DATABASE SalesSnapshot0600 ;
```
