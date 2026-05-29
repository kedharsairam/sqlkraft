---
title: "Use PowerShell Core"
topic: "linux-operations"
description: |
  07/11/2025

  Applies to:

  SQL Server

  - Linux

  This article introduces

  SQL Server PowerShell

  and walks you through a couple of examples on

  how to use it with PowerShell on macOS and Linux. PowerShel
tags:
  - "linux-operations"
  - "use-powershell-core"
pubDate: 2025-12-01
---

07/11/2025

Applies to:

SQL Server

- Linux

This article introduces

SQL Server PowerShell

and walks you through a couple of examples on

how to use it with PowerShell on macOS and Linux. PowerShell is now an open source project

on

GitHub

.

For more information about Windows PowerShell, see

What is Windows PowerShell?

All of the following steps for PowerShell work in a regular terminal, or you can run them from a

terminal within Visual Studio Code. Visual Studio Code is available on macOS and Linux. For

more information on the MSSQL extension, see

What is the MSSQL extension for Visual Studio

Code?

For more information on installing PowerShell on various supported and experimental

platforms, see the following articles:

Install PowerShell on Windows

Install PowerShell on Linux

Install PowerShell on macOS

Install PowerShell on ARM processors

The

module is maintained in the

PowerShell Gallery

. When working with SQL

Server, you should always use the most recent version of the

PowerShell module.

To install the

module, open a PowerShell session and run the following code:

PowerShell

```cmd
SqlServer
SqlServer
SqlServer
Install-Module
-Name
SqlServer
```
