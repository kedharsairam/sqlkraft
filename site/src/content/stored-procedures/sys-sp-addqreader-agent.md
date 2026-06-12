---
name: "sys.sp_addqreader_agent"
title: "sp_addqreader_agent"
category: "general"
description: "Adds a Queue Reader agent for a given Distributor. This stored procedure is executed at the Distributor on the distribution database or at the Publisher on the publication database. The login for the Windows account under which the agent runs."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addqreader_agent
  [ [ @job_login = ]
  N
  'job_login'
  ]
  [ , [ @job_password = ]
  N
  'job_password'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @frompublisher = ] frompublisher ]
  [ ; ]
---

## Description

Adds a Queue Reader agent for a given Distributor. This stored procedure is executed at the Distributor on the distribution database or at the Publisher on the publication database. The login for the Windows account under which the agent runs. This Windows account is always used for agent connections to the The password for the Windows account under which the agent runs.

## Syntax

```sql
sp_addqreader_agent
[ [ @job_login = ]
N
'job_login'
]
[ , [ @job_password = ]
N
'job_password'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @frompublisher = ] frompublisher ]
[ ; ]
```
