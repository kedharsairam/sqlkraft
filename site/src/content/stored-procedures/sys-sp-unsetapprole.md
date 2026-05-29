---
name: 'sys.sp_unsetapprole'
title: 'sp_unsetapprole'
category: 'general'
description: 'Deactivates an application role and reverts to the previous security context. Transact-SQL syntax conventions Specifies the cookie that was created when the application role was activated. , with no default. The cookie is created by 0 (success) and 1 (failure) is currently documented as which is the correct maximum length. However the current implementation returns . Applications should continue t'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_unsetapprole [ @cookie = ] cookie
  [ ; ]
---

## Description

Deactivates an application role and reverts to the previous security context. Transact-SQL syntax conventions Specifies the cookie that was created when the application role was activated. , with no default. The cookie is created by 0 (success) and 1 (failure) is currently documented as which is the correct maximum length. However the current implementation returns . Applications should continue to reserve so that the application continues to operate correctly if the cookie return size increases in a future release.

## Syntax

```sql
sp_unsetapprole [ @cookie = ] cookie
[ ; ]
```

## Remarks

Applies to:

Deactivates an application role and reverts to the previous security context.

Transact-SQL syntax conventions

Specifies the cookie that was created when the application role was activated.

, with no default. The cookie is created by

sp_setapprole

0 (success) and 1 (failure)

parameter for

is currently documented as

which is the correct maximum length. However the current

implementation returns

. Applications should continue to reserve

so that the application continues to operate correctly if the cookie return

size increases in a future release.
