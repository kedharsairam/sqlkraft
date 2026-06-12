---
name: "WITH GRANT OPTION"
title: "WITH GRANT OPTION"
category: "statements"
description: "Granting a permission removes"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Granting a permission removes

or

of that permission on the specified securable. If

the same permission is denied at a higher scope that contains the securable, the

takes

precedence. But revoking the granted permission at a higher scope doesn't take precedence.

Database-level permissions are granted within the scope of the specified database. If a user

needs permissions to objects in another database, create the user account in the other

database, or grant the user account access to the other database, as well as the current

database.

The

system stored procedure reports permissions on a database-level

securable.

In Microsoft Fabric,

can't be explicitly executed currently. When

or

is

executed, the user is created automatically.

The

specifies that the security principal receiving the permission

is given the ability to grant the specified permission to other security accounts. When the

principal that receives the permission is a role or a Windows group, the

clause must be

used when the object permission needs to be further granted to users who aren't members of

the group or role. Because only a user, rather than a group or role, can execute a

statement, a specific member of the group or role must use the

clause to explicitly invoke

the role or group membership when granting the permission. The following example shows

how the

is used when granted to a role or Windows group.

Ｕ

Caution

A table-level

does not take precedence over a column-level. This

inconsistency in the permissions hierarchy has been preserved for the sake of backward

compatibility. It will be removed in a future release.

### sysadmin

### db_owner

#### Securable

`DENY`

`REVOKE`

`DENY`

`sp_helprotect`

```sql
CREATE USER
```

`GRANT`

`DENY`

```sql
GRANT. WITH GRANT OPTION
```

`AS`

`GRANT`

`AS`

```sql
WITH GRANT OPTION
```

`DENY`

`GRANT`

```sql
-- Execute the following as a database owner
GRANT
EXECUTE
ON
TestProc
TO
TesterRole
WITH
GRANT
OPTION
;
EXEC sp_addrolemember TesterRole, User1;
-- Execute the following as User1
-- The following fails because User1 does not have the permission as the User1
GRANT
EXECUTE
ON
TestProc
TO
User2;
```
