---
title: "Install SQL Server tools"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  The following steps install the command-line tools, Microsoft ODBC drivers, and their

  dependencies. The

  package contains:

  : Command-line query utility.

  : Bulk im
tags:
  - "linux-operations"
  - "install-sql-server-tools"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

The following steps install the command-line tools, Microsoft ODBC drivers, and their

dependencies. The

package contains:

: Command-line query utility.

: Bulk import-export utility.

Install the tools for your platform:

Red Hat Enterprise Linux

SUSE Linux Enterprise Server

Ubuntu

macOS

Docker

This article describes how to install the command-line tools. If you're looking for examples of

how to use

or

, see the

at the end of this article.

These instructions are for installing the Microsoft ODBC 18 packages. For previous versions, see

Install the Microsoft ODBC driver for SQL Server (Linux)

.

Use the following steps to install the

on Red Hat Enterprise Linux.

1. Download the Microsoft Red Hat repository configuration file.

）

Important

and

are available in

for

and

architectures. For a

modern alternative across Linux, macOS, and Windows, see

.

Red Hat Enterprise Linux

```cmd
sqlcmd sqlcmd sqlcmd x64 arm64
```
