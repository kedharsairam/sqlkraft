---
name: "sys.synonyms"
title: "sys.synonyms"
category: "compatibility"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each synonym object that is For a list of columns that this view inherits, see Fully quoted name of the object to which the user of The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Object Cat"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
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

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each synonym object that is For a list of columns that this view inherits, see Fully quoted name of the object to which the user of The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Object Catalog Views (Transact-SQL)

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

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Contains a row for each synonym object that is = SN. Description For a list of columns that this view inherits, see sys.objects (Transact-SQL) . Fully quoted name of the object to which the user of this synonym is redirected. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) Last updated on 11/18/2025 ﾉ Expand table See Also
