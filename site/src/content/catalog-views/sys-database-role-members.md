---
name: 'sys.database_role_members'
title: 'sys.database_role_members'
category: 'security'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "security"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric


## Returns one row for each member of each database role. Database users, application roles, and
other database roles can be members of a database role. To add members to a role, use the

ALTER ROLE

statement with the

option. Join with

sys.database_principals

to return

the names of the

values.


## Description
Database principal ID of the role.

Database principal ID of the member.

Any user can view their own role membership. To view other role memberships requires

membership in the

fixed database role or

on the database.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following query returns the members of the database roles.

ﾉ

Expand table

Security Catalog Views (Transact-SQL)

Principals (Database Engine)

Catalog Views (Transact-SQL)

ALTER ROLE (Transact-SQLL)

sys.server_role_members (Transact-SQL)

Last updated on 11/18/2025

See Also

```sql
ADD MEMBER
```

```sql
principal_id
```

```sql
db_securityadmin
```

```sql
VIEW DEFINITION
```

```sql
SELECT DP1.name AS DatabaseRoleName,
isnull (DP2.name, 'No members') AS DatabaseUserName
FROM sys.database_role_members AS DRM
RIGHT OUTER JOIN sys.database_principals AS DP1
ON DRM.role_principal_id = DP1.principal_id
LEFT OUTER JOIN sys.database_principals AS DP2
ON DRM.member_principal_id = DP2.principal_id
WHERE DP1.type = 'R'
ORDER BY DP1.name;
```
