---
title: "Introduction to adutil"
topic: "linux-operations"
description: |
  Applies to:
  
  SQL Server
  
  on Linux
  
  The
  
  tool is a command-line interface (CLI) utility for configuring and managing Windows
  
  Active Directory domains for SQL Server on Linux and containers. It elimina
tags:
  - "linux-operations"
  - "introduction-to-adutil"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

The

tool is a command-line interface (CLI) utility for configuring and managing Windows

Active Directory domains for SQL Server on Linux and containers. It eliminates the need to switch

between Windows and Linux machines to manage Active Directory.

Before you get started, make sure you download

to a host that is already joined to an

Active Directory domain.

The

tool is designed as a series of commands and subcommands, with extra flags that

you specify as further input. Each top-level command represents a category of administrative

functions. Within that category, each subcommand is an operation. This article shows you how to

download and get started with

.

You should use Lightweight Directory Access Protocol over SSL (LDAPS) instead of Lightweight

Directory Access Protocol (LDAP). For more information about LDAP, see

Lightweight Directory

Access Protocol (LDAP)

.

You can set the

option to

in the

configuration file. When you run

under the

user, the configuration file is located at

. This JSON code sample shows how to configure the

setting:

７

Note

Support for

is limited to SQL Server use cases only. You can also use other utilities

like

to enable Active Directory authentication, as explained in

.

```cmd
useLdaps
true
adutil.json
mssql
/var/opt/mssql/.adutil/adutil.json
```