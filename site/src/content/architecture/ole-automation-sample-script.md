---
title: "OLE automation sample script"
topic: "spatial-data"
description: |
  Article

  •

  10/17/2024

  Applies to:

  SQL Server

  This article contains an example of a Transact-SQL statement batch that uses the OLE

  Automation stored procedures to create and use a SQL-DMO SQLServe
tags:
  - "spatial-data"
  - "ole-automation-sample-script"
pubDate: 2025-12-01
---

Article

•

10/17/2024

Applies to:

SQL Server

This article contains an example of a Transact-SQL statement batch that uses the OLE

Automation stored procedures to create and use a SQL-DMO SQLServer object in the local

instance of the Database Engine. Parts of the code are used as examples in the reference

articles for the OLE Automation system stored procedures.

```sql
USE
AdventureWorks2022;
GO
DECLARE
@
Object int
;
DECLARE
@HR int
;
DECLARE
@Property nvarchar (255);
DECLARE
@
Return nvarchar (255);
DECLARE
@
Source nvarchar (255), @
Desc nvarchar (255);
-- Create a SQLServer object.
SET
NOCOUNT
ON
;
-- First, create the object.
EXEC @HR = sp_OACreate N'SQLDMO.SQLServer',
@Object OUT;
IF @HR <> 0
BEGIN
-- Report the error.
EXEC sp_OAGetErrorInfo @
Object
,
@
Source
OUT
,
@
Desc
OUT
;
SELECT
HR =
convert (varbinary(4),@HR),
Source
=@
Source
,
Description=@
Desc
;
GOTO END_ROUTINE
END
ELSE
-- A DMO.SQLServer object has been successfully created.
BEGIN
-- Specify Windows Authentication for connections.
EXEC @HR = sp_OASetProperty @
Object
,
N
'LoginSecure'
,
N
'TRUE'
;
IF @HR <> 0 GOTO CLEANUP
-- Set a property.
EXEC @HR = sp_OASetProperty @Object,
N'HostName',
N'SampleScript';
IF @HR <> 0 GOTO CLEANUP
```
