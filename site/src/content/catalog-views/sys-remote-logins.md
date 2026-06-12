---
name: "sys.remote_logins"
title: "sys.remote_logins"
category: "security"
description: |
  'Returns a row per remote-login mapping. This catalog view is used to map incoming local logins that claim to be coming from a corresponding server to an actual local login. . This name is supplied by the connection from the "remote" server. Login name that the connection will supply to be mapped. If NULL, the login name that is specified in the connection is used. ID of the server principal to who'
tags: ["security","catalog-view"]
pubDate: "2026-05-29"
---

## Description

Returns a row per remote-login mapping. This catalog view is used to map incoming local logins that claim to be coming from a corresponding server to an actual local login. This name is supplied by the connection from the "remote" server. Login name that the connection will supply to be mapped. If NULL, the login name that is specified in the connection is used.

## Permissions

ﾃ Summarize this article for me This catalog view is used to map incoming local logins that claim to be coming from a corresponding server to an actual local login. Description ID of the server in. This name is supplied by the connection from the "remote" server. Login name that the connection will supply to be mapped. If NULL, the login name that is specified in the connection is used. ID of the server principal to whom the login is mapped. If 0, the remote login is mapped to the login with the same name. Date the linked login was last changed. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. SQL Server 2022 (16.x) and later versions require VIEW SERVER SECURITY STATE permission on the server. Linked Servers Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) ﾉ Expand table
## Code Blocks

`server_id`

`sys.servers`

`remote_name`

`local_principal_id`

`modify_date`
