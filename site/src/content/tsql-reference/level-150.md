---
name: "level 150"
title: "Level 150"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

data distribution and usage patterns for all

databases and queries. The only way to change

or adjust any one of those assumptions is when

the user undertakes a manual process to

explicitly indicate which model assumptions

should be used, by using query hints. No

internal adjustment can be made to this default

model after a query plan is generated.

distribution and usage patterns, but after some

executions for a given query, the Database Engine

learns which different sets of model assumptions

might yield more accurate estimates, and therefore

adjusts the assumptions in use to better match the

data set being queried. CE Feedback is enabled by

default in compatibility level 160. For more

information, see

Cardinality estimation (CE) feedback.

No automatic determination of the optimal

degree of parallelism is attempted by the

Database Engine. For information on manually

controlling the maximum degree of parallelism

(

) at the instance, database, query, or

workload levels, see

Server configuration: max

degree of parallelism

Degree of parallelism (DOP) Feedback improves query

performance by identifying parallelism inefficiencies

for repeating queries, based on elapsed time and

waits. If parallelism usage is deemed inefficient, DOP

Feedback will lower the DOP for the next execution of

the query, from whatever is the configured DOP, and

verify if it helps. DOP Feedback isn't enabled by

default. To enable DOP Feedback, enable the

database scoped configuration in a

database. For more information, see

Degree of

parallelism (DOP) feedback.

This section describes new behaviors introduced with compatibility level 150.

Relational data warehouse and analytic workloads

might not be able to use columnstore indexes due to

OLTP-overhead, lack of vendor support or other

limitations. Without columnstore indexes, these

workloads can't benefit from batch execution mode.

Batch execution mode is now available for

analytic workloads without requiring

columnstore indexes. For more information, see

batch mode on rowstore.

Row-mode queries that request insufficient memory

grant sizes that result in spills to disk might continue

to have issues on consecutive executions.

Row-mode queries that request insufficient

memory grant sizes that result in spills to disk

might have improved performance on

consecutive executions. For more information,

see

row mode memory grant feedback.

Row-mode queries that request an excessive memory

grant size that results in concurrency issues might

continue to have issues on consecutive executions.

Row-mode queries that request an excessive

memory grant size that results in concurrency

issues might have improved concurrency on

Expand table

#### Compatibility level setting of 140 or lower

#### Compatibility level setting of 150

#### Compatibility level setting of 130 or lower

#### Compatibility level setting of 140

#### interleaved execution

#### batch mode

#### memory grant feedback

#### batch

#### mode memory grant feedback

`MAXDOP`

`DOP_FEEDBACK`
