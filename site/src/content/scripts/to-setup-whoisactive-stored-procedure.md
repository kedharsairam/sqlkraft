---
name: "To Setup WhoIsActive Stored Procedure"
title: "To Setup WhoIsActive Stored Procedure"
description: "Deploys Adam Machanic's sp_WhoIsActive — the industry-standard real-time SQL Server activity monitoring stored procedure."
category: performance
tags: ["performance", "monitoring", "whoisactive"]
pubDate: 2025-03-15
---

```sql
SET QUOTED_IDENTIFIER ON;
SET ANSI_PADDING ON;
SET CONCAT_NULL_YIELDS_NULL ON;
SET ANSI_WARNINGS ON;
SET NUMERIC_ROUNDABORT OFF;
SET ARITHABORT ON;
GO

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_NAME = 'sp_WhoIsActive')
 EXEC ('CREATE PROC dbo.sp_WhoIsActive AS SELECT ''stub version, to be replaced''')
GO

/*********************************************************************************************
Who Is Active? v12.00 (2021-11-10) (C) 2007-2021, Adam Machanic

Feedback: https://github.com/amachanic/sp_whoisactive/issues
Releases: https://github.com/amachanic/sp_whoisactive/releases
Docs: http://whoisactive.com

License: https://github.com/amachanic/sp_whoisactive/blob/master/LICENSE
*********************************************************************************************/

ALTER PROC dbo.sp_WhoIsActive (
 --Filters - Both inclusive and exclusive
 --Set either filter to '' to disable
 --Valid filter types are: session, program, database, login, and host
 --Session is a session ID, and either 0 or '' can be used to indicate "all" sessions
```

> **Note:** This is a reference stub for the sp_WhoIsActive stored procedure. The full source code (~5,500 lines) is maintained by Adam Machanic.
>
> Download the complete script: [github.com/amachanic/sp_whoisactive](https://github.com/amachanic/sp_whoisactive)
>
> To install: run the full `sp_WhoIsActive.sql` from the repository against your SQL Server instance.
