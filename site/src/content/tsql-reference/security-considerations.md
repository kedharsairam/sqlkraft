---
name: "Security considerations"
title: "Security considerations"
category: "statements"
description: "principal must exist even when the user is accessing the database or instance of SQL Server"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

principal must exist even when the user is accessing the database or instance of SQL Server

through a Windows group membership. For example, assume the following conditions:

group has access to the

database.

is a member of

SQLUsers

and, therefore, has implicit access

to the

database.

Although

has access to the database through membership in the

SQLUsers

group, the statement

fails because

does not exist as a principal in the database.

If the user is orphaned (the associated login no longer exists), and the user was not created

with

,

will fail for the user.

Specify a login or user that has the least privileges required to perform the operations in the

session. For example, do not specify a login name with server-level permissions, if only

database-level permissions are required; or do not specify a database owner account unless

those permissions are required.

Executing under the dbo ownership context, for example by using the statement

, changes how explicit DENY permissions are evaluated. When you switch the

execution context to the dbo ownership context, permission-based DENY restrictions that

apply to the original calling principal aren't enforced for the duration of the impersonation. As

a result, a principal that can switch execution context to dbo, for example through membership

in the db_owner fixed database role, can perform actions that would otherwise be blocked by

explicit DENY permissions applied to that principal.

Ｕ

Caution

The EXECUTE AS statement can succeed as long as the Database Engine can resolve the

name. If a domain user exists, Windows might be able to resolve the user for the Database

Engine, even though the Windows user does not have access to SQL Server. This can lead

to a condition where a login with no access to SQL Server appears to be logged in, though

the impersonated login would only have the permissions granted to public or guest.

### EXECUTE AS

### IMPERSONATE

### IMPERSONATE ANY LOGIN

### EXECUTE AS

### IMPERSONATE

### EXECUTE AS CALLER

### IMPERSONATE

```sql
EXECUTE AS USER = 'CompanyDomain\SqlUser1'
```

```sql
CompanyDomain\SqlUser1
```

```sql
EXECUTE AS
USER = 'dbo'
```
