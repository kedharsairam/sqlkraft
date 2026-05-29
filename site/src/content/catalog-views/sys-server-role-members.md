---
name: 'sys.server_role_members'
title: 'sys.server_role_members'
category: 'security'
description: '## A. Return list of server-role members'
tags: ["catalog-view", "security"]
pubDate: 2026-05-29
---

## A. Return list of server-role members

Article

•

04/15/2024

Applies to:

SQL Server

Azure SQL Managed Instance

Analytics Platform System

(PDW)


## Returns one row for each member of each fixed and user-defined server role.

## Description
Server-Principal ID of the role.

Server-Principal ID of the member.

To add or remove server role membership, use the

ALTER SERVER ROLE (Transact-SQL)

statement.

Logins can view their own server role membership and can view the principal_id's of the

members of the fixed server roles. To view all server role membership requires the

permission or membership in the

fixed server role.

Logins can also view role memberships of roles they own.

In Azure SQL Database, members of the server-role

can query all

catalog views.

For more information, see

Metadata Visibility Configuration

.

The examples in this section show how to work with server-level roles in Azure SQL Database.

The following example returns the names and IDs of the roles and their members.

ﾉ

Expand table

## B. Azure SQL Database: Listing all principals (SQL

## authentication) which are members of a server-level role

The following statement returns all members of any fixed server-level role using the

and

catalog views. This statement has to be run in

the virtual master database.

SQL

Catalog Views (Transact-SQL)

Security Catalog Views (Transact-SQL)

Server-Level Roles

Principals (Database Engine)

７

Note

In Azure SQL Database, SQL logins are not persisted in the

catalog

view. Therefore, to retrieve the server-level role membership in Azure SQL Database, the

catalog view

needs to be joined.

See Also

```sql
SELECT
roles.principal_id
AS RolePrincipalID
,
roles.name
AS RolePrincipalName
```

```sql
sys.server_role_members
```

```sql
sys.sql_logins
```

```sql
,
server_role_members.member_principal_id
AS MemberPrincipalID
,
members.name
AS MemberPrincipalName
FROM sys.server_role_members AS server_role_members
INNER JOIN sys.server_principals AS roles
ON server_role_members.role_principal_id = roles.principal_id
INNER JOIN sys.server_principals AS members
ON server_role_members.member_principal_id = members.principal_id
;
```

```sql
sys.server_principals
```

```sql
sys.sql_logins
```

```sql
SELECT
sql_logins.principal_id
AS
MemberPrincipalID
,
sql_logins.name
AS
MemberPrincipalName
,
roles.principal_id
AS
RolePrincipalID
,
roles.name
AS
RolePrincipalName
FROM
sys.server_role_members
AS
server_role_members
INNER
JOIN
sys.server_principals
AS
roles
ON
server_role_members.role_principal_id = roles.principal_id
INNER
JOIN
sys.sql_logins
AS
sql_logins
ON
server_role_members.member_principal_id = sql_logins.principal_id
;
GO
```
