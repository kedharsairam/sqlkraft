---
name: "sys.sp_helpserver"
title: "sp_helpserver"
category: "general"
description: "Reports information about a particular remote or replication server, or about all servers of both types. Provides the server name, the network name of the server, the replication status of the server, the identification number of the server, and the collation name. Also provides time-out values for connecting to, or queries against, linked servers."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_helpserver
      [ [ @server = ]
      N
      'server'
      ]
      [ , [ @optname = ]
      'optname'
      ]
      [ , [ @show_topology = ]
      'show_topology'
      ]
      [ ; ]
---

## Description

Reports information about a particular remote or replication server, or about all servers of both types. Provides the server name, the network name of the server, the replication status of the server, the identification number of the server, and the collation name. Also provides time-out values for connecting to, or queries against, linked servers. Specifies the server about which information is reported.

## Syntax

```sql
sp_helpserver
[ [ @server = ]
N
'server'
]
[ , [ @optname = ]
'optname'
]
[ , [ @show_topology = ]
'show_topology'
]
[ ; ]
```
