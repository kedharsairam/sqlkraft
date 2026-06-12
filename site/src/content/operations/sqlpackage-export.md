---
title: "SqlPackage Export"
topic: "sqlpackage"
description: |
  SqlPackage Export parameters and properties

  07/28/2025

  The SqlPackage Export action exports a connected database to a BACPAC file (.bacpac). By default, data for all tables will

  be included in the
tags:
  - "sqlpackage"
  - "sqlpackage-export"
pubDate: 2025-12-01
---

SqlPackage Export parameters and properties

07/28/2025

The SqlPackage Export action exports a connected database to a BACPAC file (.bacpac). By default, data for all tables will

be included in the.bacpac file. Optionally, you can specify only a subset of tables for which to export data. The Export

action is part of the

database portability

functionality of SqlPackage. For an export to be transactionally consistent, you

must ensure either that no write activity is occurring during the export, or that you're exporting from a

transactionally

consistent copy

of your database.

SqlPackage

initiates the actions specified using the parameters, properties, and SQLCMD variables specified on the

command line.

Bash

The Export action requires a

parameter to specify the name and location of the.bacpac file to be created.

This location must be writable by the user running the command and the containing folder must exist.

The Export action also requires a database source to be specified, either through a combination of:

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

SqlPackage export performs best for databases under 200GB. For larger databases, you may want to optimize the

operation using properties available in this article and tips in

Troubleshooting with SqlPackage

or alternatively

achieve database portability through

data in parquet files.

```cmd
TargetFile
SourceServerName
SourceDatabaseName
SourceConnectionString
SqlPackage /Action:Export {parameters} {properties}
```
