---
name: 'sys.fn_builtin_permissions'
title: 'sys.fn_builtin_permissions'
category: 'system'
description: 'Azure SQL Managed Instance'
tags: ["function"]
pubDate: 2026-05-29
---

is a table-valued function that emits a copy of the predefined

permission hierarchy. This hierarchy includes covering permissions. The

result set

describes a directed, acyclic graph of the permissions hierarchy, of which the root is (class =

, permission =

).

does not accept correlated parameters.

will return an empty set when it is called with a class name that is

not valid.

The following image shows the permissions and their relationships to each other. Some of the

higher level permissions (such as

) are listed many times. In this article, the

poster is far too small to read. You can download the full-sized

in PDF format.

Requires membership in the public role.

## A. List all built in permissions

## B. List permissions that can be set on a symmetric key

## C. List classes on which there is a SELECT permission

Use

or an empty string to return all permissions.

SQL

Specify a class to return all possible permissions for that class.

SQL

SQL


## Permissions Hierarchy (Database Engine)
GRANT (Transact-SQL)

CREATE SCHEMA (Transact-SQL)

DROP SCHEMA (Transact-SQL)


## Permissions (Database Engine)
sys.fn_my_permissions (Transact-SQL)

HAS_PERMS_BY_NAME (Transact-SQL)

Last updated on 11/18/2025

See also

```sql
sys.fn_builtin_permissions
```

```sql
DEFAULT
```

```sql
SERVER
```

```sql
CONTROL SERVER
```

```sql
sys.fn_builtin_permissions
```

```sql
sys.fn_builtin_permissions
```

```sql
CONTROL SERVER
```

```sql
DEFAULT
```

```sql
SELECT
*
FROM
sys.fn_builtin_permissions(
DEFAULT
);
SELECT
*
FROM
sys.fn_builtin_permissions(
''
);
```

```sql
SELECT
*
FROM
sys.fn_builtin_permissions(N
'SYMMETRIC KEY'
);
```

```sql
SELECT
*
FROM
sys.fn_builtin_permissions(
DEFAULT
)
WHERE
permission_name =
'SELECT'
;
```
