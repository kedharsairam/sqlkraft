---
name: "sys.sp_update_targetservergroup"
title: "sp_update_targetservergroup"
category: "general"
description: "Changes the name of the specified target server group. Transact-SQL syntax conventions The name of the target server group. , with no default. The new name for the target server group. , with no default. To run this stored procedure, users must be granted the fixed server role."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_update_targetservergroup
  [ @name = ]
  N
  'name'
  , [ @new_name = ]
  N
  'new_name'
  [ ; ]
---

## Description

Changes the name of the specified target server group. Transact-SQL syntax conventions The name of the target server group. , with no default. The new name for the target server group. , with no default. To run this stored procedure, users must be granted the fixed server role.

## Syntax

```sql
sp_update_targetservergroup
[ @name = ]
N
'name'
, [ @new_name = ]
N
'new_name'
[ ; ]
```

## Remarks

Applies to:

Changes the name of the specified target server group.

Transact-SQL syntax conventions

The name of the target server group.

, with no default.

The new name for the target server group.

, with no default.

(success) or

To run this stored procedure, users must be granted the

fixed server role.

## Examples

### Example 1

`sp_update_targetservergroup`

### Example 2

`msdb`

### Example 3

```sql
Servers Processing
Customer Orders
```

### Example 4

```sql
Local Servers Processing Customer Orders
```

### Example 5

```sql
USE msdb;
GO
EXECUTE dbo.sp_update_targetservergroup
@
name
= N
'Servers Processing Customer Orders'
,
@new_name = N
'Local Servers Processing Customer Orders'
;
GO
```
