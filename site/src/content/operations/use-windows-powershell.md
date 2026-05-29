---
title: "Use Windows PowerShell"
topic: "linux-operations"
description: |
  SQL Server on Linux
  
  07/03/2025
  
  Applies to:
  
  SQL Server
  
  - Linux
  
  This article introduces
  
  SQL Server PowerShell
  
  and walks you through a couple of examples on
  
  how to use it with SQL Server on Linux
tags:
  - "linux-operations"
  - "use-windows-powershell"
pubDate: 2025-12-01
---

SQL Server on Linux

07/03/2025

Applies to:

SQL Server

- Linux

This article introduces

SQL Server PowerShell

and walks you through a couple of examples on

how to use it with SQL Server on Linux. PowerShell support for SQL Server is currently available

on Windows, macOS, and Linux. This article walks you through using a Windows machine to

connect to a remote SQL Server instance on Linux.

The

SQL Server PowerShell module

on Windows is maintained in the PowerShell Gallery. When

working with SQL Server, you should always use the most recent version of the SqlServer

PowerShell module.

Read the

Known issues

for SQL Server on Linux.

Let's start by launching PowerShell on Windows. Use

+

, on your Windows computer, and

type

to launch a new Windows PowerShell session.

SQL Server provides a PowerShell module named

SqlServer

. You can use the

SqlServer

module

to import the SQL Server components (SQL Server provider and cmdlets) into a PowerShell

environment or script.

Copy and paste the following command at the PowerShell prompt to import the

SqlServer

module into your current PowerShell session:

PowerShell

sqlserver

```cmd
Win
R
Import-Module
SqlServer
```