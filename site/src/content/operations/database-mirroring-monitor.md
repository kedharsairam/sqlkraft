---
title: "Database Mirroring Monitor"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  The Database Mirroring Monitor is part of the SQL Server Monitor, which is launched from SQL

  Server Management Studio.

  1. After connecting to the pri
tags:
  - "high-availability"
  - "database-mirroring-monitor"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

The Database Mirroring Monitor is part of the SQL Server Monitor, which is launched from SQL

Server Management Studio.

1. After connecting to the principal server instance, in Object Explorer, click the server name

to expand the server tree.

2. Expand

, and select the database to be monitored.

3. Right-click the database, select

, and then click

.

4. In the

dialog box, click

to

register one or more mirrored database.

For more information about Database Mirroring Monitor, see

Database Mirroring Monitor

Overview

.

７

Note

Database Mirroring Monitor is not available in every edition of Microsoft SQL Server. For a

list of features that are supported by the editions of SQL Server, see

.

７

Note

When you register a database at one partner, the database is automatically

registered at the other partner. If the monitor already has connection credentials for

the other partner instance, those are used to connect. Otherwise the monitor

attempts to connect using Windows Authentication. If you want to change the

credentials used to connect to either server instance, click

.
