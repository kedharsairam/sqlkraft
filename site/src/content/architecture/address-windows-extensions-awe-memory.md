---
title: "Address Windows Extensions (AWE) memory"
topic: "memory-management"
description: "grow."
tags: ["memory-management", "architecture"]
pubDate: 2026-05-29
---

grow. To resolve this problem, add physical memory, or tune the queries to use a different and

faster query plan.

All SQL Server editions support conventional memory on 64-bit platform. The SQL Server

process can access virtual address space up to operating system maximum on x64 architecture.

With IA64 architecture, the limit was 7 TB (IA64 not supported in SQL Server 2012 (11.x) and

later versions).

For more information, see

Memory Limits for Windows

.

By using

Address Windowing Extensions

(AWE) and the

Lock pages in memory

(LPIM) privilege

required by AWE, you can keep most of SQL Server process memory

locked

in physical RAM

under low virtual memory conditions. This happens in both 32-bit and 64-bit AWE allocations.

The locking of memory occurs because AWE memory doesn't go through the Virtual Memory

Manager in Windows, which controls paging of memory. The AWE memory allocation API

requires the

Lock pages in memory

(SeLockMemoryPrivilege) privilege; see

AllocateUserPhysicalPages notes

. Therefore, the main benefit of using the AWE API is to keep

most of the memory resident in RAM if there's memory pressure on the system. For

information on how to allow SQL Server to use AWE, see

Enable the Lock pages in memory

option (Windows)

.

If LPIM is granted, we strongly recommend that you set

to a specific

value, rather than leaving the default of 2,147,483,647 megabytes (MB). For more information,

see

Server memory configuration options: Set options manually

and

Lock pages in memory

(LPIM)

.

If LPIM isn't enabled, SQL Server switches to using conventional memory and in cases of OS

memory exhaustion, and the

MSSQLSERVER_17890

error might be reported in the error log.

The error resembles the following example:

７

Note

Starting with SQL Server 2025 (17.x), SQL Server Standard edition supports up to 256 GB.

In SQL Server 2022 (16.x) and earlier versions, SQL Server Standard edition supports up to

128 GB.

### Single-Page Allocator (SPA)

### Multi-Page Allocator (MPA)

### CLR Allocator

### thread stacks

### Direct Windows allocations (DWA)

### "Any size" Page Allocator

```sql
max server memory (MB)
```
