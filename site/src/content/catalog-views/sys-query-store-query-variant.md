---
name: 'sys.query_store_query_variant'
title: 'sys.query_store_query_variant (Transact-'
category: 'query-store'
description: '## View Query Store variant information'
tags: ["catalog-view", "query-store"]
pubDate: 2026-05-29
---

## View Query Store variant information

SQL)

Applies to:

SQL Server 2022 (16.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

Contains information about the parent-child relationships between the original parameterized

queries (also known as parent queries), dispatcher plans, and their child query variants. This

catalog view offers the ability to view all query variants associated with a dispatcher as well as

the original parameterized queries. Query variants will have the same query_hash value as

viewed from within the sys.query_store_query catalog view, which when joined with the

sys.query_store_query_variant and sys.query_store_runtime_stats catalog views, aggregate

resource usage statistics can be obtained for queries that differ only by their input values.


## Description
Primary key. ID of the parameterized sensitive query variant.

ID of the original parameterized query.

ID of the parameter sensitive plan optimization dispatcher plan.

Since more than one query variant can be associated with one dispatcher plan, there will be

multiple plans that belong to query variants which will eventually add to the overall resource

usage statistics of the parent query. The dispatcher plan for query variants does not produce

any runtime statistics in the Query Store, which will cause existing Query Store queries to no

longer be sufficient when gathering overall statistics unless an additional join to the

view is included.

Requires the

permission.

ﾉ

Expand table

## View Query Store dispatcher and variant information

SQL

SQL

sys.query_store_plan (Transact-SQL)

sys.query_store_query (Transact-SQL)

sys.query_store_runtime_stats (Transact-SQL)

sys.query_store_wait_stats (Transact-SQL)

sys.query_store_runtime_stats_interval (Transact-SQL)

Monitoring Performance By Using the Query Store

Catalog Views (Transact-SQL)

Query Store Stored Procedures (Transact-SQL)

Last updated on 11/18/2025

See Also

```sql
SELECT
qspl.plan_type_desc
AS
query_plan_type,
qspl.plan_id
as
query_store_planid,
qspl.query_id
as
query_store_queryid,
qsqv.query_variant_query_id
as
query_store_variant_queryid,
qsqv.parent_query_id
as
query_store_parent_queryid,
qsqv.dispatcher_plan_id
as
query_store_dispatcher_planid,
OBJECT_NAME(qsq.object_id)
as
module_name,
qsq.query_hash,
qsqtxt.query_sql_text,
convert
(
xml
,qspl.query_plan)
as
show_plan_xml,
qsrs.last_execution_time
as
last_execution_time,
qsrs.count_executions
AS
number_of_executions,
qsq.count_compiles
AS
number_of_compiles
FROM
sys.query_store_runtime_stats
AS
qsrs
JOIN
sys.query_store_plan
AS
qspl
ON
qsrs.plan_id = qspl.plan_id
JOIN
sys.query_store_query_variant qsqv
ON
qspl.query_id = qsqv.query_variant_query_id
JOIN
sys.query_store_query
as
qsq
ON
qsqv.parent_query_id = qsq.query_id
JOIN
sys.query_store_query_text
AS
qsqtxt
ON
qsq.query_text_id = qsqtxt .query_text_id
ORDER
BY
qspl.query_id, qsrs.last_execution_time;
GO
```

```sql
SELECT
qspl.plan_type_desc
AS
query_plan_type,
qspl.plan_id
as
query_store_planid,
qspl.query_id
as
query_store_queryid,
qsqv.query_variant_query_id
as
query_store_variant_queryid,
qsqv.parent_query_id
as
query_store_parent_queryid,
qsqv.dispatcher_plan_id
as
query_store_dispatcher_planid,
qsq.query_hash,
qsqtxt.query_sql_text,
CONVERT
(
xml
,qspl.query_plan)
as
show_plan_xml,
qsq.count_compiles
AS
number_of_compiles,
qsrs.last_execution_time
as
last_execution_time,
qsrs.count_executions
AS
number_of_executions
FROM
sys.query_store_query qsq
LEFT
JOIN
sys.query_store_query_text qsqtxt
ON
qsq.query_text_id = qsqtxt.query_text_id
LEFT
JOIN
sys.query_store_plan qspl
ON
qsq.query_id = qspl.query_id
LEFT
JOIN
sys.query_store_query_variant qsqv
ON
qsq.query_id = qsqv.query_variant_query_id
```

```sql
LEFT
JOIN
sys.query_store_runtime_stats qsrs
ON
qspl.plan_id = qsrs.plan_id
LEFT
JOIN
sys.query_store_runtime_stats_interval qsrsi
ON
qsrs.runtime_stats_interval_id = qsrsi.runtime_stats_interval_id
WHERE
qspl.plan_type = 1
or
qspl.plan_type = 2
ORDER
BY
qspl.query_id, qsrs.last_execution_time;
GO
```
