---
name: "sys.fn_builtin_permissions"
title: "sys.fn_builtin_permissions"
category: "system"
description: "SQL database in Microsoft Fabric Returns a description of the built in permissions hierarchy of the server. can only be called on SQL Server and Azure SQL Database, and it returns all permissions regardless of whether they are supported on the current platform. Most permissions apply to all platforms, but some do not. For example server level permissions cannot be granted on SQL Database. For info"
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_builtin_permissions"
---

## Description

SQL database in Microsoft Fabric Returns a description of the built in permissions hierarchy of the server. can only be called on SQL Server and Azure SQL Database, and it returns all permissions regardless of whether they are supported on the current platform. Most permissions apply to all platforms, but some do not. For example server level permissions cannot be granted on SQL Database. For information about which platforms support each

## Syntax

```sql
sys.fn_builtin_permissions
```

## Permissions

When called with the name of one securable class, will return all permissions that apply to the class. is a string literal of type that requires quotation marks. Description class_desc Collation of the server Description of the securable class. permission_name Collation of the server Permission name. type Collation of the server Compact permission type code. See the table that follows. covering_permission_name Collation of the server If not NULL, this is the name of the permission on this class that implies the other permissions on this class. parent_class_desc Collation of the server If not NULL, this is the name of the parent class that contains the current class. parent_covering_permission_name Collation of the server If not NULL, this is the name of the permission on the parent class that implies all other permissions on that class. AADS ALTER ANY DATABASE EVENT SESSION : SQL Server 2014 (12.x) and later versions . DATABASE AAES ALTER ANY EVENT SESSION SERVER ﾉ Expand table ﾉ Expand table Use or an empty string to return all permissions. SQL Specify a class to return all possible permissions for that class. SQL SQL Permissions Hierarchy (Database Engine) GRANT (Transact-SQL) CREATE SCHEMA (Transact-SQL) DROP SCHEMA (Transact-SQL) Permissions (Database Engine) sys.fn_my_permissions (Transact-SQL) HAS_PERMS_BY_NAME (Transact-SQL) Last updated on 11/18/2025 See also

## Examples

### Example 1

```sql
sys.fn_builtin_permissions
```

### Example 2

```sql
DEFAULT
```

### Example 3

```sql
SERVER
```

### Example 4

```sql
CONTROL SERVER
```

### Example 5

```sql
sys.fn_builtin_permissions
```

### Example 6

```sql
sys.fn_builtin_permissions
```

### Example 7

```sql
CONTROL SERVER
```

### Example 8

```sql
sys.fn_builtin_permissions
```

### Example 9

```sql
sys.fn_translate_permissions
```

### Example 10

```sql
SELECT * FROM sys.fn_builtin_permissions('CERTIFICATE');
SELECT '0001' AS Input, * FROM sys.fn_translate_permissions('CERTIFICATE', 0001);
SELECT '0010' AS Input, * FROM sys.fn_translate_permissions('CERTIFICATE', 0010);
SELECT '0011' AS Input, * FROM sys.fn_translate_permissions('CERTIFICATE', 0011);
```
