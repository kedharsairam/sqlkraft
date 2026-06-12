---
title: "SqlPackage Script"
topic: "sqlpackage"
description: |
  SqlPackage Script parameters and properties
  
    07/30/2025
  
    The SqlPackage Script action creates a Transact-SQL incremental update script that updates the schema of a target
  
    database to match the schema
tags: ["sqlpackage","sqlpackage-script"]
pubDate: "2025-12-01"
---

SqlPackage Script parameters and properties

The SqlPackage Script action creates a Transact-SQL incremental update script that updates the schema of a target

database to match the schema of a source database.

SqlPackage

initiates the actions specified using the parameters, properties, and SQLCMD variables specified on the

command line.

Bash

Parameter

Short

Form

Value

Description

/AccessToken:

/at

{string}

Specifies the token based

authentication access token to use

when connect to the target database.

/Action:

/a:

Script

Specifies the action to be performed.

/AzureCloudConfig:

/acc:

{string}

Specifies the custom endpoints for

connecting to Microsoft Entra ID in the

format:

AzureActiveDirectoryAuthority=

{value};DatabaseServicePrincipalName=

{value}".

/DeployReportPath:

/drp:

{string}

Specifies an optional file path to

output the deployment report xml file.

/DeployScriptPath:

/dsp:

{string}

Specifies an optional file path to

output the deployment script. For

Azure deployments, if there are

Transact-SQL commands to create or

modify the master database, a script

will be written to the same path but

with "Filename_Master.sql" as the

output file name.

/Diagnostics:

/d:

{True|False}

Specifies whether diagnostic logging is

output to the console. Defaults to

７

Note

While Microsoft Entra ID is the

new name for Azure Active Directory (Azure AD)

, to prevent disrupting existing

environments, Azure AD still remains in some hardcoded elements such as UI fields, connection providers, error

codes, and cmdlets. In this article, the two names are interchangeable.

ﾉ

Expand table

```cmd
SqlPackage {parameters}{properties}{SQLCMD Variables}
```
