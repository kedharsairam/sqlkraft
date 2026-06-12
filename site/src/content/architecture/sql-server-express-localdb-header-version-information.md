---
title: "SQL Server Express LocalDB Header & Version Information"
topic: "clr-integration"
description: ""
tags: ["clr-integration","sql-server-express-localdb-header-version-information"]
pubDate: 2025-12-01
---

Express LocalDB header and

There's no separate header file for the SQL Server Express LocalDB instance API; the LocalDB

function signatures and error codes are defined in the Microsoft OLE DB Driver for SQL Server

header file (

). To use the LocalDB instance API, you must include the

header file in your project. This article no longer references the SQL Server Native Client header

file (

).

The LocalDB installation uses a single set of binaries per major SQL Server version. These

LocalDB versions are maintained and patched independently. This means that the user has to

specify which LocalDB baseline release (that is, major SQL Server version) they're using. The

version is specified in the standard version format defined by the.NET Framework

class:

The first two numbers in the version string (

and

) are mandatory. The last two

numbers in the version string (

and

) are optional and default to zero if the

user leaves them out. This means that if the user specifies only

as the LocalDB version

number, it's treated as if the user specified.

The version for the LocalDB installation is defined in the

registry

key under the SQL Server instance registry key, for example:

text

Multiple LocalDB versions on the same workstation are supported side-by-side. However, user

code always uses the latest available

DLL on the local computer to connect to

LocalDB instances.

```sql
msoledbsql.h msoledbsql.h sqlncli.h
System.Version
<major>.<minor>[.<build>[.<revision>]]
<major>
<minor>
<build>
<revision>
12.2
12.2.0.0
MSSQLServer\CurrentVersion
SQLUserInstance
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft SQL Server\MSSQL13E.LOCALDB\
MSSQLServer\CurrentVersion: "CurrentVersion"="12.0.2531.0"
```
