---
name: "sys.sp_helppeerrequests"
title: "sp_helppeerrequests"
category: "general"
description: "Returns information on all status requests received by participants in a peer-to-peer replication topology, where these requests were initiated by executing published database in the topology. This stored procedure is executed on the publication database at a Publisher participating in a peer-to-peer replication topology. For more Peer-to-Peer - Transactional Replication Transact-SQL syntax conven"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helppeerrequests
  [ @publication = ]
  N
  'publication'
  [ , [ @description = ]
  N
  'description'
  ]
  [ ; ]
---

## Description

Returns information on all status requests received by participants in a peer-to-peer replication topology, where these requests were initiated by executing published database in the topology. This stored procedure is executed on the publication database at a Publisher participating in a peer-to-peer replication topology. For more Peer-to-Peer - Transactional Replication ## Syntax

```sql
sp_helppeerrequests
[ @publication = ]
N
'publication'
[ , [ @description = ]
N
'description'
]
[ ; ]
```
