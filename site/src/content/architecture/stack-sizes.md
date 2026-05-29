---
title: 'Stack sizes'
topic: 'query-processing'
description: 'Memory for thread stacks , CLR , extended procedure .dll files, the OLE DB providers'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Memory for thread stacks , CLR , extended procedure .dll files, the OLE DB providers

referenced by distributed queries, automation objects referenced in Transact-SQL statements,

and any memory allocated by a non SQL Server DLL, are

not

controlled by

.

Refer to

Server configuration: max worker threads

, for information on the calculated default

worker threads for a given number of affinitized CPUs in the current host. SQL Server stack

sizes are as follows:

SQL Server architecture

x86 (32-bit)

x86 (32-bit)

512 KB

x86 (32-bit)

x64 (64-bit)

768 KB

x64 (64-bit)

x64 (64-bit)

2,048 KB

IA64 (Itanium)

IA64 (Itanium)

4,096 KB

CLR memory is managed under

allocations starting with SQL Server

2012 (11.x).

SQL Server uses the memory notification API

to determine

when the SQL Server memory manager might allocate memory and release memory.

When SQL Server starts, it computes the size of virtual address space for the buffer pool based

on several parameters such as amount of physical memory on the system, number of server

threads and various startup parameters. SQL Server reserves the computed amount of its

process virtual address space for the buffer pool, but it acquires (commits) only the required

amount of physical memory for the current load.

The instance then continues to acquire memory as needed to support the workload. As more

users connect and run queries, SQL Server acquires more physical memory on demand. A SQL

Server instance continues to acquire physical memory until it either reaches its

allocation target or the OS indicates there's no longer an excess of free memory; it

frees memory when it's more than the min server memory setting, and the OS indicates that

there's a shortage of free memory.

As other applications are started on a computer running an instance of SQL Server, they

consume memory and the amount of free physical memory drops below the SQL Server target.

1

2

1

ﾉ

Expand table

2

```sql
max server memory
(MB)
```

```sql
max server memory (MB)
```

```sql
QueryMemoryResourceNotification
```

```sql
max server
memory (MB)
```
