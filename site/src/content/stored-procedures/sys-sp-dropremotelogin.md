---
name: "sys.sp_dropremotelogin"
title: "sp_dropremotelogin"
category: "general"
description: "Removes a remote login mapped to a local login used to execute remote stored procedures against the local server running SQL Server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropremotelogin
  [ @remotename = ]
  N
  '@remotename'
  [ , [ @loginame = ]
  N
  'loginame'
  ]
  [ , [ @remotename = ]
  N
  'remotename'
  ]
  [ ; ]
---

## Description

Removes a remote login mapped to a local login used to execute remote stored procedures against the local server running SQL Server.

## Syntax

```sql
sp_dropremotelogin
[ @remotename = ]
N
'@remotename'
[ , [ @loginame = ]
N
'loginame'
]
[ , [ @remotename = ]
N
'remotename'
]
[ ; ]
```
