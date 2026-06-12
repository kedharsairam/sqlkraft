---
title: "Run and connect (containers)"
topic: "linux-operations"
description: "Quickstart: Run SQL Server Linux container on Linux In this quickstart, you use Docker to pull and run the SQL Server 2025 (17.x) Linux container image, mssql-server-linux"
tags: ["linux-operations","run-and-connect-containers"]
pubDate: 2025-12-01
---

Quickstart: Run SQL Server Linux container

on Linux

In this quickstart, you use Docker to pull and run the SQL Server 2025 (17.x) Linux container

image,

mssql-server-linux. Then you can connect with

to create your first database and

run queries.

For more information on supported platforms, see

Release notes for SQL Server 2025 on Linux.

This quickstart creates SQL Server 2025 (17.x) containers. If you prefer to create Linux containers

for different versions of SQL Server, see:

2022

2019

2017

This image consists of SQL Server running on Linux, based on Ubuntu. You can use it with the

Docker Engine 1.8+ on Linux.

Starting with SQL Server 2022 (16.x) CU 14 and SQL Server 2019 (15.x) CU 28, the container

images include the

new mssql-tools18

package. The previous directory

is

being phased out. The new directory for Microsoft ODBC 18 tools is

,

７

Note

container images are supported only on Linux hosts running on. Emulation or translation environments (for example, Rosetta 2, Prism, or

QEMU) aren't tested or supported. If you want to create a feature request, or report an

emulator-related issue, visit the.

２

Warning

When you stop and remove a container, you permanently delete your SQL Server data in the

container. For more information on preserving your data,

or use a.

```cmd
sqlcmd
/opt/mssql-tools/bin
/opt/mssql-tools18/bin
```
