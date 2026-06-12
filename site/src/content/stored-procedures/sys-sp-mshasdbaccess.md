---
name: "sys.sp_mshasdbaccess"
title: "sp_MShasdbaccess"
category: "general"
description: "Lists the name and owner of all the databases to which the user has access. Execute permission is granted to the sys.sysdatabases (Transact-SQL)"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_
  MS
  hasdbaccess
  [ ; ]
---

## Description

Lists the name and owner of all the databases to which the user has access. Execute permission is granted to the sys.sysdatabases (Transact-SQL)

## Syntax

```sql
sp_
MS hasdbaccess
[ ; ]
```

## Permissions

06/23/2025 syntaxsql None. (success) or (failure). Execute permission is granted to the role. sys.sysdatabases (Transact-SQL)
