---
name: "sys.sp_wait_for_database_copy_sync"
title: "sp_wait_for_database_copy_sync"
category: "general"
description: "This procedure is scoped to an Active Geo-Replication relationship between a primary and causes the application to wait until all committed transactions are replicated and acknowledged by the active secondary database. The name of the Azure SQL Database server that hosts the active secondary database. The name of the active secondary database. Returns 0 for success or an error number for failure. "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sys.sp_wait_for_database_copy_sync"
---

## Description

This procedure is scoped to an Active Geo-Replication relationship between a primary and causes the application to wait until all committed transactions are replicated and acknowledged by the active secondary database. The name of the Azure SQL Database server that hosts the active secondary database. The name of the active secondary database. Returns 0 for success or an error number for failure. The most likely error conditions are as follows:

## Syntax

```sql
sys.sp_wait_for_database_copy_sync
```

## Examples

### Example 1

```sql
sys.sp_wait_for_database_copy_sync
```

### Example 2

```sql
sp_wait_for_database_copy_sync
```

### Example 3

```sql
sp_wait_for_database_copy_sync
```

### Example 4

```sql
AdventureWorks
```

### Example 5

```sql
serverSecondary
```

### Example 6

```sql
USE
AdventureWorks;
GO
EXECUTE
sys.sp_wait_for_database_copy_sync
@target_server = N
'serverSecondary'
,
@target_database = N
'AdventureWorks'
;
GO
```
