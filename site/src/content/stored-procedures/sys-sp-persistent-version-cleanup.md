---
name: 'sys.sp_persistent_version_cleanup'
title: 'sys.sp_persistent_version_cleanup'
category: 'general'
description: 'SQL Server 2019 (15.x) and later versions'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

,

, or the

fixed database role in order to call the function

successfully.

(success), or

(failure).

Lock was successfully released.

Indicates parameter validation or other call error.

When an application calls

multiple times for the same lock resource,

must be called the same number of times to release the lock.

When the server shuts down for any reason, the locks are released.

Requires membership in the

role.

The following example releases the lock associated with the current transaction on the

resource

in the

database.

SQL

ﾉ

Expand table

```sql
>= 0
```

```sql
< 0
```

```sql
0
```

```sql
-999
```

```sql
sp_getapplock
```

```sql
sp_releaseapplock
```

```sql
Form1
```

```sql
AdventureWorks2025
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sp_getapplock
@DbPrincipal =
'dbo'
,
@
Resource
=
'Form1'
,
@LockMode =
'Shared'
;
EXECUTE
sp_releaseapplock
@DbPrincipal =
'dbo'
,
```
