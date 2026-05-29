---
name: 'sys.ledger_table_history'
title: 'sys.ledger_table_history'
category: 'objects'
description: 'Consider the following sequence of operations on ledger tables.'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Requires the

permission.

Consider the following sequence of operations on ledger tables.

1. A user creates a ledger table.

SQL

2. A user renames the ledger table.

SQL

3. A user renames the ledger view of the ledger table.

SQL

4. A user drops the ledger table.

SQL

The below query joins sys.ledger_table_history and sys.database_ledger_transactions to

produce the history of changes on ledger tables, including the time of each and change and

the name of the user who triggered it.

SQL

Ledger considerations and limitations

Ledger overview

See also

```sql
CREATE
TABLE
[Employees]
(
EmployeeID
INT
NOT
NULL
,
Salary Money
NOT
NULL
)
WITH
(SYSTEM_VERSIONING =
ON
, LEDGER =
ON
);
GO
EXEC sp_rename 'Employees', 'Employees_Copy';
EXEC sp_rename 'Employees_Ledger', 'Employees_Ledger_Copy';
DROP
TABLE
[Employees];
```

```sql
SELECT
t.[principal_name]
, t.[commit_time]
, h.[schema_name] +
'.'
+ h.[table_name]
AS
[table_name]
, h.[ledger_view_schema_name] +
'.'
+ h.[ledger_view_name]
AS
[view_name]
, h.[operation_type_desc]
FROM
sys.ledger_table_history h
JOIN
sys.database_ledger_transactions t
ON
h.transaction_id = t.transaction_id
```
