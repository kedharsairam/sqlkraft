---
title: "Establish a session"
topic: "high-availability"
description: |
  Article
  
  •
  
  02/01/2024
  
  Applies to:
  
  SQL Server
  
  To establish a database mirroring session and to modify the properties of database mirroring
  
  for a database, use the
  
  page of the
  
  dialog box.Before y
tags:
  - "high-availability"
  - "establish-a-session"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

To establish a database mirroring session and to modify the properties of database mirroring

for a database, use the

page of the

dialog box.Before you use

the

page to configure database mirroring, ensure that the following requirements

have been met:

The principal and mirror server instances must be running the same edition of SQL

Server-either Standard or Enterprise. Also, we strongly recommend that they run on

comparable systems that can handle identical workloads.

The mirror database must exist and be current.

Creating a mirror database requires restoring a recent backup of the principal database

(using WITH NORECOVERY) on the mirror server instance. It also requires taking one or

more log backups after the full backup and restoring them in sequence to the mirror

database (using WITH NORECOVERY). For more information, see

Prepare a Mirror

Database for Mirroring (SQL Server)

.

If the server instances are running under different domain user accounts, each requires a

login in the

database of the others. If the login does not exist, you must create it

before configuring mirroring. For more information, see

Allow Network Access to a

Database Mirroring Endpoint Using Windows Authentication (SQL Server)

.

７

Note

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use Always On availability groups instead.

７

Note

A witness server instance is not available in every edition of Microsoft SQL Server. For

a list of features that are supported by the editions of SQL Server, see

.