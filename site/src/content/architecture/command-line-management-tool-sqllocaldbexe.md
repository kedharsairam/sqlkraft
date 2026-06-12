---
title: "Command-Line Management Tool: SqlLocalDB.exe"
topic: "clr-integration"
description: |
  SqlLocalDB.exe

  07/14/2025

  Applies to:

  SQL Server

  SqlLocalDB.exe is a simple tool that enables the user to easily manage LocalDB instances from

  the command line. It's implemented as a simple wrapp
tags:
  - "clr-integration"
  - "command-line-management-tool-sqllocaldbexe"
pubDate: 2025-12-01
---

SqlLocalDB.exe

07/14/2025

SQL Server

SqlLocalDB.exe is a simple tool that enables the user to easily manage LocalDB instances from

the command line. It's implemented as a simple wrapper around the LocalDB instance API. As

in many similar SQL Server tools (for example, SQLCMD), parameters are passed to SqlLocalDB

as command-line arguments and output is sent to the console.

SqlLocalDB enables developers to use LocalDB without having to write code to call the API or

depend on other tools to do it for them.

SqlLocalDB supports the following options.

Prints help text.

Creates a new LocalDB instance with a specified name and version.

If the [version-number] parameter is omitted, it defaults to the

SqlLocalDB build version.

starts the new LocalDB instance after it's created.

Deletes the LocalDB instance with the specified name.

Starts the LocalDB instance with the specified name.

Stops the LocalDB instance with the specified name, after current

queries finish running.

requests the LocalDB instance shutdown with the

option.

kills the LocalDB instance process without contacting it.

Shares the specified private instance using the specified shared

name. If the user SID or account name is omitted, it defaults to the

current user.

SqlLocalDB Options

ﾉ

Expand table

```sql
-s
-i
NOWAIT
-k
```
