---
name: 'sys.fn_validate_plan_guide'
title: 'sys.fn_validate_plan_guide'
category: 'date-time'
description: 'Azure SQL Managed Instance'
tags: ["function"]
pubDate: 2026-05-29
---

## A. Validating all plan guides in a database

## B. Testing plan guide validation before implementing a

## change to the database


## Description
state

State number of the error indicating the point in the code in which the

error occurred.

message

Message text of the error.

OBJECT-scoped plan guides require VIEW DEFINITION or ALTER permission on the referenced

object and permissions to compile the query or batch that is provided in the plan guide. For

example, if a batch contains SELECT statements, SELECT permissions on the referenced objects

are required.

SQL- or TEMPLATE-scoped plan guides require ALTER permission on the database and


## permissions to compile the query or batch that is provided in the plan guide. For example, if a
batch contains SELECT statements, SELECT permissions on the referenced objects are required.

The

function is not available in Azure SQL Database.

The following example checks the validity of all plan guides in the current database. If an

empty result set is returned, all plan guides are valid.

SQL

The following example uses an explicit transaction to drop an index. The

function is executed to determine whether this action will

invalidate any plan guides in the database. Based on the results of the function, the

statement is either committed or the transaction is rolled back, and the index is not dropped.

SQL

Plan Guides

sp_create_plan_guide (Transact-SQL)

sp_create_plan_guide_from_handle (Transact-SQL)

See Also

```sql
sys.fn_validate_plan_guide
```

```sql
USE
AdventureWorks2022;
GO
SELECT
plan_guide_id, msgnum, severity, state, message
FROM
sys.plan_guides
CROSS
APPLY
fn_validate_plan_guide(plan_guide_id);
GO
```

```sql
sys.fn_validate_plan_guide
```

```sql
DROP INDEX
```

```sql
USE
AdventureWorks2022;
GO
BEGIN
TRANSACTION
;
DROP
INDEX
IX_SalesOrderHeader_CustomerID
ON
Sales.SalesOrderHeader;
-- Check for invalid plan guides.
IF EXISTS (
SELECT
plan_guide_id, msgnum, severity, state, message
FROM
sys.plan_guides
CROSS
APPLY
sys.fn_validate_plan_guide(plan_guide_id))
ROLLBACK
TRANSACTION
;
ELSE
COMMIT
TRANSACTION
;
GO
```
