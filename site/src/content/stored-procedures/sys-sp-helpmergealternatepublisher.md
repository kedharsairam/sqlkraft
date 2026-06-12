---
name: "sys.sp_helpmergealternatepublisher"
title: "sp_helpmergealternatepublisher"
category: "general"
description: "Returns a list of all servers enabled as alternate Publishers for merge publications. This stored procedure is executed at the Subscriber on the subscription database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpmergealternatepublisher
  [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  [ ; ]
---

## Description

Returns a list of all servers enabled as alternate Publishers for merge publications. This stored procedure is executed at the Subscriber on the subscription database.

## Syntax

```sql
sp_helpmergealternatepublisher
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
[ ; ]
```
