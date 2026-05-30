---
name: "sys.sp_helpdistributor"
title: "sp_helpdistributor"
category: "general"
description: "Lists information about the Distributor, distribution database, working directory, and SQL Server Agent user account. This stored procedure is executed at the Publisher on the publication database or any database. Transact-SQL syntax conventions value that returns a result set. The name of the distribution database. only value that returns a result set."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpdistributor [ [ @distributor = ]
  'distributor'
  OUTPUT
  ]
  [ , [ @distribdb = ]
  'distribdb'
  OUTPUT
  ]
  [ , [ @directory = ]
  'directory'
  OUTPUT
  ]
  [ , [ @account = ]
  'account'
  OUTPUT
  ]
  [ , [ @min_distretention = ] min_distretention
  OUTPUT
  ]
  [ , [ @max_distretention = ] max_distretention
  OUTPUT
  ]
  [ , [ @history_retention = ] history_retention
  OUTPUT
  ]
  [ , [ @history_cleanupagent = ]
  'history_cleanupagent'
  OUTPUT
  ]
  [ , [ @distrib_cleanupagent = ]
  'distrib_cleanupagent'
  OUTPUT
  ]
  [ , [ @publisher = ]
  'publisher'
  ]
  [ , [ @local = ]
  'local'
  ]
  [ , [ @rpcsrvname = ]
  'rpcsrvname'
  OUTPUT
  ]
  [ , [ @publisher_type = ]
  'publisher_type'
  OUTPUT
  ]
  [ ; ]
---

## Description

Lists information about the Distributor, distribution database, working directory, and SQL Server Agent user account. This stored procedure is executed at the Publisher on the publication database or any database. Transact-SQL syntax conventions value that returns a result set. The name of the distribution database. only value that returns a result set.

## Syntax

```sql
sp_helpdistributor [ [ @distributor = ]
'distributor'
OUTPUT
]
[ , [ @distribdb = ]
'distribdb'
OUTPUT
]
[ , [ @directory = ]
'directory'
OUTPUT
]
[ , [ @account = ]
'account'
OUTPUT
]
[ , [ @min_distretention = ] min_distretention
OUTPUT
]
[ , [ @max_distretention = ] max_distretention
OUTPUT
]
[ , [ @history_retention = ] history_retention
OUTPUT
]
[ , [ @history_cleanupagent = ]
'history_cleanupagent'
OUTPUT
]
[ , [ @distrib_cleanupagent = ]
'distrib_cleanupagent'
OUTPUT
]
[ , [ @publisher = ]
'publisher'
]
[ , [ @local = ]
'local'
]
[ , [ @rpcsrvname = ]
'rpcsrvname'
OUTPUT
]
[ , [ @publisher_type = ]
'publisher_type'
OUTPUT
]
[ ; ]
```
