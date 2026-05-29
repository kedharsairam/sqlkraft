---
name: 'sys.sp_create_removable'
title: 'sp_create_removable'
category: 'general'
description: 'Creates a removable media database. Creates three or more files (one for the system catalog tables, one for the transaction log, and one or more for the data tables) and places the Transact-SQL syntax conventions This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_create_removable
  [ [ @dbname = ]
  N
  'dbname'
  ]
  [ , [ @syslogical = ]
  N
  'syslogical'
  ]
  [ , [ @sysphysical = ]
  N
  'sysphysical'
  ]
  [ , [ @syssize = ] syssize ]
  [ , [ @loglogical = ]
  N
  'loglogical'
  ]
  [ , [ @logphysical = ]
  N
  'logphysical'
  ]
  [ , [ @logsize = ] logsize ]
  [ , [ @datalogical1 = ]
  N
  'datalogical1'
  ]
  [ , [ @dataphysical1 = ]
  N
  'dataphysical1'
  ]
  [ , [ @datasize1 = ] datasize1 ]
  [ , ... ]
  [ , [ @datalogical16 = ]
  N
  'datalogical16'
  ]
  [ , [ @dataphysical16 = ]
  N
  'dataphysical16'
  ]
  [ , [ @datasize16 = ] datasize16 ]
  [ ; ]
---

## Description

Creates a removable media database. Creates three or more files (one for the system catalog tables, one for the transaction log, and one or more for the data tables) and places the Transact-SQL syntax conventions This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_create_removable
[ [ @dbname = ]
N
'dbname'
]
[ , [ @syslogical = ]
N
'syslogical'
]
[ , [ @sysphysical = ]
N
'sysphysical'
]
[ , [ @syssize = ] syssize ]
[ , [ @loglogical = ]
N
'loglogical'
]
[ , [ @logphysical = ]
N
'logphysical'
]
[ , [ @logsize = ] logsize ]
[ , [ @datalogical1 = ]
N
'datalogical1'
]
[ , [ @dataphysical1 = ]
N
'dataphysical1'
]
[ , [ @datasize1 = ] datasize1 ]
[ , ... ]
[ , [ @datalogical16 = ]
N
'datalogical16'
]
[ , [ @dataphysical16 = ]
N
'dataphysical16'
]
[ , [ @datasize16 = ] datasize16 ]
[ ; ]
```

## Examples

### Example 1

```sql
inventory
```

### Example 2

```sql
EXECUTE
sp_create_removable
'inventory'
,
'invsys'
,
'C:\Program Files\Microsoft SQL
Server\MSSQL16.MSSQLSERVER\MSSQL\Data\invsys.mdf'
,
2,
'invlog'
,
'C:\Program Files\Microsoft SQL
Server\MSSQL16.MSSQLSERVER\MSSQL\Data\invlog.ldf'
,
4,
'invdata'
,
'C:\Program Files\Microsoft SQL
Server\MSSQL16.MSSQLSERVER\MSSQL\Data\invdata.ndf'
,
10;
```
