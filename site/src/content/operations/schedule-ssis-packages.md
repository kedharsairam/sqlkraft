---
title: "Schedule SSIS packages"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  When you run SQL Server Integration Services (SSIS) and SQL Server on Windows, you can

  automate the execution of SSIS packages by using SQL Server Agent. When you r
tags:
  - "linux-operations"
  - "schedule-ssis-packages"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

When you run SQL Server Integration Services (SSIS) and SQL Server on Windows, you can

automate the execution of SSIS packages by using SQL Server Agent. When you run SQL Server

and SSIS on Linux, however, the SQL Server Agent utility isn't available to schedule jobs on Linux.

Instead, you use the cron service, which is widely used on Linux platforms to automate package

execution.

This article provides examples that show how to automate the execution of SSIS packages. The

examples are written to run on Red Hat Enterprise. The code is similar for other Linux

distributions, such as Ubuntu.

Before you use the cron service to run jobs, check to see whether it's running on your computer.

To check the status of the cron service, use the following command:

If the service isn't active (that is, it's not running), consult your administrator to set up and

configure the cron service properly.

A cron job is a task that you can configure to run regularly at a specified interval. The job can be

as simple as a command that you would normally type directly in the console or run as a shell

script.

For easy management and maintenance purposes, we recommend that you put your package-

execution commands in a script that contains a descriptive name.

```cmd
systemctl status crond.service
```
