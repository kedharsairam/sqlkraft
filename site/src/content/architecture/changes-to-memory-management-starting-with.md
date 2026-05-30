---
title: "Changes to memory management starting with"
topic: "memory-management"
description: "In older versions of SQL Server, memory allocation was done using five different mechanisms:"
tags: ["memory-management", "architecture"]
pubDate: 2026-05-29
---

Output

In older versions of SQL Server, memory allocation was done using five different mechanisms:

, including only memory allocations that were less than, or

equal to 8 KB in the SQL Server process. The

and

configuration options determined the limits of physical memory that the SPA

consumed. The Buffer Pool was simultaneously the mechanism for SPA, and the largest

consumer of single-page allocations.

, for memory allocations that request more than 8 KB.

, including the SQL CLR heaps and its global allocations that are created

during CLR initialization.

Memory allocations for

in the SQL Server process.

, for memory allocation requests made directly to

Windows. These include Windows heap usage and direct virtual allocations made by

modules that are loaded into the SQL Server process. Examples of such memory

allocation requests include allocations from extended stored procedure DLLs, objects that

are created by using Automation procedures (

calls), and allocations from linked

server providers.

Starting with SQL Server 2012 (11.x), Single-Page allocations, Multi-Page allocations and CLR

allocations are all consolidated into an

, and included in memory

limits controlled by

and

configuration

options. This change provided a more accurate sizing ability for all memory requirements that

go through the SQL Server memory manager.

SQL Server 2012

）

Important

Carefully review your current

and

configurations after you upgrade to SQL Server 2012 (11.x) and later versions. This is

because starting in SQL Server 2012 (11.x), such configurations now include and account

for more memory allocations compared to earlier versions. These changes apply to both

### Total Server

### Memory (KB)

### Target Server Memory (KB)

### Total Server

### Memory (KB)

### Target Server Memory (KB)

### Total Server Memory (KB)

### Target Server Memory (KB)

```sql
max server memory (MB)
```

```sql
min server
memory (MB)
```

```sql
sp_OA
```

```sql
max server memory (MB)
```

```sql
min server memory (MB)
```

```sql
A significant part of SQL Server process memory has been paged out. This may result
in a performance degradation. Duration: #### seconds. Working set (KB): ####,
committed (KB): ####, memory utilization: ##%.
```

```sql
max server memory (MB)
```

```sql
min server memory (MB)
```
