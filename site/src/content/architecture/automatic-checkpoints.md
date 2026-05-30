---
title: "Automatic checkpoints"
topic: "query-processing"
description: "A minimally logged operation is performed in the database; for example, a bulk-copy"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

A minimally logged operation is performed in the database; for example, a bulk-copy

operation is performed on a database that is using the Bulk-Logged recovery model.

Database files have been added or removed by using

.

An instance of SQL Server is stopped by a

statement or by stopping the SQL

Server (MSSQLSERVER) service. Either action causes a checkpoint in each database in the

instance of SQL Server.

An instance of SQL Server periodically generates automatic checkpoints in each database

to reduce the time that the instance would take to recover the database.

A database backup is taken.

An activity requiring a database shutdown is performed. This can happen when the

option is

and the last user connection to the database is closed. Another

example is when a database option change is made that requires a restart of the

database.

The SQL Server Database Engine generates automatic checkpoints. The interval between

automatic checkpoints is based on the amount of log space used and the time elapsed since

the last checkpoint. The time interval between automatic checkpoints can be highly variable

and long, if few modifications are made in the database. Automatic checkpoints can also occur

frequently if lots of data is modified.

Use the

server configuration option to calculate the interval between

automatic checkpoints for all the databases on a server instance. This option specifies the

maximum time the Database Engine should use to recover a database during a system restart.

The Database Engine estimates how many log records it can process in the

during a recovery operation.

The interval between automatic checkpoints also depends on the recovery model:

If the database is using either the full or bulk-logged recovery model, an automatic

checkpoint is generated whenever the number of log records reaches the number the

Database Engine estimates it can process during the time specified in the recovery

interval option.

If the database is using the simple recovery model, an automatic checkpoint is generated

whenever the number of log records reaches the lesser of these two values:

The log becomes 70 percent full.

```sql
ALTER DATABASE
```

```sql
SHUTDOWN
```

```sql
AUTO_CLOSE
```

```sql
ON
```
