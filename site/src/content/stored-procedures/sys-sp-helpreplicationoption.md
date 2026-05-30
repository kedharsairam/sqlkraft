---
name: "sys.sp_helpreplicationoption"
title: "sp_helpreplicationoption"
category: "general"
description: "Shows the types of replication options enabled for a server. This stored procedure is executed at any server on any database. Transact-SQL syntax conventions The name of the replication option to query for. A result set is returned when transactional replication is enabled. A result set is returned when merge replication is enabled."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpreplicationoption [ [ @optname = ]
  N
  'optname'
  ]
  [ ; ]
---

## Description

Shows the types of replication options enabled for a server. This stored procedure is executed at any server on any database. Transact-SQL syntax conventions The name of the replication option to query for. A result set is returned when transactional replication is enabled. A result set is returned when merge replication is enabled.

## Syntax

```sql
sp_helpreplicationoption [ [ @optname = ]
N
'optname'
]
[ ; ]
```
