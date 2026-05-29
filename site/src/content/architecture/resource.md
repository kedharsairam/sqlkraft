---
title: "Resource"
topic: "collation"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  The Resource database is a read-only database that contains all the system objects that are

  included with SQL Server. SQL Server system objects, such
tags:
  - "collation"
  - "resource"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

The Resource database is a read-only database that contains all the system objects that are

included with SQL Server. SQL Server system objects, such as sys.objects, are physically

persisted in the Resource database, but they logically appear in the sys schema of every

database. The Resource database does not contain user data or user metadata.

The Resource database makes upgrading to a new version of SQL Server an easier and faster

procedure. In earlier versions of SQL Server, upgrading required dropping and creating system

objects. Because the Resource database file contains all system objects, an upgrade is now

accomplished simply by copying the single Resource database file to the local server.

The physical file names of the Resource database are mssqlsystemresource.mdf and

mssqlsystemresource.ldf. These files are located in <

drive

> :\Program Files\Microsoft SQL

Server\MSSQL<version>.<

instance_name

> \MSSQL\Binn\ and should not be moved. Each

instance of SQL Server has one and only one associated mssqlsystemresource.mdf file, and

instances do not share this file.

SQL Server cannot back up the Resource database. You can perform your own file-based or a

disk-based backup by treating the mssqlsystemresource.mdf file as if it were a binary (.EXE) file,

rather than a database file, but you cannot use SQL Server to restore your backups. Restoring a

backup copy of mssqlsystemresource.mdf can only be done manually, and you must be careful

not to overwrite the current Resource database with an out-of-date or potentially insecure

version.

２

Warning

Upgrades and service packs sometimes provide a new resource database which is installed

to the BINN folder. Changing the location of the resource database is not supported or

recommended.

）

Important
