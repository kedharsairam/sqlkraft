---
title: "Options and workarounds"
topic: "io-fundamentals"
description: "In the previous example, the most interesting stacks have the highest slot counts (35,668 and"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

In the previous example, the most interesting stacks have the highest slot counts (35,668 and

8,506), which, in fact, have a slot count greater than 1,000.

Now the question might be, "what do I do with this information"? In general, deep knowledge

of the SQL Server engine is required to make use of the callstack information and so at this

point the troubleshooting process moves into a gray area. In this particular case, by looking at

the call stacks, we can see that the code path where the issue occurs is related to security and

metadata lookups (As evident by the following stack frames

.

In isolation, it's difficult to use this information to resolve the problem but it does give us some

ideas where to focus additional troubleshooting to isolate the issue further.

Because this issue looked to be related to code paths that perform security-related checks, we

decided to run a test in which the application user connecting to the database was granted

privileges. While this technique is never recommended in a production environment,

in our test environment it proved to be a useful troubleshooting step. When the sessions were

run using elevated privileges (

), the CPU spikes related to contention disappeared.

Clearly, troubleshooting spinlock contention can be a non-trivial task. There's no "one common

best approach". The first step in troubleshooting and resolving any performance problem is to

identify the root cause. Using the techniques and tools described in this article is the first step

in performing the analysis needed to understand the spinlock-related contention points.

As new versions of SQL Server are developed, the engine continues to improve scalability by

implementing code that is better optimized for high concurrency systems. SQL Server has

introduced many optimizations for high concurrency systems, one of which being exponential

backoff for the most common contention points. There are enhancements starting in SQL

Server 2012 that specifically improved this particular area by leveraging exponential backoff

algorithms for all spinlocks within the engine.

When designing high end applications that need extreme performance and scale, consider how

to keep the code path needed within SQL Server as short as possible. A shorter code path

means less work is performed by the database engine and will naturally avoid contention

points. Many best practices have a side effect of reducing the amount of work required of the

engine, and hence, result optimizing workload performance.

Taking a couple best practices from earlier in this article as examples:

Fully qualifying names of all objects will result in removing the

need for SQL Server to execute code paths that are required to resolve names. We have

### Parameterized Queries:

### Contention:

```sql
CMEDCatalogOwner::GetProxyOwnerBySID & CMEDProxyDatabase::GetOwnerBySID)
```

`sysadmin`

`sysadmin`
