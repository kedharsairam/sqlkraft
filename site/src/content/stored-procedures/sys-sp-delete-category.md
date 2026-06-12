---
name: "sys.sp_delete_category"
title: "sp_delete_category"
category: "general"
description: "Removes the specified category of jobs, alerts, or operators from the current server. , with no default, and must be one of these The name of the category to be removed."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_category
              [ @class = ]
              'class'
              , [ @name = ]
              N
              'name'
              [ ; ]
---

## Description

Removes the specified category of jobs, alerts, or operators from the current server. , with no default, and must be one of these The name of the category to be removed.

## Syntax

```sql
sp_delete_category
[ @class = ]
'class'
, [ @name = ]
N
'name'
[ ; ]
```
