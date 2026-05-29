---
name: 'sys.sp_helplogins'
title: 'sp_helplogins'
category: 'general'
description: 'Provides information about logins and the users associated with them in each database. Transact-SQL syntax conventions isn''t specified, information about all logins is The first report contains information about each login specified, as shown in the following'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helplogins [ [ @
  L
  ogin
  N
  ame
  P
  attern = ]
  N
  'LoginNamePattern'
  ]
  [ ; ]
---

## Description

Provides information about logins and the users associated with them in each database. Transact-SQL syntax conventions isn't specified, information about all logins is The first report contains information about each login specified, as shown in the following

## Syntax

```sql
sp_helplogins [ [ @
L
ogin
N
ame
P
attern = ]
N
'LoginNamePattern'
]
[ ; ]
```

## Examples

### Example 1

```sql
sp_helplogins
```

### Example 2

```sql
sp_helplogins
```

### Example 3

```sql
sp_helplogins
```

### Example 4

```sql
sp_helplogins
```

### Example 5

```sql
John
```

### Example 6

```sql
EXECUTE
sp_helplogins
'John'
;
GO
LoginName SID                        DefDBName DefLangName AUser ARemote
--------- -------------------------- --------- ----------- ----- -------
John      0x23B348613497D11190C100C  master    us_english  yes   no
LoginName   DBName   UserName   UserOrAlias
---------   ------   --------   -----------
John        pubs     John       User
```
