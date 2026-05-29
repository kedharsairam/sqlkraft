---
title: sys.dm_db_missing_index_columns
name: sys.dm_db_missing_index_columns
category: execution
description:
pubDate: 2026-05-29
---

Requires VIEW SERVER PERFORMANCE STATE permission on the server, for SQL Server 2022

(16.x) and later versions.

The following examples illustrate how to use the

dynamic management view.

The following query returns the last recorded query text for the 10 missing indexes that would

produce the highest anticipated cumulative improvement, in descending order.

SQL

Tune nonclustered indexes with missing index suggestions

sys.dm_db_missing_index_columns (Transact-SQL)

sys.dm_db_missing_index_details (Transact-SQL)

sys.dm_db_missing_index_groups (Transact-SQL)

sys.dm_db_missing_index_group_stats (Transact-SQL)

sys.dm_exec_sql_text (Transact-SQL)

CREATE INDEX (Transact-SQL)

sys.dm_os_sys_info (Transact-SQL)

Monitor performance by using the Query Store

Last updated on 11/18/2025

## Applies to:

Article

•

02/28/2023

SQL Server

This section contains the following dynamic management objects.

sys.dm_io_backup_tapes (Transact-SQL)

sys.dm_io_pending_io_requests (Transact-SQL)

sys.dm_io_cluster_valid_path_names (Transact-SQL)

sys.dm_io_cluster_shared_drives (Transact-SQL)

sys.dm_io_virtual_file_stats (Transact-SQL)

Dynamic Management Views and Functions (Transact-SQL)

System Views (Transact-SQL)

## Applies to:

## Note

## sys.dm_pdw_nodes_io_cluster_shared_drives

## Note

Article

•

02/28/2023

SQL Server

Azure SQL Managed Instance

Analytics Platform System

(PDW)

This view returns the drive name of each of the shared drives if the current server instance is a

clustered server. If the current server instance is not a clustered instance it returns an empty

rowset.

The name of the drive (the drive letter) that represents an individual disk

taking part in the cluster shared disk array. Column is not nullable.

: ssPDW

The identifier for the node that this distribution is on.

When clustering is enabled, the failover cluster instance requires data and log files to be on

shared disks so that they may be accessed after the instance fails over to another node. Each of

the rows in this view represents a single shared disk which is used by this clustered SQL Server

instance. Only disks listed by this view can be used to store data or log files for this instance of

SQL Server. The disks listed in this view are those that are in the cluster resource group

associated with the instance.

７

To call this from Analytics Platform System (PDW), use the name

.

ﾉ

７

## sys.dm_io_cluster_valid_path_names (Transact-SQL)

```sql
sys.dm_db_missing_index_group_stats_query
```

```sql
SELECT
TOP 10
SUBSTRING
(
sql_text.text,
misq.last_statement_start_offset / 2 + 1,
(
CASE
misq.last_statement_start_offset
WHEN
-1
THEN
DATALENGTH
(sql_text.text)
ELSE
misq.last_statement_end_offset
END
- misq.last_statement_start_offset
) / 2 + 1
),
misq.*
FROM
sys.dm_db_missing_index_group_stats_query
AS
misq
CROSS
APPLY
sys.dm_exec_sql_text(misq.last_sql_handle)
AS
sql_text
ORDER
BY
misq.avg_total_user_cost
* misq.avg_user_impact
* (misq.user_seeks + misq.user_scans)
DESC
;
```
