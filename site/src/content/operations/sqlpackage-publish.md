---
title: "SqlPackage Publish"
topic: "sqlpackage"
description: |
  SqlPackage Publish parameters, properties, and

  SQLCMD variables

  07/30/2025

  The SqlPackage publish operation incrementally updates the schema of a target database to match the structure of a

  source
tags:
  - "sqlpackage"
  - "sqlpackage-publish"
pubDate: 2025-12-01
---

SqlPackage Publish parameters, properties, and

SQLCMD variables

07/30/2025

The SqlPackage publish operation incrementally updates the schema of a target database to match the structure of a

source database. Publishing a deployment package that contains user data for all or a subset of tables update the table

data in addition to the schema. Data deployment overwrites the schema and data in existing tables of the target

database. Data deployment will not change existing schema or data in the target database for tables not included in the

deployment package. A new database can be created by the publish action when the authenticated user has

create

database permissions

. The required permissions for the publish action on an existing database is

db_owner

.

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

When a database with SQL authentication user credentials is extracted, the password is replaced with a different

password of suitable complexity. It is assumed that after the dacpac is published that the user password is changed.

```cmd
SqlPackage /Action:Publish {parameters} {properties} {sqlcmd variables}
# example publish from Azure SQL Database using SQL authentication and a connection string
SqlPackage /Action:Publish /SourceFile:
"C:\AdventureWorksLT.dacpac"
\
/TargetConnectionString:
"Server=tcp:{yourserver}.database.windows.net,1433;Initial
Catalog=AdventureWorksLT;Persist Security Info=False;User ID=sqladmin;Password=
{your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection
Timeout=30;"
# example publish using short form parameter names, skips schema validation
SqlPackage /a:Publish /tsn:
"{yourserver}.database.windows.net,1433"
/tdn:
"AdventureWorksLT"
/tu:
"sqladmin"
\
/tp:
"{your_password}"
/sf:
"C:\AdventureWorksLT.dacpac"
/p:VerifyDeployment=False
# example publish using Microsoft Entra managed identity
SqlPackage /Action:Publish /SourceFile:
"C:\AdventureWorksLT.dacpac"
\
/TargetConnectionString:
"Server=tcp:{yourserver}.database.windows.net,1433;Initial
Catalog=AdventureWorksLT;Authentication=Active Directory Managed
Identity;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
```
