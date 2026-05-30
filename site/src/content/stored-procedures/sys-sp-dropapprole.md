---
name: "sys.sp_dropapprole"
title: "sp_dropapprole"
category: "general"
description: "Removes an application role from the current database. Transact-SQL syntax conventions The application role to remove. , with no default. in the current database. can only be used to remove application roles. If a role owns any securables, the role can't be dropped. Before dropping an application role that owns securables, you must first transfer ownership of the securables, or drop them. This fea"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropapprole [ @rolename = ]
  N
  'rolename'
  [ ; ]
---

## Description

Removes an application role from the current database. Transact-SQL syntax conventions The application role to remove. , with no default. in the current database. can only be used to remove application roles. If a role owns any securables, the role can't be dropped. Before dropping an application role that owns securables, you must first transfer ownership of the securables, or drop them. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_dropapprole [ @rolename = ]
N
'rolename'
[ ; ]
```

## Remarks

Applies to:

Removes an application role from the current database.

Transact-SQL syntax conventions

The application role to remove.

, with no default.

in the current database.

(success) or

can only be used to remove application roles. If a role owns any securables, the

role can't be dropped. Before dropping an application role that owns securables, you must first

transfer ownership of the securables, or drop them.

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

## Examples

### Example 1

`sp_dropapprole`

### Example 2

```sql
ALTER ANY APPLICATION ROLE
```

### Example 3

`SalesApp`

### Example 4

```sql
EXECUTE sp_dropapprole
'SalesApp'
;
```
