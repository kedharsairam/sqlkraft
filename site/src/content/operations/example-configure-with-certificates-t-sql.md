---
title: "Example: Configure with Certificates (T-SQL)"
topic: "high-availability"
description: "This example shows all the stages required to create a database mirroring session using certificate-based authentication. The examples in this topic u"
tags: ["high-availability","example-configure-with-certificates-t-sql"]
pubDate: "2025-12-01"
---

This example shows all the stages required to create a database mirroring session using

certificate-based authentication. The examples in this topic use Transact-SQL. Unless you can

guarantee that your network is secure, we recommend that you use encryption for database

mirroring connections.

When copying a certificate to another system, use a secure copy method. Be extremely careful

to keep all of your certificates secure.

The following example demonstrates what must be done on one partner that resides on

HOST_A. In this example, the two partners are the default server instances on three computer

systems. The two server instances run in nontrusted Windows domains, so certificate-based

authentication is required.

The initial principal role is taken by HOST_A, and the mirror role is taken by HOST_B.

Setting up database mirroring using certificates involves four general stages, of which three

stages-1, 2, and 4-are demonstrated by this example. These stages are as follows:

1.

Configuring Outbound Connections

This example shows the steps for:

a. Configuring Host_A for outbound connections.

b. Configuring Host_B for outbound connections.

For information about this stage of setting up database mirroring, see

Allow a Database

Mirroring Endpoint to Use Certificates for Outbound Connections (Transact-SQL).

2.

Configuring Inbound Connections

This example shows the steps for:

a. Configuring Host_A for inbound connections.

b. Configuring Host_B for inbound connections.
