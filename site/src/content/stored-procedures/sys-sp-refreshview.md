---
name: "sys.sp_refreshview"
title: "sp_refreshview"
category: "general"
description: "Updates the metadata for the specified non-schema-bound view. Persistent metadata for a view can become outdated because of changes to the underlying objects upon which the view identifier, but can only refer to views in the current database. (success) or a nonzero number (failure). should be run when changes are made to the objects"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_refreshview [ @viewname = ]
      'viewname'
      [ ; ]
---

## Description

Updates the metadata for the specified non-schema-bound view. Persistent metadata for a view can become outdated because of changes to the underlying objects upon which the view identifier, but can only refer to views in the current database. (success) or a nonzero number (failure). should be run when changes are made to the objects underlying the view, which affects the definition of the view. Otherwise,

## Syntax

```sql
sp_refreshview [ @viewname = ]
'viewname'
[ ; ]
```

## Permissions
