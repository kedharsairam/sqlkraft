---
name: 'sys.sp_resyncmergesubscription'
title: 'sp_resyncmergesubscription'
category: 'general'
description: 'Resynchronizes a merge subscription to a known validation state that you specify. You can force convergence or synchronize the subscription database to a specific point in time, such as the last time there was a successful validation, or to a specified date. The snapshot isn''t reapplied when resynchronizing a subscription using this method. This stored procedure isn''t used for snapshot replication'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_resyncmergesubscription
  [ [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @publisher_db = ]
  N
  'publisher_db'
  ]
  , [ @publication = ]
  N
  'publication'
  [ , [ @subscriber = ]
  N
  'subscriber'
  ]
  [ , [ @subscriber_db = ]
  N
  'subscriber_db'
  ]
  , [ @resync_type = ] resync_type
  [ , [ @resync_date_str = ]
  N
  'resync_date_str'
  ]
  [ ; ]
---

## Description

Resynchronizes a merge subscription to a known validation state that you specify. You can force convergence or synchronize the subscription database to a specific point in time, such as the last time there was a successful validation, or to a specified date. The snapshot isn't reapplied when resynchronizing a subscription using this method. This stored procedure isn't used for snapshot replication subscriptions or transactional replication subscriptions. This

## Syntax

```sql
sp_resyncmergesubscription
[ [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
, [ @publication = ]
N
'publication'
[ , [ @subscriber = ]
N
'subscriber'
]
[ , [ @subscriber_db = ]
N
'subscriber_db'
]
, [ @resync_type = ] resync_type
[ , [ @resync_date_str = ]
N
'resync_date_str'
]
[ ; ]
```
