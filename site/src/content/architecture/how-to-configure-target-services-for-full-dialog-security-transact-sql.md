---
title: "How to: Configure Target Services for Full Dialog Security (Transact-SQL)"
topic: "service-broker"
description: |
  09/02/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  SQL Server uses dialog security for any conversation to a service for which a remote service

  binding exists in the database that hosts
tags:
  - "service-broker"
  - "how-to-configure-target-services-for-full-dialog-security-transact-sql"
pubDate: 2025-12-01
---

09/02/2025

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server uses dialog security for any conversation to a service for which a remote service

binding exists in the database that hosts the initiating service. When the database that hosts

the target service contains a user that corresponds to the user that created the dialog, then the

dialog uses full security.

To make sure that a target service uses dialog security, create a user the initiating service can

use to log in. For each initiating service, create a user and install the certificate for the initiating

user. A target service doesn't use a remote service binding.

1. Create a user without a login.

2. Create a certificate for the user.

3. Make that user the owner of the target service.

4. Back up the certificate to a file.

5. Grant permission for the target service user to receive messages from the queue that the

target service uses.

6. Provide the certificate and the name of the initiating service to the database administrator

for the remote database.

７

Note

The certificate must be encrypted with the master key. For more information, see

.

７

Note

Only back up the certificate for this user. Don't back up or distribute the private key

associated with the certificate.
