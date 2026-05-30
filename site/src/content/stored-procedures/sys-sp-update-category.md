---
name: "sys.sp_update_category"
title: "sp_update_category"
category: "general"
description: "Changes the name of a category. Transact-SQL syntax conventions The class of the category to update. , and can be one of these values. The current name of the category."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_update_category
  [ @class = ]
  'class'
  , [ @name = ]
  N
  'name'
  , [ @new_name = ]
  N
  'new_name'
  [ ; ]
---

## Description

Changes the name of a category. Transact-SQL syntax conventions The class of the category to update. , and can be one of these values. The current name of the category.

## Syntax

```sql
sp_update_category
[ @class = ]
'class'
, [ @name = ]
N
'name'
, [ @new_name = ]
N
'new_name'
[ ; ]
```
