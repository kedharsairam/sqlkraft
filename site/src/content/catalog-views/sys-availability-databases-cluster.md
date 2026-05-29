---
name: 'sys.availability_databases_cluster'
title: 'sys.availability_databases_cluster (Transact-'
category: 'databases-files'
description: 'Summarize this article for me'
tags: ["catalog-view", "databases-files"]
pubDate: 2026-05-29
---

SQL)

ﾃ

Summarize this article for me

Applies to:

SQL Server


## Returns one row for each availability database on the instance of SQL Server that hosts an
availability replica for any Always On availability group in the Windows Server Failover

Clustering (WSFC) cluster, regardless of whether the local copy database has been joined to the

availability group yet.


## Description
Unique identifier of the availability group in which the database

is participating.

NULL = database isn't part of an availability replica in an

availability group.

Unique identifier of the database within the availability group, if

any, in which the database is participating.

is

the same for this database on the primary replica and on every

secondary replica on which the database has been joined to the

availability group.

NULL = database isn't part of an availability replica in any

availability group.

Name of the database that was added to the availability group.

If the caller of

isn't the owner of the database, the minimum


## permissions required to see the corresponding row are ALTER ANY DATABASE or VIEW ANY
７

Note

When a database is added to an availability group, the primary database is automatically

joined to the group. Secondary databases must be prepared on each secondary replica

before they can be joined to the availability group.

ﾉ

Expand table

DATABASE server-level permission, or CREATE DATABASE permission in the

database.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

sys.availability_groups (Transact-SQL)

sys.databases (Transact-SQL)

sys.dm_hadr_database_replica_states (Transact-SQL)

sys.dm_hadr_database_replica_cluster_states (Transact-SQL)

What is an Always On availability group?

Last updated on 03/03/2026


## Permissions for SQL Server 2022 and later
Related content

```sql
group_id
```

```sql
group_database_id
```

```sql
group_database_id
```

```sql
database_name
```
