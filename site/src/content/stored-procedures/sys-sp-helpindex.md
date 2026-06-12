---
name: "sys.sp_helpindex"
title: "sp_helpindex"
category: "general"
description: "Reports information about the indexes on a table or view. The qualified or nonqualified name of a user-defined table or view. , with no default. Quotation marks are required only if a qualified table or view name is specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpindex [ @objname = ]
              N
              'objname'
              [ ; ]
---

## Description

Reports information about the indexes on a table or view. The qualified or nonqualified name of a user-defined table or view. , with no default. Quotation marks are required only if a qualified table or view name is specified. If a fully qualified name, including a database name, is provided, the database name must be the name of the current database.

## Syntax

```sql
sp_helpindex [ @objname = ]
N
'objname'
[ ; ]
```
