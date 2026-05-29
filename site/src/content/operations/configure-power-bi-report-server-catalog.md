---
title: "Configure Power BI Report Server catalog"
topic: "linux-operations"
description: |
  07/03/2025
  
  Applies to:
  
  SQL Server 2019 (15.x) and later - Linux
  
  SQL Server Reporting Services
  
  (2019 and later)
  
  This article explains how to install and configure the Power BI Report Server (PBIRS
tags:
  - "linux-operations"
  - "configure-power-bi-report-server-catalog"
pubDate: 2025-12-01
---

07/03/2025

Applies to:

SQL Server 2019 (15.x) and later - Linux

SQL Server Reporting Services

(2019 and later)

This article explains how to install and configure the Power BI Report Server (PBIRS) catalog

database for SQL Server on Linux.

In this article, the examples use the domain

, and the following

configuration.

Windows domain

controller

Windows Server 2019 or Windows

Server 2022

Report development

and deployment

(

)

Windows Server 2019, running Visual

Studio 2019

- Report development and

deployment

- File share services to serve as a

repository for demand driven or

scheduled report output

SQL Server Reporting

Services (

)

Windows Server 2022, running a

supported version of Power BI Report

Server (PBIRS)

Developer machine

Windows 11 client, running SQL Server

Management Studio (SSMS)

SQL Server 2019

(

)

Red Hat Enterprise Linux (RHEL) 8.x

Server, running SQL Server 2019 (15.x)

with the latest CU

ﾉ

Expand table

1

```cmd
CORPNET.CONTOSO.COM
WIN19
WIN22
rhel8test
```