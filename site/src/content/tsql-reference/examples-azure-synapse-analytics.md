---
name: "Examples: Azure Synapse Analytics"
title: "Examples: Azure Synapse Analytics"
category: "statements"
description: ": SQL Server 2019 (15.x)."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## A: Basic procedure execution

: SQL Server 2019 (15.x).

The following example passes a command string to an external data source pointing to

compute pool in SQL Server Big Data Cluster (BDC). The example creates a data source

against a data pool in BDC and executes a

statement against the data

source.

: SQL Server 2019 (15.x).

The following example passes a command string to an external data source pointing to

compute pool in SQL Server Big Data Cluster. The example creates a data source

against a data pool in SQL Server Big Data Cluster and executes a

statement against the data source.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

Execute a stored procedure:

## B: Execute strings

## C: Procedures with parameters

Call a stored procedure with name determined at runtime:

Call a stored procedure from within a stored procedure:

Execute a SQL string:

Execute a nested string:

Execute a string variable:

The following example creates a procedure with parameters and demonstrates three ways to

execute the procedure:

Execute using positional parameters:

Execute using named parameters in order:

Execute using named parameters out of order:

@@NESTLEVEL (Transact-SQL)

DECLARE @local_variable (Transact-SQL)

EXECUTE AS clause (Transact-SQL)

osql Utility

Principals (Database Engine)

REVERT (Transact-SQL)

sp_addlinkedserver (Transact-SQL)

Related content

sqlcmd Utility

SUSER_NAME (Transact-SQL)

sys.database_principals (Transact-SQL)

sys.server_principals (Transact-SQL)

USER_NAME (Transact-SQL)

OPENDATASOURCE (Transact-SQL)

Scalar User-Defined Functions for In-Memory OLTP

Last updated on 11/18/2025

`SqlDataPool`

`SELECT`

`SqlStoragePool`

`SELECT`

`AdventureWorks2025`

`AdventureWorksDW2025`

```sql
CREATE
EXTERNAL
DATA
SOURCE
SqlDataPool
WITH (LOCATION =
'sqldatapool://controller-svc/default'
);
EXECUTE (
'SELECT @@SERVERNAME'
)
AT
DATA_SOURCE SqlDataPool;
GO
```

```sql
CREATE
EXTERNAL
DATA
SOURCE
SqlStoragePool
WITH (LOCATION =
'sqlhdfs://controller-svc/default'
);
EXECUTE (
'SELECT @@SERVERNAME'
)
AT
DATA_SOURCE SqlStoragePool;
GO
```

```sql
EXECUTE proc1;
EXECUTE (
'EXECUTE '
+ @
var
);
CREATE sp_first
AS
EXECUTE sp_second;
EXECUTE sp_third;
```

```sql
EXECUTE (
'SELECT * FROM sys.types'
);
EXECUTE (
'EXECUTE (''SELECT * FROM sys.types'')'
);
DECLARE
@stringVar
AS
NVARCHAR (100);
SET
@stringVar = N
'SELECT name FROM'
+
' sys.sql_logins'
;
EXECUTE (@stringVar);
```

```sql
CREATE
PROCEDURE
ProcWithParameters (
@
name
NVARCHAR (50),
@color
NVARCHAR (15)
)
AS
SELECT
ProductKey,
EnglishProductName,
Color
FROM
[dbo].[DimProduct]
WHERE
EnglishProductName
LIKE
@namef
AND
Color = @color;
GO
EXECUTE
ProcWithParameters N
'%arm%'
, N
'Black'
;
EXECUTE
ProcWithParameters
@
name
= N
'%arm%'
,
@color = N
'Black'
;
EXECUTE
ProcWithParameters
@color = N
'Black'
,
@
name
= N
'%arm%'
;
GO
```
