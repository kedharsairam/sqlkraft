---
title: "master"
topic: "collation"
description: "The database records all the system-level information for a SQL Server system. This includes instance"
tags: ["collation","master"]
pubDate: 2025-12-01
---

The

database records all the system-level information for a SQL Server system. This

includes instance-wide metadata such as logon accounts, endpoints, linked servers, and system

configuration settings. In SQL Server, system objects are no longer stored in the

database; instead, they are stored in the

Resource database. Also,

is the database that

records the existence of all other databases and the location of those database files and

records the initialization information for SQL Server. Therefore, SQL Server cannot start if the

database is unavailable.

The following table lists the initial configuration values of the

data and log files for SQL

Server and Azure SQL Managed Instance. The sizes of these files may vary slightly for different

editions of SQL Server.

Primary data

master

master.mdf

Autogrow by 10 percent until the disk is full.

Log

mastlog

mastlog.ldf

Autogrow by 10 percent to a maximum of 2 terabytes.

For information about how to move the

data and log files, see

Move System Databases.

）

Important

For Azure SQL Database single databases and elastic pools, only master database and

tempdb database apply. For more information, see. For a discussion of tempdb in the context of Azure SQL Database, see. For Azure SQL Managed Instance, all system databases

apply. For more information on Managed Instances in Azure SQL Database, see

ﾉ

Expand table

）

Important
