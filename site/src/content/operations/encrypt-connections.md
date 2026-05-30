---
title: "Encrypt connections"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  SQL Server on Linux can use Transport Layer Security (TLS) to encrypt data that is transmitted

  across a network between a client application and an instance of SQL
tags:
  - "linux-operations"
  - "encrypt-connections"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

SQL Server on Linux can use Transport Layer Security (TLS) to encrypt data that is transmitted

across a network between a client application and an instance of SQL Server. SQL Server supports

the same TLS protocols on both Windows and Linux: 1.2, 1.1, and 1.0.

The steps to configure TLS are specific to the operating system on which SQL Server is running.

Make sure your certificates follow these requirements:

The current system time must be after the

property of the certificate and before

the

property of the certificate.

The certificate must be meant for server authentication. This requires the

property of the certificate to specify

.

The certificate must be created by using the

option of

. Usually, the

certificate's key usage property (

) also includes key encipherment

(

).

The

property of the certificate must indicate that the common name (CN) is the

same as the host name or fully qualified domain name (FQDN) of the server computer.

７

Note

Starting in SQL Server 2025 (17.x):

TLS 1.3 is enabled by default

SUSE Linux Enterprise Server (SLES) isn't supported

７

Note

Wild card certificates are supported.

```cmd
Valid from
Valid to
Enhanced Key
Usage
Server Authentication (1.3.6.1.5.5.7.3.1)
KeySpec
```
