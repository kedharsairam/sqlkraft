---
name: 'sys.symmetric_keys'
title: 'sys.symmetric_keys'
category: 'objects'
description: 'Visibility Configuration'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Visibility Configuration

.

The RC4 algorithm is deprecated. This feature will be removed in a future version of SQL

Server. Avoid using this feature in new development work, and plan to modify applications that

currently use this feature.

DESX was incorrectly named. Symmetric keys created with ALGORITHM = DESX actually

use the TRIPLE DES cipher with a 192-bit key. The DESX algorithm is not provided. This

feature will be removed in a future version of SQL Server. Avoid using this feature in new

development work, and plan to modify applications that currently use this feature.

Symmetric keys created with ALGORITHM = TRIPLE_DES_3KEY use TRIPLE DES with a 192-

bit key.

Symmetric keys created with ALGORITHM = TRIPLE_DES use TRIPLE DES with a 128-bit

key.

Catalog Views (Transact-SQL)

Extensible Key Management (EKM)

Security Catalog Views (Transact-SQL)

Encryption Hierarchy

CREATE SYMMETRIC KEY (Transact-SQL)

Last updated on 11/18/2025

７

Note

The RC4 algorithm is only supported for backward compatibility. New material can only be

encrypted using RC4 or RC4_128 when the database is in compatibility level 90 or 100.

(Not recommended.) Use a newer algorithm such as one of the AES algorithms instead. In

SQL Server 2012 (11.x) material encrypted using RC4 or RC4_128 can be decrypted in any

compatibility level.

See Also
