---
title: "Register Mirrored Database"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  Use this dialog box to register one or more mirrored databases on a given server instance by

  adding the database or databases to the Database Mirrorin
tags:
  - "high-availability"
  - "register-mirrored-database"
pubDate: 2025-12-01
---

Article

•

02/01/2024

SQL Server

Use this dialog box to register one or more mirrored databases on a given server instance by

adding the database or databases to the Database Mirroring Monitor. When a database is

added, Database Mirroring Monitor locally caches information about the database, its partners,

and how to connect to the partners.

Start Database Mirroring Monitor (SQL Server Management Studio)

Select a server instance from the list, which contains server instances to which Database

Mirroring Monitor already has a connection stored, or click. To specify new credentials

for a listed server instance, click

and connect using the new credentials.

To specify new credentials for the server instance, click

and connect using the new

credentials. While connecting to a server instance, Database Mirroring Monitor displays.

The

grid lists the mirrored databases on the server instance.

The grid contains the following columns:

）

Important

If you are a member of the

fixed server role on the principal server instance but

not on the mirror server instance, you can only see status on the principal server instance.

７

Note

To register databases on multiple server instances, after you finish checking the desired

databases for one server instance, click

, and then select another server instance.
