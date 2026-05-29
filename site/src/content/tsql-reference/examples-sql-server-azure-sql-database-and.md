---
name: 'Examples: SQL Server , Azure SQL Database, and'
title: 'Examples: SQL Server , Azure SQL Database, and'
category: 'operators'
description: 'In versions before SQL Server 2012 (11.x) Service Pack 1, the user must own the table or the'
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

## A. Return all statistics information

be a member of the

role.

In versions before SQL Server 2012 (11.x) Service Pack 1, the user must own the table or the

user must be a member of the

fixed server role, the

fixed database role, or

the

fixed database role. To change the behavior back to the pre SQL Server 2012

(11.x) Service Pack 1 behavior, use trace flag 9485.

In order to view the statistics object in Fabric Data Warehouse or the SQL analytics endpoint,

the user must have the

permission on the table, or a member of the Viewer Fabric

workspace role or higher role membership.

requires

permission on the table or membership in the

fixed server role, the

fixed database role, or the

fixed database role.

shows statistics stored in the

database at the Control node level.

It doesn't show statistics that are autocreated by SQL Server on the Compute nodes.

isn't supported on external tables.

In Warehouse in Microsoft Fabric,

only shows results for histogram

statistics, not

statistics.

SQL database in Fabric

### AdventureWorksPDW2022

## B. Specify the HISTOGRAM option

```sql
SELECT
```

```sql
DBCC SHOW_STATISTICS
```

```sql
SELECT
```

```sql
DBCC SHOW_STATISTICS
```

```sql
Shell
```

```sql
DBCC SHOW_STATISTICS
```

```sql
DBCC SHOW_STATISTICS
```

```sql
ACE-*
```
