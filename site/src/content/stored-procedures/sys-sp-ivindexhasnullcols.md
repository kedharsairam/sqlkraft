---
name: "sys.sp_ivindexhasnullcols"
title: "sp_ivindexhasnullcols"
category: "general"
description: "Validates that the clustered index of the indexed view is unique, and doesn't contain any when the indexed view is going to be used to create a transactional publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the view to verify. The flag indicating whether the view index has columns that allow if the view index h"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_ivindexhasnullcols
  [ @viewname = ]
  N
  'viewname'
  , [ @fhasnullcols = ] fhasnullcols
  OUTPUT
  [ ; ]
---

## Description

Validates that the clustered index of the indexed view is unique, and doesn't contain any when the indexed view is going to be used to create a transactional publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the view to verify. The flag indicating whether the view index has columns that allow if the view index has columns that allow

## Syntax

```sql
sp_ivindexhasnullcols
[ @viewname = ]
N
'viewname'
, [ @fhasnullcols = ] fhasnullcols
OUTPUT
[ ; ]
```
