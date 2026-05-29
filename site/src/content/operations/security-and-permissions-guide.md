---
title: "Security and permissions guide"
topic: "linux-operations"
description: |
  SQL Server on Linux - Security and
  
  10/15/2025
  
  This article describes the required service accounts, and file system permissions for SQL Server
  
  on Linux. For more information about SQL Server on Win
tags:
  - "linux-operations"
  - "security-and-permissions-guide"
pubDate: 2025-12-01
---

SQL Server on Linux - Security and

10/15/2025

This article describes the required service accounts, and file system permissions for SQL Server

on Linux. For more information about SQL Server on Windows permissions, see

Configure

Windows service accounts and permissions

.

Even though SQL Server on Linux runs under the

operating system account, the

following Windows principals exist at the SQL Server layer for compatibility. Don't remove or

deny them unless you fully understand the risks.

SQL Server

Maps to the root‑level administrators of the host. Certain

system objects run in the context of this account.

Service identifier (SID) reserved for the Windows

account. Still created so that cross‑platform scripts that

expect it succeed.

(no

fixed role)

Historically the default startup account for several SQL

Server services on Windows. Present only for backward

compatibility. Not used by the SQL Server on Linux

Database Engine itself.

All files under the folder

must be owned by the

user, and

group

(

), with read and write access for both. If you change the default umask (

), or

use alternative mount points, you must reapply these permissions manually.

The default permissions for the

folder are as follows:

Output

ﾉ

Expand table

```cmd
mssql
BUILTIN\Administrators
NT AUTHORITY\SYSTEM
SYSTEM
NT AUTHORITY\NETWORK
SERVICE
```