---
title: "Configure to send usage and diagnostic data to Microsoft"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  By default, Microsoft collects information about how its customers use SQL Server. Specifically,

  SQL Server collects information about the installation experience,
tags:
  - "linux-operations"
  - "configure-to-send-usage-and-diagnostic-data-to-microsoft"
pubDate: 2025-12-01
---

SQL Server

on Linux

By default, Microsoft collects information about how its customers use SQL Server. Specifically,

collects information about the installation experience, usage, and performance. This

information helps Microsoft improve the product to better meet customer needs. For example,

Microsoft collects information about what kinds of error codes customers encounter so that we

can fix related bugs, improve our documentation about how to use SQL Server, and determine

whether features should be added to the product to better serve customers.

This document provides details about what kind of information is collected, and about how to

configure SQL Server on Linux to send that collected information to Microsoft. SQL Server

includes a privacy statement that explains what information we do and don't collect from users.

For more information, see the

privacy statement.

Specifically, Microsoft doesn't send any of the following types of information through this

mechanism:

Any values from inside user tables

Any sign-in credentials or other authentication information

Personal data

always collects and sends information about the installation experience from the

setup process so that we can quickly find and fix any installation problems that the customer is

experiencing. SQL Server can be configured not to send information (on a per-server instance

basis) to Microsoft through.

is a configuration script that installs with SQL

Server for Red Hat Enterprise Linux, SUSE Linux Enterprise Server, and Ubuntu.

７

Note

You can disable the sending of information to Microsoft only in paid versions of SQL Server.
