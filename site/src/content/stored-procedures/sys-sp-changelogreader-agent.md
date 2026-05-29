---
name: 'sys.sp_changelogreader_agent'
title: 'sp_changelogreader_agent'
category: 'general'
description: 'Changes security properties of a Log Reader agent. This stored procedure is executed at the Publisher on the publication database. The login for the account under which the agent runs. . On Azure SQL Managed Instance, use a SQL Server account. When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the conn'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changelogreader_agent
  [ [ @job_login = ]
  N
  'job_login'
  ]
  [ , [ @job_password = ]
  N
  'job_password'
  ]
  [ , [ @publisher_security_mode = ] publisher_security_mode ]
  [ , [ @publisher_login = ]
  N
  'publisher_login'
  ]
  [ , [ @publisher_password = ]
  N
  'publisher_password'
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Changes security properties of a Log Reader agent. This stored procedure is executed at the Publisher on the publication database. The login for the account under which the agent runs. . On Azure SQL Managed Instance, use a SQL Server account. When configuring a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain text. You should encrypt the connection between the Publisher and its remote Distributor

## Syntax

```sql
sp_changelogreader_agent
[ [ @job_login = ]
N
'job_login'
]
[ , [ @job_password = ]
N
'job_password'
]
[ , [ @publisher_security_mode = ] publisher_security_mode ]
[ , [ @publisher_login = ]
N
'publisher_login'
]
[ , [ @publisher_password = ]
N
'publisher_password'
]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
