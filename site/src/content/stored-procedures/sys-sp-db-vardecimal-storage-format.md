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

storage format state of a database or enables a database for storage format. In SQL Server 2008 (10.0.x) and later versions, user databases are always enabled. However, because storage format is deprecated. Enabling databases for the format is only necessary in SQL Server 2005 (9.x).

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
