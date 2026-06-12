---
name: "sys.sp_helprotect"
title: "sp_helprotect"
category: "general"
description: "Returns a report that's information about user permissions for an object, or statement permissions, in the current database. Doesn't list permissions that are always assigned to the fixed server roles or fixed database roles. Doesn't include logins or users that receive permissions based on their membership in a The name of the object in the current database, or a s"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_helprotect
      [ [ @name = ]
      N
      'name'
      ]
      [ , [ @username = ]
      N
      'username'
      ]
      [ , [ @grantorname = ]
      N
      'grantorname'
      ]
      [ , [ @permissionarea = ]
      'permissionarea'
      ]
      [ ; ]
---

## Description

Returns a report that's information about user permissions for an object, or statement permissions, in the current database. Doesn't list permissions that are always assigned to the fixed server roles or fixed database roles.

## Syntax

```sql
sp_helprotect
[ [ @name = ]
N
'name'
]
[ , [ @username = ]
N
'username'
]
[ , [ @grantorname = ]
N
'grantorname'
]
[ , [ @permissionarea = ]
'permissionarea'
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

```sql
CREATE TABLE
```

### Example 5

```sql
EXECUTE sp_helprotect @
name
=
'CREATE TABLE'
;
```
