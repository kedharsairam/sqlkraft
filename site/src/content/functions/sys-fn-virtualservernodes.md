---
name: 'sys.fn_virtualservernodes'
title: 'sys.fn_virtualservernodes'
category: 'system'
description: 'Azure SQL Managed Instance'
tags: ["function"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Managed Instance

Analytics Platform System

(PDW)


## Returns a list of failover clustered instance nodes on which an instance of SQL Server can run.
This information is useful in failover clustering environments.

Transact-SQL syntax conventions

If the current server is a clustered server,


## returns a list of failover
clustered instance nodes on which this instance of SQL Server has been defined.

If the current server instance is not a clustered server,


## returns an empty
rowset.

The user must have VIEW SERVER STATE permission for the instance of SQL Server.

The following example uses

to query on a clustered server instance:

）

Important

This Microsoft SQL Server 2012 (11.x) system function is included for backward

compatibility. We recommend that you use

instead.

Here's the result set.

NodeName

--------

SS3-CLUSN1

SS3-CLUSN2

sys.dm_os_cluster_nodes (Transact-SQL)

sys.fn_servershareddrives (Transact-SQL)

See Also

```sql
fn_virtualservernodes
```

```sql
fn_virtualservernodes()
```

```sql
SELECT * FROM fn_virtualservernodes();
```
