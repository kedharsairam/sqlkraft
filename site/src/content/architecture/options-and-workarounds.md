---
title: "Options and workarounds"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

In the previous example, the most interesting stacks have the highest slot counts (35,668 and

8,506), which, in fact, have a slot count greater than 1,000.

Now the question might be, "what do I do with this information"? In general, deep knowledge

of the SQL Server engine is required to make use of the callstack information and so at this

point the troubleshooting process moves into a gray area. In this particular case, by looking at

the call stacks, we can see that the code path where the issue occurs is related to security and

metadata lookups (As evident by the following stack frames.

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

in performing the analysis needed to understand the spinlock-
### Parameterized Queries:

### Contention:

```sql
CMEDCatalogOwner::GetProxyOwnerBySID & CMEDProxyDatabase::GetOwnerBySID)
```

`sysadmin`

`sysadmin`
