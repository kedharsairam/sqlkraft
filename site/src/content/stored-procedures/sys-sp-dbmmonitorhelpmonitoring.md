---
name: "sys.sp_dbmmonitorhelpmonitoring"
title: "sp_dbmmonitorhelpmonitoring"
category: "general"
description: "Returns the current update period. Returns the current update period, that is, the number of minutes between updates of database mirroring status table. This value ranges from 1 to 120 minutes. fixed server role, or execute permission directly on this The following example returns the current update period."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dbmmonitorhelpmonitoring
  [ ; ]
---

## Description

Returns the current update period. Returns the current update period, that is, the number of minutes between updates of database mirroring status table. This value ranges from 1 to 120 minutes. fixed server role, or execute permission directly on this The following example returns the current update period.

## Syntax

```sql
sp_dbmmonitorhelpmonitoring
[ ; ]
```

## Examples

### Example 1

```sql
sp_dbmmonitorhelpmonitoring
[ ; ]
```

### Example 2

```sql
EXECUTE sp_dbmmonitorhelpmonitoring;
```
