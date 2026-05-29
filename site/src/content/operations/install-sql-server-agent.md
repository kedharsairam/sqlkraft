---
title: "Install SQL Server Agent"
topic: "linux-operations"
description: |
  Applies to:
  
  SQL Server
  
  on Linux
  
  This article describes how to enable or install the SQL Server Agent on Linux.
  
  The
  
  SQL Server Agent
  
  runs scheduled SQL Server jobs. Starting with SQL Server 2017 
tags:
  - "linux-operations"
  - "install-sql-server-agent"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

This article describes how to enable or install the SQL Server Agent on Linux.

The

SQL Server Agent

runs scheduled SQL Server jobs. Starting with SQL Server 2017 (14.x) CU

4, SQL Server Agent is included with the

package and is disabled by default.

For a list of features supported by the editions of SQL Server on Linux, see:

Editions and supported features of SQL Server 2025

Editions and supported features of SQL Server 2022

Editions and supported features of SQL Server 2019

Editions and supported features of SQL Server 2017

Before using the SQL Server Agent on Linux, use the following steps to enable or install it.

1. Add your hostname (with and without domain) in the

files. The following lines

show an example of the format for these entries:

Bash

2. Follow the instructions in one of the following sections based on your version of SQL

Server:

SQL Server 2017 (14.x) CU 4 and later versions

Enable the SQL Server Agent

SQL Server 2017 (14.x) CU 3 and earlier versions

Install the SQL Server Agent

For SQL Server 2017 (14.x) CU 4 and later versions, you only need to enable the SQL Server

Agent. You don't need to install a separate package.

ﾉ

Expand table

```cmd
/etc/hosts
"IP Address"
"hostname"
"IP Address"
"hostname.domain.com"
```