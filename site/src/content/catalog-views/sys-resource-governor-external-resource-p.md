---
name: 'sys.resource_governor_external_resource_p'
title: 'sys.resource_governor_external_resource_p'
category: 'external'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["catalog-view", "external"]
pubDate: 2026-05-29
---

Article

•

02/11/2025

Applies to:

SQL Server 2016 (13.x) and later versions

Applies to:

SQL Server 2016 (13.x) R Services (In-Database) and SQL Server 2017 (14.x) Machine

Learning Services


## Returns the stored external resource pool configuration in SQL Server. Each row of the view
determines the configuration of a pool.


## Description
Unique ID of the resource pool. Not nullable.

Name of the resource pool. Not nullable.

Maximum average CPU bandwidth allowed for all requests in the

resource pool when there is CPU contention. Not nullable.

Percentage of total server memory that can be used by requests in this

resource pool. Not nullable. The effective maximum depends on the

pool minimums. For example, max_memory_percent can be set to 100,

but the effective maximum is lower.

Maximum number of concurrent external processes. The default value,

0, specifies no limit. Not nullable.

Internal version number.

Requires the

permission.

Resource governance for machine learning in SQL Server

Resource governor Catalog Views

(Transact-SQL)

sys.dm_resource_governor_resource_pools (Transact-SQL)

Resource governor

sys.dm_resource_governor_resource_pool_affinity (Transact-SQL)

external scripts enabled

Server Configuration Option

ALTER EXTERNAL RESOURCE POOL (Transact-SQL)

ﾉ

Expand table

Related content

```sql
external_pool_id
```

```sql
name
```

```sql
max_cpu_percent
```

```sql
max_memory_percent
```

```sql
max_processes
```

```sql
version
```

```sql
VIEW SERVER STATE
```
