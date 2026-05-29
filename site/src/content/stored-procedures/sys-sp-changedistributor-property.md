---
name: 'sys.sp_changedistributor_property'
title: 'sp_changedistributor_property'
category: 'general'
description: 'SQL Server 2025 (17.x) and later versions. Specifies whether to trust the certificate used by the Distributor for encrypted connections. The default is SQL Server 2025 (17.x) and later versions. Specifies the expected host name in the Distributor''s certificate. SQL Server 2025 (17.x) and later versions. The value for the given Distributor property. , with a default of Secure defaults pertain to th'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  encrypt_distributor_connection
  mandatory
---

## Description

SQL Server 2025 (17.x) and later versions. Specifies whether to trust the certificate used by the Distributor for encrypted connections. The default is SQL Server 2025 (17.x) and later versions. Specifies the expected host name in the Distributor's certificate. SQL Server 2025 (17.x) and later versions. The value for the given Distributor property. , with a default of Secure defaults pertain to the underlying OLEDB provider 19, which enhances security. The option to override the default is less secure than configuring your instance to use a trusted certificate. After overriding the default, you have the option to configure SQL Server to use a certificate, and then use the procedure to set the property back to the secure

## Syntax

```sql
encrypt_distributor_connection
mandatory
```

## Permissions

is used in all types of replication. SQL To override the secure default of the OLEDB provider 19 and set so the distributor trusts the self-signed certificate, use the following example: SQL For more information, review the remote distributor breaking change in SQL Server 2025 . Only members of the fixed server role can execute . ７ Note Secure defaults pertain to the underlying OLEDB provider 19, which enhances security. The option to override the default is less secure than configuring your instance to use a trusted certificate. After overriding the default, you have the option to configure SQL Server to use a certificate, and then use the stored procedure to set the property back to the secure default.

## Remarks

Description

Applies to:

SQL Server 2025 (17.x) and

later versions.

Specifies whether to trust the certificate

used by the Distributor for encrypted

connections. The default is

Applies to:

SQL Server 2025 (17.x) and

later versions.

Specifies the expected host name in the

Distributor's certificate.

Applies to:

SQL Server 2025 (17.x) and

later versions.

All available

are printed.

The value for the given Distributor property.

, with a default of

(success) or

Secure defaults pertain to the underlying OLEDB provider 19, which enhances security. The

option to override the default is less secure than configuring your instance to use a

trusted certificate. After overriding the default, you have the option to configure SQL

Server to use a certificate, and then use the

procedure to set the

property back to the secure
