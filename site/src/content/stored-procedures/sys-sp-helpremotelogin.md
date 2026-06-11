---
name: "sys.sp_helpremotelogin"
title: "sp_helpremotelogin"
category: "general"
description: "Reports information about remote logins for a particular remote server, or for all remote servers, defined on the local server. Transact-SQL syntax conventions Specifies the remote server about which the remote login information is returned. about all remote servers defined on the local server is returned. A specific remote login on the remote server. isn't specified, information about all remote"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpremotelogin
  [ [ @remoteserver = ]
  N
  'remoteserver'
  ]
  [ , [ @remotename = ]
  N
  'remotename'
  ]
  [ ; ]
---

## Description

Reports information about remote logins for a particular remote server, or for all remote servers, defined on the local server. Transact-SQL syntax conventions Specifies the remote server about which the remote login information is returned. about all remote servers defined on the local server is returned. A specific remote login on the remote server. isn't specified, information about all remote users defined for

## Syntax

```sql
sp_helpremotelogin
[ [ @remoteserver = ]
N
'remoteserver'
]
[ , [ @remotename = ]
N
'remotename'
]
[ ; ]
```
