---
title: "SqlPackage Extract"
topic: "sqlpackage"
description: |
  SqlPackage Extract parameters and properties
          
            Article
          
            •
          
            04/15/2025
          
            The SqlPackage Extract action creates a schema of a connected database in a DACPAC file (.dacpac). By default, data isn't
          
            include
tags: ["sqlpackage","sqlpackage-extract"]
pubDate: 2025-12-01
---

SqlPackage Extract parameters and properties

The SqlPackage Extract action creates a schema of a connected database in a DACPAC file (.dacpac). By default, data isn't

included in the.dacpac file. To include data, utilize the

Export action

or use the Extract properties

ExtractAllTableData

/

TableData.

SqlPackage

initiates the actions specified using the parameters, properties, and SQLCMD variables specified on the

command line.

Bash

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

When a database with password credentials (for example, a SQL authentication user) is extracted, the password is

replaced with a different password of suitable complexity. SqlPackage or DacFx users should change the password

after the dacpac is published.

```cmd
SqlPackage /Action:Extract {parameters} {properties}
# example extract to create a schema-only.dacpac file connecting using SQL authentication
SqlPackage /Action:Extract /TargetFile:{filename}.dacpac /DiagnosticsFile:{logFile}.
log
/p:ExtractAllTableData=
false
/p:VerifyExtraction=
true
\
/SourceServerName:{serverFQDN} /SourceDatabaseName:{databaseName} /SourceUser:{username}
/SourcePassword:{password}
# example extract to create a.sql file containing the schema definition of the database
SqlPackage /Action:Extract /TargetFile:{filename}.dacpac /DiagnosticsFile:{logFile}.
log
/SourceServerName:
{serverFQDN} \
/SourceDatabaseName:{databaseName} /SourceUser:{username} /SourcePassword:{password}
/p:ExtractTarget=File
# example extract to create a.dacpac file with data connecting using SQL authentication
SqlPackage /Action:Extract /TargetFile:{filename}.dacpac /DiagnosticsFile:{logFile}.
log
/p:ExtractAllTableData=
true
/p:VerifyExtraction=
true
\
/SourceServerName:{serverFQDN} /SourceDatabaseName:{databaseName} /SourceUser:{username}
/SourcePassword:{password}
# example extract to create a schema-only.dacpac file connecting using Microsoft Entra managed identity
SqlPackage /Action:Extract /TargetFile:
"C:\AdventureWorksLT.dacpac"
\
/SourceConnectionString:
"Server=tcp:{yourserver}.database.windows.net,1433;Initial
Catalog=AdventureWorksLT;Authentication=Active Directory Managed
```
