---
name: "sys.sp_replqueuemonitor"
title: "sp_replqueuemonitor"
category: "general"
description: "Lists the queue messages from a SQL Server queue or Microsoft Message Queuing for queued updating subscriptions to a specified publication. If SQL Server queues are used, this stored procedure is executed at the Subscriber on the subscription database. If Message Queuing is used, this stored procedure is executed at the Distributor on the distribution database. Transact-SQL syntax conventions is u"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replqueuemonitor
  [ [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @publisherdb = ]
  N
  'publisherdb'
  ]
  [ , [ @publication = ]
  N
  'publication'
  ]
  [ , [ @tranid = ]
  N
  'tranid'
  ]
  [ , [ @queuetype = ] queuetype ]
  [ ; ]
---

## Description

Lists the queue messages from a SQL Server queue or Microsoft Message Queuing for queued updating subscriptions to a specified publication. If SQL Server queues are used, this stored procedure is executed at the Subscriber on the subscription database. If Message Queuing is used, this stored procedure is executed at the Distributor on the distribution database. Transact-SQL syntax conventions is used to get all Publishers.

## Syntax

```sql
sp_replqueuemonitor
[ [ @publisher = ]
N
'publisher'
]
[ , [ @publisherdb = ]
N
'publisherdb'
]
[ , [ @publication = ]
N
'publication'
]
[ , [ @tranid = ]
N
'tranid'
]
[ , [ @queuetype = ] queuetype ]
[ ; ]
```
