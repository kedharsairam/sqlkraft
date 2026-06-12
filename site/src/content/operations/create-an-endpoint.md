---
title: "Create an endpoint"
topic: "high-availability"
description: "This topic describes how to create a database mirroring endpoint that uses Windows Authentication in SQL Server by using Transact-SQL."
tags: ["high-availability","create-an-endpoint"]
pubDate: 2025-12-01
---

This topic describes how to create a database mirroring endpoint that uses Windows

Authentication in SQL Server by using Transact-SQL. To support database mirroring or Always

On availability groups each instance of SQL Server requires a database mirroring endpoint. A

server instance can have only one database mirroring endpoint, which has a single port. A

database mirroring endpoint can use any port that is available on the local system when the

endpoint is created. All database mirroring sessions on a server instance listen on that port,

and all incoming connections for database mirroring use that port.

Security

Transact-SQL

The authentication and encryption methods of the server instance are established by the

system administrator.

）

Important

If a database mirroring endpoint exists and is already in use, we recommend that you use

that endpoint. Dropping an in-use endpoint disrupts existing sessions.

２

Warning

The RC4 algorithm is deprecated. This feature will be removed in a future version of SQL

Server. Avoid using this feature in new development work, and plan to modify applications

that currently use this feature. We recommend that you use AES.
