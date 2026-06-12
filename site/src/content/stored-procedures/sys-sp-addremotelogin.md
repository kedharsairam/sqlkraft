---
name: "sys.sp_addremotelogin"
title: "sp_addremotelogin"
category: "general"
description: "Adds a new remote login ID on the local server. This enables remote servers to connect and execute remote procedure calls."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addremotelogin
  [ @remoteserver = ]
  N
  'remoteserver'
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

Adds a new remote login ID on the local server. This enables remote servers to connect and execute remote procedure calls.

## Syntax

```sql
sp_addremotelogin
[ @remoteserver = ]
N
'remoteserver'
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
