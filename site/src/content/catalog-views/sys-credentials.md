---
name: "sys.credentials"
title: "sys.credentials"
category: "compatibility"
description: "Returns one row for each server-level credential."
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  ALTER
      CREDENTIAL Saddles
      WITH
      IDENTITY
      =
      'RettigB'
      ,
      SECRET =
      'sdrlk8$40-dksli87nNN8'
      ;
      GO
---

## Description

Analytics Platform System (PDW) Returns one row for each server-level credential.

## Syntax

```sql
ALTER
CREDENTIAL Saddles
WITH
IDENTITY
=
'RettigB'
,
SECRET =
'sdrlk8$40-dksli87nNN8'
;
GO
```

## Permissions

Article • 02/28/2023 Returns one row for each server-level credential. Description credential_id ID of the credential. Is unique in the server. name Name of the credential. Is unique in the server. credential_identity Name of the identity to use. This will generally be a Windows user. It does not have to be unique. create_date Time at which the credential was created. modify_date Time at which the credential was last modified. target_type Type of credential. Returns NULL for traditional credentials, CRYPTOGRAPHIC PROVIDER for credentials mapped to a cryptographic provider. For more information about external key management providers, see Extensible Key Management (EKM). target_id ID of the object that the credential is mapped to. Returns 0 for traditional credentials and non-0 for credentials mapped to a cryptographic provider. For more information about external key management providers, see Extensible Key Management (EKM). For database-level credentials, see sys.database_scoped_credentials. Requires either permission or permission. In addition, the principal must not be denied permission. ﾉ Expand table See Also DROP DATABASE SCOPED CREDENTIAL (Transact-SQL) CREATE CREDENTIAL (Transact-SQL) sys.credentials (Transact-SQL) xp_cmdshell (Transact-SQL) CREATE CREDENTIAL (Transact-SQL) sys.credentials (Transact-SQL) System stored procedures (Transact-SQL) Security stored procedures (Transact-SQL)
## Examples

### Example 1

`sys.credentials`

### Example 2

```sql
ALTER ANY CREDENTIAL
```

### Example 3

```sql
CONTROL
SERVER
```

### Example 4

```sql
DROP
CREDENTIAL credential_name
```
