---
name: "sys.sp_helpmergealternatepublisher"
title: "sp_helpmergealternatepublisher"
category: "general"
description: "Returns a list of all servers enabled as alternate Publishers for merge publications. This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions The name of the alternate Publisher. The name of the publication database."
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

Returns a list of all servers enabled as alternate Publishers for merge publications. This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions The name of the alternate Publisher. The name of the publication database.

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
