---
name: "sys.sp_syscollector_enable_collector"
title: "sp_syscollector_enable_collector"
category: "general"
description: "Enables the data collector. Because there's only one data collector per server, no parameters Defaults to the data collector on the server. (with EXECUTE permission) fixed database role to execute this procedure. The following example enables the data collector."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_enable_collector
              [ ; ]
---

## Description

Enables the data collector. Because there's only one data collector per server, no parameters Defaults to the data collector on the server. (with EXECUTE permission) fixed database role to execute this procedure. The following example enables the data collector.

## Syntax

```sql
sp_syscollector_enable_collector
[ ; ]
```

## Examples

### Example 1

```sql
0
```

### Example 2

```sql
1
```

### Example 3

```sql
sp_syscollector_enable_collector
[ ; ]
```

### Example 4

```sql
USE msdb;
GO
EXECUTE dbo.sp_syscollector_enable_collector;
```

### Example 5

```sql
D:\tempdata
```

### Example 6

```sql
USE msdb;
GO
EXECUTE dbo.sp_syscollector_disable_collector;
GO
EXECUTE dbo.sp_syscollector_set_cache_directory @cache_directory = N
'D:\tempdata'
;
GO
EXECUTE dbo.sp_syscollector_enable_collector;
GO
```

### Example 7

```sql
USE msdb;
GO
EXECUTE dbo.sp_syscollector_disable_collector;
GO
EXECUTE dbo.sp_syscollector_set_cache_window 3;
GO
EXECUTE dbo.sp_syscollector_enable_collector;
```
