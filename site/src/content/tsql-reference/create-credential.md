---
name: "CREATE CREDENTIAL"
title: "CREATE CREDENTIAL"
category: "statements"
description: "Creates a server-level credential for authentication to external resources."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---
## Syntax

```sql
CREATE CREDENTIAL credential_name
WITH IDENTITY = 'identity_name'
    [ , SECRET = 'secret' ]
[ FOR CRYPTOGRAPHIC PROVIDER cryptographic_provider_name ]
```

## Arguments

### credential_name

Specifies the name of the credential being created.

### IDENTITY = 'identity_name'

Specifies the name of the account to be used for authentication.

### SECRET = 'secret'

Specifies the secret (password or other authentication material) required for outgoing authentication.

### FOR CRYPTOGRAPHIC PROVIDER

Specifies that the credential is used by a cryptographic provider.

## Remarks

Credentials are used by SQL Server to authenticate to external resources such as file shares, Azure Storage, or other services.

## Examples

```sql
-- Create a credential for Azure Storage access
CREATE CREDENTIAL MyAzureStorageCredential
WITH IDENTITY = 'mystorageaccount',
     SECRET = '<storage_account_key>';
```
