---
name: "Filtered indexes"
title: "Filtered indexes"
category: "statements"
description: "When partitioning a non-unique, clustered index, the Database Engine by default adds any"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Required SET options for filtered indexes

When partitioning a non-unique, clustered index, the Database Engine by default adds any

partitioning columns to the list of clustered index keys, if not already specified.

Indexed views can be created on partitioned tables in the same manner as indexes on tables.

For more information about partitioned indexes, see

Partitioned tables and indexes

and the

SQL Server index architecture and design guide

.

When an index is created or rebuilt, the query optimizes updates statistics on the index. For a

partitioned index, the query optimizer uses the default sampling algorithm instead of scanning

all the rows in the table for a nonpartitioned index. To obtain statistics on partitioned indexes

by scanning all the rows in the table, use

or

with the

clause.

A filtered index is an optimized nonclustered index, suited for queries that select a small

percentage of rows from a table. It uses a filter predicate to index a portion of the data in the

table. A well-designed filtered index can improve query performance, reduce storage costs, and

reduce maintenance costs.

The

options in the

column are required whenever any of the following

conditions occur:

You create a filtered index.

An

,

,

, or

statement modifies data in a filtered index.

The filtered index is used by the query optimizer to produce the query plan.

Creating and rebuilding nonaligned indexes on a table with more than 1,000 partitions is

possible, but is not supported. Doing so may cause degraded performance or excessive

memory consumption during these operations. We recommend only using aligned

indexes when the number of partitions exceeds 1,000.

Expand table

#### option

#### Required

#### Default

#### server value

#### Default OLE DB

#### and ODBC value

#### Default DB-

#### Library value

```sql
CREATE STATISTICS
```

```sql
UPDATE STATISTICS
```

`FULLSCAN`

`SET`

`INSERT`

`UPDATE`

`DELETE`

`MERGE`

`SET`

```sql
ANSI_NULLS
ON
ON
ON
OFF
```
