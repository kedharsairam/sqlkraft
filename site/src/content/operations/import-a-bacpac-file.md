---
title: "Import a bacpac file"
topic: "ssms"
description: "Import a file - to create a copy of the original database, with the data, on a new instance"
tags: ["ssms","import-a-bacpac-file"]
pubDate: 2025-12-01
---

Import a

file - to create a copy of the original database, with the data, on a new

instance of the Database Engine, or to Azure SQL Database. An export operation can be

combined with an import operation to migrate a database between instances or to create a

copy of a database deployed in Azure SQL Database. Options for easily importing a

include:

1. the

Wizard in SQL Server Management Studio

2. the

Wizard in SQL Server

Management Studio to deploy a database between an instance of the Database Engine

and a Azure SQL Database server, or between two Azure SQL Database servers

3. the

SqlPackage

command-line utility

The import process builds a new database in two stages.

1. The import creates a new database using the database model definition stored in the

export file, the same way a

deploy creates a new database from the

definition in a

file.

2. The import bulk copies in the data from the

export file.

By default, the database created during the import has all of the default settings from the

CREATE DATABASE statement, except that the database collation and compatibility level are set

to the values defined in the

export file. A

export file uses the values from the

original database.

Some database options, such as TRUSTWORTHY, DB_CHAINING, and

HONOR_BROKER_PRIORITY, can't be adjusted as part of the import process. Physical

properties, such as the number of filegroups, or the numbers and sizes of files can't be altered

as part of the import process. After the import completes, you can use the ALTER DATABASE

statement, SQL Server Management Studio, or SQL Server PowerShell to tailor the database.

For more information, see

Databases.

```cmd.bacpac.bacpac.bacpac.dacpac.dacpac
```
