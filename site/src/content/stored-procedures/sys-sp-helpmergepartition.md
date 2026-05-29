---
name: 'sys.sp_helpmergepartition'
title: 'sp_helpmergepartition'
category: 'general'
description: 'Returns partition information for the specified merge publication. This stored procedure is executed at the Publisher on any database. Transact-SQL syntax conventions value used to define a partition. . Supply this parameter to limit the result set to only partitions where resolves to the supplied value. value used to define a partition. . Supply this parameter to limit the result set to only part'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpmergepartition
  [ @publication = ]
  N
  'publication'
  [ , [ @suser_sname = ]
  N
  'suser_sname'
  ]
  [ , [ @host_name = ]
  N
  'host_name'
  ]
  [ ; ]
---

## Description

Returns partition information for the specified merge publication. This stored procedure is executed at the Publisher on any database. Transact-SQL syntax conventions value used to define a partition. . Supply this parameter to limit the result set to only partitions where resolves to the supplied value. value used to define a partition. . Supply this parameter to limit the result set to only partitions where

## Syntax

```sql
sp_helpmergepartition
[ @publication = ]
N
'publication'
[ , [ @suser_sname = ]
N
'suser_sname'
]
[ , [ @host_name = ]
N
'host_name'
]
[ ; ]
```
