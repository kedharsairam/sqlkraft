---
title: "Cache multiple plans for the same query"
topic: "query-processing"
description: "### sys.dm_exec_requests (Transact-SQL)"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

### sys.dm_exec_requests (Transact-SQL)

### sys.dm_exec_query_stats (Transact-SQL)

CONCAT_NULL_YIELDS_NULL

DATEFORMAT

ANSI_WARNINGS

QUOTED_IDENTIFIER

ANSI_NULLS

NO_BROWSETABLE

ANSI_DEFAULTS

Queries and execution plans are uniquely identifiable in the Database Engine, much like a

fingerprint:

The

is a binary hash value calculated on the execution plan for a given

query, and used to uniquely identify similar execution plans.

The

is a binary hash value calculated on the Transact-SQL text of a query, and

is used to uniquely identify queries.

A compiled plan can be retrieved from the plan cache using a

, which is a transient

identifier that remains constant only while the plan remains in the cache. The plan handle is a

hash value derived from the compiled plan of the entire batch. The plan handle for a compiled

plan remains the same even if one or more statements in the batch get recompiled.

７

Note

If a plan was compiled for a batch instead of a single statement, the plan for individual

statements in the batch can be retrieved using the plan handle and statement offsets. The

DMV contains the

and

columns for each record, which refer to the currently executing

statement of a currently executing batch or persisted object. For more information, see

. The

DMV also contains

these columns for each record, which refer to the position of a statement within a batch or

persisted object. For more information, see

.

The actual Transact-SQL text of a batch is stored in a separate memory space from the plan

cache, called the

SQL Manager

cache (SQLMGR). The Transact-SQL text for a compiled plan

can be retrieved from the sql manager cache using a

SQL Handle

, which is a transient identifier

that remains constant only while at least one plan that references it remains in the plan cache.

The sql handle is a hash value derived from the entire batch text and is guaranteed to be

unique for every batch.

The query below provides information about memory usage for the sql manager cache:

SQL

There is a 1:N relation between a sql handle and plan handles. Such a condition occurs when

the cache key for the compiled plans is different. This might occur due to change in SET

options between two executions of the same batch.

Consider the following stored procedure:

SQL

Verify what can be found in the plan cache using the query below:

SQL

７

Note

Like a compiled plan, the Transact-SQL text is stored per batch, including the comments.

The sql handle contains the MD5 hash of the entire batch text and is guaranteed to be

unique for every batch.

Here's the result set.

Output

Now execute the stored procedure with a different parameter, but no other changes to

execution context:

SQL

Verify again what can be found in the plan cache. Here's the result set.

Output

Notice the

has increased to 2, which means the same cached plan was reused as-is,

because the execution context data structures were reused. Now change the

option and execute the stored procedure using the same parameter.

SQL

Verify again what can be found in the plan cache. Here's the result set.

Output

```sql
sys.dm_exec_requests
```

```sql
statement_start_offset
```

```sql
statement_end_offset
```

```sql
sys.dm_exec_query_stats
```

```sql
SELECT
*
FROM
sys.dm_os_memory_objects
WHERE
type
=
'MEMOBJ_SQLMGR'
;
USE
WideWorldImporters;
GO
CREATE
PROCEDURE
usp_SalesByCustomer @CID
int
AS
SELECT
*
FROM
Sales.Customers
WHERE
CustomerID = @CID
GO
SET
ANSI_DEFAULTS
ON
GO
EXEC usp_SalesByCustomer 10
GO
```

```sql
SELECT
cp.memory_object_address, cp.objtype, refcounts, usecounts,
qs.query_plan_hash, qs.query_hash,
qs.plan_handle, qs.sql_handle
FROM
sys.dm_exec_cached_plans
AS
cp
CROSS
APPLY
sys.dm_exec_sql_text (cp.plan_handle)
CROSS
APPLY
sys.dm_exec_query_plan (cp.plan_handle)
INNER
JOIN
sys.dm_exec_query_stats
AS
qs
ON
qs.plan_handle = cp.plan_handle
WHERE
text
LIKE
'%usp_SalesByCustomer%'
GO
memory_object_address    objtype   refcounts   usecounts   query_plan_hash
query_hash
---------------------   -------  ---------  ---------  ------------------ ----------
--------
0x000001CC6C534060        Proc      2           1           0x3B4303441A1D7E6D
0xA05D5197DA1EAC2D
plan_handle
------------------------------------------------------------------------------------
------
0x0500130095555D02D022F111CD01000001000000000000000000000000000000000000000000000000
000000
sql_handle
------------------------------------------------------------------------------------
------
0x0300130095555D02C864C10061AB000001000000000000000000000000000000000000000000000000
000000
EXEC usp_SalesByCustomer 8
GO
memory_object_address    objtype   refcounts   usecounts   query_plan_hash
query_hash
---------------------   -------  ---------  ---------  ------------------ ----------
--------
0x000001CC6C534060        Proc      2           2           0x3B4303441A1D7E6D
```

```sql
usecounts
```

```sql
SET
ANSI_DEFAULTS
```

```sql
0xA05D5197DA1EAC2D
plan_handle
------------------------------------------------------------------------------------
------
0x0500130095555D02D022F111CD01000001000000000000000000000000000000000000000000000000
000000
sql_handle
------------------------------------------------------------------------------------
------
0x0300130095555D02C864C10061AB000001000000000000000000000000000000000000000000000000
000000
SET
ANSI_DEFAULTS
OFF
GO
EXEC usp_SalesByCustomer 8
GO
memory_object_address    objtype   refcounts   usecounts   query_plan_hash
query_hash
---------------------   -------  ---------  ---------  ------------------ ----------
--------
0x000001CD01DEC060        Proc      2           1           0x3B4303441A1D7E6D
0xA05D5197DA1EAC2D
0x000001CC6C534060        Proc      2           2           0x3B4303441A1D7E6D
0xA05D5197DA1EAC2D
plan_handle
------------------------------------------------------------------------------------
------
0x0500130095555D02B031F111CD01000001000000000000000000000000000000000000000000000000
000000
0x0500130095555D02D022F111CD01000001000000000000000000000000000000000000000000000000
000000
sql_handle
------------------------------------------------------------------------------------
------
0x0300130095555D02C864C10061AB000001000000000000000000000000000000000000000000000000
```
