---
name: "sys.sp_tables"
title: "sp_tables"
category: "general"
description: "Returns a list of objects that can be queried in the current environment. This means any table or view, except synonym objects. Syntax for SQL Server, Azure SQL Database, Azure Synapse Analytics, Analytics Platform System The table used to return catalog information."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_tables
      [ [ @table_name = ]
      N
      'table_name'
      ]
      [ , [ @table_owner = ]
      N
      'table_owner'
      ]
      [ , [ @table_qualifier = ]
      N
      'table_qualifier'
      ]
      [ , [ @table_type = ]
      'table_type'
      ]
      [ , [ @f
      U
      se
      P
      attern = ] f
      U
      se
      P
      attern ]
      [ ; ]
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns a list of objects that can be queried in the current environment. This means any table or view, except synonym objects. Syntax for SQL Server, Azure SQL Database, Azure Synapse Analytics, Analytics Platform System The table used to return catalog information. Wildcard pattern matching is supported.

## Syntax

```sql
sp_tables
[ [ @table_name = ]
N
'table_name'
]
[ , [ @table_owner = ]
N
'table_owner'
]
[ , [ @table_qualifier = ]
N
'table_qualifier'
]
[ , [ @table_type = ]
'table_type'
]
[ , [ @f
U se
P attern = ] f
U se
P attern ]
[ ; ]
```
