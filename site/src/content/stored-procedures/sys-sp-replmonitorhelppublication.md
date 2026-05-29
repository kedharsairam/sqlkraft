---
name: "sys.sp_replmonitorhelppublication"
title: "sp_replmonitorhelppublication"
category: "general"
description: "Returns current status information for one or more publications at a Publisher. This stored procedure, which is used to monitor replication, is executed at the Distributor on the Transact-SQL syntax conventions The name of the Publisher the status of which is being monitored. , information is returned for all Publishers that use the Distributor. The name of the published database. , then informati"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replmonitorhelppublication
  [ [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @publisher_db = ]
  N
  'publisher_db'
  ]
  [ , [ @publication = ]
  N
  'publication'
  ]
  [ , [ @publication_type = ] publication_type ]
  [ , [ @refreshpolicy = ] refreshpolicy ]
  [ ; ]
---

## Description

Returns current status information for one or more publications at a Publisher. This stored procedure, which is used to monitor replication, is executed at the Distributor on the Transact-SQL syntax conventions The name of the Publisher the status of which is being monitored. , information is returned for all Publishers that use the Distributor. The name of the published database. , then information is returned for all published databases at the Publisher.

## Syntax

```sql
sp_replmonitorhelppublication
[ [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ , [ @publication = ]
N
'publication'
]
[ , [ @publication_type = ] publication_type ]
[ , [ @refreshpolicy = ] refreshpolicy ]
[ ; ]
```
