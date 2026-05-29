---
title: "Export a bacpac file"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  Exporting a database creates an export file that includes the definitions of the objects in t
tags:
  - "ssms"
  - "export-a-bacpac-file"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Exporting a database creates an export file that includes the definitions of the objects in the

database and all of the data in the tables. The export file (

) can then be imported to

another instance of the Database Engine, or to Azure SQL Database. The export-import

operations can be combined to migrate a

between instances, to create an archive, or

to create an on-premises copy of a database deployed in SQL Database.

The data-tier application (DAC) export process is related to the DAC extract process. Both

export and extract include the database schema in the produced file, but the export process is

limited to functionality available in the Azure SQL Database surface area. Learn more from the

SqlPackage portability documentation

.

The export process builds a

export file in two stages.

1. The export builds a portable definition in the export file -

file - the same way a

DAC extract builds a DAC definition in a DAC package file. The exported DAC definition

includes all of the objects in the current database. Suppose the export process is run

against a database initially deployed from a DAC, and changes were made directly to the

database after deployment. In that case, the exported definition matches the object set in

the database, not what was defined in the original DAC.

2. The export bulk copies out the data from all of the tables in the database and

incorporates the data into the export file.

The export process sets the DAC version to 1.0.0.0 and the DAC description in the export file to

an empty string. If the database was deployed from a DAC, the DAC definition in the export file

contains the name given to the original DAC. Otherwise, the DAC name is set to the database

name.

To export a DAC, you need to possess at least ALTER ANY sign-in and database-level

permissions and

permissions on

. This

task is achievable for individuals holding membership in the

fixed server role

and the

fixed database role within the source database of the DAC.

```cmd
.bacpac
.bacpac
.bacpac
.bacpac
VIEW
DEFINITION
```
