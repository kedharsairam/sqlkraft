---
name: "sys.dm_exec_query_optimizer_info"
title: "sys.dm_exec_query_optimizer_info"
category: "execution"
description: "On Azure SQL Database service objectives, and for databases in Microsoft Entra admin account, or membership in the is required. On all other SQL Database service objectives, either the permission on the database, or membership in the server role is required. contains the following properties (counters). All occurrence values are cumulative and are set to at system restart."
tags: ["execution","dmv"]
pubDate: "2026-05-29"
syntax: "VIEW SERVER PERFORMANCE STATE"
---

## Description

On Azure SQL Database service objectives, and for databases in Microsoft Entra admin account, or membership in the is required. On all other SQL Database service objectives, either the permission on the database, or membership in the server role is required. contains the following properties (counters). All occurrence values are cumulative and are set to at system restart. All values for value fields are set to at system restart. All value-column values that specify an average use the occurrence value from the same row as the denominator in the calculation of the average. All query optimizations are measured when SQL Server determines changes to , including both user-generated and system-generated queries. Execution of an already-cached plan doesn't change values in only optimizations are significant.

## Syntax

```sql
VIEW SERVER PERFORMANCE STATE
```

## Permissions

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns detailed statistics about the operation of the SQL Server query optimizer. You can use this view when tuning a workload to identify query optimization problems or improvements. For example, you can use the total number of optimizations, the elapsed time value, and the final cost value to compare the query optimizations of the current workload and any changes observed during the tuning process. Some counters provide data that is relevant only for SQL Server internal diagnostic use. These counters are marked as "Internal only." Name of optimizer statistics event. Number of occurrences of optimization event for this counter. Average property value per event occurrence. The identifier for the node that this distribution is on. : Azure Synapse Analytics, Analytics Platform System (PDW) SQL Server 2019 (15.x) and earlier versions, and Azure SQL Managed Instance, require permission. SQL Server 2022 (16.x) and later versions, requires permission on the server. ７ To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the name. This syntax is not supported by serverless SQL pool in Azure Synapse Analytics. ﾉ

## Remarks

On Azure SQL Database

service objectives, and for databases in

elastic pools

server admin

account, the

Microsoft Entra admin

account, or membership in the

server role

is required. On all other SQL Database service

objectives, either the

permission on the database, or membership in the

server role is required.

contains the following properties (counters). All occurrence

values are cumulative and are set to

at system restart. All values for value fields are set to

at system restart. All value-column values that specify an average use the occurrence

value from the same row as the denominator in the calculation of the average. All query

optimizations are measured when SQL Server determines changes to

, including both user-generated and system-generated queries.

Execution of an already-cached plan doesn't change values in

only optimizations are significant.

Total number of optimizations.

Not applicable

Total number of optimizations.

Average elapsed time per optimization of

an individual statement (query), in

Total number of optimizations.

Average estimated cost for an optimized

plan in internal cost units.

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only

Internal only
