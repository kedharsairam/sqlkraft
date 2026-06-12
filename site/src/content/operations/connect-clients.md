---
title: "Connect clients"
topic: "high-availability"
description: "To connect to a database mirroring session, a client can use either SQL Server Native Client or .NET Framework Data Provider for SQL Server."
tags: ["high-availability","connect-clients"]
pubDate: "2025-12-01"
---

To connect to a database mirroring session, a client can use either SQL Server Native Client or.NET Framework Data Provider for SQL Server. When configured for a SQL Server database,

these data access providers both fully support database mirroring. For information about

programming considerations for using a mirrored database, see

Using Database Mirroring. In

addition, the current principal server instance must be available and the login of the client must

have been created on the server instance. For more information, see

Troubleshoot Orphaned

Users (SQL Server). Client connections to a database mirroring session do not involve the

witness server instance, if one exists.

For the initial connection to a mirrored database, a client must supply a connection string that

minimally supplies the name of a server instance. This required server name should identify the

current principal server instance and is known as the

initial partner name.

Optionally, the connection string can also supply the name of another server instance, which

should identify the current mirror server instance, for use if the initial partner is unavailable

during the first connection attempt. The second name is known as the

failover partner name.

The connection string must also supply a database name. This is necessary to enable failover

attempts by the data access provider.

On receiving a connection string, the data access provider stores the initial partner name and

the failover partner name, if supplied, in a cache in the client's volatile memory (for managed

code, the cache is scoped to the application domain). Once cached, the initial partner name is

never updated by the data access provider. When the client supplies the failover partner name,

the data access provider also stores this failover partner name temporarily in case the provider

cannot connect using the initial partner name.

A database mirroring session does not protect against server-access problems that are specific

to clients, such as when a client computer is having a problems communicating with the

network. A connection attempt to a mirrored database can also fail for a variety of reasons that

are unrelated to the data-access provider; for example, a connection attempt can fail because
