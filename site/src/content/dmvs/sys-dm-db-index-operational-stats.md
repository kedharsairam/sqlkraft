---
name: 'sys.dm_db_index_operational_stats'
title: 'sys.dm_db_index_operational_stats'
category: 'execution'
description: 'SQL Server 2016 (13.x) and later versions'
pubDate: 2026-05-29
---

SQL Server 2016 (13.x) and later versions

The following example shows how to query server broker queues for fragmentation.

System dynamic management views

Index Related Dynamic Management Views and Functions (Transact-SQL)

sys.dm_db_index_operational_stats (Transact-SQL)

sys.dm_db_index_usage_stats (Transact-SQL)

sys.dm_db_partition_stats (Transact-SQL)

sys.allocation_units (Transact-SQL)

Transact-SQL reference (Database Engine)

Last updated on 03/19/2026

## sys.dm_db_xtp_index_stats (Transact-SQL)

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric


## Returns counts of different types of index operations and the time each type of operation was
last performed.

In Azure SQL Database, dynamic management views cannot expose information that would

impact database containment or expose information about other databases the user has access

to. To avoid exposing this information, every row that contains data that doesn't belong to the

connected tenant is filtered out.

ID of the database on which the table or view is defined.

In Azure SQL Database, the values are unique within a single database

or an elastic pool, but not within a logical server.

ID of the table or view on which the index is defined

ID of the index.

Number of seeks by user queries.

７

The DMV

does not return information about memory-

optimized indexes or spatial indexes. For information about memory-optimized index use,

see

.

７

To call this view from Azure Synapse Analytics or Analytics Platform System (PDW), use

. This syntax is not supported by serverless SQL

pool in Azure Synapse Analytics.

ﾉ

Number of scans by user queries that did not use 'seek' predicate.

Number of bookmark lookups by user queries.

Number of updates by user queries. This includes Insert, Delete, and

Updates representing number of operations done not the actual rows

affected. For example, if you delete 1000 rows in one statement, this

count increments by 1

Time of last user seek

Time of last user scan.

Time of last user lookup.

Time of last user update.

Number of seeks by system queries.

Number of scans by system queries.

Number of lookups by system queries.

Number of updates by system queries.

Time of last system seek.

Time of last system scan.

Time of last system lookup.

Time of last system update.

pdw_node_id

: Azure Synapse Analytics, Analytics Platform System (PDW)

The identifier for the node that this distribution is on.

Every individual seek, scan, lookup, or update on the specified index by one query execution is

counted as a use of that index and increments the corresponding counter in this view.

Information is reported both for operations caused by user-submitted queries, and for

operations caused by internally generated queries, such as scans for gathering statistics.

The

column is a counter of maintenance on the index caused by insert, update,

or delete operations on the underlying table or view. You can use this view to determine which

## Basic

## S0

## S1

## elastic pools

```sql
SET
@idx = @idx + 1
END
COMMIT
;
GO
SELECT
page_count,
compressed_page_count,
forwarded_record_count,
*
FROM
sys.dm_db_index_physical_stats(db_id(), object_id(
't3'
),
NULL
,
NULL
,
'SAMPLED'
);
SELECT
page_count,
compressed_page_count,
forwarded_record_count,
*
FROM
sys.dm_db_index_physical_stats(db_id(), object_id(
't3'
),
NULL
,
NULL
,
'DETAILED'
);
```

```sql
--Using queue internal table name
SELECT
*
FROM
sys.dm_db_index_physical_stats(db_id(),
object_id(
'sys.queue_messages_549576996'
),
DEFAULT
,
DEFAULT
,
DEFAULT
);
--Using queue name directly
SELECT
*
FROM
sys.dm_db_index_physical_stats(db_id(), object_id(
'ExpenseQueue'
),
DEFAULT
,
DEFAULT
,
DEFAULT
);
```

```sql
sys.dm_db_index_usage_stats
```

```sql
sys.dm_pdw_nodes_db_index_usage_stats
```

```sql
user_updates
```
