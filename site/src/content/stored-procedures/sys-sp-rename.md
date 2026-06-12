---
name: "sys.sp_rename"
title: "sp_rename"
category: "general"
description: "SQL analytics endpoint in Microsoft Fabric Changes the name of a user-created object in the current database. This object can be a table, index, column, alias data type, or Microsoft .NET Framework common language runtime (CLR) user-defined type. in SQL Server and Azure SQL Database: (preview) in Azure Synapse Analytics: Some system objects and Transact-SQL syntax a"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_rename"
---

## Description

SQL analytics endpoint in Microsoft Fabric Changes the name of a user-created object in the current database. This object can be a table, index, column, alias data type, or Microsoft.NET Framework common language runtime (CLR) user-defined type.

## Syntax

`sp_rename`

## Permissions

the PRIMARY KEY constraint is also automatically renamed by. can be used to rename primary and secondary XML indexes. Renaming a stored procedure, function, view, or trigger won't change the name of the corresponding object either in the definition column of the sys.sql_modules catalog view or obtained using the OBJECT_DEFINITION built-in function. Therefore, we recommend that not be used to rename these object types. Instead, drop and re-create the object with its new name. SQL Server (all supported versions), Azure SQL Database, and Azure Synapse Analytics: Renaming an object such as a table or column won't automatically rename references to that object. You must modify any objects that reference the renamed object manually. For example, if you rename a table column and that column is referenced in a trigger, you must modify the trigger to reflect the new column name. Use sys.sql_expression_dependencies to list dependencies on the object before renaming it. Renaming a column doesn't automatically update the metadata for any objects which SELECT all columns (using the ) from that table. For example, if you rename a table column and that column is referenced by a non-schema-bound view or function that SELECTs all columns (using the ), the metadata for the view or function continues to reflect the original column name. Refresh the metadata using sp_refreshsqlmodule or sp_refreshview. You can change the name of an object or data type in the current database only. The names of most system data types and system objects can't be changed. If you use more than 128 characters for the new name, only the first 128 characters are used and the rest is truncated. Azure Synapse Analytics: In Azure Synapse Analytics, is in for dedicated SQL pools. To rename objects, columns, and indexes, requires ALTER permission on the object. To rename user types, requires CONTROL permission on the type. To rename a database, requires membership in the or fixed server roles. To rename a ledger table, ALTER LEDGER permission is required.

## Examples

### Example 1

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
WITH (SYSTEM_VERSIONING =
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

### Example 2

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
WITH (SYSTEM_VERSIONING =
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
NVARCHAR (256)
NULL
;
EXEC sp_rename 'dbo.Employees.Lastname', 'Firstname', 'COLUMN';
ALTER
TABLE
[Employees]
DROP
COLUMN
Firstname;
SELECT t.[principal_name]
, t.[commit_time]
, h.[column_name]
AS
[column_name]
, h.[operation_type_desc]
FROM sys.ledger_column_history h
JOIN sys.database_ledger_transactions t
ON h.transaction_id = t.transaction_id
ORDER
BY t.[commit_time];
```

### Example 3

`sys.sql_modules`

### Example 4

`sp_rename`

### Example 5

```sql
SELECT sm.object_id,
ss.[
name
]
AS
[
schema
],
o.[
name
]
AS object_name,
o.[
type
],
o.[type_desc],
sm.[definition]
FROM sys.sql_modules
AS sm
INNER
JOIN sys.objects
AS o
ON sm.object_id = o.object_id
INNER
JOIN sys.schemas
AS ss
ON o.schema_id = ss.schema_id
ORDER
BY o.[
type
], ss.[
name
], o.[
name
];
```
