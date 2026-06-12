---
name: "sys.sp_publisherproperty"
title: "sp_publisherproperty"
category: "general"
description: "Displays or changes publisher properties for non-SQL Server Publishers. This stored procedure is executed at the Distributor."
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

Displays or changes publisher properties for non-SQL Server Publishers. This stored procedure is executed at the Distributor.

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

When changing the property for a running job, you must restart the job for the new interval to take effect. Only members of the fixed server role at the Distributor can execute. Configure the Transaction Set Job for an Oracle Publisher System stored procedures (Transact-SQL)
