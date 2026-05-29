---
name: 'sys.dm_os_threads'
title: 'sys.dm_os_threads'
category: 'execution'
description: 'On SQL Server and SQL Managed Instance, requires'
pubDate: 2026-05-29
---

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

Due to how the SQL engine works in Linux, some of this information doesn't match Linux

diagnostics data. For example,

does not match the result of tools like

,

or

the procfs (/proc/

). This is due the Platform Abstraction Layer (SQLPAL), a layer between

SQL Server components and the operating system.

Upon startup, SQL Server starts threads and then associates workers with those threads.

However, external components, such as an extended stored procedure, can start threads under

the SQL Server process. SQL Server has no control of these threads. sys.dm_os_threads can

provide information about rogue threads that consume resources in the SQL Server process.

The following query is used to find workers, along with time used for execution, that are

running threads not started by SQL Server.

７

For conciseness, the following query uses an asterisk (

) in the

statement. You

should avoid using the asterisk (*), especially against catalog views, dynamic management

views, and system table-valued functions. Future upgrades and releases of Microsoft SQL

Server may add columns and change the order of columns to these views and functions.

These changes might break applications that expect a particular order and number of

columns.

sys.dm_os_workers (Transact-SQL)

SQL Server Operating System Related Dynamic Management Views (Transact-SQL)

Last updated on 11/18/2025

## VirtualQuery

## sys.dm_pdw_nodes_os_virtual_address_dump

Article

•

02/28/2023

SQL Server

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)


## Returns information about a range of pages in the virtual address space of the calling process.
Pointer to the base address of the region of pages. Is

not nullable.

Pointer to the base address of a range of pages

allocated by the VirtualAlloc Windows API function. The

page pointed to by the BaseAddress member is

contained within this allocation range. Is not nullable.

Protection attributes when the region was first

allocated. The value is one of the following:

- PAGE_READONLY

- PAGE_READWRITE

- PAGE_NOACCESS

- PAGE_WRITECOPY

- PAGE_EXECUTE

- PAGE_EXECUTE_READ

- PAGE_EXECUTE_READWRITE

- PAGE_EXECUTE_WRITECOPY

- PAGE_GUARD

- PAGE_NOCACHE

７

This information is also returned by the

Windows API.

７

To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the

name

. This syntax is not supported by

serverless SQL pool in Azure Synapse Analytics.

ﾉ

Is not nullable.

Size of the region, in bytes, starting at the base address

in which all the pages have the same attributes. Is not

nullable.

Current state of the region. This is one of the following:

- MEM_COMMIT

- MEM_RESERVE

- MEM_FREE

Is not nullable.

Protection attributes. The value is one of the following:

- PAGE_READONLY

- PAGE_READWRITE

- PAGE_NOACCESS

- PAGE_WRITECOPY

- PAGE_EXECUTE

- PAGE_EXECUTE_READ

- PAGE_EXECUTE_READWRITE

- PAGE_EXECUTE_WRITECOPY

- PAGE_GUARD

- PAGE_NOCACHE

Is not nullable.

Identifies the types of pages in the region. The value

can be one of the following:

- MEM_PRIVATE

- MEM_MAPPED

- MEM_IMAGE

Is not nullable.

: Azure Synapse Analytics, Analytics Platform

System (PDW)

The identifier for the node that this distribution is on.

Requires VIEW SERVER STATE permission on the server.

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
os_thread_id
```

```sql
ps
```

```sql
top
```

```sql
pid
```

```sql
*
```

```sql
SELECT
```

```sql
SELECT *
FROM sys.dm_os_threads
WHERE started_by_sqlservr = 0;
```
