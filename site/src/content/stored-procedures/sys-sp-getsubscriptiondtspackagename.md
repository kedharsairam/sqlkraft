---
name: "sys.sp_getsubscriptiondtspackagename"
title: "sp_getsubscriptiondtspackagename"
category: "general"
description: "Returns the name of the Data Transformation Services (DTS) package used to transform data before they are sent to a Subscriber."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_getsubscriptiondtspackagename
              [ @publication = ]
              N
              'publication'
              [ , [ @subscriber = ]
              N
              'subscriber'
              ]
              [ ; ]
---

## Description

Returns the name of the Data Transformation Services (DTS) package used to transform data before they are sent to a Subscriber. This stored procedure is executed at the Publisher on any ## Syntax

```sql
sp_getsubscriptiondtspackagename
[ @publication = ]
N
'publication'
[ , [ @subscriber = ]
N
'subscriber'
]
[ ; ]
```

## Permissions

Description The name of the DTS package. is used in snapshot replication and transactional replication. Only members of the fixed server role or the fixed database role can execute. ﾉ Expand table
