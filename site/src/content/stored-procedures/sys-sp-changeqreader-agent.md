---
name: 'sys.sp_changeqreader_agent'
title: 'sp_changeqreader_agent'
category: 'general'
description: 'Changes security properties of a Queue Reader agent. This stored procedure is executed at the Distributor on the distribution database or at the Publisher on the publication database. Transact-SQL syntax conventions The login for the Windows account under which the agent runs. The password for the Windows account under which the agent runs. Specifies whether the procedure is being executed at the '
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changeqreader_agent
  [ [ @job_login = ]
  N
  'job_login'
  ]
  [ , [ @job_password = ]
  N
  'job_password'
  ]
  [ , [ @frompublisher = ] frompublisher ]
  [ ; ]
---

## Description

Changes security properties of a Queue Reader agent. This stored procedure is executed at the Distributor on the distribution database or at the Publisher on the publication database. Transact-SQL syntax conventions The login for the Windows account under which the agent runs. The password for the Windows account under which the agent runs. Specifies whether the procedure is being executed at the Publisher.

## Syntax

```sql
sp_changeqreader_agent
[ [ @job_login = ]
N
'job_login'
]
[ , [ @job_password = ]
N
'job_password'
]
[ , [ @frompublisher = ] frompublisher ]
[ ; ]
```
