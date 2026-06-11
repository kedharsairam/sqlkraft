---
name: "sys.sp_helprolemember"
title: "sp_helprolemember"
category: "general"
description: "Returns information about the direct members of a role in the current database. Transact-SQL syntax conventions The name of a role in the current database. must exist in the current database. If isn't specified, then all roles that contain at least one member from the current database are returned."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helprolemember [ [ @rolename = ]
  N
  'rolename'
  ]
  [ ; ]
---

## Description

Returns information about the direct members of a role in the current database. Transact-SQL syntax conventions The name of a role in the current database. must exist in the current database. If isn't specified, then all roles that contain at least one member from the current database are returned. Name of the role in the current database.

## Syntax

```sql
sp_helprolemember [ [ @rolename = ]
N
'rolename'
]
[ ; ]
```

## Examples

### Example 1

`sp_helprotect`

### Example 2

`sp_helprolemember`

### Example 3

```sql
EXECUTE sp_helprole;
```

### Example 4

`MemberName`

### Example 5

`sp_helprolemember`

### Example 6

`User1`

### Example 7

`Role1`

### Example 8

`Role1`

### Example 9

`Role2`

### Example 10

```sql
EXECUTE sp_helprolemember
'Role2';
```

_(... and 8 more examples)_
