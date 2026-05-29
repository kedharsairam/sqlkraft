---
name: 'sys.sp_dropmergealternatepublisher'
title: 'sp_dropmergealternatepublisher'
category: 'general'
description: 'Removes an alternate Publisher from a merge publication. This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions The name of the current Publisher. The name of the current publication database. The name of the current publication.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropmergealternatepublisher
  [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  , [ @alternate_publisher = ]
  N
  'alternate_publisher'
  , [ @alternate_publisher_db = ]
  N
  'alternate_publisher_db'
  , [ @alternate_publication = ]
  N
  'alternate_publication'
  [ ; ]
---

## Description

Removes an alternate Publisher from a merge publication. This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions The name of the current Publisher. The name of the current publication database. The name of the current publication.

## Syntax

```sql
sp_dropmergealternatepublisher
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
, [ @alternate_publisher = ]
N
'alternate_publisher'
, [ @alternate_publisher_db = ]
N
'alternate_publisher_db'
, [ @alternate_publication = ]
N
'alternate_publication'
[ ; ]
```
