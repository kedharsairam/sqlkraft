---
title: "Log Shipping Monitor Settings"
topic: "high-availability"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Use this page to configure and to modify the properties of the log shipping monitor server.

  For an explanation of log shipping concepts, see

  About Lo
tags:
  - "high-availability"
  - "log-shipping-monitor-settings"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Use this page to configure and to modify the properties of the log shipping monitor server.

For an explanation of log shipping concepts, see

About Log Shipping (SQL Server).

Displays the name of the server instance that is currently configured as the monitor server for

the log shipping configuration.

Choose and connect to an instance of SQL Server to be used as the monitor server. The

account used to connect must be a member of the sysadmin fixed server role on the secondary

server instance.

Have log shipping impersonate the SQL Server Agent proxy account when connecting to the

monitor server instance. The backup, copy, and restore processes must be able to connect to

the monitor server to update the status of log shipping operations.

Allow log shipping to use a specific SQL Server login when connecting to the monitor server

instance. The backup, copy, and restore processes must be able to connect to the monitor

server to update the status of log shipping operations. Choose this option if you want log

shipping to use a specific SQL Server login and then specify the login and password.

Specify the amount of time to retain log shipping history information on the monitor server

before it is deleted.

Indicates the name of the SQL Server Agent alert job used by log shipping to raise alerts when

backup or restore thresholds have been exceeded. When first creating this job, you can change

the name by typing in the box.

Indicates the current schedule of the SQL Server Agent alert job.
