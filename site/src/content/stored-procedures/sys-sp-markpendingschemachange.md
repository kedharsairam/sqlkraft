---
name: "sys.sp_markpendingschemachange"
title: "sp_markpendingschemachange"
category: "general"
description: "Used for supportability of merge publications by enabling an administrator to skip selected pending schema changes, so that they aren't replicated. This stored procedure is executed at the Publisher on the publication database. Identifies a pending schema change. sp_enumeratependingschemachanges to list the pending schema changes for the publication. This stored procedure can cause schema changes"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_markpendingschemachange
              [ @publication = ]
              N
              'publication'
              [ , [ @schemaversion = ] schemaversion ]
              [ , [ @status = ]
              N
              'status'
              ]
              [ ; ]
---

## Description

Used for supportability of merge publications by enabling an administrator to skip selected pending schema changes, so that they aren't replicated. This stored procedure is executed at the Publisher on the publication database. Identifies a pending schema change. sp_enumeratependingschemachanges to list the pending schema changes for the publication. This stored procedure can cause schema changes not to be replicated.

## Syntax

```sql
sp_markpendingschemachange
[ @publication = ]
N
'publication'
[ , [ @schemaversion = ] schemaversion ]
[ , [ @status = ]
N
'status'
]
[ ; ]
```
