---
name: 'sys.server_principals'
title: 'sys.server_principals'
category: 'objects'
description: 'members of the server role'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

members of the server role

or special database role

in

the Microsoft Entra admin and SQL server admin

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

In Azure SQL Database, SQL logins are not persisted in the

catalog

view. Therefore, to retrieve the server-level role membership in Azure SQL Database, the

catalog view

needs to be joined.

The following query lists the permissions explicitly granted or denied to server principals.

SQL

Security Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Principals (Database Engine)


## Permissions Hierarchy (Database Engine)
）

Important

The permissions of fixed server roles (other than public) do not appear in

sys.server_permissions. Therefore, server principals may have additional permissions not

listed here.

Related content

```sql
master
```

```sql
sys.server_principals
```

```sql
sys.sql_logins
```

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
