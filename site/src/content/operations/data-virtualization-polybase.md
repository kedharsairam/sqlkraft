---
title: "Data virtualization (PolyBase)"
topic: "linux-operations"
description: "2025 (17.x) This article describes how you can use PolyBase services with SQL Server on Linux. Beginning with SQL Server 2025 (17.x), deployments on Linux can use ODBC data s"
tags: ["linux-operations","data-virtualization-polybase"]
pubDate: "2025-12-01"
---

2025 (17.x)

This article describes how you can use PolyBase services with SQL Server on Linux.

Beginning with SQL Server 2025 (17.x), deployments on Linux can use ODBC data sources for

PolyBase. This allows you to bring your own driver (BYOD). On Linux, this feature works similarly

to how it works on Windows. For more information, see

Configure PolyBase to access external

data with ODBC generic types.

The following example demonstrates the SQL ODBC driver on Ubuntu.

1. Add the Microsoft repository:

a. Import the Microsoft GPG key

Bash

b. Add the Microsoft repository to your system

Bash

2. Update the package list:

Ｕ

Caution

The bring-your-own-driver (BYOD) model involves risks that are the responsibility of the

customer and the driver provider. Microsoft isn't responsible for any issues the third-party

driver could cause.

```cmd
curl https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -
o /usr/share/keyrings/microsoft-prod.gpg curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -
rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
```
