---
title: "Known issues"
topic: "linux-operations"
description: |
  SQL Server on Linux: Known issues
          
            The following sections describe known issues with SQL Server on Linux.
          
            The following table lists the most common issues with SQL Server on Linux.
          
            The length of the
tags: ["linux-operations","known-issues"]
pubDate: 2025-12-01
---

on Linux: Known issues

The following sections describe known issues with SQL Server on Linux.

The following table lists the most common issues with SQL Server on Linux.

The length of the hostname where SQL Server is installed needs to be

15 characters or less.

Change the name in

to a value 15

characters long or less.

Manually setting the system time backward in time causes SQL Server

to stop updating the internal system time within the Database Engine.

Restart SQL Server.

Only single instance installations are supported.

If you want to have more than

one instance on a given host,

consider using

virtual

machines

or

Linux containers.

Configuration Manager can't connect to SQL Server on

Linux.

None.

The default language of the

account is English.

Change the language of the

account with the

statement.

The OLE DB provider logs the following warning:

No action is required. The OLE

DB provider is signed using

SHA256. The SQL Server

Database Engine doesn't

validate the signed.dll

correctly.

The Reset password command using

throws the following

error:

The error message is a false

negative. The password reset

was successful, and you can

continue using the new

password.

2022

(16.x) container images only.

ﾉ

Expand table

```cmd
/etc/hostname sa sa
ALTER
LOGIN
Failed to verify the Authenticode signature of
'C:\binn\msoledbsql.dll'. Signature verification of SQL Server DLLs will be skipped. Genuine copies of SQL Server are signed. Failure to verify the Authenticode signature might indicate that this isn't an authentic release of SQL Server. Install a genuine copy of SQL
Server or contact customer support.
```
