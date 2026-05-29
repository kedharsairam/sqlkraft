---
name: 'sys.database_principals'
title: 'sys.database_principals'
category: 'objects'
description: '## C: Listing all the permissions of database principals'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## C: Listing all the permissions of database principals

The following query lists the permissions explicitly granted or denied to database principals.

The following query joins sys.database_principals and sys.database_permissions to sys.objects

and sys.schemas to list permissions granted or denied to specific schema objects.

）

Important

The permissions of fixed database roles do not appear in sys.database_permissions.

Therefore, database principals may have additional permissions not listed here.

## D: Listing permissions on schema objects within a database

The following query lists the permissions explicitly granted or denied to database principals.

The following query joins

and

to

and

to list permissions granted or denied to specific schema objects.

Principals (Database Engine)

sys.server_principals (Transact-SQL)

Security Catalog Views (Transact-SQL)

Contained Database Users - Making Your Database Portable

Connecting to Azure SQL with Microsoft Entra authentication

Last updated on 11/18/2025

）

Important

The permissions of fixed database roles do not appear in

.

Therefore, database principals may have additional permissions not listed here.

See Also

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pr.authentication_type_desc, pe.state_desc, pe.permission_name
FROM sys.database_principals AS pr
JOIN sys.database_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id;
```

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pr.authentication_type_desc, pe.state_desc,
pe.permission_name, s.name + '.' + o.name AS ObjectName
FROM sys.database_principals AS pr
JOIN sys.database_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id
JOIN sys.objects AS o
ON pe.major_id = o.object_id
JOIN sys.schemas AS s
ON o.schema_id = s.schema_id;
```

```sql
sys.database_principals
```

```sql
sys.database_permissions
```

```sql
sys.objects
```

```sql
sys.schemas
```

```sql
sys.database_permissions
```

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pr.authentication_type_desc, pe.state_desc, pe.permission_name
FROM sys.database_principals AS pr
JOIN sys.database_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id;
```

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pr.authentication_type_desc, pe.state_desc,
pe.permission_name, s.name + '.' + o.name AS ObjectName
FROM sys.database_principals AS pr
JOIN sys.database_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id
JOIN sys.objects AS o
ON pe.major_id = o.object_id
JOIN sys.schemas AS s
ON o.schema_id = s.schema_id;
```
