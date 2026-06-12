---
name: "sys.sp_helpreplicationoption"
title: "sp_helpreplicationoption"
category: "general"
description: "Shows the types of replication options enabled for a server. This stored procedure is executed at any server on any database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_helpreplicationoption [ [ @optname = ]
      N
      'optname'
      ]
      [ ; ]
---

## Description

Shows the types of replication options enabled for a server. This stored procedure is executed at any server on any database.

## Syntax

```sql
sp_helpreplicationoption [ [ @optname = ]
N
'optname'
]
[ ; ]
```
