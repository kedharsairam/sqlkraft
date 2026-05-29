---
name: 'sys.server_permissions'
title: 'sys.server_permissions'
category: 'security'
description: 'Any user can see their own permissions. To see permissions for other logins, requires VIEW'
tags: ["catalog-view", "security"]
pubDate: 2026-05-29
---

XA

EXTERNAL ACCESS

SERVER

XU

UNSAFE ASSEMBLY

SERVER

Any user can see their own permissions. To see permissions for other logins, requires VIEW

DEFINITION, ALTER ANY LOGIN, or any permission on a login. To see user-defined server roles,

requires ALTER ANY SERVER ROLE, or membership in the role.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following query lists the permissions explicitly granted or denied to server principals.

Security Catalog Views (Transact-SQL)

Securables

Catalog Views (Transact-SQL)


## Permissions (Database Engine)

## Permissions Hierarchy (Database Engine)
）

Important

The permissions of fixed server roles do not appear in sys.server_permissions. Therefore,

server principals may have additional permissions not listed here.

See Also

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pe.state_desc, pe.permission_name
FROM sys.server_principals AS pr
JOIN sys.server_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id;
```
