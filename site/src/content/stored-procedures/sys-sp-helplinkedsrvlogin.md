---
name: "sys.sp_helplinkedsrvlogin"
title: "sp_helplinkedsrvlogin"
category: "general"
description: "Provides information about login mappings defined against a specific linked server used for distributed queries and remote stored procedures."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helplinkedsrvlogin
              [ [ @rmtsrvname = ]
              N
              'rmtsrvname'
              ]
              [ , [ @locallogin = ]
              N
              'locallogin'
              ]
              [ ; ]
---

## Description

Provides information about login mappings defined against a specific linked server used for distributed queries and remote stored procedures.

## Syntax

```sql
sp_helplinkedsrvlogin
[ [ @rmtsrvname = ]
N
'rmtsrvname'
]
[ , [ @locallogin = ]
N
'locallogin'
]
[ ; ]
```
