---
name: "sys.sp_getapplock"
title: "sp_getapplock"
category: "general"
description: "SQL database in Microsoft Fabric Places a lock on an application resource. Transact-SQL syntax conventions A string specifying a name that identifies the lock resource. . If a resource string is longer than The application must ensure that the resource name is unique. The specified name is hashed internally into a value that can be stored in the SQL Server lock manager. is binary-compared, and thu"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_getapplock
  [ [ @
  R
  esource = ]
  N
  'Resource'
  ]
  , [ @
  L
  ock
  M
  ode = ]
  'LockMode'
  [ , [ @
  L
  ock
  O
  wner = ]
  'LockOwner'
  ]
  [ , [ @
  L
  ock
  T
  imeout = ]
  L
  ock
  T
  imeout ]
  [ , [ @
  D
  b
  P
  rincipal = ]
  N
  'DbPrincipal'
  ]
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Places a lock on an application resource. Transact-SQL syntax conventions A string specifying a name that identifies the lock resource. . If a resource string is longer than The application must ensure that the resource name is unique. The specified name is hashed internally into a value that can be stored in the SQL Server lock manager. is binary-compared, and thus is case-sensitive regardless of the collation settings of

## Syntax

```sql
sys.sp_getapplock
[ [ @
R
esource = ]
N
'Resource'
]
, [ @
L
ock
M
ode = ]
'LockMode'
[ , [ @
L
ock
O
wner = ]
'LockOwner'
]
[ , [ @
L
ock
T
imeout = ]
L
ock
T
imeout ]
[ , [ @
D
b
P
rincipal = ]
N
'DbPrincipal'
]
[ ; ]
```

## Examples

### Example 1

```sql
sp_getapplock
```

### Example 2

```sql
sys.dm_tran_locks
```

### Example 3

```sql
sp_lock
```

### Example 4

```sql
Form1
```

### Example 5

```sql
AdventureWorks2025
```

### Example 6

```sql
dbo
```

### Example 7

```sql
BEGIN
ROLLBACK
;
END
ELSE
BEGIN
EXECUTE
@
result
= sp_releaseapplock
@
Resource
=
'Form1'
;
COMMIT
TRANSACTION
;
END
GO
```

### Example 8

```sql
USE
AdventureWorks2025;
GO
BEGIN
TRANSACTION
;
DECLARE
@
result
AS
INT
;
EXECUTE
@
result
= sp_getapplock
@
Resource
=
'Form1'
,
@LockMode =
'Shared'
;
COMMIT
TRANSACTION
;
GO
```

### Example 9

```sql
BEGIN
TRANSACTION
;
EXECUTE
sp_getapplock
@DbPrincipal =
'dbo'
,
@
Resource
=
'AdventureWorks2025'
,
@LockMode =
'Shared'
;
COMMIT
TRANSACTION
;
GO
```

### Example 10

```sql
@
Resource
=
'Form1'
;
GO
```

_(... and 2 more examples)_
