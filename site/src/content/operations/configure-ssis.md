---
title: "Configure SSIS"
topic: "linux-operations"
description: "on Linux You run the configuration script when you install SQL Server Integration Services (SSIS) for Red Hat Enterprise Linux and Ubuntu. For more info about installing SS"
tags: ["linux-operations","configure-ssis"]
pubDate: "2025-12-01"
---

on Linux

You run the

configuration script when you install SQL Server Integration Services (SSIS)

for Red Hat Enterprise Linux and Ubuntu. For more info about installing SSIS, see

Install SQL

Server Integration Services (SSIS) on Linux.

You can also use the

utility to configure the following properties:

Description

Set the edition of SQL Server.

Enable or disable SQL Server Integration Services telemetry service.

Initialize and set up Microsoft SQL Server Integration Services.

The examples in this article run

by specifying the full path:. If

you navigate to that location before you run

, you can run the utility in the context of

the current directory:.

Be sure to run the commands that are described in this article with root (super user) privileges.

For example, run

and not.

To run these commands with prompts in the language that you prefer, you can specify a locale.

For example, to receive prompts in Chinese, run the following command:

ﾉ

Expand table

```cmd
ssis-conf ssis-conf set-edition telemetry setup
```
