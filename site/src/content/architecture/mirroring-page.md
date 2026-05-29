---
title: "Mirroring page"
topic: "collation"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Access this page from the principal database, and use it to configure and to modify the
  
  properties of database mirroring for a database. Also use it t
tags:
  - "collation"
  - "mirroring-page"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Access this page from the principal database, and use it to configure and to modify the

properties of database mirroring for a database. Also use it to launch the Configure Database

Mirroring Security Wizard, to view the status of a mirroring session, and to pause or remove

the database mirroring session.

Establish a Database Mirroring Session Using Windows Authentication (SQL Server

Management Studio)

Click this button to launch the

If the wizard completes successfully, the action taken depends on whether mirroring has

already begun, as follows:

If mirroring has

not begun.

The property page caches that connection information and, also, caches a value that

indicates whether the mirror database has the partner property set.

At the end of the wizard, you are prompted to start database mirroring using the

default server network addresses and operating mode. If you need to change the

addresses or operating mode, click

.

If mirroring has

begun.

If the witness server was changed in the wizard, it is set accordingly.

）

Important

Security must be configured before you can start mirroring. If mirroring has not been

started, you must begin by using the wizard. The

page textboxes are disabled

until the wizard has been finished.

ﾉ

Expand table