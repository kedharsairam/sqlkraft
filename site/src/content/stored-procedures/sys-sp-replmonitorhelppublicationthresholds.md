---
name: 'sys.sp_replmonitorhelppublicationthresholds'
title: 'sp_replmonitorhelppublicationthresholds'
category: 'general'
description: 'Returns the threshold metrics set for a monitored publication. This stored procedure, which is used to monitor replication, is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the published database. , and can be one of these values.'
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

Returns the threshold metrics set for a monitored publication. This stored procedure, which is used to monitor replication, is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the published database. , and can be one of these values.

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
