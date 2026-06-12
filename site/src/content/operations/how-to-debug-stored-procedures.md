---
title: "How to: Debug Stored Procedures"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
    The Transact-SQL debugger allows you to interactively debug stored procedures by displaying
  
    the SQL call stack, local variables, and parameters for the SQL stored procedure. The Transact-
tags: ["ssb-diagnose","how-to-debug-stored-procedures"]
pubDate: "2025-12-01"
---

The Transact-SQL debugger allows you to interactively debug stored procedures by displaying

the SQL call stack, local variables, and parameters for the SQL stored procedure. The Transact-

SQL debugger supports viewing and modifying local variables and parameters, viewing global

variables. It also provides the ability to control and manage breakpoints when debugging your

Transact-SQL script.

This example shows how to create and debug a Transact-SQL stored procedure by stepping

into it.

1. In the Database Engine Query Editor window, connect to an instance of the SQL Server

Database Engine. Select a database in which you can create an example stored procedure.

2. Paste the following code in the Query Editor.

3. Press

to run the Transact-SQL code.

７

Note

Transact-SQL debugging isn't available for Azure SQL Database or Azure SQL Managed

Instance.

```cmd
CREATE
TABLE
[dbo].[Products] ([
Id
]
INT
, [
Name
]
NVARCHAR (128))
CREATE
PROCEDURE
[dbo].[AddProduct]
@
id
INT
,
@
name
NVARCHAR (128)
AS
BEGIN
INSERT
INTO
[dbo].[Products] ([
Id
], [
Name
])
VALUES (@
id
, @
name
)
SELECT
[
Name
]
FROM
[dbo].[Products]
WHERE
[
Id
] = @
id
DECLARE
@nextid
INT
SET
@nextid = @
id
+ 1
INSERT
INTO
[dbo].[Products] ([
Id
], [
Name
])
VALUES (@
id
, @
name
)
SELECT
[
Name
]
FROM
[dbo].[Products]
WHERE
[
Id
] = @nextid
END
```
