---
name: 'Limitations'
title: 'Limitations'
category: 'statements'
description: 'To drop a database published for transactional replication, or published or subscribed to merge'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

### Example D

Output

To drop a database published for transactional replication, or published or subscribed to merge

replication, you must first remove replication from the database. If a database is damaged, or

replication can't first be removed (or both), in most cases you still can drop the database by

using

to set the database offline and then dropping it.

If the database is involved in log shipping, remove log shipping before dropping the database.

For more information, see

About log shipping (SQL Server)

.

System databases

can't be dropped.

The

statement must run in autocommit mode and isn't allowed in an explicit or

implicit transaction. Autocommit mode is the default transaction management mode.

Any database snapshots on a database must be dropped before the database can be dropped.

Dropping a database enable for Stretch Database doesn't remove the remote data. If you want

to delete the remote data, you have to remove it manually.

SQL Server

２

Warning

You can't drop a database currently being used. This means locks being held for reading

or writing by any user. One way to remove users from the database is to use

to set the database to SINGLE_USER. In this strategy, you should execute the

and

in the same batch, to avoid another connection

claiming single user session allowed. For more information, see

.

SQL Server

### db_owner

### dbmanager

### db_owner

## Azure SQL Database

## Azure Synapse Analytics

```sql
ALTER DATABASE
```

```sql
DROP DATABASE
```

```sql
SQL Server has encountered %d occurrence(s) of cachestore flush for the '%s'
cachestore (part of plan cache) due to some database maintenance or reconfigure
operations.
```

```sql
ALTER
DATABASE
```

```sql
ALTER DATABASE
```

```sql
DROP DATABASE
```
