---
name: "sys.dm_db_xtp_undeploy_status"
title: "sys.dm_db_xtp_undeploy_status"
category: "in-memory"
description: "SQL Server 2025 (17.x) Preview and later versions Returns a single row reflecting the status of the In-Memory OLTP (XTP) database engine when removing the engine from a database. XTP engine removal, or undeployment, is a multi-step process initiated by the statement that removes the last remaining memory-optimized container from step in the process."
tags: ["in-memory", "dmv"]
pubDate: 2026-05-29
syntax: |
  ALTER DATABASE
  ... REMOVE FILE
---

## Description

SQL Server 2025 (17.x) Preview and later versions Returns a single row reflecting the status of the In-Memory OLTP (XTP) database engine when removing the engine from a database. XTP engine removal, or undeployment, is a multi-step process initiated by the statement that removes the last remaining memory-optimized container from step in the process. It can be used to monitor and troubleshoot memory-optimized container

## Syntax

```sql
ALTER DATABASE
... REMOVE FILE
```
