---
name: "sys.sp_addremotelogin"
title: "sp_addremotelogin"
category: "general"
description: "Adds a new remote login ID on the local server. This enables remote servers to connect and execute remote procedure calls. Transact-SQL syntax conventions The name of the remote server that the remote login applies to. existing logins of the same name on the local server. The server must be known to the local server. This is added by using server that is running SQL Server to execute a remote stor"
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

Adds a new remote login ID on the local server. This enables remote servers to connect and execute remote procedure calls. Transact-SQL syntax conventions The name of the remote server that the remote login applies to. existing logins of the same name on the local server. The server must be known to the local server. This is added by using server that is running SQL Server to execute a remote stored procedure, they connect as the

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
