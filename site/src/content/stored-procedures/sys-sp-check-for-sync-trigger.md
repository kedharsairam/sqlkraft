---
name: "sys.sp_check_for_sync_trigger"
title: "sp_check_for_sync_trigger"
category: "general"
description: "Determines whether a user-defined trigger or stored procedure is being called in the context of a replication trigger, which is used for immediate updating subscriptions. This stored procedure is executed at the Publisher on the publication database or at the Subscriber on the The object ID of the table being checked for immediate updating triggers."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_check_for_sync_trigger
              [ @tabid = ] tabid
              [ , [ @trigger_op = ]
              'trigger_op'
              OUTPUT
              ]
              [ , [ @fonpublisher = ] fonpublisher ]
              [ ; ]
---

## Description

Determines whether a user-defined trigger or stored procedure is being called in the context of a replication trigger, which is used for immediate updating subscriptions. This stored procedure is executed at the Publisher on the publication database or at the Subscriber on the The object ID of the table being checked for immediate updating triggers. Specifies if the output parameter is to return the type of trigger it's being called from.

## Syntax

```sql
sp_check_for_sync_trigger
[ @tabid = ] tabid
[ , [ @trigger_op = ]
'trigger_op'
OUTPUT
]
[ , [ @fonpublisher = ] fonpublisher ]
[ ; ]
```

## Permissions

The code can also be added to a trigger on a table at the Publisher; the code is similar, but the call to includes an extra parameter. SQL Any user with permissions in the sys.objects system view can execute.
