---
name: "sys.sp_dropmessage"
title: "sp_dropmessage"
category: "general"
description: "Drops a specified user-defined error message from an instance of the SQL Server Database Engine. User-defined messages can be viewed using the user-defined message that's a message number greater than The language of the message to drop."
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

Drops a specified user-defined error message from an instance of the SQL Server Database Engine. User-defined messages can be viewed using the user-defined message that's a message number greater than The language of the message to drop.

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
