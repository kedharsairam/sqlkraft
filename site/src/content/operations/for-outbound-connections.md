---
title: "For outbound connections"
topic: "high-availability"
description: |
  Article
  
  •
  
  11/25/2024
  
  Applies to:
  
  SQL Server
  
  This topic describes the steps for configuring server instances to use certificates to authenticate
  
  outbound connections for database mirroring. Outbo
tags:
  - "high-availability"
  - "for-outbound-connections"
pubDate: 2025-12-01
---

Article

•

11/25/2024

Applies to:

SQL Server

This topic describes the steps for configuring server instances to use certificates to authenticate

outbound connections for database mirroring. Outbound connection configuration must be

done before you can set up inbound connections.

The process of configuring outbound connections, involves the following general steps:

1. In the

database, create a database Master Key.

2. In the

database, create an encrypted certificate on the server instance.

3. Create an endpoint for the server instance using its certificate.

4. Back up the certificate to a file and securely copy it to the other system or systems.

You must complete these steps for each partner and the witness, if there is one.

The following procedure describes these steps in detail. For each step, the procedure provides

an example for configuring a server instance on a system named HOST_A. The accompanying

Example section demonstrates the same steps for another server instance on a system named

HOST_B.

1. On the

database, create the database Master Key, if none exists. To view the

existing keys for a database, use the

sys.symmetric_keys

catalog view.

７

Note

All mirroring connections on a server instance use a single database mirroring endpoint,

and you must specify the authentication method of the server instance when you create

the endpoint.