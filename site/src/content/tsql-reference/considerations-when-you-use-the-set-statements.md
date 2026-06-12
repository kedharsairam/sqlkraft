---
name: "Considerations When You Use the SET Statements"
title: "Considerations When You Use the SET Statements"
category: "statements"
description: "SET TRANSACTION ISOLATION LEVEL"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

SET TRANSACTION ISOLATION LEVEL

SET XACT_ABORT

All SET statements run at execute or run time, except these statements, which run at parse

time:

SET FIPS_FLAGGER

SET OFFSETS

SET PARSEONLY

and SET QUOTED_IDENTIFIER

If a SET statement runs in a stored procedure or trigger, the value of the SET option gets

restored after the stored procedure or trigger returns control. Also, if you specify a SET

statement in a dynamic SQL string that runs by using either

or EXECUTE,

the value of the SET option gets restored after control returns from the batch that you

specified in the dynamic SQL string.

Stored procedures execute with the SET settings specified at execute time except for SET

ANSI_NULLS and SET QUOTED_IDENTIFIER. Stored procedures specifying SET

ANSI_NULLS or SET QUOTED_IDENTIFIER use the setting specified at stored procedure

creation time. If used inside a stored procedure, any SET setting is ignored.

The

setting of

allows for server-wide settings and works across

multiple databases. This setting also behaves like an explicit SET statement, except that it

occurs at login time.

Database settings set by using ALTER DATABASE are valid only at the database level and

take effect only if explicitly set. Database settings override instance option settings that

are set by using.

If a SET statement uses ON and OFF, you can specify either one for multiple SET options.

For example,

sets both QUOTED_IDENTIFIER and

ANSI_NULLS to ON.

７

Note

This doesn't apply to the statistics related SET options.

### sp_configure user options

### db1.dbo.sp1

### db2.dbo.sp2

### sp1

### db1

### sp2

### db2

SET statement settings override identical database option settings that are set by using

ALTER DATABASE. For example, the value specified in a SET ANSI_NULLS statement will

override the database setting for ANSI_NULLs. Additionally, some connection settings get

automatically set ON when a user connects to a database based on the values that go

into effect by the previous use of the

setting, or the values

that apply to all ODBC and OLE/DB connections.

ALTER, CREATE and DROP DATABASE statements don't honor the SET LOCK_TIMEOUT

setting.

When a global or shortcut SET statement sets several settings, issuing the shortcut SET

statement resets the previous settings for all those options that the shortcut SET

statement affects. If a SET option that gets affected by a shortcut SET statement gets set

after the shortcut SET statement gets issued, the individual SET statement overrides the

comparable shortcut settings. An example of a shortcut SET statement would be SET

ANSI_DEFAULTS.

When batches are used, the database context is determined by the batch that is

established by using the USE statement. Unplanned queries and all other statements that

run outside the stored procedure and that are in batches inherit the option settings of the

database and connection established by the USE statement.

Multiple Active Result Set (MARS) requests share a global state that contains the most

recent session SET option settings. When each request executes, it can modify the SET

options. The changes are specific to the request context in which they're set, and don't

affect other concurrent MARS requests. However, after the request execution is

completed, the new SET options are copied to the global session state. New requests that

execute under the same session after this change will use these new SET option settings.

When a stored procedure runs from a batch or from another stored procedure, it's run

under the option values set up in the database that has the stored procedure. For

example, when stored procedure

calls stored procedure

, stored

procedure

executes under the current compatibility level setting of database

, and

stored procedure

executes under the current compatibility level setting of database.

When a Transact-SQL statement concerns objects that are in multiple databases, the

current database context and the current connection context applies to that statement. In

this case, if Transact-SQL statement is in a batch, the current connection context is the

database defined by the USE statement; if the Transact-SQL statement is in a stored

procedure, the connection context is the database that contains the stored procedure.

When you're creating and manipulating indexes on computed columns or indexed views,

you must set these SET options to ON: ARITHABORT, CONCAT_NULL_YIELDS_NULL,

QUOTED_IDENTIFIER, ANSI_NULLS, ANSI_PADDING, and ANSI_WARNINGS. Set the option

NUMERIC_ROUNDABORT to OFF.

If you don't set any one of these options to the required values, INSERT, UPDATE, DELETE,

DBCC CHECKDB, and DBCC CHECKTABLE actions on indexed views or tables with indexes

on computed columns will fail. SQL Server will raise an error listing all the options that are

incorrectly set. Also, SQL Server will process SELECT statements on these tables or

indexed views as if the indexes on computed columns or on the views don't exist.

When SET RESULT_SET_CACHING is ON, it enables the result caching feature for the

current client session. Result_set_caching cannot be turned ON for a session if it is turned

OFF at the database level. When SET RESULT_SET_CACHING is OFF, the result set caching

feature is disabled for the current client session. Changing this setting requires

membership in the public role. Applies to: Azure Synapse Analytics Gen2

```sql
SET QUOTED_IDENTIFIER, ANSI_NULLS ON
```
