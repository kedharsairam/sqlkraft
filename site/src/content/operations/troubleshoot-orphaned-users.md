---
title: "Troubleshoot Orphaned Users"
topic: "high-availability"
description: |
  ﾃ

  Summarize this article for me

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  Users are orphaned in SQL Server wh
tags:
  - "high-availability"
  - "troubleshoot-orphaned-users"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

Users are orphaned in SQL Server when a database user is based on a login in the

database but the login no longer exists in

. This can occur when the login is deleted or

when the database is moved to another server on which the login doesn't exist. This article

describes how to find orphaned users and remap them to logins.

For connections to a database on an instance of SQL Server that use a security principal

(database user identity) based on a login, the principal must have a valid login in the

database. This login is used in the authentication process that verifies the principal's identity

and determines whether the principal is allowed to connect to the instance of SQL Server. The

SQL Server logins on a server instance are visible in the

sys.server_principals

catalog view and

the

sys.sql_logins

compatibility view.

SQL Server logins access individual databases as a "database user" that's mapped to the SQL

Server login. There are three exceptions to this rule:

Contained database users

Contained database users authenticate at the user-database level and aren't associated

with logins. This model is recommended because the databases are more portable, and

７

Note

Reduce the possibility of orphaned users by using contained database users for databases

that might be moved. For more information, see

.

）

Important

The

stored procedure was previously used to fix orphaned users

but is now deprecated. Use

instead, as described in the

section. For more information, see

.

```cmd
master master master sp_change_users_login
ALTER USER ... WITH LOGIN
```
