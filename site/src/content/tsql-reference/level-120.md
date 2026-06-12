---
name: "level 120"
title: "Level 120"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

Database improvements in handling some data types and

uncommon operations.

The

function isn't available.

The

function is available under compatibility

level 130 or above. If your database compatibility level is

lower than 130, SQL Server won't be able to find and

execute

function.

Fixes that were under trace flag 4199 in earlier versions of SQL Server prior to SQL Server 2016

(13.x) are now enabled by default. With compatibility mode 130. Trace flag 4199 will still be

applicable for new query optimizer fixes that are released after SQL Server 2016 (13.x). To use

the older query optimizer in SQL Database you must select compatibility level 110. For

information, see

trace flag 4199.

This section describes new behaviors introduced with compatibility level 120.

The older query optimizer is

used.

2014 (12.x) includes substantial improvements to the

component that creates and optimizes query plans. This new query

optimizer feature is dependent upon use of the database compatibility

level 120. New database applications should be developed using

database compatibility level 120 to take advantage of these

improvements. Applications that are migrated from earlier versions of

should be carefully tested to confirm that good

performance is maintained or improved. If performance degrades, you

can set the database compatibility level to 110 or earlier to use the

older query optimizer methodology.

Database compatibility level 120 uses a new cardinality estimator that

is tuned for modern data warehousing and OLTP workloads. Before

setting database compatibility level to 110 because of performance

issues, see the recommendations in the

Query Plans

section of

What's

new in SQL Server 2016.

In compatibility levels lower

than 120, the language setting

is ignored when converting a

The language setting isn't ignored when converting a

value to a

string value.

Expand table

#### Compatibility level setting of

#### 110 or lower

#### Compatibility level setting of 120

`STRING_SPLIT`

`STRING_SPLIT`

`STRING_SPLIT`
