---
title: "Specify parameters"
topic: "spatial-data"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  Azure Synapse Analytics
  
  Analytics Platform System (PDW)
  
  SQL database in Microsoft
  
  Fabric
  
  By specifying procedure parameters
tags:
  - "spatial-data"
  - "specify-parameters"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

By specifying procedure parameters, calling programs are able to pass values into the body of

the procedure. Those values can be used for various purposes during procedure execution.

Procedure parameters can also return values to the calling program if the parameter is marked

as an

parameter.

A procedure can have a maximum of 2,100 parameters; each assigned a name, data type, and

direction. Optionally, parameters can be assigned default values.

The following section provides information about passing values into parameters and about

how each of the parameter attributes is used during a procedure call.

The parameter values supplied with a procedure call must be constants or a variable; a function

name cannot be used as a parameter value. Variables can be user-defined or system variables

such as

.

The following examples demonstrate passing parameter values to the procedure

. They illustrate how to pass parameters as constants and variables

and also how to use a variable to pass the value of a function.

SQL

７

Note

Refer to the

series of sample databases for this article's exercises. For

more information, see

.

```sql
OUTPUT
@@spid
uspGetWhereUsedProductID
AdventureWorks
USE
AdventureWorks2022;
GO
-- Passing values as constants.
EXEC dbo.uspGetWhereUsedProductID 819, '20050225';
GO
-- Passing values as variables.
DECLARE
@ProductID
int
, @CheckDate datetime;
SET
@ProductID = 819;
SET
@CheckDate =
'20050225'
;
```