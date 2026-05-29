---
name: 'sys.sp_replmonitorhelppublisher'
title: 'sp_replmonitorhelppublisher'
category: 'general'
description: 'Returns current status information for one or more Publishers associated with a Distributor. This stored procedure, which is used to monitor replication, is executed at the Distributor on Transact-SQL syntax conventions The name of the Publisher the status of which is being monitored. , information is returned for all Publishers that use the Distributor. Identified for informational purposes only.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replmonitorhelppublisher
  [ [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @refreshpolicy = ] refreshpolicy ]
  [ ; ]
---

## Description

Returns current status information for one or more Publishers associated with a Distributor. This stored procedure, which is used to monitor replication, is executed at the Distributor on Transact-SQL syntax conventions The name of the Publisher the status of which is being monitored. , information is returned for all Publishers that use the Distributor. Identified for informational purposes only. Not supported. Future compatibility is not

## Syntax

```sql
sp_replmonitorhelppublisher
[ [ @publisher = ]
N
'publisher'
]
[ , [ @refreshpolicy = ] refreshpolicy ]
[ ; ]
```

## Permissions

is used with all types of replication. Only members of the fixed server role at the Distributor or members of the or fixed database roles in the distribution database can execute . Programmatically monitor replication Related content
