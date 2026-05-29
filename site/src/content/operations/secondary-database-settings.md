---
title: "Secondary Database Settings"
topic: "high-availability"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Use this dialog box to configure and to modify the properties of a secondary database in the
  
  log shipping configuration.
  
  For an explanation of log sh
tags:
  - "high-availability"
  - "secondary-database-settings"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Use this dialog box to configure and to modify the properties of a secondary database in the

log shipping configuration.

For an explanation of log shipping concepts, see

About Log Shipping (SQL Server)

.

Displays the name of the instance of SQL Server currently configured to be a secondary server

in the log shipping configuration.

Displays the name of the secondary database for the log shipping configuration. When adding

a new secondary database to a log shipping configuration, you can choose a database from

the list or type the name of a new of the database into the box. If you enter the name of a new

database, you must select an option on the

tab that restores a full database

backup of the primary database into the secondary database. The new database is created as

part of the restore operation.

Connect to an instance of SQL Server for use as a secondary server in the log shipping

configuration. The account used to connect must be a member of the sysadmin fixed server

role on the secondary server instance.

The options are as follows:

Have SQL Server Management Studio configure your secondary database by backing up the

primary database and restoring it on the secondary server. If you entered a new database

name in the

box, the database will be created as part of the restore

operation.

Click if you want to restore the data and log files for the secondary database into nondefault

locations on the secondary server.