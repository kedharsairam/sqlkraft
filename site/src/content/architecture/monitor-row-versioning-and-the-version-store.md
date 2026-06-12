---
title: "Monitor row versioning and the version store"
topic: "io-fundamentals"
description: "Enough disk space should be allocated to accommodate this requirement."
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

Enough disk space should be allocated to accommodate this requirement.

For monitoring row versioning, version store, and snapshot isolation processes for performance

and problems, the Database Engine provides tools in the form of Dynamic Management Views

(DMVs) and performance counters.

The following DMVs provide information about the current system state of

and the

version store, as well as transactions using row versioning. Returns space usage information for each file in the database.

For more information, see

sys.dm_db_file_space_usage (Transact-SQL). Returns page allocation and deallocation activity by session

for the database. For more information, see

sys.dm_db_session_space_usage (Transact-SQL). Returns page allocation and deallocation activity by task for

the database. For more information, see

sys.dm_db_task_space_usage (Transact-SQL). Returns a virtual table for the objects producing the

most versions in the version store. It groups the top 256 aggregated record lengths by

database_id and rowset_id. Use this function to find the largest consumers of the version

store. Applies to the version store in

only. For more information, see

sys.dm_tran_top_version_generators (Transact-SQL). Returns a virtual table that displays all version records in the

common version store. Applies to the version store in

only. For more information,

see

sys.dm_tran_version_store (Transact-SQL). Returns a virtual table that displays the total space

in

used by version store records for each database. Applies to the version store in

only. For more information, see

sys.dm_tran_version_store_space_usage (Transact-

SQL).

DMVs

７

Note

Querying

and

can be

expensive, since both scan the entire version store, which could be large.

## Free Space in tempdb (KB). Returns a virtual table for all active

transactions in all databases within the SQL Server instance that use row versioning. System

transactions don't appear in this DMV. For more information, see

sys.dm_tran_active_snapshot_database_transactions (Transact-SQL). Returns a virtual table that displays snapshots taken by

each transaction. The snapshot contains the sequence number of the active transactions

that use row versioning. For more information, see

sys.dm_tran_transactions_snapshot

(Transact-SQL). Returns a single row that displays row versioning-related

state information of the transaction in the current session. For more information, see

sys.dm_tran_current_transaction (Transact-SQL). Returns a virtual table that displays all active transactions at

the time the current snapshot isolation transaction starts. If the current transaction is using

snapshot isolation, this function returns no rows. The DMV

is

similar to

, except that it returns only the active

transactions for the current snapshot. For more information, see

sys.dm_tran_current_snapshot (Transact-SQL). Returns statistics for the persistent version

store in each database used when accelerated database recovery is enabled. For more

information, see

sys.dm_tran_persistent_version_store_stats (Transact-SQL).

The following performance counters monitor the version store in

, as well as transactions

using row versioning. The performance counters are contained in the

performance object. Monitors the amount, in kilobytes (KB), of free space in the

database. There must be enough free space in

to handle the version store

that supports snapshot isolation.

is efficient and isn't expensive to run because

it doesn't navigate through individual version store records, and instead returns

aggregated version store space consumed in

per database.

Performance counters

## Version Store Size (KB)

## Version Generation rate (KB/s)

## Version Cleanup rate (KB/s)

## Version Store unit count

## Version Store unit creation

## Version Store unit truncation

## Update conflict ratio

The following formula provides a rough estimate of the size of the version store. For long-

running transactions, it might be useful to monitor the generation and cleanup rate to

estimate the maximum size of the version store.

[size of common version store] = 2 _ [version store data generated per minute] _ [longest

running time (minutes) of the transaction]

The longest running time of transactions shouldn't include online index builds. Because

these operations might take a long time on very large tables, online index builds use a

separate version store. The approximate size of the online index build version store equals

the amount of data modified in the table, including all indexes, while the online index build

is active. Monitors the size in KB of all version stores in. This

information helps determine the amount of space needed in the

database for the

version store. Monitoring this counter over a period of time provides a useful estimate of

additional space needed for. Monitors the version generation rate in KB per second in all

version stores in. Monitors the version cleanup rate in KB per second in all

version stores in. Monitors the count of version store units. Monitors the total number of version store units created to

store row versions since the instance was started. Monitors the total number of version store units truncated

since the instance was started. A version store unit is truncated when SQL Server determines

that none of the version rows stored in the version store unit are needed to run active

transactions. Monitors the ratio of update snapshot transactions that have update

conflicts to the total number of update snapshot transactions.

７

Note

Information from Version Generation rate (KB/s) and Version Cleanup rate (KB/s) can be

used to predict

space requirements.

## Longest Transaction Running Time

## Transactions

## Snapshot Transactions

## Update Snapshot Transactions

## NonSnapshot Version Transactions

`tempdb`

`sys.dm_db_file_space_usage`

`sys.dm_db_session_space_usage`

`sys.dm_db_task_space_usage`

`sys.dm_tran_top_version_generators`

`tempdb`

`sys.dm_tran_version_store`

`tempdb`

`sys.dm_tran_version_store_space_usage`

`tempdb`

`tempdb`

`sys.dm_tran_top_version_generators`

`sys.dm_tran_version_store`

`sys.dm_tran_active_snapshot_database_transactions`

`sys.dm_tran_transactions_snapshot`

`sys.dm_tran_current_transaction`

`sys.dm_tran_current_snapshot`

`sys.dm_tran_current_snapshot`

`sys.dm_tran_transactions_snapshot`

`sys.dm_tran_persistent_version_store_stats`

`tempdb`

```sql
SQLServer:Transactions
```

`tempdb`

`tempdb`

`sys.dm_tran_version_store_space_usage`

`tempdb`

`tempdb`

`tempdb`

`tempdb`

`tempdb`

`tempdb`

`tempdb`
