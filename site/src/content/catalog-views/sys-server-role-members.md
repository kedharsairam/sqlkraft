---
name: "sys.server_role_members"
title: "sys.server_role_members"
category: "security"
description: "Returns one row for each member of each fixed and user-defined server role. Server-Principal ID of the role. Server-Principal ID of the member. To add or remove server role membership, use the ALTER SERVER ROLE (Transact-SQL) Logins can view their own server role membership and can view the principal_id's of the members of the fixed server roles."
tags: ["security","catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT
              roles.principal_id
              AS RolePrincipalID
              ,
              roles.name
              AS RolePrincipalName
---

## Description

Returns one row for each member of each fixed and user-defined server role. Server-Principal ID of the role. Server-Principal ID of the member. To add or remove server role membership, use the ALTER SERVER ROLE (Transact-SQL) Logins can view their own server role membership and can view the principal_id's of the members of the fixed server roles.

## Syntax

```sql
SELECT roles.principal_id
AS RolePrincipalID
,
roles.name
AS RolePrincipalName
```

## Permissions

Removes the specified server principal from the server role. server_principal can be a login or a user-defined server role. server_principal cannot be a fixed server role, a database role, or sa. Specifies the new name of the user-defined server role. This name cannot already exist in the server. Changing the name of a user-defined server role does not change ID number, owner, or permissions of the role. For changing role membership, replaces sp_addsrvrolemember and sp_dropsrvrolemember. These stored procedures are deprecated. You can view server roles by querying the and catalog views. To change the owner of a user-defined server role, use ALTER AUTHORIZATION (Transact-SQL). In Azure SQL Database, must be run in the database. Requires permission on the server to change the name of a user- defined server role. To add a member to a fixed server role, you must be a member of that fixed server role, or be a member of the fixed server role. ７ Note The and permissions are not sufficient to execute for a fixed server role, and permission cannot be granted on a fixed server role.
