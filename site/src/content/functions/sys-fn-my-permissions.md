---
name: 'sys.fn_my_permissions'
title: 'sys.fn_my_permissions'
category: 'system'
description: 'Azure SQL Managed Instance'
tags: ["function"]
pubDate: 2026-05-29
---

the query fails.


## Description
Name of the securable on which the listed permissions are effectively

granted.

Column name if the securable has columns, otherwise

.

Name of the permission.

This table-valued function returns a list of the effective permissions held by the calling principal

on a specified securable. An effective permission is any one of the following options:

A permission granted directly to the principal, and not denied.

A permission implied by a higher-level permission held by the principal and not denied.

A permission granted to a role or group of which the principal is a member, and not

denied.

A permission held by a role or group of which the principal is a member, and not denied.

The permission evaluation is always performed in the security context of the caller. To

determine whether some other principal has an effective permission, the caller must have

permission on that principal.

For schema-level entities, one-, two-, or three-part non-null names are accepted. For database-

level entities, a one-part name is accepted, with a null value meaning the

current database

. For

the server itself, a null value (meaning the

current server

) is required.

can't

check permissions on a linked server.

The following query returns a list of built-in securable classes:

SQL

If

is supplied as the value of

securable

or

securable_class

, the value is interpreted as

.

ﾉ

Expand table

```sql
entity_name
```

```sql
subentity_name
```

```sql
NULL
```

```sql
permission_name
```

```sql
IMPERSONATE
```

```sql
fn_my_permissions
```

```sql
DEFAULT
```

```sql
NULL
```

```sql
SELECT
DISTINCT
class_desc
FROM
fn_builtin_permissions(
DEFAULT
)
ORDER
BY
class_desc;
GO
```
