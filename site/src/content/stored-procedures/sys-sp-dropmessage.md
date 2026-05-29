---
name: 'sys.sp_dropmessage'
title: 'sp_dropmessage'
category: 'general'
description: 'Drops a specified user-defined error message from an instance of the SQL Server Database Engine. User-defined messages can be viewed using the Transact-SQL syntax conventions user-defined message that''s a message number greater than The language of the message to drop. specified, all language versions of'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropmessage
  [ [ @msgnum = ] msgnum ]
  [ , [ @lang = ]
  N
  'lang'
  ]
  [ ; ]
---

## Description

Drops a specified user-defined error message from an instance of the SQL Server Database Engine. User-defined messages can be viewed using the Transact-SQL syntax conventions user-defined message that's a message number greater than The language of the message to drop. specified, all language versions of

## Syntax

```sql
sp_dropmessage
[ [ @msgnum = ] msgnum ]
[ , [ @lang = ]
N
'lang'
]
[ ; ]
```
