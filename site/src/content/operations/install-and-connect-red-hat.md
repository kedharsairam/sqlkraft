---
title: "Install and connect (Red Hat)"
topic: "linux-operations"
description: "Quickstart: Install SQL Server and create a on Linux In this quickstart, you install SQL Server 2025 (17.x) on Red Hat Enterprise Linux (RHEL) 9.x or 10.x. Then you connect"
tags: ["linux-operations","install-and-connect-red-hat"]
pubDate: "2025-12-01"
---

Quickstart: Install SQL Server and create a

on Linux

In this quickstart, you install SQL Server 2025 (17.x) on Red Hat Enterprise Linux (RHEL) 9.x or 10.x.

Then you connect by using

to create your first database and run queries.

If you want to automate your installation using Ansible, see

Quickstart: Deploy SQL Server on

Linux using an Ansible playbook.

For more information on supported platforms, see

Release notes for SQL Server 2025 on Linux.

You need a machine running RHEL 8.x with

of memory.

To install Red Hat Enterprise Linux on your own machine, go to

https://access.redhat.com/products/red-hat-enterprise-linux/evaluation. You can also create

RHEL virtual machines in Azure. See

Create and Manage Linux VMs with the Azure CLI

, and use

in the call to.

If you previously installed a preview version of SQL Server, you must first remove the old

repository before following these steps. For more information, see

Configure repositories for

installing and upgrading SQL Server 2025 on Linux.

７

Note

Red Hat 9 includes support for SQL Server 2025 (17.x) and TLS 1.3, which is enabled by

default. Starting with SQL Server 2025 (17.x) CU 1, Red Hat 10 is supported.



Tip

This tutorial requires user input and an internet connection. If you're interested in the

or

installation procedures, see. If you choose to have a preinstalled SQL Server VM on RHEL ready to run your

production-based workload, follow the

for creating the SQL Server VM.

```cmd
sqlcmd
-
-image RHEL az vm create
```
