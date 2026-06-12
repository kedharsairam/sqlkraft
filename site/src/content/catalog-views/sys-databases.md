---
name: "sys.databases"
title: "sys.databases"
category: "databases-files"
description: "Lists databases that either reside in an instance of the SQL Server or are accessible through a database gateway."
tags: ["databases-files","catalog-view"]
pubDate: 2026-05-29
syntax: "sys.dm_database_copies"
---

## Description

Lists databases that either reside in an instance of the SQL Server or are accessible through a database gateway.

## Syntax

`sys.dm_database_copies`

## Arguments

If the caller of

does not own a specific non-

server-level permissions at minimum are required to see the

corresponding

row. For the

at minimum. The database to which the caller connects will always appear in

This example returns the database ID of the current database.

This example returns the database ID of the

This example uses

to return the database ID of the

database in the

system function. The function takes a database ID as the

By default, the public role has the

permission, which allows all logins to

see database information. To prevent a login from detecting a database,

permission from public, or

permission for

individual logins.

DB_NAME (Transact-SQL)

Metadata Functions (Transact-SQL)

sys.databases (Transact-SQL)

sys.dm_db_index_operational_stats (Transact-SQL)

## Remarks

Lists databases that either reside in an instance of the SQL Server or are accessible through a

database gateway.

Description

Name of the database. In the Database Engine, this column represents

the database name as stored in the

catalog view.

Size of database, in kilobytes.

For the Database Engine, this field always returns

Database names that are returned can be used as parameters in the

statement to change

the current database context.

value for databases larger than 2.15 TB.

Expand table

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

This function returns the database identification (ID) number of a specified database.

database_name

The name of the database whose database ID number

will return. If the call to

database_name

returns the ID of the current database.

may only be used to return the database identifier of the current database in Azure SQL

Database. NULL is returned if the specified database name is other than the current database.

In Azure SQL Database,

may not return the same value as the. These two views return

values that are unique within the logical server, while

column in other system views return values that are unique within a single

database or within an elastic pool.

READ_WRITE | READWRITE Specifies the group is READ_WRITE. Updates are enabled for the

objects in the filegroup. To change this state, you must have exclusive access to the database.

For more information, see the SINGLE_USER clause.

To decrease the size of a database, use

DBCC SHRINKDATABASE

You cannot add or remove a file while a

statement is running.

A maximum of 32,767 files and 32,767 filegroups can be specified for each database.

Starting with SQL Server 2005 (9.x), the state of a database file (for example, online or offline),

is maintained independently from the state of the database. For more information, see

The state of the files within a filegroup determines the availability of the whole filegroup.

For a filegroup to be available, all files within the filegroup must be online.

If a filegroup is offline, any try to access the filegroup by a SQL statement will fail with an

error. When you build query plans for

statements, the query optimizer avoids

nonclustered indexes and indexed views that reside in offline filegroups. This enables

these statements to succeed. However, if the offline filegroup contains the heap or

clustered index of the target table, the

statements fail. Additionally, any

The keyword

will be removed in a future version of Microsoft SQL Server. Avoid

in new development work, and plan to modify applications that currently

The keyword

will be removed in a future version of Microsoft SQL Server. Avoid

in new development work, and plan to modify applications that currently

The status of these options can be determined by examining the

catalog view or the

property of the

Specifies the name of a database snapshot to be removed.

A database can be dropped regardless of its state: offline, read-only, suspect, and so on. To

display the current state of a database, use the

catalog view.

A dropped database can be re-created only by restoring a backup. Database snapshots can't

be backed up and, therefore, can't be restored.

When a database is dropped, the

master database

should be backed up.

Dropping a database deletes the database from an instance of SQL Server and deletes the

physical disk files used by the database. If the database, or any one of its files, is offline when

dropped, the disk files aren't deleted. These files can be deleted manually by using a file

manager such as File Explorer. To remove a database from the current server without deleting

the files from the file system, use

sp_detach_db

Dropping a database snapshot deletes the database snapshot from an instance of SQL Server

and deletes the physical NTFS file system sparse files used by the snapshot. For information

about using sparse files by database snapshots, see

Database snapshots (SQL Server)

Dropping a database snapshot clears entries in the plan cache associated with the database

snapshot, not the instance as a whole. Clearing the plan cache causes a recompilation of all

subsequent execution plans and can cause a sudden, temporary decrease in query

performance.

For each cleared cachestore in the plan cache, the SQL Server error log contains the following

informational message. This message is logged every five minutes as long as the cache is

flushed within that time interval.

In SQL Server 2016 (13.x) and later versions, dropping a database that has

backups associated with it will succeed, but the database files that have associated

snapshots will not be deleted to avoid invalidating the backups referring to these

database files. The file will be truncated, but will not be physically deleted in order to keep

backups intact. For more information, see

backup and

ALTER DATABASE (Transact-SQL)

CREATE DATABASE

EVENTDATA (Transact-SQL)

sys.databases

## Examples

### Example 1

```sql
DECLARE
@
Out
AS
INT
;
EXECUTE sp_prepexec
@
Out
OUTPUT
, N
'@P1 nvarchar(128), @P2 nvarchar(100)'
,
N
'SELECT database_id, name
FROM sys.databases
WHERE name=@P1 AND state_desc = @P2'
,
@P1 =
'tempdb'
,
@P2 =
'ONLINE'
;
EXECUTE sp_unprepare @
Out
;
```

### Example 2

```sql
SELECT collation_name FROM sys.databases WHERE name = 'database_name';
```
