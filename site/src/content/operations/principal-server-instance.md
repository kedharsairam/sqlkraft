---
title: "Principal Server Instance"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  Use this page to specify information about the server instance of the principal database. The

  principal database is the copy of the database that begi
tags:
  - "high-availability"
  - "principal-server-instance"
pubDate: 2025-12-01
---

Article

•

02/01/2024

SQL Server

Use this page to specify information about the server instance of the principal database. The

principal database is the copy of the database that begins the mirroring session. After the

session has begun, the principal database is the copy of the database that accepts user

changes. (When a failover occurs, the principal and mirroring roles are swapped; therefore, the

initial principal database might not remain the principal database.)

Establish a Database Mirroring Session Using Windows Authentication (SQL Server

Management Studio)

Start the Configuring Database Mirroring Security Wizard (SQL Server Management

Studio)

Because database mirroring in SQL Server Management Studio is always configured from the

principal server, the current server instance is always the principal server instance.

The behavior of this option depends on whether the mirroring endpoint exists for this server

instance, as follows:

If the listener port does not exist for this server instance, port number 5022 is displayed in

the

text box. You can use any available port number, such as, 7022.

When the mirroring endpoint already exists, the port number from the endpoint is

displayed. If you need to change the port, use an ALTER ENDPOINT command. For more

information, see

ALTER ENDPOINT (Transact-SQL).

７

Note

A port number is required.
