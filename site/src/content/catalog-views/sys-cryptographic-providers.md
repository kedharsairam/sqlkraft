---
name: 'sys.cryptographic_providers'
title: 'sys.cryptographic_providers'
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

Azure SQL Database

Azure SQL Managed Instance


## Returns one row for each registered cryptographic provider.

## Description
Identification number of the cryptographic provider.

Name of the cryptographic provider.

Unique provider GUID.

Version of the provider in the format '

aa.bb.cccc.dd

'.

Path to DLL that implements the Extensible Key Management (EKM)

Application Program Interface (API).

Whether the provider is enabled on the server or not.

0 = not enabled (default)

1 = enabled

The

view is visible to the public.

Security Catalog Views (Transact-SQL)

Encryption Hierarchy

Extensible Key Management (EKM)

CREATE CRYPTOGRAPHIC PROVIDER (Transact-SQL)

ﾉ

Expand table

See Also
