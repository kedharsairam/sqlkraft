---
name: 'sys.query_store_plan'
title: 'sys.query_store_plan'
category: 'query-store'
description: '## A. Find the reason SQL Server couldn''t force a plan via QDS'
tags: ["catalog-view", "query-store"]
pubDate: 2026-05-29
---

## A. Find the reason SQL Server couldn't force a plan via QDS

Second, when objects that plan relies on, are no longer available:

Database (if database, where plan originated, doesn't exist anymore)

Index (no longer there or disabled)

Finally, problems with the plan itself:

Not legal for query

Query Optimizer exceeded number of allowed operations

Incorrectly formed plan XML

Requires the

permission.

Pay attention to the

and

columns:

SQL

Azure SQL Database and SQL Server 2019 and later build versions support plan forcing for

static and fast forward cursors.

## B. Query to view query plan results in Azure Synapse Analytics

Use the following sample query to find the 100 most recent execution plans in the Query Store

in Azure Synapse Analytics.

SQL

Monitor performance by using the Query Store

sys.database_query_store_options (Transact-SQL)

sys.query_context_settings (Transact-SQL)

sys.query_store_query (Transact-SQL)

sys.query_store_query_text (Transact-SQL)

sys.query_store_runtime_stats (Transact-SQL)

sys.query_store_wait_stats (Transact-SQL)

sys.query_store_runtime_stats_interval (Transact-SQL)

Related content

System catalog views (Transact-SQL)

Query Store stored procedures (Transact-SQL)

Last updated on 11/18/2025

```sql
VIEW DATABASE STATE
```

```sql
last_force_failure_reason_desc
```

```sql
force_failure_count
```

```sql
SELECT
TOP 1000
p.query_id,
p.plan_id,
p.last_force_failure_reason_desc,
p.force_failure_count,
p.last_compile_start_time,
p.last_execution_time,
q.last_bind_duration,
q.query_parameterization_type_desc,
q.context_settings_id,
c.set_options,
c.STATUS
FROM
sys.query_store_plan p
INNER
JOIN
sys.query_store_query q
ON
p.query_id = q.query_id
INNER
JOIN
sys.query_context_settings c
ON
c.context_settings_id = q.context_settings_id
LEFT
JOIN
sys.query_store_query_text t
ON
q.query_text_id = t.query_text_id
```

```sql
WHERE
p.is_forced_plan = 1
AND
p.last_force_failure_reason != 0;
```

```sql
SELECT
TOP 100
plan_id,
query_id,
plan_group_id,
engine_version,
compatibility_level,
query_plan_hash,
query_plan,
is_online_index_plan,
is_trivial_plan,
is_parallel_plan,
is_forced_plan,
is_natively_compiled,
force_failure_count,
last_force_failure_reason,
last_force_failure_reason_desc,
count_compiles,
initial_compile_start_time,
last_compile_start_time,
last_execution_time,
avg_compile_duration,
last_compile_duration,
plan_forcing_type,
plan_forcing_type_desc
FROM
sys.query_store_plan
ORDER
BY
last_execution_time
DESC
;
```
