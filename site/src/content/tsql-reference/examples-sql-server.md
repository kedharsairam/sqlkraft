---
name: "Examples: SQL Server"
title: "Examples: SQL Server"
category: "statements"
description: "permissions on the specified user name. When no execution context is specified,"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## A. Use EXECUTE to pass a single parameter

## B. Use multiple parameters

## permissions on the specified user name. When no execution context is specified,

or

is specified,

## permissions aren't required.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

The

stored procedure in the AdventureWorks2025 database expects

one parameter (

). The following examples execute the

stored procedure with

as its parameter value.

The variable can be explicitly named in the execution:

If the following is the first statement in a batch or a

sqlcmd

script,

isn't required.

The following example executes the

stored procedure in the

AdventureWorks2025 database. It passes two parameters: the first parameter is a product ID

(

) and the second parameter

is a

value.

## C. Use EXECUTE 'tsql_string' with a variable

## D. Use EXECUTE with a remote stored procedure

The following example shows how

handles dynamically built strings that contain

variables. This example creates the

cursor to hold a list of all user-defined tables

in the

database, and then uses that list to rebuild all indexes on the tables.

The following example executes the

stored procedure on the remote

server

and stores the return status that indicates success or failure in.

## E. Use EXECUTE with a stored procedure variable

## F. Use EXECUTE with DEFAULT

The following example creates a variable that represents a stored procedure name.

The following example creates a stored procedure with default values for the first and third

parameters. When the procedure is run, these defaults are inserted for the first and third

parameters when no value is passed in the call or when the default is specified. Note the

various ways the

keyword can be used.

The

stored procedure can be executed in many combinations.

## G. Use EXECUTE with AT

## linked_server_name

## H. Use EXECUTE WITH RECOMPILE

The following example passes a command string to a remote server. It creates a linked server

that points to another instance of SQL Server and executes a DDL statement

(

) against that linked server.

The following example executes the

stored procedure and forces a new

query plan to be compiled, used, and discarded after the module is executed.

## I. Use EXECUTE with a user-defined function

## J. Use EXECUTE to query an Oracle database on a linked server

The following example executes the

scalar user-defined function

in the AdventureWorks2025 database. It uses the variable

to store the value

returned by the function. The function expects one input parameter,. This is defined as

a

data type.

The following example executes several

statements at the remote Oracle server. The

example begins by adding the Oracle server as a linked server and creating linked server login.

### Applies to

## K. Use EXECUTE AS USER to switch context to another user

## L. Use a parameter with EXECUTE and AT

## linked_server_name

## M. Use EXECUTE to redefine a single result set

The following example executes a Transact-SQL string that creates a table and specifies the

clause to switch the execution context of the statement from the caller to. The

Database Engine checks the permissions of

when the statement is run.

must exist

as a user in the database and must have permission to create tables in the

schema, or

the statement fails.

The following example passes a command string to a remote server by using a question mark

(

) placeholder for a parameter. The example creates a linked server

that points

to another instance of SQL Server and executes a

statement against that linked server.

The

statement uses the question mark as a place holder for the

parameter

(

), which is provided after the statement.

: SQL Server 2012 (11.x) and later versions, and Azure SQL Database.

### Applies to

## N. Use EXECUTE to redefine a two result sets

Some of the previous examples executed

which

returned seven columns. The following example demonstrates using the

## syntax to change the names and data types of the returning result set.

: SQL Server 2012 (11.x) and later versions, and Azure SQL Database.

When executing a statement that returns more than one result set, define each expected result

set. The following example in

creates a procedure that returns two result

sets. Then the procedure is executed using the

clause, and specifying two

result set definitions.

### Applies to

### Applies to

## O. Use EXECUTE with AT DATA_SOURCE

## data_source_name

## to

## query a remote SQL Server

## P. Use EXECUTE with AT DATA_SOURCE

## data_source_name

## to

## query compute pool in SQL Server Big Data Cluster

## Q. Use EXECUTE with AT DATA_SOURCE

## data_source_name

## to

## query data pool in SQL Server Big Data Cluster

: SQL Server 2019 (15.x) and later versions.

The following example passes a command string to an external data source pointing to a SQL

Server instance.

: SQL Server 2019 (15.x).

The following example passes a command string to an external data source pointing to a

compute pool in SQL Server Big Data Cluster. The example creates a data source

against a compute pool in SQL Server Big Data Cluster and executes a

statement against the data source.

### Applies to

### Applies to

## R. Use EXECUTE with AT DATA_SOURCE

## data_source_name

## to

## query storage pool in SQL Server Big Data Cluster

`IMPERSONATE`

