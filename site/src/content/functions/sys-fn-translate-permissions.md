---
name: "sys.fn_translate_permissions"
title: "sys.fn_translate_permissions"
category: "system"
description: "Translates the permissions bitmask returned by SQL Trace into a table of permissions names. Is the kind of securable to which the permission is applied. Is a bitmask that is returned in the permissions column. column of a SQL Trace is an integer representation of a bitmask used by SQL Server to calculate effective permissions."
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_translate_permissions ( level , perms )"
---

## Description

Translates the permissions bitmask returned by SQL Trace into a table of permissions names. Is the kind of securable to which the permission is applied. Is a bitmask that is returned in the permissions column. column of a SQL Trace is an integer representation of a bitmask used by SQL Server to calculate effective permissions. Each of the 25 kinds of securables has its own set of permissions with corresponding numerical values.

## Syntax

```sql
sys.fn_translate_permissions ( level , perms )
```

## Permissions

Article • 02/28/2023 level Is the kind of securable to which the permission is applied. level is. perms Is a bitmask that is returned in the permissions column. perms is. The value returned in the column of a SQL Trace is an integer representation of a bitmask used by SQL Server to calculate effective permissions. Each of the 25 kinds of securables has its own set of permissions with corresponding numerical values. translates this bitmask into a table of permissions names. Requires membership in the role.

## Examples

### Example 1

`sys.fn_builtin_permissions`

### Example 2

`sys.fn_translate_permissions`

### Example 3

```sql
SELECT * FROM sys.fn_builtin_permissions('CERTIFICATE');
SELECT '0001' AS Input, * FROM sys.fn_translate_permissions('CERTIFICATE', 0001);
SELECT '0010' AS Input, * FROM sys.fn_translate_permissions('CERTIFICATE', 0010);
SELECT '0011' AS Input, * FROM sys.fn_translate_permissions('CERTIFICATE', 0011);
```
