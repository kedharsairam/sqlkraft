---
title: "Exchange Spill Event Class"
topic: "event-classes"
description: ""
tags: ["event-classes","exchange-spill-event-class"]
pubDate: 2025-12-01
---

The

event class indicates that communication buffers in a parallel query plan

have been temporarily written to the

database. This occurs rarely and only when a

query plan has multiple range scans.

Normally, the Transact-SQL query that generates such range scans has many BETWEEN

operators, each of which selects a range of rows from a table or an index. Alternatively, you can

obtain multiple ranges using expressions such as (T.a > 10 AND T.a < 20) OR (T.a > 100 AND

T.a < 120). Additionally, the query plans must require that these ranges be scanned in order

either because there is an ORDER BY clause on T.a, or because an iterator within the plan

requires that it consume the tuples in sorted order.

When a query plan for such a query has multiple

operators, the memory

communication buffers used by the

operators become full, and a situation can arise

whereby the query's execution progress stops. In this situation, one of the

operators writes its output buffer to

(an operation called an

exchange spill

) so that it

can consume rows from some of its input buffers. Eventually, the spilled rows are returned to

the consumer when the consumer is ready to consume them.

Very rarely, multiple exchange spills can occur within the same execution plan, causing the

query to execute slowly. If you notice more than five spills within the same query plan's

execution, contact your support professional.

Exchange spills are sometimes transient and may disappear as data distribution changes.

There are several ways to avoid exchange spill events:

Omit the ORDER BY clause if you do not need the result set to be ordered.

If ORDER BY is required, eliminate the column that participates in the multiple range

scans (T.a in the example above) from the ORDER BY clause.

Using an index hint, force the optimizer to use a different access path on the table in

question.

Rewrite the query to produce a different query execution plan.

Force serial execution of the query by adding the MAXDOP = 1 option to the end of the

query or index operation. For more information, see

Configure the max degree of

parallelism Server Configuration Option

and

Configure Parallel Index Operations.
