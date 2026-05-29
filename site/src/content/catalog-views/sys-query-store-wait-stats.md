---
name: 'sys.query_store_wait_stats'
title: 'sys.query_store_wait_stats'
category: 'query-store'
description: 'TRACEWRITE, SQLTRACE_LOCK, SQLTRACE_FILE_BUFFER,'
tags: ["catalog-view", "query-store"]
pubDate: 2026-05-29
---

TRACEWRITE, SQLTRACE_LOCK, SQLTRACE_FILE_BUFFER,

SQLTRACE_FILE_WRITE_IO_COMPLETION,

SQLTRACE_FILE_READ_IO_COMPLETION,

SQLTRACE_PENDING_BUFFER_WRITERS, SQLTRACE_SHUTDOWN,

QUERY_TRACEOUT, TRACE_EVTNOTIFF

FT_RESTART_CRAWL, FULLTEXT GATHERER, MSSEARCH, FT_METADATA_MUTEX,

FT_IFTSHC_MUTEX, FT_IFTSISM_MUTEX, FT_IFTS_RWLOCK,

FT_COMPROWSET_RWLOCK, FT_MASTER_MERGE, FT_PROPERTYLIST_CACHE,

FT_MASTER_MERGE_COORDINATOR,

PWAIT_RESOURCE_SEMAPHORE_FT_PARALLEL_QUERY_SYNC

ASYNC_IO_COMPLETION, IO_COMPLETION, BACKUPIO, WRITE_COMPLETION,

IO_QUEUE_LIMIT, IO_RETRY

SE_REPL_%, REPL_%, HADR_%

, PWAIT_HADR_%,

REPLICA_WRITES, FCB_REPLICA_WRITE, FCB_REPLICA_READ, PWAIT_HADRSIM

LOG_RATE_GOVERNOR, POOL_LOG_RATE_GOVERNOR,

HADR_THROTTLE_LOG_RATE_GOVERNOR, INSTANCE_LOG_RATE_GOVERNOR,

RBIO_RG_%

* Query Store tracks wait stats only during query

execution

, not during query

compilation

. This

restricts Query Store's ability to track compilation wait stats.

Requires the

permission.

Learn more about Query Store in the following articles:

sys.query_store_replicas (Transact-SQL)

sys.database_query_store_options (Transact-SQL)

sys.query_context_settings (Transact-SQL)

sys.query_store_plan (Transact-SQL)

sys.query_store_query (Transact-SQL)

sys.query_store_query_text (Transact-SQL)

sys.query_store_runtime_stats_interval (Transact-SQL)

Monitoring Performance By Using the Query Store

Next steps

Catalog Views (Transact-SQL)

Query Store Stored Procedures (Transact-SQL)

Last updated on 11/18/2025

```sql
VIEW DATABASE STATE
```
