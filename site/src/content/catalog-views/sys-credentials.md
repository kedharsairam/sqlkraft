---
name: 'sys.credentials'
title: 'sys.credentials'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)


## Returns one row for each server-level credential.

## Description
credential_id

ID of the credential. Is unique in the server.

name

Name of the credential. Is unique in the server.

credential_identity

Name of the identity to use. This will generally be a Windows user.

It does not have to be unique.

create_date

Time at which the credential was created.

modify_date

Time at which the credential was last modified.

target_type

Type of credential. Returns NULL for traditional credentials,

CRYPTOGRAPHIC PROVIDER for credentials mapped to a

cryptographic provider. For more information about external key

management providers, see

Extensible Key Management (EKM)

.

target_id

ID of the object that the credential is mapped to. Returns 0 for

traditional credentials and non-0 for credentials mapped to a

cryptographic provider. For more information about external key

management providers, see

Extensible Key Management (EKM)

.

For database-level credentials, see

sys.database_scoped_credentials

.

Requires either

permission or

permission. In

addition, the principal must not be denied

permission.

ﾉ

Expand table

See Also

sys.database_scoped_credentials

Credentials (Database Engine)

Security Catalog Views (Transact-SQL)

Principals (Database Engine)

CREATE CREDENTIAL (Transact-SQL)

```sql
VIEW ANY DEFINITION
```

```sql
ALTER ANY CREDENTIAL
```

```sql
VIEW ANY DEFINITION
```
