---
name: "sys.servers"
title: "sys.servers"
category: "compatibility"
description: |
  'Returns a row per linked or remote server registered, and a row for the local server that has value is the local name of linked Product name of the linked server. A value of "SQL Server" indicates another instance of SQL Server. Starting with SQL Server 2019 (15.x), the value "SQLNCLI" maps to the Microsoft OLE DB Driver for SQL OLE DB provider-string connection Is NULL unless the caller has the'
tags: ["compatibility","catalog-view"]
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

Returns a row per linked or remote server registered, and a row for the local server that has value is the local name of linked Product name of the linked server. A value of "SQL Server" indicates another instance of SQL Server.

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

## Permissions

ﾃ Summarize this article for me This catalog view is used to map incoming local logins that claim to be coming from a corresponding server to an actual local login. Description ID of the server in. This name is supplied by the connection from the "remote" server. Login name that the connection will supply to be mapped. If NULL, the login name that is specified in the connection is used. ID of the server principal to whom the login is mapped. If 0, the remote login is mapped to the login with the same name. Date the linked login was last changed. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. SQL Server 2022 (16.x) and later versions require VIEW SERVER SECURITY STATE permission on the server. Linked Servers Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) ﾉ Expand table
