---
name: "sys.sp_replmonitorhelpmergesession"
title: "sp_replmonitorhelpmergesession"
category: "general"
description: "Returns information on past sessions for a given replication Merge Agent, with one row returned for each session that matches the filtering criterion. This stored procedure, which is used to monitor merge replication, is executed at the Distributor on the distribution database or at the Subscriber on the subscription database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_replmonitorhelpmergesession
      [ [ @agent_name = ]
      N
      'agent_name'
      ]
      [ , [ @hours = ] hours ]
      [ , [ @session_type = ] session_type ]
      [ , [ @publisher = ]
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
      [ ; ]
---

## Description

Returns information on past sessions for a given replication Merge Agent, with one row returned for each session that matches the filtering criterion. This stored procedure, which is used to monitor merge replication, is executed at the Distributor on the distribution database or at the Subscriber on the subscription database. The range of time, in hours, for which historical agent session information is returned.

## Syntax

```sql
sp_replmonitorhelpmergesession
[ [ @agent_name = ]
N
'agent_name'
]
[ , [ @hours = ] hours ]
[ , [ @session_type = ] session_type ]
[ , [ @publisher = ]
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
[ ; ]
```
