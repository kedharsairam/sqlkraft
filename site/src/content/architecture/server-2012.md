---
title: "Server 2012"
topic: "query-processing"
description: "Large columnstore index queries"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Large columnstore index queries

Large

batch mode on rowstore

queries

Columnstore index (re)builds, which use large volumes of memory to perform Hash and

Sort operations

Backup operations that require large memory buffers

Tracing operations that have to store large input parameters

Large memory grant requests

If you observe this behavior frequently, consider using

trace flag 8121

in SQL Server 2019 (15.x)

to allow the Resource Monitor to clean up more quickly. Starting with SQL Server 2022 (16.x),

this functionality is enabled by default, and the trace flag has no effect.

In older versions of SQL Server, the SQL Server memory manager set aside a part of the

process virtual address space (VAS) for use by the

,

,

memory allocations for

in the SQL Server process, and. This part of the virtual address space is also known as "Mem-To-Leave" or

"non-Buffer Pool" region.

The virtual address space that is reserved for these allocations is determined by the

configuration option. The default value that SQL Server uses is 256 MB.

Because the "any size" page allocator also handles allocations greater than 8 KB, the

value doesn't include the multi-page allocations. Except for this change,

everything else remains the same with this configuration option.

The following table indicates whether a specific type of memory allocation falls into the

region of the virtual address space for the SQL Server process:

2005 (9.x), SQL Server 2008

Single-page

allocations

No

No, consolidated into "any

size" page allocations

Multi-page

allocations

Yes

No, consolidated into "any

size" page allocations

CLR allocations

Yes

Yes

ﾉ

Expand table

### Server memory configuration options

`memory_to_reserve`

`memory_to_reserve`

`memory_to_reserve`
