---
name: "sys.sp_helpfilegroup"
title: "sp_helpfilegroup"
category: "general"
description: "Returns the names and attributes of filegroups associated with the current database. Transact-SQL syntax conventions The logical name of any filegroup in the current database. isn't specified, all filegroups in the current database are listed and only the first result set shown in the Result Sets section is displayed."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpfilegroup [ [ @filegroupname = ]
  N
  'filegroupname'
  ]
  [ ; ]
---

## Description

Returns the names and attributes of filegroups associated with the current database. Transact-SQL syntax conventions The logical name of any filegroup in the current database. isn't specified, all filegroups in the current database are listed and only the first result set shown in the Result Sets section is displayed.

## Syntax

```sql
sp_helpfilegroup [ [ @filegroupname = ]
N
'filegroupname'
]
[ ; ]
```
