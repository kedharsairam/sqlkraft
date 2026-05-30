---
name: "sys.servers"
title: "sys.servers"
category: "compatibility"
description: 'Returns a row per linked or remote server registered, and a row for the local server that has value is the local name of linked Product name of the linked server. A value of "SQL Server" indicates another instance of SQL Server. Starting with SQL Server 2019 (15.x), the value "SQLNCLI" maps to the Microsoft OLE DB Driver for SQL OLE DB provider-string connection Is NULL unless the caller has the'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
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

Returns a row per linked or remote server registered, and a row for the local server that has value is the local name of linked Product name of the linked server. A value of "SQL Server" indicates another instance of SQL Server. Starting with SQL Server 2019 (15.x), the value "SQLNCLI" maps to the Microsoft OLE DB Driver for SQL OLE DB provider-string connection Is NULL unless the caller has the

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

ﾃ Summarize this article for me Applies to: SQL Server Returns a row per remote-login mapping. This catalog view is used to map incoming local logins that claim to be coming from a corresponding server to an actual local login. Description ID of the server in . This name is supplied by the connection from the "remote" server. Login name that the connection will supply to be mapped. If NULL, the login name that is specified in the connection is used. ID of the server principal to whom the login is mapped. If 0, the remote login is mapped to the login with the same name. Date the linked login was last changed. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . SQL Server 2022 (16.x) and later versions require VIEW SERVER SECURITY STATE permission on the server. Linked Servers Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) Last updated on 03/03/2026 ﾉ Expand table Related content ﾃ Summarize this article for me Applies to: SQL Server Azure SQL Managed Instance Returns a row per linked-server-login mapping, for use by RPC and distributed queries from local server to the corresponding linked server. Description ID of the server in . Server-principal to whom mapping applies. 0 = wildcard or public. If 1, mapping indicates session should use its own credentials; otherwise, 0 indicates that session uses the name and password that are supplied. Remote user name to use when connecting. Password is also stored, but not exposed in catalog view interfaces. Date the linked login was last changed. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . SQL Server 2022 (16.x) and later versions require VIEW SERVER SECURITY STATE permission on the server. Catalog Views (Transact-SQL) Linked Servers Catalog Views (Transact-SQL) Last updated on 03/03/2026 ﾉ Expand table Related content Name of the originating server returned by the column in this result (if it originates from a remote server). The name is given as it appears in sys.servers. Returns NULL if the column originates on the local server, or if it cannot be determined which server it originates on. Is only populated if browsing information is requested. Name of the originating database returned by the column in this result. Returns NULL if the database cannot be determined. Is only populated if browsing information is requested. Name of the originating schema returned by the column in this result. Returns NULL if the schema cannot be determined. Is only populated if browsing information is requested. Name of the originating table returned by the column in this result. Returns NULL if the table cannot be determined. Is only populated if browsing information is requested. Name of the originating column returned by the column in this result. Returns NULL if the column cannot be determined. Is only populated if browsing information is requested. Returns 1 if the column is an identity column and 0 if not. Returns NULL if it cannot be determined that the column is an identity column. Returns 1 if the column is part of a unique index (including unique and primary constraint) and 0 if not. Returns NULL if it cannot be determined that the column is part of a unique index. Only populated if browsing information is requested. Returns 1 if the column is updateable and 0 if not. Returns NULL if it cannot be determined that the column is updateable. Returns 1 if the column is a computed column and 0 if not. Returns NULL if it cannot be determined that the column is a computed column. Returns 1 if the column is a sparse column and 0 if not. Returns NULL if it cannot be determined that the column is a part of a sparse column set.
