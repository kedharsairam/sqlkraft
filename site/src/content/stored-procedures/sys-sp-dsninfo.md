---
name: "sys.sp_dsninfo"
title: "sp_dsninfo"
category: "general"
description: "Returns ODBC or OLE DB data source information from the Distributor associated with the current server. This stored procedure is executed at the Distributor on any database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dsninfo
  [ @dsn = ]
  'dsn'
  [ , [ @infotype = ]
  'infotype'
  ]
  [ , [ @login = ]
  'login'
  ]
  [ , [ @password = ]
  'password'
  ]
  [ , [ @dso_type = ] dso_type ]
  [ ; ]
---

## Description

Returns ODBC or OLE DB data source information from the Distributor associated with the current server. This stored procedure is executed at the Distributor on any database.

## Syntax

```sql
sp_dsninfo
[ @dsn = ]
'dsn'
[ , [ @infotype = ]
'infotype'
]
[ , [ @login = ]
'login'
]
[ , [ @password = ]
'password'
]
[ , [ @dso_type = ] dso_type ]
[ ; ]
```

## Permissions

is used in all types of replication. retrieves ODBC or OLE DB data source information that shows whether the database can be used for replication or querying. Only members of the fixed server role can execute. sp_enumdsn (Transact-SQL) System stored procedures (Transact-SQL)
