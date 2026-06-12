---
name: "sys.sp_msx_set_account"
title: "sp_msx_set_account"
category: "general"
description: "Sets the SQL Server Agent master server account name and password on the target server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_msx_set_account
  [ [ @credential_name = ]
  N
  'credential_name'
  ]
  [ , [ @credential_id = ] credential_id ]
  [ ; ]
---

## Description

Sets the SQL Server Agent master server account name and password on the target server.

## Syntax

```sql
sp_msx_set_account
[ [ @credential_name = ]
N
'credential_name'
]
[ , [ @credential_id = ] credential_id ]
[ ; ]
```

## Examples

### Example 1

`sp_msx_set_account`

### Example 2

`EXECUTE`

### Example 3

```sql
USE msdb;
GO
EXECUTE dbo.sp_msx_get_account;
GO msx_connection msx_credential_id msx_credential_name msx_login_name
-------------- ----------------- -------------------- ----------------------------
-
1 65538 MsxAccount
AdventureWorks2022\MsxAccount
```

### Example 4

`sp_msx_set_account`

### Example 5

`MsxAccount`

### Example 6

```sql
USE msdb;
GO
EXECUTE dbo.sp_msx_set_account @credential_name = MsxAccount;
GO
```
