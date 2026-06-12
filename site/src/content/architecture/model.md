---
title: "model"
topic: "collation"
description: "The database is used as the template for all databases created on an instance of SQL Server."
tags: ["collation","model"]
pubDate: 2025-12-01
---

The

database is used as the template for all databases created on an instance of SQL

Server. Because

is created every time SQL Server is started, the

database must

always exist on a SQL Server system. The entire contents of the

database, including

database options, are copied to the new database. Some of the settings of

are also used

for creating a new

during start up, so the

database must always exist on a SQL

Server system.

Newly created user databases use the same

recovery model

as the model database. The default

is user configurable. To learn the current recovery model of the model, see

View or Change the

Recovery Model of a Database (SQL Server).

When a CREATE DATABASE statement is issued, the first part of the database is created by

copying in the contents of the

database. The rest of the new database is then filled with

empty pages.

If you modify the

database, all databases created afterward will inherit those changes.

For example, you could set permissions or database options, or add objects such as tables,

functions, or stored procedures. File properties of the

database are an exception, and

are ignored except the initial size of the data file. The default initial size of the model database

data and log file is 8 MB.

The following table lists initial configuration values of the

data and log files.

）

Important

If you modify the

database with user-specific template information, we recommend

that you back up. For more information, see.

ﾉ

Expand table
