---
name: 'sys.query_store_query_hints'
title: 'sys.query_store_query_hints'
category: 'query-store'
description: '## View Query Store hints'
tags: ["catalog-view", "query-store"]
pubDate: 2026-05-29
---

## View Query Store hints

SQL Server 2019 (15.x) and previous versions require

permission on the

server.

SQL Server 2022 (16.x) and later versions require

permission on

the server.

The following example returns existing Query Store hints for

39:

SQL

Query Store hints

sys.sp_query_store_set_hints

sys.sp_query_store_clear_hints

sys.query_store_query (Transact-SQL)

Last updated on 11/18/2025

Related content

```sql
VIEW SERVER STATE
```

```sql
VIEW SERVER PERFORMANCE STATE
```

```sql
query_id
```

```sql
SELECT
query_hint_id,
query_id,
replica_group_id,
query_hint_text,
last_query_hint_failure_reason,
last_query_hint_failure_reason_desc,
query_hint_failure_count,
source
,
source_desc
FROM
sys.query_store_query_hints
WHERE
query_id = 39;
```
