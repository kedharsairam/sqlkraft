---
name: 'ALTER AUTHORIZATION for databases'
title: 'ALTER AUTHORIZATION for databases'
category: 'statements'
description: 'The new owner principal must be one of the following:'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## For SQL Server

## For Azure SQL Database

The new owner principal must be one of the following:

A SQL Server authentication login.

A Windows authentication login representing a Windows user (not a group).

A Windows user that authenticates through a Windows authentication login representing

a Windows group.

If you are not

a member of the

fixed server role, you must have at least TAKE OWNERSHIP

permission on the database, and must have IMPERSONATE permission on the new owner login.

The new owner principal must be one of the following:

A SQL Server authentication login.

A federated user (not a group) present in Microsoft Entra ID.

A managed user (not a group) or an application present in Microsoft Entra ID.

If the new owner is a Microsoft Entra user, it cannot exist as a user in the database where the

new owner will become the new database owner (dbo). The Microsoft Entra user must first be

removed from the database before executing the ALTER AUTHORIZATION statement changing

the database ownership to the new user. For more information about configuring Microsoft

Entra users with SQL Database, see

Configure Microsoft Entra authentication

.

You must

connect to the target database to change the owner of that database.

The following types of accounts can change the owner of a database.

The service-level principal login, which is the SQL administrator provisioned when the

logical server in Azure

was created.

The Microsoft Entra administrator for the logical server..

The current owner of the database.

The following table summarizes the requirements:

ﾉ

Expand table

#### Executor

#### Target

#### Result

### db_owner

### db_owner

SQL Server Authentication login

SQL Server Authentication login

Success

SQL Server Authentication login

Microsoft Entra user

Fail

Microsoft Entra user

SQL Server Authentication login

Success

Microsoft Entra user

Microsoft Entra user

Success

To verify a Microsoft Entra owner of the database, execute the following Transact-SQL

command in a user database (in this example

).

SQL

The output will be a GUID (such as XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX) which

corresponds to the object ID of the Microsoft Entra user or service principal assigned as the

database owner. You can verify this by

checking the user's object ID in Microsoft Entra ID

.

When a SQL Server authentication login user is the database owner, execute the following

statement in the master database to verify the database owner:

SQL

Instead of using Microsoft Entra users as individual owners of the database, use a Microsoft

Entra group as a member of the

fixed database role. The following steps show how

to configure a disabled login as the database owner, and make a Microsoft Entra group

(

) a member of the

role.

1. Login to SQL Server as Microsoft Entra admin, and change the owner of the database to a

disabled SQL Server authentication login. For example, from the user database execute:

SQL

### db_owner

### db_owner

```sql
testdb
```

```sql
mydbogroup
```

```sql
SELECT
CAST
(owner_sid
as
uniqueidentifier)
AS
Owner_SID
FROM
sys.databases
WHERE
name
=
'testdb'
;
SELECT
d.name, d.owner_sid, sl.name
FROM
sys.databases
AS
d
JOIN
sys.sql_logins
AS
sl
ON
d.owner_sid = sl.sid;
```
