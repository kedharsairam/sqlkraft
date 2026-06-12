---
title: "Options page"
topic: "collation"
description: "Use this page to view or modify options for the selected database. For more information about the options available on this page, see ALTER DATABASE"
tags: ["collation","options-page"]
pubDate: "2025-12-01"
---

Use this page to view or modify options for the selected database. For more information about

the options available on this page, see

ALTER DATABASE SET Options (Transact-SQL)

and

ALTER

DATABASE SCOPED CONFIGURATION (Transact-SQL).

Specify the collation of the database by selecting from the list. For more information, see

Set or

Change the Database Collation.

Specify one of the following models for recovering the database:

,

, or.

For more information about recovery models, see

Recovery Models (SQL Server).

Specify the latest version of SQL Server that the database supports. For possible values, see

ALTER DATABASE (Transact-SQL) Compatibility Level. When a SQL Server database is upgraded,

the compatibility level for that database is retained if possible, or changed to the minimum

level supported for the new SQL Server.

Specify none or partial to designate if this is a contained database. For more information about

contained databases, see

Contained Databases. The server property

must be set to

before a database can be configured as contained.

Specify whether the database shuts down cleanly and frees resources after the last user exits.

）

Important

Enabling partially contained databases delegates control over access to the instance of

to the owners of the database. For more information, see.
