---
name: "sys.dm_fts_population_ranges"
title: "sys.dm_fts_population_ranges"
category: "io"
description: "SQL database in Microsoft Fabric Returns information about the specific ranges related to a full-text index population currently Address of memory buffers allocated for activity related to this subrange of a full-text index population. Address of memory buffers representing the parent object of all ranges of population related to a full-text index. If the value is 1, this subrange is responsible f"
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: "##MS_ServerStateReader##"
---

## Description

SQL database in Microsoft Fabric Returns information about the specific ranges related to a full-text index population currently Address of memory buffers allocated for activity related to this subrange of a full-text index population. Address of memory buffers representing the parent object of all ranges of population related to a full-text index. If the value is 1, this subrange is responsible for retrying rows

## Syntax

```sql
##MS_ServerStateReader##
```

## Permissions

SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns information about the specific ranges related to a full-text index population currently in progress. Address of memory buffers allocated for activity related to this subrange of a full-text index population. Address of memory buffers representing the parent object of all ranges of population related to a full-text index. If the value is 1, this subrange is responsible for retrying rows that encountered errors. ID of the session that is currently processing this task. Number of rows that have been processed by this range. Forward progress is persisted and counted every 5 minutes, rather than with every batch commit. Number of rows that have encountered errors by this range. Forward progress is persisted and counted every 5 minutes, rather than with every batch commit. On SQL Server and SQL Managed Instance, requires permission. On SQL Database , , and service objectives, and for databases in , the server admin account, the Microsoft Entra admin account, or membership in the server role is required. On all other SQL Database service objectives, either the permission on the database, or membership in the server role is required. ﾉ
