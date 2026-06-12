---
name: "sys.database_role_members"
title: "sys.database_role_members"
category: "security"
description: "Returns one row for each member of each database role. Database users, application roles, and other database roles can be members of a database role. To add members to a role, use the Database principal ID of the role. Database principal ID of the member. Any user can view their own role membership."
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
