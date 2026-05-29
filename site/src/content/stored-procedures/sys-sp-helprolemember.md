---
name: 'sys.sp_helprolemember'
title: 'sp_helprolemember'
category: 'general'
description: 'Returns information about the direct members of a role in the current database. Transact-SQL syntax conventions The name of a role in the current database. must exist in the current database. If isn''t specified, then all roles that contain at least one member from the current database are returned. Name of the role in the current database.'
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

```sql
sp_helprotect
```

### Example 2

```sql
sp_helprolemember
```

### Example 3

```sql
EXECUTE
sp_helprole;
```

### Example 4

```sql
MemberName
```

### Example 5

```sql
sp_helprolemember
```

### Example 6

```sql
User1
```

### Example 7

```sql
Role1
```

### Example 8

```sql
Role1
```

### Example 9

```sql
Role2
```

### Example 10

```sql
EXECUTE sp_helprolemember
'Role2';
```


*(... and 8 more examples)*
