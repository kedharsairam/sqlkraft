---
title: "Install and connect (Ubuntu)"
topic: "linux-operations"
description: |
  Quickstart: Install SQL Server and create a

  Applies to:

  SQL Server

  on Linux

  In this quickstart, you install SQL Server 2025 (17.x) on Ubuntu 22.04. Then you can connect with

  to create your first
tags:
  - "linux-operations"
  - "install-and-connect-ubuntu"
pubDate: 2025-12-01
---

Quickstart: Install SQL Server and create a

SQL Server

on Linux

In this quickstart, you install SQL Server 2025 (17.x) on Ubuntu 22.04. Then you can connect with

to create your first database and run queries.

For more information on supported platforms, see

Release notes for SQL Server 2025 on Linux.

You need an Ubuntu 22.04 or 24.04 machine with

of memory.

To install Ubuntu 22.04 on your own machine, go to

https://releases.ubuntu.com/22.04/. You

can also create Ubuntu or Ubuntu Pro virtual machines in Azure. See

Tutorial: Create and Manage

Linux VMs with the Azure CLI.

７

Note

Starting with SQL Server 2025 (17.x) Cumulative Update (CU) 1, Ubuntu 24.04 is supported.



Tip

This tutorial requires user input and an internet connection. If you're interested in the

or

installation procedures, see.

Ｕ

Caution

Your password should follow the SQL Server default. By default, the

password must be at least eight characters long and contain characters from three of the

following four sets: uppercase letters, lowercase letters, base-10 digits, and symbols.

Passwords can be up to 128 characters long. Use passwords that are as long and complex as

possible.

```cmd
sqlcmd
```
