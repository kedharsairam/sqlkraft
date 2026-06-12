---
name: "sys.sp_delete_alert"
title: "sp_delete_alert"
category: "general"
description: "Removing an alert also removes any notifications associated with the alert. permissions on this procedure, but these permissions might be overridden during a SQL Server upgrade."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_alert [ @name = ]
              N
              'name'
              [ ; ]
---

## Description

## Syntax

```sql
sp_delete_alert [ @name = ]
N
'name'
[ ; ]
```

## Permissions

06/23/2025 syntaxsql The name of the alert. @name is , with no default. (success) or (failure). None. Removing an alert also removes any notifications associated with the alert. You can grant permissions on this procedure, but these permissions might be overridden during a SQL Server upgrade.

## Examples

### Example 1

```sql
Test Alert
```

### Example 2

```sql
USE msdb;
GO
EXECUTE dbo.sp_delete_alert @
name
= N
'Test Alert'
;
GO
```
