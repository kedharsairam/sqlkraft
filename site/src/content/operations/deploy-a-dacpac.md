---
title: "Deploy a dacpac"
topic: "ssms"
description: ""
tags: ["ssms","deploy-a-dacpac"]
pubDate: 2025-12-01
---

Deploying, or publishing, a registered data-tier application (DAC) from a DAC package to an

existing instance of the database engine or Azure SQL Database is available in a wizard from

Management Studio or Visual Studio SQL Server Data Tools. The publish action

incrementally updates a database schema to match the schema of a source

file. If the

database doesn't exist on the server, the publish operation creates it.

The deployment process registers a DAC instance by storing the DAC definition in the

system database (

in SQL Database); creates a database, then populates that database

with all the database objects defined in the DAC.

You can deploy the same DAC package to a single instance of the Database Engine multiple

times, but you must run the deployments one at a time. The DAC instance name specified for

each deployment must be unique within the instance of the Database Engine.

By default, the database created during the deployment has all of the default settings from the

CREATE DATABASE statement, except:

The database collation and compatibility level are set to the values defined in the DAC

package. A DAC package built from a database project in the SQL Server Developer Tools

uses the values set in the database project. A package extracted from an existing

database uses the values from the original database.

You can adjust some of the database settings, such as database name and file paths, in

the

page. You can't set the file paths when deploying to SQL

Database.

Some database options, such as TRUSTWORTHY, DB_CHAINING, and

HONOR_BROKER_PRIORITY, can't be adjusted as part of the deployment process. Physical

properties, such as the number of filegroups, or the numbers and sizes of files can't be altered

as part of the deployment process. After the deployment completes, you can use the ALTER

DATABASE statement, SQL Server Management Studio, or SQL Server PowerShell to tailor the

database.

```cmd.dacpac msdb master
```
