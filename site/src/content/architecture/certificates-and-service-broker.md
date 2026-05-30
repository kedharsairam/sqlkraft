---
title: "Certificates and Service Broker"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes how SQL Server uses certificates for Service Broker remote security.

  Service Broker remote security refers to o
tags:
  - "service-broker"
  - "certificates-and-service-broker"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes how SQL Server uses certificates for Service Broker remote security.

Service Broker remote security refers to operations that involve more than one SQL Server

instance when those operations use either dialog security or transport security.

Service Broker remote security maps an operation from outside an instance to a SQL Server

database principal. The operation then proceeds in the security context of that database

principal, with normal SQL Server permission checks. For example, when a message arrives for a

conversation that uses dialog security, Service Broker uses information in the message to

identify a database principal for the remote side of the conversation. SQL Server then verifies

that the principal has permission to connect to the database that hosts the destination service,

and permission to send a message to the destination service.

SQL Server uses certificates to verify a remote database's identity and to identify the local

database principal for the operation. Therefore, installing a certificate in SQL Server constitutes

a statement of trust in the database that holds the private key for the certificate. Carefully

manage the certificates that you install and the remote service bindings that you create.

To verify a remote server's identity, SQL Server must receive information that can be decrypted

with the public key in a certificate owned by a local database principal. If SQL Server can

successfully decrypt the information, it means that the remote database contains the private

key that corresponds to the public key in the local certificate. Once SQL Server verifies a

remote database's identity, the remote database can act with the permissions of the local

database principal.

For transport security, each database must trust the other database. Transport security can use

either certificates or Windows Authentication. For more information on transport security, see

Service Broker Transport Security

.

For dialog security, the initiator of the dialog must trust the target, and must be able to verify

the identity of the target. However, the target might allow connections from initiators that

７

Note

Only install certificates from trusted sources. Don't distribute private keys.
