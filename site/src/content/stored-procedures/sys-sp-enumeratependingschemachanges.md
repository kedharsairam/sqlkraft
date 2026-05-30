---
name: "sys.sp_enumeratependingschemachanges"
title: "sp_enumeratependingschemachanges"
category: "general"
description: "Returns a list of all pending schema changes. This stored procedure can be used with , which enables an administrator to skip selected pending schema changes so that they aren't replicated. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The lowest number schema change to include in the result set."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_enumeratependingschemachanges
  [ @publication = ]
  N
  'publication'
  [ , [ @starting_schemaversion = ] starting_schemaversion ]
  [ ; ]
---

## Description

Returns a list of all pending schema changes. This stored procedure can be used with , which enables an administrator to skip selected pending schema changes so that they aren't replicated. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The lowest number schema change to include in the result set.

## Syntax

```sql
sp_enumeratependingschemachanges
[ @publication = ]
N
'publication'
[ , [ @starting_schemaversion = ] starting_schemaversion ]
[ ; ]
```
