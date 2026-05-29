---
name: "sys.sp_dropremotelogin"
title: "sp_dropremotelogin"
category: "general"
description: "Removes a remote login mapped to a local login used to execute remote stored procedures against the local server running SQL Server. Transact-SQL syntax conventions The name of the remote server mapped to the remote login that is to be removed. The optional login name on the local server that is associated with the remote server. must already exist if specified. This feature will be removed in a f"
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

Removes a remote login mapped to a local login used to execute remote stored procedures against the local server running SQL Server. Transact-SQL syntax conventions The name of the remote server mapped to the remote login that is to be removed. The optional login name on the local server that is associated with the remote server. must already exist if specified. This feature will be removed in a future version of SQL Server. Avoid using this feature in

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
