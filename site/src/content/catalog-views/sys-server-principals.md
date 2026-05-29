---
name: 'sys.server_principals'
title: 'sys.server_principals'
category: 'compatibility'
description: 'Azure SQL Managed Instance Returns the login identification number of the user. Transact-SQL syntax conventions Is the login name of the user. is specified as can be any SQL Server login or Windows user or group that has permission to connect to an instance of SQL Server. If is not specified, the login identification number for the current user is returned. If the parameter contains the word NULL '
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT pr.principal_id, pr.name, pr.type_desc,
  pe.state_desc, pe.permission_name
  FROM sys.server_principals AS pr
  JOIN sys.server_permissions AS pe
  ON pe.grantee_principal_id = pr.principal_id;
---

## Description

Azure SQL Managed Instance Returns the login identification number of the user. Transact-SQL syntax conventions Is the login name of the user. is specified as can be any SQL Server login or Windows user or group that has permission to connect to an instance of SQL Server. If is not specified, the login identification number for the current user is returned. If the parameter contains the word NULL will return NULL. SUSER_ID returns an identification number only for logins that have been explicitly provisioned inside SQL Server. This ID is used within SQL Server to track ownership and permissions. This ID is not equivalent to the SID of the login that is returned by SUSER_SID. If is a SQL Server Starting with SQL Server 2005 (9.x), SUSER_ID returns the value listed as Azure SQL Database Azure SQL Managed Instance

## Syntax

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pe.state_desc, pe.permission_name
FROM sys.server_principals AS pr
JOIN sys.server_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id;
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Analytics Platform System (PDW) Returns one row for every SQL Server authentication login. Description N/A Inherits from . Password policy is checked. Password expiration is checked. Hash of SQL login password. In SQL Server 2022 (16.x) and earlier versions, the stored password information is calculated using SHA-512 of the salted password. Starting with SQL Server 2025 (17.x), an iterated hash algorithm, RFC2898 (PBKDF), is used. The first byte of the hash indicates the version: for version 2 (SQL Server 2022 (16.x) and earlier versions) and for version 3 (SQL Server 2025 (17.x) and later versions). For a list of columns that this view inherits, see sys.server_principals . The columns and isn't inherited from sys.server_principals. To view both SQL Server authentication logins and Windows authentication logins, see sys.server_principals . When contained database users are enabled, connections can be made without logins. To identify those accounts, see sys.database_principals . In SQL Server, any SQL Server authentication login can see their own login name, and the login. To see other logins, the principal requires , , or a permission on the login. ﾉ Expand table Description sys.login_token (Transact-SQL) sys.server_principals (Transact-SQL) sys.database_principals (Transact-SQL) Principals (Database Engine) Last updated on 11/18/2025 See Also Description sys.user_token (Transact-SQL) sys.server_principals (Transact-SQL) sys.database_principals (Transact-SQL) Principals (Database Engine) See Also

## Remarks

Applies to:

Azure SQL Managed Instance

Returns the login identification number of the user.

Transact-SQL syntax conventions

Is the login name of the user.

is specified as

is implicitly

converted to

can be any SQL Server login or Windows user or group that has

permission to connect to an instance of SQL Server. If

is not specified, the login

identification number for the current user is returned. If the parameter contains the word NULL

will return NULL.

SUSER_ID returns an identification number only for logins that have been explicitly provisioned

inside SQL Server. This ID is used within SQL Server to track ownership and permissions. This ID

is not equivalent to the SID of the login that is returned by SUSER_SID. If

is a SQL Server

Starting with SQL Server 2005 (9.x), SUSER_ID returns the value listed as

catalog view.

Applies to:

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Returns the login name associated with a security identification number (SID).

Transact-SQL syntax conventions

The optional login security identification number.

server_user_sid

server_user_sid

can be the security identification number of any SQL Server login or Microsoft

Windows user or group. Refer to the

catalog views. If

server_user_sid

isn't specified, information about the current user is returned. If

the parameter contains the word

server_user_sid

is not supported on Azure SQL Database or SQL database in Microsoft Fabric.

can be used as a

constraint in either

can be used in a select list, in a

clause, and anywhere an expression is

must always be followed by parentheses, even if no parameter is

## Examples

### Example 1

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pe.state_desc, pe.permission_name
FROM sys.server_principals AS pr
JOIN sys.server_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id;
```

### Example 2

```sql
master
```

### Example 3

```sql
sys.server_principals
```

### Example 4

```sql
sys.sql_logins
```

### Example 5

```sql
SELECT
pr.principal_id, pr.name, pr.type_desc,
pe.state_desc, pe.permission_name
FROM
sys.server_principals
AS
pr
JOIN
sys.server_permissions
AS
pe
ON
pe.grantee_principal_id = pr.principal_id;
```