```sql
EXECUTE AS CALLER
```

`IMPERSONATE`

`AdventureWorks2025`

`AdventureWorksDW2025`

`uspGetEmployeeManagers`

```sql
@EmployeeID
```

`uspGetEmployeeManagers`

```sql
Employee ID 6
```

`EXECUTE`

`spGetWhereUsedProductID`

```sql
819
```

```sql
@CheckDate
```

```sql
EXECUTE dbo.uspGetEmployeeManagers 6;
GO
EXECUTE dbo.uspGetEmployeeManagers @EmployeeID = 6;
GO
EXECUTE dbo.uspGetEmployeeManagers 6;
GO
--Or
EXECUTE dbo.uspGetEmployeeManagers @EmployeeID = 6;
GO
```

`EXECUTE`

`tables_cursor`

`AdventureWorks2025`

`uspGetEmployeeManagers`

`SQLSERVER1`

```sql
@retstat
```

```sql
DECLARE
@CheckDate
AS
DATETIME;
SET
@CheckDate =
GETDATE ();
EXECUTE dbo.uspGetWhereUsedProductID 819, @CheckDate;
GO
```

```sql
DECLARE tables_cursor
CURSOR
FOR
SELECT s.name, t.name
FROM sys.objects
AS t
INNER
JOIN sys.schemas
AS s
ON s.schema_id = t.schema_id
WHERE t.type =
'U'
;
OPEN tables_cursor;
DECLARE
@schemaname
AS sysname;
DECLARE
@tablename
AS sysname;
FETCH NEXT FROM tables_cursor INTO @schemaname, @tablename;
WHILE (@@FETCH_STATUS <> -1)
BEGIN
EXECUTE (
'ALTER INDEX ALL ON '
+
@schemaname +
'.'
+
@tablename +
' REBUILD;'
);
FETCH NEXT FROM tables_cursor INTO @schemaname, @tablename;
END
PRINT
'The indexes on all tables have been rebuilt.'
;
CLOSE tables_cursor;
DEALLOCATE tables_cursor;
```

`DEFAULT`

`Proc_Test_Defaults`

```sql
DECLARE
@retstat
AS
INT
;
EXECUTE
@retstat = SQLSERVER1.AdventureWorks2022.dbo.uspGetEmployeeManagers
@BusinessEntityID = 6;
```

```sql
DECLARE
@proc_name
AS
VARCHAR (30);
SET
@proc_name =
'sys.sp_who'
;
EXECUTE
@proc_name;
```

```sql
IF OBJECT_ID(N'dbo.ProcTestDefaults', N'P') IS NOT NULL
DROP
PROCEDURE dbo.ProcTestDefaults;
GO
-- Create the stored procedure.
CREATE
PROCEDURE dbo.ProcTestDefaults (
@p1
SMALLINT
= 42,
@p2
CHAR (1),
@p3
VARCHAR (8) =
'CAR'
)
AS
SET
NOCOUNT
ON
;
SELECT
@p1, @p2, @p3;
GO
-- Specifying a value only for one parameter (@p2).
EXECUTE dbo.ProcTestDefaults @p2 =
'A'
;
```

`SeattleSales`

```sql
CREATE TABLE
```

`Proc_Test_Defaults`

```sql
-- Specifying a value for the first two parameters.
EXECUTE dbo.ProcTestDefaults 68,
'B'
;
-- Specifying a value for all three parameters.
EXECUTE dbo.ProcTestDefaults 68,
'C'
,
'House'
;
-- Using the DEFAULT keyword for the first parameter.
EXECUTE dbo.ProcTestDefaults
@p1 =
DEFAULT
,
@p2 =
'D'
;
-- Specifying the parameters in an order different from the order defined in the procedure.
EXECUTE dbo.ProcTestDefaults
DEFAULT
,
@p3 =
'Local'
,
@p2 =
'E'
;
-- Using the DEFAULT keyword for the first and third parameters.
EXECUTE dbo.ProcTestDefaults
DEFAULT
,
'H'
,
DEFAULT
;
EXECUTE dbo.ProcTestDefaults
DEFAULT
,
'I'
, @p3 =
DEFAULT
;
```

```sql
EXECUTE sp_addlinkedserver
'SeattleSales'
,
'SQL Server'
;
GO
EXECUTE (
'CREATE TABLE AdventureWorks2022.dbo.SalesTbl (SalesID INT, SalesName VARCHAR(10)); '
)
AT
SeattleSales;
GO
```

```sql
EXECUTE dbo.Proc_Test_Defaults @p2 =
'A'
WITH
RECOMPILE;
GO
```

