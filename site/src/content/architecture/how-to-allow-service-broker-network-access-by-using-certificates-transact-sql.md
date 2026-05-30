---
title: "How to: Allow Service Broker Network Access by Using Certificates (Transact-SQL)"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  To allow another instance to send messages using certificate-based Service Broker transport

  security, you create a user for the other
tags:
  - "service-broker"
  - "how-to-allow-service-broker-network-access-by-using-certificates-transact-sql"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

To allow another instance to send messages using certificate-based Service Broker transport

security, you create a user for the other instance and install the certificate for the other

instance.

1. Obtain the certificate for the other instance from a trusted source. Typically, this involves

sending the certificate using encrypted email or transferring the certificate on physical

media such as a floppy disk.

2. Create a login.

3. Create a user for the login in the

database.

4. Install the certificate for the other instance in the

database. The user created in

step 3 owns the certificate.

5. Grant the login

access to the Service Broker endpoint.

6. Dump the certificate that's used for Service Broker transport security in the local instance.

7. Provide the certificate to the administrator of the other database. The administrator of the

remote database installs this certificate using the previous steps 1 - 4.

７

Note

Only install certificates from trusted sources.

７

Note

Only dump the certificate used for transport security. Don't dump or distribute the

private key associated with the certificate.

```sql
master master
CONNECT
```
