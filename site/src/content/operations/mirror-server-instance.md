---
title: "Mirror Server Instance"
topic: "high-availability"
description: |
  Article

  •

  11/25/2024

  Applies to:

  SQL Server

  Use this page to specify information about the server instance with the mirror database.

  Establish a Database Mirroring Session Using Windows Authenti
tags:
  - "high-availability"
  - "mirror-server-instance"
pubDate: 2025-12-01
---

Article

•

11/25/2024

Applies to:

SQL Server

Use this page to specify information about the server instance with the mirror database.

Establish a Database Mirroring Session Using Windows Authentication (SQL Server

Management Studio)

Start the Configuring Database Mirroring Security Wizard (SQL Server Management

Studio)

If a mirror server instance is already specified (on the

page of the

dialog box), that instance is displayed; for more information, see

Database

Properties (Mirroring Page)

.

Otherwise, enter the name of the mirror server instance. Note that the mirror server instance

cannot be the same as the principal server instance.

If a mirror server instance has not been specified, click

. This displays the

dialog box in which you can specify the server instance and establish a connection.

If the instance has been specified, but the wizard lacks a connection with sufficient permission

to check for the existence of the endpoint, click

. This displays the

dialog box with the server instance pre-selected and unchangeable. Specify a domain account

with sufficient permission, and connect to the server instance.

）

Important

The mirror server instance must be running the same edition of SQL Server, either

Standard or Enterprise, as the principal server instance. Also, we strongly recommend that

they run on comparable systems that can handle identical workloads.
