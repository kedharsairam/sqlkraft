---
name: "sys.sp_dbmmonitordropmonitoring"
title: "sp_dbmmonitordropmonitoring"
category: "general"
description: "Stops and deletes the mirroring monitor job for all the databases on the server instance. Transact-SQL syntax conventions fixed server role, or execute permission directly on this The following example drops database mirroring monitoring on all of the mirrored databases"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dbmmonitordropmonitoring
  [ ; ]
---

## Description

Stops and deletes the mirroring monitor job for all the databases on the server instance. Transact-SQL syntax conventions fixed server role, or execute permission directly on this The following example drops database mirroring monitoring on all of the mirrored databases

## Syntax

```sql
sp_dbmmonitordropmonitoring
[ ; ]
```

## Examples

### Example 1

```sql
sp_dbmmonitordropmonitoring
[ ; ]
```

### Example 2

```sql
EXECUTE sp_dbmmonitordropmonitoring;
```
