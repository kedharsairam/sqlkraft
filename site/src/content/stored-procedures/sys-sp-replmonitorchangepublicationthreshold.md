---
name: 'sys.sp_replmonitorchangepublicationthreshold'
title: 'sp_replmonitorchangepublicationthreshold'
category: 'general'
description: 'Changes the monitoring threshold metric for a publication. This stored procedure, which is used to monitor replication, is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the published database. The name of the publication for which the monitoring threshold attributes are being changed.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replmonitorchangepublicationthreshold
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
  [ , [ @metric_id = ] metric_id ]
  [ , [ @thresholdmetricname = ]
  N
  'thresholdmetricname'
  ]
  [ , [ @value = ] value ]
  [ , [ @shouldalert = ] shouldalert ]
  [ , [ @mode = ] mode ]
  [ ; ]
---

## Description

Changes the monitoring threshold metric for a publication. This stored procedure, which is used to monitor replication, is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the published database. The name of the publication for which the monitoring threshold attributes are being changed.

## Syntax

```sql
sp_replmonitorchangepublicationthreshold
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
[ , [ @metric_id = ] metric_id ]
[ , [ @thresholdmetricname = ]
N
'thresholdmetricname'
]
[ , [ @value = ] value ]
[ , [ @shouldalert = ] shouldalert ]
[ , [ @mode = ] mode ]
[ ; ]
```
