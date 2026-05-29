---
name: 'sys.query_store_runtime_stats'
title: 'sys.query_store_runtime_stats (Transact-'
category: 'query-store'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["catalog-view", "query-store"]
pubDate: 2026-05-29
---

SQL)

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

SQL database in Microsoft Fabric

Contains information about the runtime execution statistics information for the query.


## Description
Identifier of the row that represents runtime

execution statistics for the

,

and

. It is unique only for

the past runtime statistics intervals. For currently

active interval, there may be multiple rows

representing runtime statistics for the plan

referenced by

, with the execution type

represented by

. Typically, one row

represents runtime statistics that are flushed to disk,

while other(s) represent in-memory state. Hence, to

get actual state for every interval you need to

aggregate metrics, grouping by

,

and

.

Note:

Azure Synapse Analytics will always return

zero (0).

Foreign key. Joins to

sys.query_store_plan (Transact-

SQL)

.

Foreign key. Joins to

sys.query_store_runtime_stats_interval (Transact-

SQL)

.

Determines type of query execution:

0 - Regular execution (successfully finished)

3 - Client initiated aborted execution

4 - Exception aborted execution

Textual description of the execution type field:

0 - Regular

3 - Aborted

ﾉ

Expand table


## Description
4 - Exception

First execution time for the query plan within the

aggregation interval. This is the end time of the

query execution.

Last execution time for the query plan within the

aggregation interval. This is the end time of the

query execution.

Total count of executions for the query plan within

the aggregation interval.

Average duration for the query plan within the

aggregation interval (reported in microseconds).

Last duration for the query plan within the

aggregation interval (reported in microseconds).

Minimum duration for the query plan within the

aggregation interval (reported in microseconds).

Maximum duration for the query plan within the

aggregation interval (reported in microseconds).

Duration standard deviation for the query plan

within the aggregation interval (reported in

microseconds).

Average CPU time for the query plan within the

aggregation interval (reported in microseconds).

Note:

Azure Synapse Analytics will always return

zero (0).

Last CPU time for the query plan within the

aggregation interval (reported in microseconds).

Note:

Azure Synapse Analytics will always return

zero (0).

Minimum CPU time for the query plan within the

aggregation interval (reported in microseconds).

Note:

Azure Synapse Analytics will always return

zero (0).

Maximum CPU time for the query plan within the

aggregation interval (reported in microseconds).

Note:

Azure Synapse Analytics will always return

zero (0).


## Description
CPU time standard deviation for the query plan

within the aggregation interval (reported in

microseconds).

Note:

Azure Synapse Analytics will always return

zero (0).

Average number of logical I/O reads for the query

plan within the aggregation interval (expressed as a

number of 8-KB pages read).

Note:

Azure Synapse Analytics will always return

zero (0).

Last number of logical I/O reads for the query plan

within the aggregation interval (expressed as a

number of 8-KB pages read).

Note:

Azure Synapse Analytics will always return

zero (0).

Minimum number of logical I/O reads for the query

plan within the aggregation interval (expressed as a

number of 8-KB pages read).

Note:

Azure Synapse Analytics will always return

zero (0).

Maximum number of logical I/O reads for the query

plan within the aggregation interval (expressed as a

number of 8-KB pages read).

Note:

Azure Synapse Analytics will always return

zero (0).

Number of logical I/O reads standard deviation for

the query plan within the aggregation interval

(expressed as a number of 8-KB pages read).

Note:

Azure Synapse Analytics will always return

zero (0).

Average number of logical I/O writes for the query

plan within the aggregation interval (expressed as a

number of 8-KB pages written).

Note:

Azure Synapse Analytics will always return

zero (0).

Last number of logical I/O writes for the query plan

within the aggregation interval (expressed as a

number of 8-KB pages written).

Note:

Azure Synapse Analytics will always return

zero (0).


## Description
Minimum number of logical I/O writes for the query

plan within the aggregation interval (expressed as a

number of 8-KB pages written).

Note:

Azure Synapse Analytics will always return

zero (0).

Maximum number of logical I/O writes for the query

plan within the aggregation interval (expressed as a

number of 8-KB pages written).

Note:

Azure Synapse Analytics will always return

zero (0).

Number of logical I/O writes standard deviation for

the query plan within the aggregation interval

(expressed as a number of 8-KB pages written).

Note:

Azure Synapse Analytics will always return

zero (0).

Average number of physical I/O reads for the query

plan within the aggregation interval (expressed as a

number of 8-KB pages read).

Note:

Azure Synapse Analytics will always return

zero (0).

Last number of physical I/O reads for the query plan

within the aggregation interval (expressed as a

number of 8-KB pages read).

Note:

Azure Synapse Analytics will always return

zero (0).

Minimum number of physical I/O reads for the

query plan within the aggregation interval

(expressed as a number of 8-KB pages read).

Note:

Azure Synapse Analytics will always return

zero (0).

Maximum number of physical I/O reads for the

query plan within the aggregation interval

(expressed as a number of 8-KB pages read).

Note:

Azure Synapse Analytics will always return

zero (0).

Number of physical I/O reads standard deviation for

the query plan within the aggregation interval

(expressed as a number of 8-KB pages read).

Note:

Azure Synapse Analytics will always return

zero (0).
