---
name: "sys.dm_fts_fdhosts"
title: "sys.dm_fts_fdhosts"
category: "os"
description: "Returns information on the current activity of the filter daemon host or hosts on the server Windows process ID of the filter daemon host. Type of document being processed by the filter daemon host, one Maximum number of threads in the filter daemon host. Number of batches that are being processed in the filter daemon On SQL Server and SQL Managed Instance, require"
tags: ["os","dmv"]
pubDate: 2026-05-29
syntax: "##MS_ServerStateReader##"
---

## Description

Returns information on the current activity of the filter daemon host or hosts on the server Windows process ID of the filter daemon host. Type of document being processed by the filter daemon host, one Maximum number of threads in the filter daemon host. Number of batches that are being processed in the filter daemon On SQL Server and SQL Managed Instance, requires

## Syntax

```sql
##MS_ServerStateReader##
```

## Permissions

Returns information on the current activity of the filter daemon host or hosts on the server instance. ID of the filter daemon host. Name of filter daemon host. Windows process ID of the filter daemon host. Type of document being processed by the filter daemon host, one of: Single thread Multi-thread Huge document Maximum number of threads in the filter daemon host. Number of batches that are being processed in the filter daemon host. On SQL Server and SQL Managed Instance, requires permission. On SQL Database , , and service objectives, and for databases in , the server admin account, the Microsoft Entra admin account, or membership in the server role is required. On all other SQL Database service objectives, either the permission on the database, or membership in the server role is required. Requires VIEW SERVER PERFORMANCE STATE permission on the server. ﾉ
