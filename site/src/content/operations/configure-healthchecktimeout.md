---
title: "Configure HealthCheckTimeout"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  The HealthCheckTimeout setting is used to specify the length of time, in milliseconds, that the

  SQL Server resource DLL should wait for information re
tags:
  - "high-availability"
  - "configure-healthchecktimeout"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

The HealthCheckTimeout setting is used to specify the length of time, in milliseconds, that the

SQL Server resource DLL should wait for information returned by the

sp_server_diagnostics

stored procedure before reporting the Always On Failover Cluster Instance (FCI) as

unresponsive. Changes that are made to the timeout settings are effective immediately and do

not require a restart of the SQL Server resource.

Limitations and Restrictions

,

Security

PowerShell

,

Failover Cluster

Manager

,

Transact-SQL

The default value for this property is 30,000 milliseconds (30 seconds). The minimum value is

15,000 milliseconds (15 seconds).

Requires ALTER SETTINGS and VIEW SERVER STATE permissions.

1. Start an elevated Windows PowerShell via

.

2. Import the

module to enable cluster cmdlets.

3. Use the

cmdlet to find the SQL Server resource, then use

cmdlet to set the

property for the failover cluster

To configure HealthCheckTimeout settings
