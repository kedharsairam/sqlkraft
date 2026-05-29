---
name: 'sys.sp_helpstats'
title: 'sp_helpstats'
category: 'general'
description: 'SQL database in Microsoft Fabric Returns statistics information about columns and indexes on the specified table. Transact-SQL syntax conventions Specifies the table on which to provide statistics information. no default. A one-part or two-part name can be specified. Specifies the extent of information to provide. lists statistics for all indexes and also columns that have statistics created on th'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpstats
  [ @objname = ]
  N
  'objname'
  [ , [ @results = ]
  N
  'results'
  ]
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Returns statistics information about columns and indexes on the specified table. Transact-SQL syntax conventions Specifies the table on which to provide statistics information. no default. A one-part or two-part name can be specified. Specifies the extent of information to provide. lists statistics for all indexes and also columns that have statistics created on them.

## Syntax

```sql
sp_helpstats
[ @objname = ]
N
'objname'
[ , [ @results = ]
N
'results'
]
[ ; ]
```
