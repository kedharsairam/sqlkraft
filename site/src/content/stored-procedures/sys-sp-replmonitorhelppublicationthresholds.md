---
name: "sys.sp_replmonitorhelppublicationthresholds"
title: "sp_replmonitorhelppublicationthresholds"
category: "general"
description: "Returns the threshold metrics set for a monitored publication. This stored procedure, which is used to monitor replication, is executed at the Distributor on the distribution database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replmonitorhelppublicationthresholds
  [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  [ , [ @publication_type = ] publication_type ]
  [ , [ @thresholdmetricname = ]
  N
  'thresholdmetricname'
  ]
  [ ; ]
---

## Description

Returns the threshold metrics set for a monitored publication. This stored procedure, which is used to monitor replication, is executed at the Distributor on the distribution database.

## Syntax

```sql
sp_replmonitorhelppublicationthresholds
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
[ , [ @publication_type = ] publication_type ]
[ , [ @thresholdmetricname = ]
N
'thresholdmetricname'
]
[ ; ]
```
