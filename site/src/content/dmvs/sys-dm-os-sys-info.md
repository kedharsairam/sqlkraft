---
name: 'sys.dm_os_sys_info'
title: 'sys.dm_os_sys_info'
category: 'execution'
description: 'base value is the performance counter'
pubDate: 2026-05-29
---

base value is the performance counter

where the

column value is 1073939712.

Data in the

DMV is not persisted after the database engine

restarts. Use the

column in

sys.dm_os_sys_info

to find the last database

engine startup time.

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

The following example returns all performance counters that display snapshot counter values.

SQL

SQL Server Operating System Related Dynamic Management Views (Transact-SQL)

sys.sysperfinfo (Transact-SQL)

sys.dm_os_sys_info (Transact-SQL)

Last updated on 11/18/2025

## total_virtual_address_space_reserved_kb

## virtual_memory_in_bytes

## sys.dm_os_sys_info

## sys.dm_pdw_nodes_os_process_memory

Article

•

12/18/2023

SQL Server

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

Most memory allocations that are attributed to the SQL Server process space are controlled

through interfaces that allow for tracking and accounting of those allocations. However,

memory allocations might be performed in the SQL Server address space that bypasses

internal memory management routines. Values are obtained through calls to the base

operating system. They are not manipulated by methods internal to SQL Server, except when it

adjusts for locked or large page allocations.

All returned values that indicate memory sizes are shown in kilobytes (KB). The column

is a duplicate of

from

.

The following table provides a complete picture of the process address space.

Indicates the process working set in KB, as reported by

operating system, as well as tracked allocations by

using large page APIs. Not nullable.

Specifies physical memory allocated by using large

page APIs. Not nullable.

Specifies memory pages locked in memory. Not

nullable.

Indicates the total size of the user mode part of the

virtual address space. Not nullable.

Indicates the total amount of virtual address space

reserved by the process. Not nullable.

７

To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the

name

. This syntax is not supported by serverless

SQL pool in Azure Synapse Analytics.

ﾉ

## Basic

## S0

## S1

## elastic pools

```sql
Locks:Average Wait Time Base
```

```sql
cntr_type
```

```sql
sys.dm_os_performance_counters
```

```sql
sqlserver_start_time
```

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
SELECT
object_name, counter_name, instance_name, cntr_value, cntr_type
FROM
sys.dm_os_performance_counters
WHERE
cntr_type = 65792
OR
cntr_type = 272696320
OR
cntr_type = 537003264;
```
