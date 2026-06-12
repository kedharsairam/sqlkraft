---
title: "How to: Create Certificates for Service Broker Transport Security (Transact-SQL)"
topic: "service-broker"
description: |
  09/02/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  To set up Service Broker transport security for an instance of SQL Server, you first create a

  certificate in the

  database by using th
tags:
  - "service-broker"
  - "how-to-create-certificates-for-service-broker-transport-security-transact-sql"
pubDate: 2025-12-01
---

09/02/2025

SQL Server

Azure SQL Managed Instance

To set up Service Broker transport security for an instance of SQL Server, you first create a

certificate in the

database by using the

Transact-SQL statement.

This statement creates both a public key and a private key. You can also use the

statement to load an existing X.509 certificate. For more information on creating

certificates, see

CREATE CERTIFICATE. After creating the certificate, use the

or

statement to set the Service Broker endpoint to use the new certificate.

For more information using certificates for Service Broker transport security, see

How to: Allow

Service Broker network access by using certificates.

Create a certificate in the

database.

CREATE CERTIFICATE (Transact-SQL)

CREATE ENDPOINT (Transact-SQL)

ALTER ENDPOINT (Transact-SQL)

```sql
master
CREATE CERTIFICATE
CREATE
CERTIFICATE
CREATE ENDPOINT
ALTER ENDPOINT master
USE master
;
GO
-- Create a certificate owned by dbo.
CREATE
CERTIFICATE TransportSecurity
AUTHORIZATION [dbo]
ENCRYPTION
BY
PASSWORD
=
'**(34ader#$lqQEUer13'
WITH
SUBJECT =
'Instance certificate for transport security'
;
GO
```
