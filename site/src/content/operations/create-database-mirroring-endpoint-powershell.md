---
title: "Create database mirroring endpoint (PowerShell)"
topic: "high-availability"
description: "This topic describes how to create a database mirroring endpoint for use by Always On availability groups in SQL Server by using PowerShell. Requires"
tags: ["high-availability","create-database-mirroring-endpoint-powershell"]
pubDate: "2025-12-01"
---

This topic describes how to create a database mirroring endpoint for use by Always On

availability groups in SQL Server by using PowerShell.

Requires CREATE ENDPOINT permission, or membership in the sysadmin fixed server role. For

more information, see

GRANT Endpoint Permissions (Transact-SQL).

1. Change directory (

) to the server instance for which you want to create the database

mirroring endpoint.

2. Use the

cmdlet to create the endpoint and then use the

SqlHadrEndpoint

to start the endpoint.

The following PowerShell commands create a database mirroring endpoint on an instance of

(

Machine

\

Instance

). The endpoint uses port 5022.

）

Important

The RC4 algorithm is deprecated. This feature will be removed in a future version of SQL

Server. Avoid using this feature in new development work, and plan to modify applications

that currently use this feature. We recommend that you use AES.

）

Important

This example works only on a server instance that currently lack a database mirroring

endpoint.
