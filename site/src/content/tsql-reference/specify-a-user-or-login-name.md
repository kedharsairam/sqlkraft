---
name: "Specify a user or login name"
title: "Specify a user or login name"
category: "operators"
description: "Doesn't apply to dynamic queries inside the module."
tags: ["tsql","operators"]
pubDate: "2026-05-29"
---

Doesn't apply to dynamic queries inside the module.

Regardless of the execution context that is specified in the module, the following actions

always apply:

When the module is executed, the Database Engine first verifies that the user executing

the module has

permission on the module.

Ownership chaining rules continue to apply. This means if the owners of the calling and

called objects are the same, no permissions are checked on the underlying objects.

When a user executes a module that has been specified to run in a context other than

,

the user's permission to execute the module is checked, but additional permissions checks on

objects that are accessed by the module are performed against the user account specified in

the

clause. The user executing the module is, in effect, impersonating the specified

user.

The context specified in the

clause of the module is valid only for the duration of

the module execution. Context reverts to the caller when the module execution is completed.

A database user or server login specified in the

clause of a module can't be

dropped until the module is modified to execute under another context.

The user or login name specified in

clause must exist as a principal in

or

, respectively, or else the create or alter

module operation fails. Additionally, the user that creates or alters the module must have

IMPERSONATE permissions on the principal.

If the user has implicit access to the database or instance of SQL Server through a Windows

group membership, the user specified in the

clause is implicitly created when the

module is created when one of the following requirements exists:

The specified user or login is a member of the

fixed server role.

The user that is creating the module has permission to create principals.

When neither of these requirements are met, the create module operation fails.

）

Important

If the SQL Server (MSSQLSERVER) service is running as a local account (local service or

local user account), it will not have privileges to obtain the group memberships of a

`EXECUTE`

`CALLER`

```sql
EXECUTE AS
```

```sql
EXECUTE AS
```

```sql
EXECUTE AS
```

```sql
EXECUTE AS
```

`sys.database_principals`

`sys.server_principals`

```sql
EXECUTE AS
```
