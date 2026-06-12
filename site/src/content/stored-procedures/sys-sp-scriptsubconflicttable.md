---
name: "sys.sp_scriptsubconflicttable"
title: "sp_scriptsubconflicttable"
category: "general"
description: "Generates script for creating a conflict table on the Subscriber for a given queued subscription article. The script that is generated is executed at the Subscriber on the subscription database. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_scriptsubconflicttable
              [ @publication = ]
              N
              'publication'
              , [ @article = ]
              N
              'article'
              [ , [ @alter = ] alter ]
              [ , [ @usesqlclr = ] usesqlclr ]
              [ ; ]
---

## Description

Generates script for creating a conflict table on the Subscriber for a given queued subscription article. The script that is generated is executed at the Subscriber on the subscription database. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_scriptsubconflicttable
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ , [ @alter = ] alter ]
[ , [ @usesqlclr = ] usesqlclr ]
[ ; ]
```
