---
title: 'LAQ heuristics'
topic: 'query-processing'
description: 'Lock after qualification (LAQ)'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

As described in

Lock after qualification (LAQ)

, when LAQ is used, statements using query

operators that don't support predicate requalification might be internally restarted and

processed without LAQ. If this happens frequently, the overhead of reprocessing might

become significant. To minimize the overhead, optimized locking uses a heuristics-based

feedback mechanism that disables LAQ if the overhead exceeds thresholds.

For the purposes of the feedback mechanism, the work done by a statement is measured in the

number of logical reads. If the database engine is modifying a row that was modified by

another transaction after statement processing started, then the work done by the statement is

treated as potentially wasted because the statement might need to be reprocessed.

As statements execute, the database engine maintains LAQ feedback data that tracks the

potentially wasted work, the occurrences of statement reprocessing, and the total work done

by the statements that might be reprocessed.

LAQ is disabled if the ratio of the potentially wasted work to the total work, or the ratio of the

number of reprocessed statements to the total number of statements exceed their respective

thresholds. If both of these ratios fall below thresholds, LAQ is reenabled.

LAQ feedback data is tracked at two levels:

For a

.

The database engine starts tracking LAQ feedback for a plan on the first occurrence of

statement reprocessing.

If a query is captured in

Query Store

, LAQ feedback is captured in Query Store as well.

The database engine uses this feedback to keep LAQ enabled or disabled for the plan

if the database restarts.

Query plans with captured LAQ feedback have a row with a matching

value in

the

sys.query_store_plan_feedback

catalog view. The

and

columns are set to 4 and

respectively.

For a

.

Feedback is aggregated for all statements that don't have query plan level feedback,

for example if a query isn't captured in Query Store.

Feedback is tracked since database startup and is recreated after each startup.

When deciding whether to use LAQ for a statement, the system uses the query plan feedback if

available. Otherwise, it uses the database level feedback. This means that some statements

might execute with LAQ, and some might execute without LAQ. For example, LAQ might be

disabled for a query plan, but enabled for the database, and vice versa.

```sql
plan_id
```

```sql
feature_id
```

```sql
feature_desc
```

```sql
LAQ Feedback
```
