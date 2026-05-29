---
name: 'sys.sp_validname'
title: 'sp_validname'
category: 'general'
description: 'SQL database in Microsoft Fabric Checks for valid SQL Server identifier names. All nonbinary and nonzero data, including Unicode data that can be stored by using the accepted as valid characters for identifier names. Transact-SQL syntax conventions , can''t be an empty string, and can''t contain a binary-zero character. Specifies whether to raise an error. causes no error messages to appear.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_validname
  [ @name = ]
  N
  'name'
  [ , [ @raise_error = ] raise_error ]
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Checks for valid SQL Server identifier names. All nonbinary and nonzero data, including Unicode data that can be stored by using the accepted as valid characters for identifier names. Transact-SQL syntax conventions , can't be an empty string, and can't contain a binary-zero character. Specifies whether to raise an error. causes no error messages to appear.

## Syntax

```sql
sp_validname
[ @name = ]
N
'name'
[ , [ @raise_error = ] raise_error ]
[ ; ]
```

## Permissions

Applies to: SQL Server Azure SQL Database SQL database in Microsoft Fabric Checks for valid SQL Server identifier names. All nonbinary and nonzero data, including Unicode data that can be stored by using the , , or data types, are accepted as valid characters for identifier names. Transact-SQL syntax conventions syntaxsql The name of the identifiers for which to check validity. @name is , with no default. @name can't be , can't be an empty string, and can't contain a binary-zero character. Specifies whether to raise an error. @raise_error is , with a default of , which means that errors are displayed. causes no error messages to appear. (success) or (failure). Requires membership in the role.
