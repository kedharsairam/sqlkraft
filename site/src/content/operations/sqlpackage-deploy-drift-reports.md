---
title: "SqlPackage Deploy & Drift Reports"
topic: "sqlpackage"
description: |
  SqlPackage deploy report and drift report

  07/30/2025

  The SqlPackage

  DeployReport

  action creates an XML report of the changes that would be

  made by a publish action. The SqlPackage

  DriftReport

  a
tags:
  - "sqlpackage"
  - "sqlpackage-deploy-drift-reports"
pubDate: 2025-12-01
---

SqlPackage deploy report and drift report

07/30/2025

The SqlPackage

DeployReport

action creates an XML report of the changes that would be

made by a publish action. The SqlPackage

DriftReport

action creates an XML report of the

changes that have been made to the registered database since it was last registered.

SqlPackage

initiates the actions specified using the parameters, properties, and SQLCMD

variables specified on the command line.

Bash

Description

DeployReport

Specifies the action to

be performed.

{string}

Specifies the token

based authentication

access token to use

when connect to the

target database.

{True|False}

Specifies whether

diagnostic logging is

output to the console.

Defaults to False.

７

Note

was previously known as Azure Active Directory (Azure AD).

ﾉ

Expand table

```cmd
SqlPackage {parameters}{properties}{SQLCMD Variables}
```
