---
title: "Use of the lightweight pooling option"
topic: "io-fundamentals"
description: "affinity mask option"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

### fiber mode

The

affinity mask option

is set by using

ALTER SERVER CONFIGURATION

. When the affinity

mask isn't set, the instance of SQL Server allocates worker threads evenly among the

schedulers that haven't been masked off.

Thread pooling helps optimize performance when large numbers of clients are connected to

the server. Usually, a separate operating system thread is created for each query request.

However, with hundreds of connections to the server, using one thread per query request can

consume large amounts of system resources. The

max worker threads option

enables SQL

Server to create a pool of worker threads to service a larger number of query requests, which

improves performance.

The overhead involved in switching thread contexts may not be very large. Most instances of

SQL Server don't see any performance differences between setting the

option to 0 or 1. The only instances of SQL Server that might benefit from

lightweight pooling

are those that run on a computer having the following characteristics:

A large multi-CPU server

All the CPUs are running near maximum capacity

There is a high level of context switching

These systems may see a small increase in performance if the lightweight pooling value is set

to 1.

Ｕ

Caution

Do not configure CPU affinity in the operating system and also configure the affinity mask

in SQL Server. These settings are attempting to achieve the same result, and if the

configurations are inconsistent, you may have unpredictable results. For more information,

see

.

）

Important

Starting with SQL Server 2025 (17.x), the

feature enabled by the

option is deprecated, and is planned for removal in a future version of SQL Server.

Because of known stability and compatibility issues, Microsoft recommends that you avoid

using this feature in any version of SQL Server.

）

Important

### lightweight

### pooling

```sql
lightweight pooling
```
