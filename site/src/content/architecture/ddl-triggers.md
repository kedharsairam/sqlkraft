---
title: "DDL Triggers"
topic: "change-data-capture"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  DDL triggers fire in response to various Data Definition Language (DDL) events. These events
  
tags:
  - "change-data-capture"
  - "ddl-triggers"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

DDL triggers fire in response to various Data Definition Language (DDL) events. These events

primarily correspond to Transact-SQL statements that start with the keywords

,

,

,

,

,

, or

. Certain system stored procedures that

perform DDL-like operations can also fire DDL triggers.

Use DDL triggers when you want to do the following tasks:

Prevent certain changes to your database schema.

Have something occur in the database in response to a change in your database schema.

Record changes or events in the database schema.

A special type of Transact-SQL stored procedure that executes one or more Transact-SQL

statements in response to a server-scoped or database-scoped event. For example, a DDL

trigger might fire if a statement such as

is executed or if a table is

deleted by using

.

Instead of executing a Transact-SQL stored procedure, a common language runtime (CLR)

trigger executes one or more methods written in managed code that are members of an

assembly created in the .NET Framework and uploaded in SQL Server.

DDL triggers fire only after the DDL statements that trigger them are run. DDL triggers can't be

used as

triggers. DDL triggers don't fire in response to events that affect local or

global temporary tables and stored procedures.

）

Important

Test your DDL triggers to determine their responses to system stored procedures that are

run. For example, the

statement and the

stored procedure both

fire a DDL trigger that is created on a

event.

```sql
CREATE
ALTER
DROP
GRANT
DENY
REVOKE
UPDATE STATISTICS
ALTER SERVER CONFIGURATION
DROP TABLE
INSTEAD OF
CREATE TYPE
sp_addtype
CREATE_TYPE
```