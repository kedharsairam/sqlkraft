---
title: "Configure time zone on SQL Server 2017"
topic: "linux-operations"
description: |
  07/03/2025

  Applies to:

  SQL Server

  - Linux

  This article describes how to configure the time zone for SQL Server 2017 (14.x) on Linux. You

  can also configure the time zone on Linux for

  SQL Server
tags:
  - "linux-operations"
  - "configure-time-zone-on-sql-server-2017"
pubDate: 2025-12-01
---

07/03/2025

SQL Server

- Linux

This article describes how to configure the time zone for SQL Server 2017 (14.x) on Linux. You

can also configure the time zone on Linux for

2019

, and

2022 and later

versions.

2017 (14.x) on Linux uses Windows time zones internally. All Transact-SQL (T-SQL)

commands use Windows time zones, for example the

CURRENT_TIMEZONE_ID

function and

AT

TIME ZONE

query operator.

1. SQL Server 2017 (14.x) on Linux first determines which time zone to use, using the first

valid result from the following sequence:

the

environment variable, if set;

the

symbolic link, if it exists;

the value

, if the file exists;

the

attribute from

, if they exist.

2. The resulting Linux time zone is then mapped to a corresponding Windows time zone via

a fixed

Time zone mapping

table.

The Windows time zone is derived from the Linux

timezone using the following mapping.

Symbolic links in

and

are considered. For instance, if

is set to

and the

entry is a symbolic

link to

, the Windows time zone is resolved to

via the

mapping entry.

ﾉ

Expand table

```cmd
TZ
/etc/localtime
/etc/timezone
ZONE=
/etc/sysconfig/clock
```
