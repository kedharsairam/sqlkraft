---
name: "sys.sp_helpreplfailovermode"
title: "sp_helpreplfailovermode"
category: "general"
description: "Displays the current failover mode of a subscription. This stored procedure is executed at the Subscriber on any database. For more information about failover modes, see Subscriptions - For Transactional Replication The name of the Publisher that is participating in the update of this Subscriber. , with no default. The Publisher must already be configured for publis"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_helpreplfailovermode
      [ @publisher = ]
      N
      'publisher'
      , [ @publisher_db = ]
      N
      'publisher_db'
      , [ @publication = ]
      N
      'publication'
      [ , [ @failover_mode_id = ] failover_mode_id
      OUTPUT
      ]
      [ , [ @failover_mode = ]
      N
      'failover_mode'
      OUTPUT
      ]
      [ ; ]
---

## Description

Displays the current failover mode of a subscription. This stored procedure is executed at the Subscriber on any database. For more information about failover modes, see Subscriptions - For Transactional Replication The name of the Publisher that is participating in the update of this Subscriber. , with no default. The Publisher must already be configured for publishing.

## Syntax

```sql
sp_helpreplfailovermode
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
[ , [ @failover_mode_id = ] failover_mode_id
OUTPUT
]
[ , [ @failover_mode = ]
N
'failover_mode'
OUTPUT
]
[ ; ]
```
