---
name: "sys.sp_db_increased_partitions"
title: "sp_db_increased_partitions"
category: "general"
description: "Enables or disables support for up to 15,000 partitions for the specified database. Transact-SQL syntax conventions isn't specified, the current database is used. Enables or disables support for 15,000 partitions on the specified database. isn't specified, the procedure returns to indicate support is enabled for the specified database, or to indicate support is disabled."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_db_increased_partitions
  [ [ @dbname = ]
  N
  'dbname'
  ]
  [ , [ @increased_partitions = ]
  'increased_partitions'
  ]
  [ ; ]
---

## Description

Enables or disables support for up to 15,000 partitions for the specified database. Transact-SQL syntax conventions isn't specified, the current database is used. Enables or disables support for 15,000 partitions on the specified database. isn't specified, the procedure returns to indicate support is enabled for the specified database, or to indicate support is disabled. This feature will be removed in a future version of SQL Server. Avoid using this feature in

## Syntax

```sql
sp_db_increased_partitions
[ [ @dbname = ]
N
'dbname'
]
[ , [ @increased_partitions = ]
'increased_partitions'
]
[ ; ]
```
