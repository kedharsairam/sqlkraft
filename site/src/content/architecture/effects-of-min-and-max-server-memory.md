---
title: "Effects of min and max server memory"
topic: "memory-management"
description: "The instance of SQL Server adjusts its memory consumption. If another application is stopped"
tags: ["memory-management", "architecture"]
pubDate: 2026-05-29
---

The instance of SQL Server adjusts its memory consumption. If another application is stopped

and more memory becomes available, the instance of SQL Server increases the size of its

memory allocation. SQL Server can free and acquire several megabytes of memory each

second, allowing it to quickly adjust to memory allocation changes.

The

min server memory

and

max server memory

configuration options establish upper and

lower limits to the amount of memory used by the buffer pool and other caches of the

Database Engine. The buffer pool doesn't immediately acquire the amount of memory

specified in min server memory. The buffer pool starts with only the memory required to

initialize. As the SQL Server Database Engine workload increases, it keeps acquiring the

memory required to support the workload. The buffer pool doesn't free any of the acquired

memory until it reaches the amount specified in min server memory. Once min server memory

is reached, the buffer pool then uses the standard algorithm to acquire and free memory as

needed. The only difference is that the buffer pool never drops its memory allocation below

the level specified in min server memory, and never acquires more memory than the level

specified in

.

The amount of memory acquired by the SQL Server Database Engine is entirely dependent on

the workload placed on the instance. A SQL Server instance that isn't processing many requests

might never reach the value specified by

.

If the same value is specified for both min server memory and

, then

once the memory allocated to the SQL Server Database Engine reaches that value, the SQL

Server Database Engine stops dynamically freeing and acquiring memory for the buffer pool.

If an instance of SQL Server is running on a computer where other applications are frequently

stopped or started, the allocation and deallocation of memory by the instance of SQL Server

can slow the startup times of other applications. Also, if SQL Server is one of several server

applications running on a single computer, the system administrators should control the

amount of memory allocated to SQL Server. In these cases, you can use the min server memory

and

options to control how much memory SQL Server can use. The

７

Note

SQL Server as a process acquires more memory than specified by

option. Both internal and external components can allocate memory outside of the buffer

pool, which consumes additional memory, but the memory allocated to the buffer pool

usually still represents the largest portion of memory consumed by SQL Server.

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
