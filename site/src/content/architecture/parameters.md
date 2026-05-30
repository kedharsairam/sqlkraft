---
title: "Parameters"
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

  Parameters are used to exchange da
tags:
  - "spatial-data"
  - "parameters"
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

Parameters are used to exchange data between stored procedures and functions and the

application or tool that called the stored procedure or function:

Input parameters allow the caller to pass a data value to the stored procedure or function.

Output parameters allow the stored procedure to pass a data value or a cursor variable

back to the caller. User-defined functions cannot specify output parameters.

Every stored procedure returns an integer return code to the caller. If the stored

procedure does not explicitly set a value for the return code, the return code is 0.

The following stored procedure shows the use of an input parameter, an output parameter,

and a return code:

```sql
-- Create a procedure that takes one input parameter and returns one output
parameter and a return code.
CREATE PROCEDURE SampleProcedure @EmployeeIDParm INT,
@MaxTotal INT OUTPUT
AS
-- Declare and initialize a variable to hold @@ERROR.
DECLARE @ErrorSave INT
SET @ErrorSave = 0
-- Do a SELECT using the input parameter.
SELECT FirstName, LastName, JobTitle
FROM HumanResources.vEmployee
WHERE EmployeeID = @EmployeeIDParm
-- Save any nonzero @@ERROR value.
IF (@@ERROR <> 0)
SET @ErrorSave = @@ERROR
-- Set a value in the output parameter.
SELECT @MaxTotal = MAX(TotalDue)
FROM Sales.SalesOrderHeader;
IF (@@ERROR <> 0)
SET @ErrorSave = @@ERROR
-- Returns 0 if neither SELECT statement had an error; otherwise, returns the last
error.
RETURN @ErrorSave
GO
```
