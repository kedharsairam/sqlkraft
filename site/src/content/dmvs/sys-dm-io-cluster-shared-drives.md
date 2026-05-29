---
name: 'sys.dm_io_cluster_shared_drives'
title: 'sys.dm_io_cluster_shared_drives'
category: 'execution'
description: 'The user must have VIEW SERVER STATE permission for the SQL Server instance.'
pubDate: 2026-05-29
---

The user must have VIEW SERVER STATE permission for the SQL Server instance.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

The following example uses sys.dm_io_cluster_shared_drives to determine the shared drives on

a clustered server instance:

This is the result set:

DriveName

---------

m

n

sys.dm_io_cluster_valid_path_names (Transact-SQL)

sys.dm_os_cluster_nodes (Transact-SQL)

sys.fn_servershareddrives (Transact-SQL)

Dynamic Management Views and Functions (Transact-SQL)

This view will be deprecated in a future release. We recommend that you use

instead.

## sys.dm_pdw_nodes_io_pending_io_requests

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric


## Returns a row for each pending I/O request in SQL Server.
Memory address of the IO request. Is not nullable.

Type of pending I/O request. Is not nullable.

Internal use only. Is not nullable.

Indicates whether the I/O request is pending (1) or has

been completed by the operating system (0). An I/O

request can still be pending even when OS has

completed the request, but SQL Server has not yet

performed a context switch in which it would process

the I/O request and remove it from this list. Is not

nullable.

0 = Pending SQL Server

1 = Pending OS

Internal function to call when the I/O request is

completed. Is nullable.

Internal use only. Is nullable.

Scheduler on which this I/O request was issued. The

I/O request will appear on the pending I/O list of the

scheduler. For more information, see

sys.dm_os_schedulers (Transact-SQL)

. Is not nullable.

７

To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the

name

. This syntax is not supported by

serverless SQL pool in Azure Synapse Analytics.

ﾉ

## Basic

## S0

## S1

## elastic pools

```sql
SELECT * FROM sys.dm_io_cluster_shared_drives;
```
