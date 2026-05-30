---
name: "sys.sp_droptype"
title: "sp_droptype"
category: "general"
description: "Deletes an alias data type from Transact-SQL syntax conventions The name of an alias data type that you own. , with no default. alias data type can't be dropped if tables or other database objects reference it. An alias data type can't be dropped if the alias data type is used within a table definition or if a rule or default is bound to it."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_droptype [ @typename = ]
  N
  'typename'
  [ ; ]
---

## Description

Deletes an alias data type from Transact-SQL syntax conventions The name of an alias data type that you own. , with no default. alias data type can't be dropped if tables or other database objects reference it. An alias data type can't be dropped if the alias data type is used within a table definition or if a rule or default is bound to it.

## Syntax

```sql
sp_droptype [ @typename = ]
N
'typename'
[ ; ]
```

## Remarks

Applies to:

Deletes an alias data type from

Transact-SQL syntax conventions

The name of an alias data type that you own.

, with no default.

(success) or

alias data type can't be dropped if tables or other database objects reference it.

An alias data type can't be dropped if the alias data type is used within a table definition

or if a rule or default is bound to it.

## Examples

### Example 1

```sql
birthday
```

### Example 2

```sql
USE
master
;
GO
EXECUTE
sp_droptype
'birthday'
;
GO
```
