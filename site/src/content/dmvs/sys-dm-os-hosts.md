---
name: "sys.dm_os_hosts"
title: "sys.dm_os_hosts"
category: "os"
description: "Analytics Platform System (PDW) Returns all the hosts currently registered in an instance of SQL Server. This view also returns the resources that are used by these hosts. Internal memory address of the host object. Type of hosted component. For example, SOSHOST_CLIENTID_SERVERSNI= SQL Server Native SOSHOST_CLIENTID_SQLOLEDB = SQL Server Native SOSHOST_CLIENTID_MSDART = Microsoft Data Access Total"
tags: ["os", "dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT h.type, SUM(mc.pages_kb) AS committed_memory
  FROM sys.dm_os_memory_clerks AS mc
  INNER JOIN sys.dm_os_hosts AS h
  ON mc.memory_clerk_address = h.default_memory_clerk_address
  GROUP BY h.type;
---

## Description

Analytics Platform System (PDW) Returns all the hosts currently registered in an instance of SQL Server. This view also returns the resources that are used by these hosts. Internal memory address of the host object. Type of hosted component. For example, SOSHOST_CLIENTID_SERVERSNI= SQL Server Native SOSHOST_CLIENTID_SQLOLEDB = SQL Server Native SOSHOST_CLIENTID_MSDART = Microsoft Data Access Total number of tasks that this host has placed onto

## Syntax

```sql
SELECT h.type, SUM(mc.pages_kb) AS committed_memory
FROM sys.dm_os_memory_clerks AS mc
INNER JOIN sys.dm_os_hosts AS h
ON mc.memory_clerk_address = h.default_memory_clerk_address
GROUP BY h.type;
```
