---
name: "sys.sp_helpreplicationdboption"
title: "sp_helpreplicationdboption"
category: "general"
description: "Shows whether databases at the Publisher are enabled for replication. This stored procedure is executed at the Publisher on any database. Not supported for Oracle Publishers. databases at the Publisher, otherwise only information on the specified database is returned. Information isn't returned for any databases on which the user doesn't have the appropriate Restric"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_helpreplicationdboption
      [ [ @dbname = ]
      N
      'dbname'
      ]
      [ , [ @type = ]
      N
      'type'
      ]
      [ , [ @reserved = ] reserved ]
      [ ; ]
---

## Description

Shows whether databases at the Publisher are enabled for replication. This stored procedure is executed at the Publisher on any database. Not supported for Oracle Publishers. databases at the Publisher, otherwise only information on the specified database is returned. Information isn't returned for any databases on which the user doesn't have the appropriate Restricts the result set to contain only databases on which the specified replication option

## Syntax

```sql
sp_helpreplicationdboption
[ [ @dbname = ]
N
'dbname'
]
[ , [ @type = ]
N
'type'
]
[ , [ @reserved = ] reserved ]
[ ; ]
```

## Permissions

is used in snapshot, transactional, and merge replication. Members of the fixed server role can execute for any database. Members of the fixed database role can execute for that database. sp_replicationdboption (Transact-SQL) System stored procedures (Transact-SQL)
