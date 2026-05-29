---
name: 'level 130'
title: 'level 130'
category: 'statements'
description: 'the memory grant size of a cached plan if an'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

the memory grant size of a cached plan if an

excessive amount was originally requested.

Batch-mode queries that contain join operators are

eligible for three physical join algorithms, including

nested loop, hash join and merge join. If cardinality

estimates are incorrect for join inputs, an

inappropriate join algorithm might be selected. If

this occurs, performance will suffer, and the

inappropriate join algorithm will remain in use until

the cached plan is recompiled.

There's an additional join operator called

. If cardinality estimates are incorrect for the

outer build join input, an inappropriate join

algorithm might be selected. If this occurs and the

statement is eligible for an adaptive join, a nested

loop will be used for smaller join inputs, and a hash

join will be used for larger join inputs dynamically

without requiring recompilation.

Trivial plans referencing Columnstore indexes

aren't eligible for batch mode execution.

A trivial plan referencing Columnstore indexes will

be discarded in favor of a plan that is eligible for

batch mode execution.

The

UDX operator can

only run in row mode.

The

UDX operator is

eligible for batch mode execution.

Multi-statement table-valued functions (TVFs)

don't have interleaved execution

Interleaved execution for multi-statement TVFs to

improve plan quality.

Fixes that were under trace flag 4199 in earlier versions of SQL Server prior to SQL Server 2017

are now enabled by default. With compatibility mode 140. Trace flag 4199 will still be

applicable for new query optimizer fixes that are released after SQL Server 2017. For

information, see

trace flag 4199

.

This section describes new behaviors introduced with compatibility level 130.

The

in an

-

statement

is single-threaded.

The

in an

-

statement is multi-

threaded or can have a parallel plan.

Queries on a memory-optimized table

execute single-threaded.

Queries on a memory-optimized table can now have

parallel plans.

Introduced the SQL 2014 Cardinality

estimator

Further cardinality estimation (CE) Improvements with the

Cardinality Estimation Model 130, which is visible from a

Query plan.

ﾉ

Expand table

#### Compatibility level setting of 120 or lower

#### Compatibility level setting of 130

Batch mode versus Row Mode changes with

Columnstore indexes:

Sorts on a table with Columnstore

index are in Row mode

Windowing function aggregates

operate in row mode such as

or

Queries on Columnstore tables with

Multiple distinct clauses operated in

Row mode

Queries running under

or

with a serial plan executed in Row

mode

Batch mode versus Row Mode changes with Columnstore

indexes:

Sorts on a table with a Columnstore index are now

in batch mode

Windowing aggregates now operate in batch mode

such as

or

Queries on Columnstore tables with Multiple

distinct clauses operate in Batch mode

Queries running under

or with a serial

plan execute in Batch Mode

Statistics can be automatically updated.

The logic that automatically updates statistics is more

aggressive on large tables. In practice, this should reduce

cases where customers have seen performance issues on

queries where newly inserted rows are queried frequently

but where the statistics hadn't been updated to include

those values.

Trace 2371 is

by default in SQL Server

2014 (12.x).

Trace flag 2371

is

by default in SQL Server 2016 (13.x).

Trace flag 2371 tells the auto statistics updater to sample

a smaller yet wiser subset of rows, in a table that has a

great many rows.

One improvement is to include in the sample more rows

that were inserted recently.

Another improvement is to let queries run while the

update statistics process is running, rather than blocking

the query.

For level 120, statistics are sampled by a

single-threaded process.

For level 130, statistics are sampled by a multi-threaded

process (parallel process).

253 incoming foreign keys is the limit.

A given table can be referenced by up to 10,000 incoming

foreign keys or similar references. For restrictions, see

Create foreign key relationships

.

The deprecated MD2, MD4, MD5, SHA, and

SHA1 hash algorithms are permitted.

Only SHA2_256 and SHA2_512 hash algorithms are

permitted.

SQL Server 2016 (13.x) includes improvements in some

data types conversions and some (mostly uncommon)

operations. For details see

SQL Server and Azure SQL

#### Compatibility level setting of 120 or lower

#### Compatibility level setting of 130

#### Compatibility level setting of

#### 110 or lower

#### Compatibility level setting of 120

#### date

```sql
sp_execute_external_script
```

```sql
sp_execute_external_script
```

```sql
INSERT
```

```sql
INSERT
```

```sql
SELECT
```

```sql
INSERT
```

```sql
INSERT
```

```sql
SELECT
```

```sql
CardinalityEstimationModelVersion="120"
```

```sql
LAG
```

```sql
LEAD
```

```sql
MAXDOP 1
```

```sql
LAG
```

```sql
LEAD
```

```sql
MAXDOP 1
```

```sql
OFF
```

```sql
ON
```
