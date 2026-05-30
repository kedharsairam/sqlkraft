---
title: "Best practices"
topic: "query-processing"
description: "object that appears in"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Any

object that appears in

sys.all_objects

or any securable listed in

the database or schema-scoped

securable list

.

Specified

database

Any

permission

to securable contained by database or schema.

Specified

database

(

)

SQL Server

instance

Specified

database

Performance issues, such as high CPU usage and increased memory consumption, can be

caused by excessive entries in the TokenAndPermUserStore cache. By default, SQL Server only

cleans up entries in this cache when it detects internal memory pressure. However, on servers

with plenty of RAM, internal memory pressure might not occur frequently. As the cache grows,

the time required to search for existing entries to reuse increases. This cache is managed by a

spinlock, allowing only one thread to perform the search at a time. Consequently, this behavior

can lead to decreased query performance and higher CPU usage.

SQL Server provides two trace flags (TF) that can be used to set a quota for the

TokenAndPermUserStore cache. By default, there's no quota, meaning the cache can hold an

unlimited number of entries.

TF 4618: Limits the number of entries in the TokenAndPermUserStore to 1024.

TF 4618 and TF 4610: Limits the number of entries in the TokenAndPermUserStore to

8192. If the low entry count limit of TF 4618 causes other performance issues, it's

recommended to use trace flags 4610 and 4618 together. For more information, see

DBCC TRACEON - Trace Flags (Transact-SQL)

.

For more information, you can refer to the article

Performance issues can be caused by

excessive entries in the TokenAndPermUserStore cache - SQL Server

This section lists best practices to optimize security workflow.

`DROP`

```sql
GRANT/DENY/REVOKE
```

```sql
CREATE/ALTER/DROP
LOGIN
```

`SERVICE`

```sql
MASTER KEY
```

```sql
ALTER
DATABASE
```
