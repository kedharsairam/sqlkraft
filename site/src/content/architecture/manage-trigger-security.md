---
title: "Manage Trigger Security"
topic: "change-data-capture"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  By default, both DML and DDL triggers execute under the context of the user that calls the

  t
tags:
  - "change-data-capture"
  - "manage-trigger-security"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

By default, both DML and DDL triggers execute under the context of the user that calls the

trigger. The caller of a trigger is the user that executes the statement that causes the trigger to

run. For example, if user

executes a DELETE statement that causes DML trigger

to run, the code inside

executes in the context of the user

privileges for

. This default behavior can be exploited by users who want to introduce

malicious code in the database or server instance. For example, the following DDL trigger is

created by user

:

SQL

What this trigger means is that as soon as a user that has permission to execute a

statement, such as a member of the

fixed server role, executes an

statement,

is granted

permission. In other words,

although

can't grant

permission to themselves, they enabled the

trigger code that grants them this permission to execute under escalated privileges. Both DML

and DDL triggers are open to this kind of security threat.

You can take the following measures to prevent trigger code from executing under escalated

privileges:

```sql
GRANT
CONTROL SERVER
ALTER TABLE
CONTROL SERVER
CONTROL SERVER
CREATE
TRIGGER
DDL_trigJohnDoe
ON
DATABASE
FOR
ALTER_TABLE
AS
SET
NOCOUNT
ON
;
BEGIN
TRY
EXEC(N
'
USE [master];
GRANT CONTROL SERVER TO [JohnDoe];
'
);
END
TRY
BEGIN
CATCH
DECLARE
@DoNothing
INT
;
END
CATCH;
GO
```
