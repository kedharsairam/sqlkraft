---
name: "sys.sp_pkeys"
title: "sp_pkeys"
category: "general"
description: "Returns primary key information for a single table in the current environment. Syntax for SQL Server, Azure SQL Database, Azure Synapse Analytics, Analytics Platform System Specifies the table for which to return information. Wildcard pattern matching isn't supported. Specifies the table owner of the s"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_pkeys
  [ @table_name = ]
  N
  'table_name'
  [ , [ @table_owner = ]
  N
  'table_owner'
  ]
  [ , [ @table_qualifier = ]
  N
  'table_qualifier'
  ]
  [ ; ]
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns primary key information for a single table in the current environment. Syntax for SQL Server, Azure SQL Database, Azure Synapse Analytics, Analytics Platform System Specifies the table for which to return information. Wildcard pattern matching isn't supported. Specifies the table owner of the specified table.

## Syntax

```sql
sp_pkeys
[ @table_name = ]
N
'table_name'
[ , [ @table_owner = ]
N
'table_owner'
]
[ , [ @table_qualifier = ]
N
'table_qualifier'
]
[ ; ]
```
