---
title: "SqlPackage Import"
topic: "sqlpackage"
description: |
  SqlPackage Import parameters and properties
  
  Article
  
  •
  
  11/21/2024
  
  The SqlPackage Import action imports the schema and table data from a BACPAC file (.bacpac) into a new or empty
  
  database in SQL Se
tags:
  - "sqlpackage"
  - "sqlpackage-import"
pubDate: 2025-12-01
---

SqlPackage Import parameters and properties

Article

•

11/21/2024

The SqlPackage Import action imports the schema and table data from a BACPAC file (.bacpac) into a new or empty

database in SQL Server or Azure SQL Database. At the time of the import operation to an existing database the target

database cannot contain any user-defined schema objects. Alternatively, a new database can be created by the import

action when the authenticated user has

create database permissions

. The Import action is part of the

database

portability

functionality of SqlPackage.

SqlPackage

initiates the actions specified using the parameters, properties, and SQLCMD variables specified on the

command line.

Bash

The Import action requires a

parameter to specify the name and location of the .bacpac file containing the

database objects and data.

The Export action requires a target connection where a new database will be created by SqlPackage or where a blank

database is present. This is specified either through a combination of:

and

parameters, or

parameter.

Bash

７

Note

While Microsoft Entra ID is the

new name for Azure Active Directory (Azure AD)

, to prevent disrupting existing

environments, Azure AD still remains in some hardcoded elements such as UI fields, connection providers, error

codes, and cmdlets. In this article, the two names are interchangeable.

７

Note

SqlPackage import performs best for databases under 200GB. For larger databases, you may want to optimize the

operation using properties available in this article and tips in

Troubleshooting with SqlPackage

or alternatively

achieve database portability through

data in parquet files

.

```cmd
SourceFile
TargetServerName
TargetDatabaseName
TargetConnectionString
SqlPackage /Action:Import {parameters} {properties}
```