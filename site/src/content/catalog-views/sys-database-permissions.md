---
name: 'sys.database_permissions'
title: 'sys.database_permissions'
category: 'security'
description: '## A. List all the permissions of database principals'
tags: ["catalog-view", "security"]
pubDate: 2026-05-29
---

## A. List all the permissions of database principals

## B. List permissions on schema objects within a database

Any user can see their own permissions. To see permissions for other users, requires VIEW

DEFINITION, ALTER ANY USER, or any permission on a user. To see user-defined roles, requires

ALTER ANY ROLE, or membership in the role (such as public).

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following query lists the permissions explicitly granted or denied to database principals.

SQL

The following query joins

sys.database_principals

and

to

sys.objects

and

sys.schemas

to list permissions granted or denied to specific schema objects.

SQL

）

Important

The permissions of fixed database roles do not appear in

.

Therefore, database principals may have additional permissions not listed here.

## C. List permissions for a specific object

You can use the previous example to query permissions specific to a single database object.

For example, consider the following granular permissions granted to a database user

in

the

sample database

:

SQL

Find the granular permissions assigned to

:

SQL


## Returns the output:
Securables


## Permissions Hierarchy (Database Engine)
Security Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Grant a Permission to a Principal

GRANT (Transact-SQL)

Last updated on 04/02/2026

See also

Next steps

```sql
sys.database_permissions
```

```sql
sys.database_permissions
```

```sql
SELECT
pr.principal_id
,pr.name
,pr.type_desc
,pr.authentication_type_desc
,pe.state_desc
,pe.permission_name
FROM
sys.database_principals
AS
pr
INNER
JOIN
sys.database_permissions
AS
pe
ON
pe.grantee_principal_id =
pr.principal_id;
```

```sql
SELECT
pr.principal_id
,pr.name
```

```sql
test
```

```sql
AdventureWorksDW2025
```

```sql
dbo.vAssocSeqOrders
```

```sql
,pr.type_desc
,pr.authentication_type_desc
,pe.state_desc
,pe.permission_name
,s.name +
'.'
+ o.name
AS
ObjectName
FROM
sys.database_principals
AS
pr
INNER
JOIN
sys.database_permissions
AS
pe
ON
pe.grantee_principal_id =
pr.principal_id
INNER
JOIN
sys.objects
AS
o
ON
pe.major_id = o.object_id
INNER
JOIN
sys.schemas
AS
s
ON
o.schema_id = s.schema_id
WHERE
pe.class = 1;
```

```sql
GRANT
SELECT
ON
dbo.vAssocSeqOrders
TO
[
test
];
SELECT
pr.principal_id
,pr.name
,pr.type_desc
,pr.authentication_type_desc
,pe.state_desc
,pe.permission_name
,s.name +
'.'
+ o.name
AS
ObjectName
FROM
sys.database_principals
AS
pr
INNER
JOIN
sys.database_permissions
AS
pe
ON
pe.grantee_principal_id =
pr.principal_id
INNER
JOIN
sys.objects
AS
o
ON
pe.major_id = o.object_id
INNER
JOIN
sys.schemas
AS
s
ON
o.schema_id = s.schema_id
WHERE
pe.class = 1
AND
o.name =
'vAssocSeqOrders'
AND
s.name =
'dbo'
;
```

```sql
principal_id    name    type_desc    authentication_type_desc    state_desc
permission_name    ObjectName
5    test    SQL_USER    INSTANCE    GRANT    SELECT    dbo.vAssocSeqOrders
```
