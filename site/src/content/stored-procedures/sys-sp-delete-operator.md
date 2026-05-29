---
name: "sys.sp_delete_operator"
title: "sp_delete_operator"
category: "general"
description: "Removes an operator. Transact-SQL syntax conventions The name of the operator to delete. , with no default. The name of an operator to whom the specified operator's alerts can be reassigned. @reassign_to_operator , with a default of"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_operator
  [ @name = ]
  N
  'name'
  [ , [ @reassign_to_operator = ]
  N
  'reassign_to_operator'
  ]
  [ ; ]
---

## Description

Removes an operator. Transact-SQL syntax conventions The name of the operator to delete. , with no default. The name of an operator to whom the specified operator's alerts can be reassigned. @reassign_to_operator , with a default of

## Syntax

```sql
sp_delete_operator
[ @name = ]
N
'name'
[ , [ @reassign_to_operator = ]
N
'reassign_to_operator'
]
[ ; ]
```

## Remarks

Applies to:

Removes an operator.

Transact-SQL syntax conventions

The name of the operator to delete.

, with no default.

The name of an operator to whom the specified operator's alerts can be reassigned.

@reassign_to_operator

, with a default of

(success) or

## Examples

### Example 1

```sql
sp_delete_operator
```

### Example 2

```sql
François Ajenstat
```

### Example 3

```sql
USE
msdb;
GO
EXECUTE
sp_delete_operator @
name
=
'François Ajenstat'
;
GO
```

### Example 4

```sql
USE
msdb;
GO
EXECUTE
dbo.sp_add_operator
@
name
= N
'Dan Wilson'
,
@enabled = 1,
@email_address = N
'danwi'
,
@pager_address = N
'5551290AW@pager.adventure-works.com'
,
@weekday_pager_start_time = 080000,
@weekday_pager_end_time = 170000,
@pager_days = 62;
GO
```
