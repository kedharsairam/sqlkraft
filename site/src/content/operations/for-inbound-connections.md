---
title: "For inbound connections"
topic: "high-availability"
description: "This topic describes the steps for configuring server instances to use certificates to authenticate inbound connections for database mirroring. Before"
tags: ["high-availability","for-inbound-connections"]
pubDate: "2025-12-01"
---

This topic describes the steps for configuring server instances to use certificates to authenticate

inbound connections for database mirroring. Before you can set up inbound connections, you

must configure outbound connections on each server instance. For more information, see

Allow a Database Mirroring Endpoint to Use Certificates for Outbound Connections (Transact-

SQL).

The process of configuring inbound connections, involves the following general steps:

1. Create a login for other system.

2. Create a user for that login.

3. Obtain the certificate for the mirroring endpoint of the other server instance.

4. Associate the certificate with the user created in step 2.

5. Grant CONNECT permission on the login for that mirroring endpoint.

If there is a witness, you must also set up inbound connections for it. This requires setting up

logins, users, and certificates for the witness on both of the partners, and vice versa.

The following procedure describes these steps in detail. For each step, the procedure provides

an example for configuring a server instance on a system named HOST_A. The accompanying

Example section demonstrates the same steps for another server instance on a system named

HOST_B.

1. Create a login for the other system.

The following example creates a login for the system, HOST_B, in the

database of

the server instance on HOST_A; in this example, the login is named. Replace

with a valid password.

```cmd
HOST_B_login
<password>
```
