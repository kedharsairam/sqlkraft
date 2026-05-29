---
name: 'sys.asymmetric_keys'
title: 'sys.asymmetric_keys'
category: 'objects'
description: 'Bit length of the key.'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
RSA_1024

RSA_2048

Bit length of the key.

Login SID for this key. For Extensible Key

Management keys this value will be NULL.

String representation of the login SID of the key. For

Extensible Key Management keys this value will be

NULL.

Public key.

System use only.

Type of cryptographic provider:

CRYPTOGRAPHIC PROVIDER = Extensible Key

Management keys

NULL = Non-Extensible Key Management keys

GUID for the cryptographic provider. For non-

Extensible Key Management keys this value will be

NULL.

sql_variant

Algorithm ID for the cryptographic provider. For non-

Extensible Key Management keys this value will be

NULL.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Security Catalog Views (Transact-SQL)

Extensible Key Management (EKM)

Catalog Views (Transact-SQL)

See Also

Encryption Hierarchy

CREATE ASYMMETRIC KEY (Transact-SQL)

Last updated on 11/18/2025
