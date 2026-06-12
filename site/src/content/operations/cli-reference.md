---
title: "CLI reference"
topic: "sqlpackage"
description: |
  SqlPackage CLI reference

  SqlPackage is a command-line utility for database portability and deployments in Windows, Linux, and

  macOS environments. The SqlPackage command-line interface (CLI) parses e
tags:
  - "sqlpackage"
  - "cli-reference"
pubDate: 2025-12-01
---

SqlPackage CLI reference

SqlPackage is a command-line utility for database portability and deployments in Windows, Linux, and

macOS environments. The SqlPackage command-line interface (CLI) parses each invocation for

parameters, properties, and SQLCMD variables.

Bash

specify the action to perform, the source and target databases, and other general

settings.

modify the default behavior of an action.

SQLCMD variables

pass values to the SQLCMD variables in the source file.

To create a SqlPackage command, specify an action and its additional parameters. Optionally, add

properties and SQLCMD variables to further customize the command.

The following example uses SqlPackage to create a

file of the current database schema:

Bash

These are the parameters from this example:

These are the properties from this example:

Action

Description

Version

Returns the build number of the SqlPackage application.

Extract

Creates a data-tier application (

) file containing the schema or schema and user data from a

connected SQL database.

SqlPackage actions

ﾉ

Expand table

```cmd.dacpac
/Action:Extract
/TargetFile:"C:\sqlpackageoutput\output_current_version.dacpac"
/SourceServerName:"localhost"
/SourceDatabaseName:"Contoso"
/p:IgnoreUserLoginMappings=True
/p:Storage=Memory.dacpac
SqlPackage {parameters} {properties} {SQLCMD variables}
SqlPackage /Action:Extract /TargetFile:
"C:\sqlpackageoutput\output_current_version.dacpac"
\
/SourceServerName:
"localhost"
/SourceDatabaseName:
"Contoso"
\
/p:IgnoreUserLoginMappings=True /p:Storage=Memory
```
