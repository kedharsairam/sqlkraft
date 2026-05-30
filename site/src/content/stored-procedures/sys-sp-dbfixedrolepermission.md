---
name: "sys.sp_dbfixedrolepermission"
title: "sp_dbfixedrolepermission"
category: "general"
description: "Displays the permissions of a fixed database role. information in SQL Server 2000 (8.x). The output doesn't reflect the changes to the permissions hierarchy that were implemented in SQL Server 2005 (9.x). For more information, see , which shows a list of fixed database roles and its corresponding permissions. Transact-SQL syntax conventions The name of a valid SQL Server fixed database role. isn't"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_dbfixedrolepermission"
---

## Description

Displays the permissions of a fixed database role. information in SQL Server 2000 (8.x). The output doesn't reflect the changes to the permissions hierarchy that were implemented in SQL Server 2005 (9.x). For more information, see , which shows a list of fixed database roles and its corresponding permissions. Transact-SQL syntax conventions The name of a valid SQL Server fixed database role. isn't specified, the permissions for all fixed database roles are displayed.

## Syntax

`sp_dbfixedrolepermission`

## Examples

### Example 1

```sql
EXECUTE sp_dbfixedrolepermission;
GO
```

### Example 2

```sql
sp_revokelogin
DROP LOGIN
```

### Example 3

```sql
sp_srvrolepermission sp_dbfixedrolepermission
```

### Example 4

```sql
sp_srvrolepermission sp_dbfixedrolepermissio
```

### Example 5

```sql
GRANT ALL
DENY ALL
REVOKE ALL
GRANT
```

### Example 6

`DENY`

### Example 7

`REVOKE`

### Example 8

`sys.fn_my_permissions`

### Example 9

```sql
EXECUTE AS
```

### Example 10

`DESX`

_(... and 15 more examples)_
