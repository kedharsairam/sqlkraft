---
title: "msdb"
topic: "collation"
description: "The database is used by SQL Server Agent for scheduling alerts and jobs and by other features such as SQL Server Manageme"
tags: ["collation","msdb"]
pubDate: 2025-12-01
---

The

database is used by SQL Server Agent for scheduling alerts and jobs and by other

features such as SQL Server Management Studio, Service Broker and Database Mail.

For example, SQL Server automatically maintains a complete online backup-and-restore history

within tables in. This information includes the name of the party that performed the

backup, the time of the backup, and the devices or files where the backup is stored. SQL Server

Management Studio uses this information to propose a plan for restoring a database and

applying any transaction log backups. Backup events for all databases are recorded even if they

were created with custom applications or third-party tools. For example, if you use a Microsoft

Visual Basic application that calls SQL Server Management Objects (SMO) objects to perform

backup operations, the event is logged in the

system tables, the Microsoft Windows

application log, and the SQL Server error log. To help your protect the information that is

stored in

, we recommend that you consider placing the

transaction log on fault

tolerant storage.

By default,

uses the simple recovery model. If you use the

backup and restore history

tables, we recommend that you use the full recovery model for. For more information,

see

Recovery Models (SQL Server). Notice that when SQL Server is installed or upgraded and

whenever Setup.exe is used to rebuild the system databases, the recovery model of

is

automatically set to simple.

The following table lists the initial configuration values of the

data and log files. The sizes

of these files may vary slightly for different editions of SQL Server Database Engine.

）

Important

After any operation that updates

, such as backing up or restoring any

database, we recommend that you back up. For more information, see.

There are differences to whats available in the

database in Azure SQL

Managed Instance. Review

to learn more.

ﾉ

Expand table
