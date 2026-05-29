---
name: 'level 160'
title: 'level 160'
category: 'statements'
description: 'Regular expressions can be used to match'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Regular expressions can be used to match

complex patterns and manipulate data in

SQL Server and Azure SQL database.

Regular expression support within T-SQL

has been added. Some regular expression

functions aren't available in all database

compatibility levels For more information,

see

Regular expressions functions preview

.

Regular expression functions such as

,

, and

have been

introduced to enable pattern matching, extraction, and

splitting directly in T-SQL.

The ability to create AI embeddings (vector

arrays) from text expressions has been

added the Database engine. For more

information, see

AI functions

.

Introduces the

function, which enables

chunking of text input for AI model consumption,

improving integration with AI services.

Parameterized queries can have multiple

cached query plans for different selectivity

categories of a parameter. Parameter

sensitive plan optimization is enabled by

default in compatibility level 160 for select

queries only

When

Parameter sensitive plan optimization

is operating

under compatibility level 170, DML query support as well

as support for

is also available

Parameterized queries which have optional

parameters might suffer from suboptimal

plans due to parameter sniffing.

Query plan optimization for optional parameters,

improving performance by generating more appropriate

plans for NULL and non-NULL values.

This section describes new behaviors introduced with compatibility level 160.

Parameterized queries have a single query plan

based on the parameters used for the first

execution. Only one query plan is cached and

used for all parameter values. This can cause a

query plan to be inefficient for some values of

the parameter, also known as a parameter

sensitive plan.

Parameterized queries can have multiple cached query

plans for different selectivity categories of a parameter.

Parameter sensitive plan optimization is enabled by

default in compatibility level 160. For more

information, see

PSP Optimization

.

Cardinality estimation uses only one default set

of model assumptions about the underlying

Cardinality estimation starts with the default set of

model assumptions about the underlying data

ﾉ

Expand table

#### Compatibility level setting of 150 or lower

#### Compatibility level setting of 160

#### Compatibility level setting of 140 or lower

#### Compatibility level setting of 150

```sql
REGEXP_LIKE
```

```sql
REGEXP_MATCHES
```

```sql
REGEXP_SPLIT_TO_TABLE
```

```sql
AI_GENERATE_CHUNKS
```

```sql
tempdb
```
