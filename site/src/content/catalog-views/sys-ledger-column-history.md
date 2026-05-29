---
name: 'sys.ledger_column_history'
title: 'sys.ledger_column_history'
category: 'objects'
description: 'SQL Server 2022 (16.x)'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

05/23/2023

Applies to:

SQL Server 2022 (16.x)

Azure SQL Database

Azure SQL Managed

Instance

Captures the cryptographically protected history of operations on columns of ledger tables:

adding, renaming, and dropping columns.

For more information on database ledger, see

Ledger


## Description
The object ID of the ledger table.

The column ID of the column in a ledger table.

The name of the column in ledger table. If the operation has

changed the column name, this column captures the new column

name.

The numeric value indicating the type of the operation

0 = CREATE – creating a column as part of creating the table

containing the column using CREATE TABLE.

1 = ADD – adding a column in a ledger table, using ALTER

TABLE/ADD COLUMN.

2 = RENAME - renaming a column in a ledger table.

3 = DROP - dropping a column in a ledger table.

Textual description of the value of operation_type.

A transaction ID that is unique for the database (it corresponds to

a transaction ID in the database transaction log).

The sequence number of the operation within the transaction.

Requires the

permission.

Consider the following sequence of operations on ledger tables.

ﾉ

Expand table

1. A user creates a ledger table.

SQL

2. A user adds a column to the ledger table.

SQL

3. A user renames a column of the ledger table.

SQL

4. A user drops a column of the ledger table.

SQL

The below query joins sys.ledger_column_history and sys.database_ledger_transactions to

produce the history of changes on ledger table columns, including the time of each and

change and the name of the user who triggered it.

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
ALTER
TABLE
[Employees]
ADD
Lastname
NVARCHAR
(256)
NULL
;
EXEC sp_rename 'dbo.Employees.Lastname', 'Firstname', 'COLUMN';
ALTER
TABLE
[Employees]
DROP
COLUMN
Firstname;
SELECT
t.[principal_name]
, t.[commit_time]
, h.[column_name]
AS
[column_name]
, h.[operation_type_desc]
FROM
sys.ledger_column_history h
JOIN
sys.database_ledger_transactions t
ON
h.transaction_id = t.transaction_id
ORDER
BY
t.[commit_time];
```
