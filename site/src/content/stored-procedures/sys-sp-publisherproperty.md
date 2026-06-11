---
name: "sys.sp_publisherproperty"
title: "sp_publisherproperty"
category: "general"
description: "Displays or changes publisher properties for non-SQL Server Publishers. This stored procedure is executed at the Distributor. Transact-SQL syntax conventions The name of the heterogeneous Publisher."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_publisherproperty
  [ @publisher = ]
  N
  'publisher'
  [ , [ @propertyname = ]
  N
  'propertyname'
  ]
  [ , [ @propertyvalue = ]
  N
  'propertyvalue'
  ]
  [ ; ]
---

## Description

Displays or changes publisher properties for non-SQL Server Publishers. This stored procedure is executed at the Distributor. Transact-SQL syntax conventions The name of the heterogeneous Publisher. The name of the property being set. Specifies whether transactions at the Publisher are grouped into transactionally consistent sets (Xactsets) for subsequent processing. A value of that Xactsets can be created, which is the default. A value of

## Syntax

```sql
sp_publisherproperty
[ @publisher = ]
N
'publisher'
[ , [ @propertyname = ]
N
'propertyname'
]
[ , [ @propertyvalue = ]
N
'propertyvalue'
]
[ ; ]
```

## Permissions

When changing the property for a running job, you must restart the job for the new interval to take effect. Only members of the fixed server role at the Distributor can execute . Configure the Transaction Set Job for an Oracle Publisher System stored procedures (Transact-SQL) Related content
