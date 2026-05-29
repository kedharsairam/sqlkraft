---
title: "Witness Server Instance"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  Use this page to specify information about the server instance that is to serve as the witness for

  the session.

  Establish a Database Mirroring Sessio
tags:
  - "high-availability"
  - "witness-server-instance"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

Use this page to specify information about the server instance that is to serve as the witness for

the session.

Establish a Database Mirroring Session Using Windows Authentication (SQL Server

Management Studio)

Start the Configuring Database Mirroring Security Wizard (SQL Server Management

Studio)

If a witness server instance is already specified (on the

page of the

dialog box), that instance is displayed (for more information, see

Database

Properties (Mirroring Page)

).

Otherwise, this list box displays the name of the current server. Be aware that the witness server

instance cannot be the same as the principal or mirror server instances.

If a witness server instance has not been specified, click

. This displays the

dialog box in which you can specify the server instance and establish a connection.

If the instance has been specified, but the wizard lacks a connection with sufficient permission

to check for the existence of the endpoint, click

. This displays the

dialog box with the server instance pre-selected and unchangeable. Specify a domain account

with sufficient permission, and connect to the server instance.

７

Note

A witness server instance is not available in every edition of Microsoft SQL Server. For a list

of features that are supported by the editions of SQL Server, see

.
