---
name: "sys.sp_testlinkedserver"
title: "sp_testlinkedserver"
category: "general"
description: "Tests the connection to a linked server. If the test is unsuccessful, the procedure raises an exception with the reason of the failure. Transact-SQL syntax conventions The name of the linked server. No permissions are checked. However, the caller must have the appropriate login mapping. Arguments for extended stored procedures must be entered in the specific order as section."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_testlinkedserver [ @servername ] = servername
  [ ; ]
---

## Description

Tests the connection to a linked server. If the test is unsuccessful, the procedure raises an exception with the reason of the failure. Transact-SQL syntax conventions The name of the linked server. No permissions are checked. However, the caller must have the appropriate login mapping. Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered out of order, an error

## Syntax

```sql
sp_testlinkedserver [ @servername ] = servername
[ ; ]
```

## Permissions

06/23/2025 Applies to: SQL Server Tests the connection to a linked server. If the test is unsuccessful, the procedure raises an exception with the reason of the failure. Transact-SQL syntax conventions syntaxsql The name of the linked server. @servername is , with no default. None. No permissions are checked. However, the caller must have the appropriate login mapping. ） Important Arguments for extended stored procedures must be entered in the specific order as described in the section. If the parameters are entered out of order, an error message occurs.

## Examples

### Example 1

`SEATTLESales`

### Example 2

```sql
USE master
;
GO
EXECUTE sp_addlinkedserver
'SEATTLESales'
, N
'SQL Server'
;
GO
EXECUTE sp_testlinkedserver SEATTLESales;
GO
```
