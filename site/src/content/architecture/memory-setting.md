---
title: "memory setting"
topic: "memory-management"
description: ""
tags: ["memory-management","architecture"]
pubDate: "2026-05-29"
---

The following table indicates whether a specific type of memory allocation is controlled by the

and

configuration options:

2005 (9.x), SQL Server 2008

Single-page

allocations

Yes

Yes, consolidated into "any

size" page allocations

Multi-page

allocations

No

Yes, consolidated into "any

size" page allocations

CLR allocations

No

Yes

Thread stacks

memory

No

No

Direct allocations

from Windows

No

No

Starting with SQL Server 2012 (11.x), SQL Server might allocate more memory than the value

specified in the

setting. This behavior can occur when the

value has already reached the

setting, as specified

by. If there's insufficient contiguous free memory to meet the demand

of multi-page memory requests (more than 8 KB) because of memory fragmentation, SQL

Server can perform over-commitment instead of rejecting the memory request.

As soon as this allocation is performed, the Resource Monitor background task starts to signal

all memory consumers to release the allocated memory, and tries to bring the

value below the

specification. Therefore, SQL Server

memory usage could briefly exceed the

setting. In this situation, the

performance counter reading exceeds the

and

settings.

This behavior is typically observed during the following operations:

32-bit and 64-bit versions of SQL Server 2012 (11.x) and SQL Server 2014 (12.x), and 64-bit

versions of SQL Server 2016 (13.x) and later versions.

ﾉ

Expand table

might commit memory over the max server

### Multi-Page Allocator (MPA)

### CLR Allocator

### thread stacks

### Direct Windows

### allocations (DWA)

```sql
max server memory (MB)
```

```sql
min server memory (MB)
```

```sql
max server memory (MB)
```

```sql
max server memory (MB)
```

```sql
max server memory (MB)
```

```sql
max server memory (MB)
```
