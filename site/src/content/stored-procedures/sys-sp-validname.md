---
name: "sys.sp_validname"
title: "sp_validname"
category: "general"
description: "Checks for valid SQL Server identifier names. All nonbinary and nonzero data, including Unicode data that can be stored by using the accepted as valid characters for identifier names. , can't be an empty string, and can't contain a binary-zero character. Specifies whether to raise an error. causes no error messages to appear."
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

Checks for valid SQL Server identifier names. All nonbinary and nonzero data, including Unicode data that can be stored by using the accepted as valid characters for identifier names. , can't be an empty string, and can't contain a binary-zero character. Specifies whether to raise an error. causes no error messages to appear.

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
