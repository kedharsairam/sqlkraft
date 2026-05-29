---
name: 'sys.sp_update_proxy'
title: 'sp_update_proxy'
category: 'general'
description: 'Defines attributes of a SQL Server Agent proxy account. This table is stored in the ID of the proxy account. Name of the proxy account. ID of the credential that the proxy account uses. Status of the proxy account: Description that the user entered when the proxy account was Microsoft Windows security_identifier of the user or group associated with the proxy credential at the time the proxy is add'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_update_proxy
  [ [ @proxy_id = ] proxy_id ]
  [ , [ @proxy_name = ]
  N
  'proxy_name'
  ]
  [ , [ @credential_name = ]
  N
  'credential_name'
  ]
  [ , [ @credential_id = ] credential_id ]
  [ , [ @new_name = ]
  N
  'new_name'
  ]
  [ , [ @enabled = ] enabled ]
  [ , [ @description = ]
  N
  'description'
  ]
  [ ; ]
---

## Description

Defines attributes of a SQL Server Agent proxy account. This table is stored in the ID of the proxy account. Name of the proxy account. ID of the credential that the proxy account uses. Status of the proxy account: Description that the user entered when the proxy account was Microsoft Windows security_identifier of the user or group associated with the proxy credential at the time the proxy is added. To ensure that you have the latest information (for example, after an Date and time that the credential was created. Only members of the fixed server role can access the dbo.sysproxylogin (Transact-SQL) dbo.sysproxysubsystem (Transact-SQL) dbo.syssubsystems (Transact-SQL)

## Syntax

```sql
sp_update_proxy
[ [ @proxy_id = ] proxy_id ]
[ , [ @proxy_name = ]
N
'proxy_name'
]
[ , [ @credential_name = ]
N
'credential_name'
]
[ , [ @credential_id = ] credential_id ]
[ , [ @new_name = ]
N
'new_name'
]
[ , [ @enabled = ] enabled ]
[ , [ @description = ]
N
'description'
]
[ ; ]
```

## Remarks

Applies to:

Defines attributes of a SQL Server Agent proxy account. This table is stored in the

Description

ID of the proxy account.

Name of the proxy account.

ID of the credential that the proxy account uses.

Status of the proxy account:

= Disabled.

description

Description that the user entered when the proxy account was

Microsoft Windows

security_identifier

of the user or group

associated with the proxy credential at the time the proxy is

added. To ensure that you have the latest information (for

example, after an

command), run

to refresh.

Date and time that the credential was created.

Only members of the

fixed server role can access the

dbo.sysproxylogin (Transact-SQL)

dbo.sysproxysubsystem (Transact-SQL)

dbo.syssubsystems (Transact-SQL)

Expand table
