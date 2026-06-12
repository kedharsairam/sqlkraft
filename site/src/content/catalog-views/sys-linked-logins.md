---
name: "sys.linked_logins"
title: "sys.linked_logins"
category: "security"
description: "Returns a row per linked-server-login mapping, for use by RPC and distributed queries from local server to the corresponding linked server. Server-principal to whom mapping applies. If 1, mapping indicates session should use its own credentials; otherwise, 0 indicates that session uses the name and password that Remote user name to use when connecting. Password is also stored, but not exposed in c"
tags: ["security", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Returns a row per linked-server-login mapping, for use by RPC and distributed queries from local server to the corresponding linked server. Server-principal to whom mapping applies. If 1, mapping indicates session should use its own credentials; otherwise, 0 indicates that session uses the name and password that Remote user name to use when connecting. Password is also stored, but not exposed in catalog view interfaces.

## Permissions

ﾃ Summarize this article for me Returns a row per linked-server-login mapping, for use by RPC and distributed queries from local server to the corresponding linked server. Description ID of the server in. Server-principal to whom mapping applies. 0 = wildcard or public. If 1, mapping indicates session should use its own credentials; otherwise, 0 indicates that session uses the name and password that are supplied. Remote user name to use when connecting. Password is also stored, but not exposed in catalog view interfaces. Date the linked login was last changed. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. SQL Server 2022 (16.x) and later versions require VIEW SERVER SECURITY STATE permission on the server. Catalog Views (Transact-SQL) Linked Servers Catalog Views (Transact-SQL) ﾉ Expand table
## Code Blocks

`server_id`

`sys.servers`

`local_principal_id`

`uses_self_credential`

`remote_name`
