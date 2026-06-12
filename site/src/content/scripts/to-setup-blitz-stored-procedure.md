---
name: "To Setup Blitz Stored Procedure"
title: "To Setup Blitz Stored Procedure"
description: "Deploys Brent Ozar's sp_Blitz — the industry-standard SQL Server health check stored procedure from the First Responder Kit."
category: "performance"
tags: ["performance","monitoring","health-check","blitz"]
pubDate: "2025-03-15"
---

```sql
IF OBJECT_ID('dbo.sp_Blitz') IS NULL
 EXEC ('CREATE PROCEDURE dbo.sp_Blitz AS RETURN 0;');
GO

ALTER PROCEDURE [dbo].[sp_Blitz]
 @Help TINYINT = 0 ,
 @CheckUserDatabaseObjects TINYINT = 1 ,
 @CheckProcedureCache TINYINT = 0 ,
 @OutputType VARCHAR(20) = 'TABLE' ,
 @OutputProcedureCache TINYINT = 0 ,
 @CheckProcedureCacheFilter VARCHAR(10) = NULL ,
 @CheckServerInfo TINYINT = 0 ,
 @SkipChecksServer NVARCHAR(256) = NULL ,
 @SkipChecksDatabase NVARCHAR(256) = NULL ,
 @SkipChecksSchema NVARCHAR(256) = NULL ,
 @SkipChecksTable NVARCHAR(256) = NULL ,
 @IgnorePrioritiesBelow INT = NULL ,
 @IgnorePrioritiesAbove INT = NULL ,
 @OutputServerName NVARCHAR(256) = NULL ,
 @OutputDatabaseName NVARCHAR(256) = NULL ,
 @OutputDatabaseNameLong NVARCHAR(256) = NULL ,
 @EmailRecipients NVARCHAR(MAX) = NULL ,
 @EmailProfile sysname = NULL ,
 @SummaryMode TINYINT = 0 ,
 @BringThePain TINYINT = 0 ,
 @IgnoreDates NVARCHAR(MAX) = NULL ,
 @OutputXMLFileName NVARCHAR(MAX) = NULL ,
 @OutputXML XML = NULL ,
 @CompressXML TINYINT = 0 ,
 @Debug TINYINT = 0 ,
 @Version VARCHAR(30) = NULL OUTPUT ,
 @VersionDate DATETIME = NULL OUTPUT ,
 @VersionCheckMode TINYINT = 0
AS
 SET NOCOUNT ON;
 SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

 DECLARE @Version VARCHAR(30) = '8.01';
 DECLARE @VersionDate DATETIME = '20231013';
```

> **Note:** This is a reference stub for the sp_Blitz stored procedure. The full source code (~39,000 lines) is maintained by Brent Ozar as part of the [First Responder Kit](https://www.brentozar.com/first-aid/).
>
> Download the complete script: [github.com/BrentOzarULTD/SQL-Server-First-Responder-Kit](https://github.com/BrentOzarULTD/SQL-Server-First-Responder-Kit)
>
> To install: run the full `sp_Blitz.sql` from the repository against your SQL Server instance.
