---
name: "sys.sp_delete_targetservergroup"
title: "sp_delete_targetservergroup"
category: "general"
description: "Deletes the specified target server group. Transact-SQL syntax conventions The name of the target server group to remove. permissions on this procedure, but these permissions might be overridden during a SQL Server upgrade. The following example removes the target server group"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "Servers Processing Customer Orders"
---

## Description

Deletes the specified target server group. Transact-SQL syntax conventions The name of the target server group to remove. permissions on this procedure, but these permissions might be overridden during a SQL Server upgrade. The following example removes the target server group

## Syntax

```sql
Servers Processing Customer Orders
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

`EXECUTE`

### Example 4

```sql
Servers Processing Customer Orders
```

### Example 5

```sql
sp_delete_targetservergroup [ @name = ]
N
'name'
[ ; ]
```

### Example 6

```sql
USE msdb;
GO
EXECUTE sp_delete_targetservergroup @
name
= N
'Servers Processing Customer Orders'
;
GO
```
