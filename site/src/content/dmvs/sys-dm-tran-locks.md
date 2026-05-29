---
name: 'sys.dm_tran_locks'
title: 'sys.dm_tran_locks'
category: 'transactions'
description: 'Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns information about currently active lock manager resources in SQL Server. Each row represents a currently active request to the lock manager for a lock that has been granted or is The columns in the result set are divided into two main groups: resource and request. The resource group describes the resource on which the lock re'
tags: ["transactions", "dmv"]
pubDate: 2026-05-29
syntax: 'sys.dm_pdw_nodes_tran_locks'
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns information about currently active lock manager resources in SQL Server. Each row represents a currently active request to the lock manager for a lock that has been granted or is The columns in the result set are divided into two main groups: resource and request. The resource group describes the resource on which the lock request is being made, and the request

## Syntax

```sql
sys.dm_pdw_nodes_tran_locks
```

## Examples

### Example 1

```sql
sp_getapplock
```

### Example 2

```sql
sys.dm_tran_locks
```

### Example 3

```sql
sp_lock
```

### Example 4

```sql
Form1
```

### Example 5

```sql
AdventureWorks2025
```

### Example 6

```sql
dbo
```

### Example 7

```sql
BEGIN
ROLLBACK
;
END
ELSE
BEGIN
EXECUTE
@
result
= sp_releaseapplock
@
Resource
=
'Form1'
;
COMMIT
TRANSACTION
;
END
GO
```

### Example 8

```sql
USE
AdventureWorks2025;
GO
BEGIN
TRANSACTION
;
DECLARE
@
result
AS
INT
;
EXECUTE
@
result
= sp_getapplock
@
Resource
=
'Form1'
,
@LockMode =
'Shared'
;
COMMIT
TRANSACTION
;
GO
```
