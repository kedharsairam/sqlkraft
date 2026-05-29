---
name: "sys.sp_helpfile"
title: "sp_helpfile"
category: "general"
description: "Returns the physical names and attributes of files associated with the current database. Use this stored procedure to determine the names of files to attach to or detach from the server. Transact-SQL syntax conventions The logical name of any file in the current database. isn't specified, the attributes of all files in the current database are returned. Numeric identifier of the file. A value isn'"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpfile [ [ @filename = ]
  N
  'filename'
  ]
  [ ; ]
---

## Description

Returns the physical names and attributes of files associated with the current database. Use this stored procedure to determine the names of files to attach to or detach from the server. Transact-SQL syntax conventions The logical name of any file in the current database. isn't specified, the attributes of all files in the current database are returned. Numeric identifier of the file. A value isn't returned if

## Syntax

```sql
sp_helpfile [ [ @filename = ]
N
'filename'
]
[ ; ]
```
