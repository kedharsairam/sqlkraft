---
name: 'sys.databases'
title: 'sys.databases'
category: 'databases-files'
description: 'For a full list of compatibility levels, see'
tags: ["catalog-view", "databases-files"]
pubDate: 2026-05-29
---

## A. Query the

## sys.databases

## view

For a full list of compatibility levels, see

ALTER DATABASE compatibility level

.

If the caller of

isn't the owner of the database and the database isn't

or

, the minimum permissions required to see the corresponding row are

or the

server-level permission, or

permission in the

database. The database to which the caller is connected can always be viewed in

.

In Azure SQL Database this view is available in the

database and in user databases. In the

database, this view returns the information on the

database and all user

databases on the server. In a user database, this view returns information only on the current

database and the

database.

Due to possible metadata synchronization, the

view might provide incorrect

information regarding database encryption. To ensure accurate results, we recommend you use

the

sys.dm_database_encryption_keys

view to obtain the actual encryption status.

Use the

view in the

database of the Azure SQL Database server where the

new database is being created. After the database copy starts, you can query the

and

views from the

database of the destination server to retrieve

more information about the copying progress.

The following example returns a few of the columns available in the

view.

1

）

Important

By default, the

fixed role has the

permission, allowing all logins to

see database information.

To block a login from the ability to detect a database,

the

permission from

, or

the

permission for individual logins.

## B. Check the copying status in Azure SQL Database

## C. Check the temporal retention policy status in SQL Database

SQL

The following example queries the

and

views to return

information about a database copy operation.

: Azure SQL Database

SQL

The following example queries the

to return information whether temporal

retention cleanup task is enabled. After the restore operation, temporal retention is disabled by

default. Use

to enable it explicitly.

: Azure SQL Database

SQL

Related content

ALTER DATABASE (Transact-SQL)

ALTER DATABASE (Transact-SQL) compatibility level

sys.database_mirroring_witnesses (Transact-SQL)

sys.database_recovery_status (Transact-SQL)

Databases and Files Catalog Views (Transact-SQL)

sys.dm_database_copies (Azure SQL Database)

Last updated on 04/27/2026

```sql
sys.databases
```

```sql
master
```

```sql
tempdb
```

```sql
ALTER ANY DATABASE
```

```sql
VIEW ANY DATABASE
```

```sql
CREATE DATABASE
```

```sql
master
```

```sql
sys.databases
```

```sql
master
```

```sql
master
```

```sql
master
```

```sql
master
```

```sql
sys.databases
```

```sql
sys.databases
```

```sql
master
```

```sql
sys.databases
```

```sql
sys.dm_database_copies
```

```sql
master
```

```sql
sys.databases
```

```sql
VIEW ANY DATABASE
```

```sql
REVOKE
```

```sql
VIEW ANY DATABASE
```

```sql
public
```

```sql
DENY
```

```sql
VIEW ANY DATABASE
```

```sql
sys.databases
```

```sql
sys.dm_database_copies
```

```sql
sys.databases
```

```sql
ALTER DATABASE
```

```sql
SELECT
name
,
user_access_desc,
is_read_only,
state_desc,
recovery_model_desc
FROM
sys.databases;
```

```sql
-- Execute from the master database.
SELECT
a.name,
a.state_desc,
b.start_date,
b.modify_date,
b.percent_complete
FROM
sys.databases
AS
a
INNER
JOIN
sys.dm_database_copies
AS
b
ON
a.database_id = b.database_id
WHERE
a.state = 7;
```

```sql
-- Execute from the master database.
SELECT
a.name,
a.is_temporal_history_retention_enabled
FROM
sys.databases
AS
a;
```
