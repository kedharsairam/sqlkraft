---
name: 'sys.sp_addmessage'
title: 'sp_addmessage'
category: 'general'
description: 'Stores a new user-defined error message in an instance of the SQL Server Database Engine. Transact-SQL syntax conventions error messages can be an integer between 50,001 and 2,147,483,647. The combination of must be unique; an error is returned if the ID already exists for the The severity level of the error. . For more information about severities, see Database Engine error severities'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addmessage
  [ [ @msgnum = ] msgnum ]
  [ , [ @severity = ] severity ]
  [ , [ @msgtext = ]
  N
  'msgtext'
  ]
  [ , [ @lang = ]
  N
  'lang'
  ]
  [ , [ @with_log = ] {
  'true'
  |
  'false'
  } ]
  [ , [ @replace = ]
  'replace'
  ]
  [ ; ]
---

## Description

Stores a new user-defined error message in an instance of the SQL Server Database Engine. Transact-SQL syntax conventions error messages can be an integer between 50,001 and 2,147,483,647. The combination of must be unique; an error is returned if the ID already exists for the The severity level of the error. . For more information about severities, see Database Engine error severities

## Syntax

```sql
sp_addmessage
[ [ @msgnum = ] msgnum ]
[ , [ @severity = ] severity ]
[ , [ @msgtext = ]
N
'msgtext'
]
[ , [ @lang = ]
N
'lang'
]
[ , [ @with_log = ] {
'true'
|
'false'
} ]
[ , [ @replace = ]
'replace'
]
[ ; ]
```
