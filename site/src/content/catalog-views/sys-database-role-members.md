---
name: "sys.database_role_members"
title: "sys.database_role_members"
category: "security"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns one row for each member of each database role. Database users, application roles, and other database roles can be members of a database role. To add members to a role, use the Database principal ID of the role. Database principal ID of the member. Any user can view their own role membership."
tags: ["security", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT DP1.name AS DatabaseRoleName,
  isnull (DP2.name, 'No members') AS DatabaseUserName
  FROM sys.database_role_members AS DRM
  RIGHT OUTER JOIN sys.database_principals AS DP1
  ON DRM.role_principal_id = DP1.principal_id
  LEFT OUTER JOIN sys.database_principals AS DP2
  ON DRM.member_principal_id = DP2.principal_id
  WHERE DP1.type = 'R'
  ORDER BY DP1.name;
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns one row for each member of each database role. Database users, application roles, and other database roles can be members of a database role. To add members to a role, use the Database principal ID of the role. Database principal ID of the member. Any user can view their own role membership. To view other role memberships requires

## Syntax

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

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Many of the system tables from earlier releases of SQL Server are now implemented as a set of views. These views are known as compatibility views, and they are meant for backward compatibility only. The compatibility views expose the same metadata that was available in SQL Server 2000 (8.x). However, the compatibility views do not expose any of the metadata related to features that are introduced in SQL Server 2005 (9.x) and later. Therefore, when you use new features, such as Service Broker or partitioning, you must switch to using the catalog views. Another reason for upgrading to the catalog views is that compatibility view columns that store user IDs and type IDs may return NULL or trigger arithmetic overflows. This is because you can create more than 32,767 users, groups, and roles, and 32,767 data types. For example, if you were to create 32,768 users, and then run the following query: . If ARITHABORT is set to ON, the query fails with an arithmetic overflow error. If ARITHABORT is set to OFF, the column returns NULL. To avoid these problems, we recommend that you use the new catalog views that can handle the increased number of user IDs and type IDs. The following table lists the columns that are subject to this overflow. SQL Server 2005 view ﾉ Expand table

## Examples

### Example 1

```sql
ADD MEMBER
```

### Example 2

`principal_id`

### Example 3

`db_securityadmin`

### Example 4

```sql
VIEW DEFINITION
```

### Example 5

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
