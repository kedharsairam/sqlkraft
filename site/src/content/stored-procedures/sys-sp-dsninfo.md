---
name: 'sys.sp_dsninfo'
title: 'sp_dsninfo'
category: 'general'
description: 'Returns ODBC or OLE DB data source information from the Distributor associated with the current server. This stored procedure is executed at the Distributor on any database. Transact-SQL syntax conventions The name of the ODBC DSN or OLE DB linked server. The type of information to return. If information types are returned. , and can be one of these values. Specifies the data source vendor name. S'
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

Returns ODBC or OLE DB data source information from the Distributor associated with the current server. This stored procedure is executed at the Distributor on any database. Transact-SQL syntax conventions The name of the ODBC DSN or OLE DB linked server. The type of information to return. If information types are returned. , and can be one of these values. Specifies the data source vendor name. Specifies the data source version.

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

is used in all types of replication. retrieves ODBC or OLE DB data source information that shows whether the database can be used for replication or querying. Only members of the fixed server role can execute . sp_enumdsn (Transact-SQL) System stored procedures (Transact-SQL) Related content
