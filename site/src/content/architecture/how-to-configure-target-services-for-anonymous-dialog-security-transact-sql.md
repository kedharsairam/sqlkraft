---
title: "How to: Configure Target Services for Anonymous Dialog Security (Transact-SQL)"
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
  - "how-to-configure-target-services-for-anonymous-dialog-security-transact-sql"
pubDate: 2025-12-01
---

09/02/2025

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server uses dialog security for any conversation to a service for which a remote service

binding exists in the database that hosts the initiating service. If the remote service binding

specifies

, the dialog uses anonymous security. In this case, there's no need for

the target database to contain a user for the initiating service. The initiating service acts as

public in the target database.

1. Create a user without a login.

2. Create a certificate for the user.

3. Back up the certificate to a file.

4. Grant permission for the target service user to receive messages from the queue that the

target service uses.

5. Grant permission for public to send messages to the target service.

6. Provide the certificate and the name of the target service to the database administrator

for the remote database.

７

Note

The certificate must be encrypted with the master key. For more information, see

.

７

Note

Only back up the certificate for this user. Don't back up or distribute the private key

associated with the certificate.

```sql
ANONYMOUS = ON
```
