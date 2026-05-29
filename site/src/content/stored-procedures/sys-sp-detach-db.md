---
name: 'sys.sp_detach_db'
title: 'sp_detach_db'
category: 'general'
description: 'Detaches a database that is currently not in use from a server instance and, optionally, runs on all tables before detaching. For a replicated database to be detached, it must be unpublished. For more information, see section later in this article. Transact-SQL syntax conventions The name of the database to be detached. Specifies whether to skip or run is performed to update information about the '
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_detach_db
  [ [ @dbname = ]
  N
  'dbname'
  ]
  [ , [ @skipchecks = ]
  N
  'skipchecks'
  ]
  [ , [ @keepfulltextindexfile = ]
  N
  'keepfulltextindexfile'
  ]
  [ ; ]
---

## Description

Detaches a database that is currently not in use from a server instance and, optionally, runs on all tables before detaching. For a replicated database to be detached, it must be unpublished. For more information, see section later in this article. Transact-SQL syntax conventions The name of the database to be detached. Specifies whether to skip or run is performed to update information about the data in the tables

## Syntax

```sql
sp_detach_db
[ [ @dbname = ]
N
'dbname'
]
[ , [ @skipchecks = ]
N
'skipchecks'
]
[ , [ @keepfulltextindexfile = ]
N
'keepfulltextindexfile'
]
[ ; ]
```
