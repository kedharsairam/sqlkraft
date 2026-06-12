---
title: "Dynamic memory management"
topic: "memory-management"
description: "2005 (9.x), SQL Server 2008"
tags: ["memory-management","architecture"]
pubDate: 2026-05-29
---

2005 (9.x), SQL Server 2008

Thread stacks

memory

Yes

Yes

Direct allocations

from Windows

Yes

Yes

The default memory management behavior of the SQL Server Database Engine is to acquire as

much memory as it needs without creating a memory shortage on the system. The SQL Server

Database Engine does this by using the Memory Notification APIs in Microsoft Windows.

When SQL Server is using memory dynamically, it queries the system periodically to determine

the amount of free memory. Maintaining this free memory prevents the operating system (OS)

from paging. If less memory is free, SQL Server releases memory to the OS. If more memory is

free, SQL Server can allocate more memory. SQL Server adds memory only when its workload

requires more memory; a server at rest doesn't increase the size of its virtual address space. If

you notice that Task Manager and Performance Monitor show a steady decrease in available

memory when SQL Server is using dynamic memory management, this is the default behavior

and shouldn't be perceived as a memory leak.

controls the SQL Server memory allocation, compile

memory, all caches (including the buffer pool),

query execution memory grants

,

lock manager

memory

, and CLR

memory (essentially any memory clerk found in

sys.dm_os_memory_clerks

).

CLR memory is managed under

allocations starting with SQL Server

2012 (11.x).

The following query returns information about currently allocated memory:

1

1

```sql
max server memory (MB)
```

```sql
SELECT physical_memory_in_use_kb / 1024
AS sql_physical_memory_in_use_MB,
large_page_allocations_kb / 1024
AS sql_large_page_allocations_MB,
locked_page_allocations_kb / 1024
AS sql_locked_page_allocations_MB,
virtual_address_space_reserved_kb / 1024
AS sql_VAS_reserved_MB,
virtual_address_space_committed_kb / 1024
AS sql_VAS_committed_MB,
virtual_address_space_available_kb / 1024
AS sql_VAS_available_MB,
page_fault_count
AS sql_page_fault_count,
memory_utilization_percentage
AS sql_memory_utilization_percentage,
process_physical_memory_low
AS sql_process_physical_memory_low,
process_virtual_memory_low
AS sql_process_virtual_memory_low
FROM sys.dm_os_process_memory;
```
