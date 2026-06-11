---
name: "sys.sp_db_vardecimal_storage_format"
title: "sp_db_vardecimal_storage_format"
category: "general"
description: "storage format state of a database or enables a database for storage format. In SQL Server 2008 (10.0.x) and later versions, user databases are always enabled. However, because storage format is deprecated. Enabling databases for the format is only necessary in SQL Server 2005 (9.x)."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_db_vardecimal_storage_format
  [ [ @dbname = ]
  N
  'dbname'
  ]
  [ , [ @vardecimal_storage_format = ]
  'vardecimal_storage_format'
  ]
  [ ; ]
---

## Description

storage format state of a database or enables a database for storage format. In SQL Server 2008 (10.0.x) and later versions, user databases are always enabled. However, because storage format is deprecated. Enabling databases for the format is only necessary in SQL Server 2005 (9.x). The name of the database for which the storage format is to be changed. . If the database name is omitted, the format status of all the databases in the instance of SQL Server are returned.

## Syntax

```sql
sp_db_vardecimal_storage_format
[ [ @dbname = ]
N
'dbname'
]
[ , [ @vardecimal_storage_format = ]
'vardecimal_storage_format'
]
[ ; ]
```
