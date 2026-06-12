---
name: "sys.sp_addmergealternatepublisher"
title: "sp_addmergealternatepublisher"
category: "general"
description: "Adds the ability for a Subscriber to use an alternate synchronization partner. The publication properties must specify that Subscribers can synchronize with other Publishers. This stored procedure is executed at the Subscriber on the subscription database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_addmergealternatepublisher
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
      , [ @alternate_distributor = ]
      N
      'alternate_distributor'
      [ , [ @friendly_name = ]
      N
      'friendly_name'
      ]
      [ , [ @reserved = ]
      N
      'reserved'
      ]
      [ ; ]
---

## Description

Adds the ability for a Subscriber to use an alternate synchronization partner. The publication properties must specify that Subscribers can synchronize with other Publishers. This stored procedure is executed at the Subscriber on the subscription database.

## Syntax

```sql
sp_addmergealternatepublisher
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
, [ @alternate_distributor = ]
N
'alternate_distributor'
[ , [ @friendly_name = ]
N
'friendly_name'
]
[ , [ @reserved = ]
N
'reserved'
]
[ ; ]
```
