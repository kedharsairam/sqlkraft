---
title: "Reporting Services"
topic: "high-availability"
description: |
  Article

  •

  01/29/2024

  Applies to:

  SQL Server

  This article contains information about configuring Reporting Services to work with Always On

  availability groups (AG) in SQL Server. The three scenar
tags:
  - "high-availability"
  - "reporting-services"
pubDate: 2025-12-01
---

Article

•

01/29/2024

Applies to:

SQL Server

This article contains information about configuring Reporting Services to work with Always On

availability groups (AG) in SQL Server. The three scenarios for using Reporting Services and

Always On availability groups are databases for report data sources, report server databases,

and report design. The supported functionality and required configuration is different for the

three scenarios.

A key benefit of using Always On availability groups with Reporting Services data sources is to

use readable secondary replicas as a reporting data source while, at the same time, the

secondary replicas are providing a failover for a primary database.

For general information on Always On availability groups, see

Always On FAQ for SQL Server

2012 (../../../sql-server/index.yml)

.

SQL Server Reporting Services and Power BI Report Server uses the .NET framework 4.0 and

supports Always On availability groups connection string properties for use with data sources.

To use Always On availability groups with Reporting Services 2014, and earlier, you need to

download and install a hotfix for .NET 3.5 SP1. The hotfix adds support to SQL Client for AG

features and support of the connection string properties

and

. If the Hotfix isn't installed on each computer that hosts a report server,

then users attempting to preview reports see an error message similar to the following, and the

error message will be written to the report server trace log:

"Keyword not supported 'applicationintent'"

The message occurs when you include one of the Always On availability groups properties in

the Reporting Services connection string, but the server doesn't recognize the property. The

noted error message is seen when you select the 'Test Connection' button in Reporting Services

user interfaces and when you preview the report if remote errors are enabled on the report

servers.