`ufnGetSalesOrderStatusText`

```sql
@returnstatus
```

```sql
@Status
```

`SELECT`

```sql
DECLARE
@returnstatus
AS
NVARCHAR (15);
SET
@returnstatus =
NULL
;
EXECUTE
@returnstatus = dbo.ufnGetSalesOrderStatusText
@
Status
= 2;
PRINT @returnstatus;
GO
```

```sql
-- Setup the linked server.
EXECUTE sp_addlinkedserver
@
server
=
'ORACLE'
,
@srvproduct =
'Oracle'
,
@provider =
'OraOLEDB.Oracle'
,
@datasrc =
'ORACLE10'
;
EXECUTE sp_addlinkedsrvlogin
@rmtsrvname =
'ORACLE'
,
@useself =
'false'
,
@locallogin =
NULL
,
@rmtuser =
'scott'
,
@rmtpassword =
'tiger'
;
EXECUTE sp_serveroption
'ORACLE'
,
'rpc out'
,
true
;
GO
-- Execute several statements on the linked Oracle server.
EXECUTE (
'SELECT * FROM scott.emp'
)
AT
ORACLE
;
GO
EXECUTE (
'SELECT * FROM scott.emp WHERE MGR = ?'
, 7902)
AT
ORACLE
;
GO
```

```sql
AS
USER
```

`User1`

`User1`

`User1`

`Sales`

```sql
?
```

`SeattleSales`

`SELECT`

`SELECT`

`ProductID`

```sql
952
```

```sql
DECLARE
@v
AS
INT
;
SET
@v = 7902;
EXECUTE (
'SELECT * FROM scott.emp WHERE MGR = ?'
, @v)
AT
ORACLE
;
GO
```

```sql
EXECUTE (
'CREATE TABLE Sales.SalesTable (SalesID INT, SalesName VARCHAR(10));'
)
AS
USER
=
'User1'
;
GO
```

```sql
-- Setup the linked server.
EXECUTE sp_addlinkedserver
'SeattleSales'
,
'SQL Server'
;
GO
-- Execute the SELECT statement.
EXECUTE (
'SELECT ProductID, Name
FROM AdventureWorks2022.Production.Product
WHERE ProductID = ? '
, 952)
AT
SeattleSales;
GO
```

```sql
EXECUTE dbo.uspGetEmployeeManagers 6;
```

```sql
WITH RESULT SET
```

`AdventureWorks2025`

```sql
WITH RESULT SETS
```

```sql
EXECUTE uspGetEmployeeManagers 16
WITH
RESULT
SETS ((
[Reporting
Level
]
INT
NOT
NULL
,
[
ID of
Employee]
INT
NOT
NULL
,
[Employee
First
Name
]
NVARCHAR (50)
NOT
NULL
,
[Employee
Last
Name
]
NVARCHAR (50)
NOT
NULL
,
[Employee
ID of
Manager]
NVARCHAR (
MAX
)
NOT
NULL
,
[Manager
First
Name
]
NVARCHAR (50)
NOT
NULL
,
[Manager
Last
Name
]
NVARCHAR (50)
NOT
NULL
));
```

```sql
--Create the procedure
CREATE
PROCEDURE
Production.ProductList
@ProdName
NVARCHAR (50)
AS
-- First result set
SELECT
ProductID,
Name
,
ListPrice
FROM
Production.Product
WHERE
Name
LIKE
@ProdName;
-- Second result set
SELECT
Name
,
COUNT (S.ProductID)
AS
NumberOfOrders
FROM
Production.Product
AS
P
INNER
JOIN
Sales.SalesOrderDetail
AS
S
ON
P.ProductID = S.ProductID
WHERE
Name
LIKE
@ProdName
GROUP
BY
Name
;
GO
-- Execute the procedure
```

`SqlComputePool`

`SELECT`

```sql
EXECUTE
Production.ProductList
'%tire%'
WITH
RESULT
SETS (
-- first result set definition starts here (ProductID
INT
, [
Name
]
NAME
, ListPrice MONEY)
-- comma separates result set definitions
,
-- second result set definition starts here ([
Name
]
NAME
, NumberOfOrders
INT
)
);
```

```sql
EXECUTE (
'SELECT @@SERVERNAME'
)
AT
DATA_SOURCE my_sql_server;
GO
```

```sql
CREATE
EXTERNAL
DATA
SOURCE
SqlComputePool
WITH (LOCATION =
'sqlcomputepool://controller-svc/default'
);
EXECUTE (
'SELECT @@SERVERNAME'
)
AT
DATA_SOURCE SqlComputePool;
GO
```
