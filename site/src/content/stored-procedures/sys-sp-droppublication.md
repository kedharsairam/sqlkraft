---
name: "sys.sp_droppublication"
title: "sp_droppublication"
category: "general"
description: "Drops a publication and its associated Snapshot Agent. All subscriptions must be dropped before dropping a publication. The articles in the publication are dropped automatically. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_droppublication
      [ @publication = ]
      N
      'publication'
      [ , [ @ignore_distributor = ] ignore_distributor ]
      [ , [ @publisher = ]
      N
      'publisher'
      ]
      [ , [ @from_backup = ] from_backup ]
      [ ; ]
---

## Description

Drops a publication and its associated Snapshot Agent. All subscriptions must be dropped before dropping a publication. The articles in the publication are dropped automatically. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_droppublication
[ @publication = ]
N
'publication'
[ , [ @ignore_distributor = ] ignore_distributor ]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @from_backup = ] from_backup ]
[ ; ]
```
