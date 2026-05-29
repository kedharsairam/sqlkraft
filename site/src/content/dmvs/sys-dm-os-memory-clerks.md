---
name: 'sys.dm_os_memory_clerks'
title: 'sys.dm_os_memory_clerks'
category: 'execution'
description: '## sys.dm_pdw_nodes_os_hosts'
pubDate: 2026-05-29
---

## sys.dm_pdw_nodes_os_hosts

Article

•

11/25/2024

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)


## Returns all the hosts currently registered in an instance of SQL Server. This view also returns the
resources that are used by these hosts.

Internal memory address of the host object.

Type of hosted component. For example,

SOSHOST_CLIENTID_SERVERSNI= SQL Server Native

Interface

SOSHOST_CLIENTID_SQLOLEDB = SQL Server Native

Client OLE DB Provider

SOSHOST_CLIENTID_MSDART = Microsoft Data Access

Run Time

Name of the host.

Total number of tasks that this host has placed onto

queues in SQL Server.

Number of currently running tasks that this host has

placed onto queues.

Total number of I/Os issued and completed through this

host.

Total byte count of the I/Os completed through this

host.

７

To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the

name

. This syntax is not supported by serverless SQL pool in

Azure Synapse Analytics.

ﾉ

## Basic

## S0

## S1

## elastic pools

Total number of I/O requests related to this host that

are currently waiting to complete.

Memory address of the memory clerk object associated

with this host. For more information, see

sys.dm_os_memory_clerks (Transact-SQL)

.

: Azure Synapse Analytics, Analytics Platform

System (PDW)

The identifier for the node that this distribution is on.

On SQL Server and SQL Managed Instance, requires

permission.

On SQL Database

,

, and

service objectives, and for databases in

, the

server admin

account, the

Microsoft Entra admin

account, or membership in the

server role

is required. On all other SQL Database service objectives,

either the

permission on the database, or membership in the

server role is required.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

SQL Server allows components, such as an OLE DB provider, that are not part of the SQL Server

executable to allocate memory and participate in non-preemptive scheduling. These

components are hosted by SQL Server, and all resources allocated by these components are

tracked. Hosting allows SQL Server to better account for resources used by components

external to the SQL Server executable.

ﾉ

sys.dm_os_hosts.

default_memory_clerk_address

sys.dm_os_memory_clerks.

memory_clerk_address

one to one

sys.dm_os_hosts. host_address

sys.dm_os_memory_clerks. host_address

one to one

The following example determines the total amount of memory committed by a hosted

component.

: SQL Server 2012 (11.x) and later.

sys.dm_os_memory_clerks (Transact-SQL)

SQL Server Operating System Related Dynamic Management Views (Transact-SQL)

ﾉ

## Basic

## S0

## S1

## elastic pools

## sys.dm_pdw_nodes_os_latch_stats

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric


## Returns information about all latch waits organized by class.
latch_class

Name of the latch class.

waiting_requests_count

Number of waits on latches in this class. This counter is

incremented at the start of a latch wait.

wait_time_ms

Total wait time, in milliseconds, on latches in this class.

This column is updated every five minutes during a latch

wait and at the end of a latch wait.

max_wait_time_ms

Maximum time a memory object has waited on this latch. If this

value is unusually high, it might indicate an internal deadlock.

pdw_node_id

: Azure Synapse Analytics, Analytics Platform System

(PDW)

The identifier for the node that this distribution is on.

On SQL Server and SQL Managed Instance, requires

permission.

On SQL Database

,

, and

service objectives, and for databases in

, the

server admin

account, the

Microsoft Entra admin

account, or membership in the

server role

is required. On all other SQL Database service objectives,

７

To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the

name

. This syntax is not supported by serverless SQL

pool in Azure Synapse Analytics.

ﾉ

```sql
VIEW SERVER STATE
```

```sql
##MS_ServerStateReader##
```

```sql
VIEW DATABASE STATE
```

```sql
##MS_ServerStateReader##
```

```sql
SELECT h.type, SUM(mc.pages_kb) AS committed_memory
FROM sys.dm_os_memory_clerks AS mc
INNER JOIN sys.dm_os_hosts AS h
ON mc.memory_clerk_address = h.default_memory_clerk_address
GROUP BY h.type;
```

```sql
VIEW SERVER STATE
```

```sql
##MS_ServerStateReader##
```
