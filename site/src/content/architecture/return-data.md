---
title: "Return data"
topic: "spatial-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Azure Synapse Analytics

  SQL database in Microsoft Fabric

  There are three ways of returning data from a procedure to a calling
tags:
  - "spatial-data"
  - "return-data"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

SQL database in Microsoft Fabric

There are three ways of returning data from a procedure to a calling program: result sets,

output parameters, and return codes. This article provides information on the three

approaches.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

If you include a

statement in the body of a stored procedure (but not a

or

), the rows specified by the

statement are sent directly to the

client. For large result sets, the stored procedure execution won't continue to the next

statement until the result set has been completely sent to the client. For small result sets, the

results are spooled for return to the client and execution continues. If multiple such

statements are run during the execution of the stored procedure, multiple result sets are sent

to the client. This behavior also applies to nested Transact-SQL batches, nested stored

procedures, and top-level Transact-SQL batches.

This example shows a stored procedure that returns the

and

values for all

rows that also appear in the

view.

SQL

```sql
AdventureWorks2025
AdventureWorksDW2025
SELECT
SELECT ...
INTO
INSERT ... SELECT
SELECT
SELECT
LastName
SalesYTD
SalesPerson
vEmployee
USE
AdventureWorks2022;
GO
IF OBJECT_ID('Sales.uspGetEmployeeSalesYTD', 'P') IS NOT NULL
DROP
PROCEDURE
Sales.uspGetEmployeeSalesYTD;
GO
CREATE
PROCEDURE
Sales.uspGetEmployeeSalesYTD
AS
SET
NOCOUNT
ON
;
SELECT
LastName,
SalesYTD
FROM
Sales.SalesPerson
AS
sp
```
