---
name: 'sys.sp_query_store_set_hints'
title: 'sys.sp_query_store_set_hints'
category: 'general'
description: 'SQL Server 2022 (16.x) and later versions'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## Identify a query in Query Store

The following query hints are currently unsupported:

(instead, consider Query Store's original plan forcing capability,

sp_query_store_force_plan

).

Table hints

(for example,

,

,

)

Requires the

permission on the database.

The following example queries

sys.query_store_query_text

and

sys.query_store_query

to return

the

query_id

for an executed query text fragment.

In this example, the query we're attempting to tune is in the

sample database:

SQL

## Apply single hint

## Apply multiple hints

Query Store doesn't immediately reflect query data to its system views.

Identify the query in the Query Store system catalog views:

SQL

In the following samples, the previous query example in the

database was identified as

query_id

39.

The following example applies the

hint to

query_id

39, as identified in Query Store:

SQL

The following example applies the hint to force the

legacy cardinality estimator

to

query_id

39,

identified in Query Store:

SQL

The following example applies multiple query hints to

query_id

39, including

,

, and the query optimizer behavior in compatibility level 110:

## View Query Store hints

## Remove the hint from a query

SQL

The following example returns existing Query Store hints:

SQL

Use the following example to remove the hint from

query_id

39, using the

sp_query_store_clear_hints

system stored procedure.

SQL

Query Store hints

Table hints (Transact-SQL)

sp_query_store_clear_hints (Transact-SQL)

sys.query_store_query_hints (Transact-SQL)

Monitor performance by using the Query Store

Last updated on 11/18/2025

Related content

```sql
OPTIMIZE FOR ( @var = val)
MAXRECURSION
USE PLAN
```

```sql
DISABLE_DEFERRED_COMPILATION_TV
DISABLE_TSQL_SCALAR_UDF_INLINING
```

```sql
FORCESEEK
```

```sql
READUNCOMMITTED
```

```sql
INDEX
```

```sql
ALTER
```

```sql
SalesLT
```

```sql
|
EXPAND
VIEWS
|
FAST
number_rows
|
FORCE
ORDER
|
IGNORE
_
NONCLUSTERED
_
COLUMNSTORE
_
INDEX
|
KEEP
PLAN
|
KEEPFIXED
PLAN
|
MAX
_
GRANT
_
PERCENT
= percent
|
MIN
_
GRANT
_
PERCENT
= percent
|
MAXDOP
number_of_processors
|
NO
_
PERFORMANCE
_
SPOOL
|
OPTIMIZE
FOR
UNKNOWN
|
PARAMETERIZATION
{
SIMPLE
|
FORCED
}
|
RECOMPILE
|
ROBUST
PLAN
|
USE
HINT
(
'<hint_name>'
[ , ...n ] )
```

```sql
SELECT
*
FROM
SalesLT.Address
AS
A
INNER
JOIN
SalesLT.CustomerAddress
AS
CA
ON
A.AddressID = CA.AddressID
```

```sql
SalesLT
```

```sql
RECOMPILE
```

```sql
RECOMPILE
```

```sql
MAXDOP
1
```

```sql
WHERE
PostalCode =
'98052'
ORDER
BY
A.ModifiedDate
DESC
;
SELECT
q.query_id,
qt.query_sql_text
FROM
sys.query_store_query_text
AS
qt
INNER
JOIN
sys.query_store_query
AS
q
ON
qt.query_text_id = q.query_text_id
WHERE
query_sql_text
LIKE
N
'%PostalCode =%'
AND
query_sql_text
NOT
LIKE
N
'%query_store%'
;
GO
```

```sql
EXECUTE
sys.sp_query_store_set_hints
@query_id = 39,
@query_hints = N
'OPTION(RECOMPILE)'
;
EXECUTE
sys.sp_query_store_set_hints
@query_id = 39,
@query_hints = N
'OPTION(USE HINT(''FORCE_LEGACY_CARDINALITY_ESTIMATION''))'
;
```

```sql
EXECUTE
sys.sp_query_store_set_hints
@query_id = 39,
@query_hints = N
'OPTION(RECOMPILE, MAXDOP 1, USE
HINT(''QUERY_OPTIMIZER_COMPATIBILITY_LEVEL_110''))'
;
```

```sql
SELECT
query_hint_id,
query_id,
replica_group_id,
query_hint_text,
last_query_hint_failure_reason,
last_query_hint_failure_reason_desc,
query_hint_failure_count,
source
,
source_desc
FROM
sys.query_store_query_hints
WHERE
query_id = 39;
```

```sql
EXECUTE
sys.sp_query_store_clear_hints @query_id = 39;
```
