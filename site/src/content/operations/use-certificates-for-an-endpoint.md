---
title: "Use certificates for an endpoint"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  To enable certificate authentication for database mirroring on a given server instance, the

  system administrator must configure each server instance t
tags:
  - "high-availability"
  - "use-certificates-for-an-endpoint"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

To enable certificate authentication for database mirroring on a given server instance, the

system administrator must configure each server instance to use certificates on both outbound

and inbound connections. Outbound connections must be configured first.

Follow these steps on each server instance that you are configuring for database mirroring:

1. In the

database, create a database master key.

2. In the

database, create an encrypted certificate on the server instance.

3. Create an endpoint for the server instance using its certificate.

4. Back up the certificate to a file and securely copy it to the other system or systems.

You must complete these steps for each partner and the witness, if there is one.

For more information, see

Allow a Database Mirroring Endpoint to Use Certificates for

Outbound Connections (Transact-SQL)

.

Next, follow these steps for each partner that you are configuring for database mirroring. In the

database:

1. Create a login for the other system.

2. Create a user for that login.

７

Note

All mirroring connections on a server instance use a single database mirroring endpoint,

and you must specify the authentication method of the server instance when you create

the endpoint. Therefore, you can use only one form of authentication per server instance

for database mirroring.
