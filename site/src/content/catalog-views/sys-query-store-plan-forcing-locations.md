---
name: 'sys.query_store_plan_forcing_locations'
title: 'sys.query_store_plan_forcing_locations'
category: 'query-store'
description: 'SQL Server 2025 (17.x)'
tags: ["catalog-view", "query-store"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2025 (17.x)

Azure SQL Database

Contains information about Query Store plans that have been forced on secondary replicas

using

sp_query_store_force_plan

, when Query Store for secondary replicas is enabled. You can

use this information to determine what queries have plans forced on different replica sets.

Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later

versions, and in Azure SQL Database. For complete platform support, see

Query Store for

secondary replicas

.


## Description
System-assigned ID for this plan forcing location.

References

in

sys.query_store_query

References

in

sys.query_store_plan

From the parameter

in

sp_query_store_force_plan (Transact-SQL)

. References

in

sys.query_store_replicas

Requires the

permission.

Use

, joined with

sys.query_store_replicas

, to retrieve

Query Store plans forced on all secondary replicas

.

SQL

ﾉ

Expand table

sys.query_store_replicas (Transact-SQL)

sys.sp_query_store_force_plan (Transact-SQL)

sys.database_query_store_internal_state (Transact-SQL)

sys.query_store_plan (Transact-SQL)

sys.query_store_query (Transact-SQL)

Monitoring Performance By Using the Query Store


## Best Practice with the Query Store
Last updated on 11/18/2025

Related content

```sql
plan_forcing_location_id
```

```sql
query_id
```

```sql
query_id
```

```sql
plan_id
```

```sql
plan_id
```

```sql
replica_group_id
```

```sql
force_plan_scope
```

```sql
replica_group_id
```

```sql
VIEW DATABASE STATE
```

```sql
sys.query_store_plan_forcing_locations
```

```sql
SELECT
query_plan
FROM
sys.query_store_plan
AS
qsp
INNER
JOIN
sys.query_store_plan_forcing_locations
AS
pfl
ON
pfl.query_id = qsp.query_id
INNER
JOIN
sys.query_store_replicas
AS
qsr
```

```sql
ON
qsr.replica_group_id = qsp.replica_group_id
WHERE
qsr.replica_name =
'yourSecondaryReplicaName'
;
```
