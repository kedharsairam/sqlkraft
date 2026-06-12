---
name: "sys.sp_helppullsubscription"
title: "sp_helppullsubscription"
category: "general"
description: "Drops an anonymous agent for replication monitoring at the distributor from the Publisher. This stored procedure is executed at the Publisher on any database. The global identifier for an anonymous subscription. default. This identifier can be retrieved at the Subscriber using field of the returned result set is this global identifier. The type of subscription."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_helppullsubscription
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
      [ , [ @show_push = ]
      N
      'show_push'
      ]
      [ ; ]
---

## Description

Drops an anonymous agent for replication monitoring at the distributor from the Publisher. This stored procedure is executed at the Publisher on any database. The global identifier for an anonymous subscription. default. This identifier can be retrieved at the Subscriber using field of the returned result set is this global identifier. The type of subscription. , with no default. Valid values are , if snapshot replication or transactional replication using the Distribution Agent. , if merge replication using the Merge Agent.

## Syntax

```sql
sp_helppullsubscription
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
[ , [ @show_push = ]
N
'show_push'
]
[ ; ]
```

## Remarks

Drops an anonymous agent for replication monitoring at the distributor from the Publisher.

This stored procedure is executed at the Publisher on any database.

The global identifier for an anonymous subscription.

default. This identifier can be retrieved at the Subscriber using

value in the

field of the returned result set is this global identifier.

The type of subscription.

, with no default. Valid values are

, if snapshot replication or transactional replication using the Distribution Agent.

, if merge replication using the Merge Agent.

(success) or
