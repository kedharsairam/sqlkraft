---
name: "sys.sp_changereplicationserverpasswords"
title: "sp_changereplicationserverpasswords"
category: "general"
description: "Changes stored passwords for the Windows account or SQL Server login used by replication agents when connecting to servers in a replication topology. You would normally have to change a password for each individual agent running at a server, even if they all use the same login or account. This stored procedure enables you to change the password for all instances of a given SQL Server Login or Wind"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changereplicationserverpasswords
              [ @login_type = ] login_type
              , [ @login = ]
              N
              'login'
              , [ @password = ]
              N
              'password'
              [ , [ @server = ]
              N
              'server'
              ]
              [ ; ]
---

## Description

Changes stored passwords for the Windows account or SQL Server login used by replication agents when connecting to servers in a replication topology. You would normally have to change a password for each individual agent running at a server, even if they all use the same login or account. This stored procedure enables you to change the password for all instances of a given SQL Server Login or Windows account used by all replication agents that run at a

## Syntax

```sql
sp_changereplicationserverpasswords
[ @login_type = ] login_type
, [ @login = ]
N
'login'
, [ @password = ]
N
'password'
[ , [ @server = ]
N
'server'
]
[ ; ]
```
