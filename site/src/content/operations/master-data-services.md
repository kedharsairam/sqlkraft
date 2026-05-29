---
title: "Master Data Services"
topic: "upgrade"
description: |
  06/04/2025

  Applies to:

  SQL Server

  - Windows only

  The following are the scenarios for upgrading Microsoft SQL Server Master Data Services.

  Upgrade without Database Engine Upgrade

  Upgrade with Dat
tags:
  - "upgrade"
  - "master-data-services"
pubDate: 2025-12-01
---

06/04/2025

Applies to:

SQL Server

- Windows only

The following are the scenarios for upgrading Microsoft SQL Server Master Data Services.

Upgrade without Database Engine Upgrade

Upgrade with Database Engine Upgrade

Upgrade in Two-Computer Scenario

Upgrade with Restoring a Database from Backup

Back up your database before performing any upgrade.

The upgrade process recreates stored procedures and upgrades tables used by Master Data

Services. Any customizations you make to either of these components might be lost.

Model deployment packages can be used only in the edition of SQL Server they were created

in. You can't deploy model deployment packages created in SQL Server 2008 R2 (10.50.x), SQL

Server 2012 (11.x), or SQL Server 2014 (12.x) to SQL Server 2016 (13.x).

After you upgrade Data Quality Services (DQS) and Master Data Services (MDS) to the latest

version of SQL Server, any earlier version of the MDS add-in for Excel no longer works. You can

download the SQL Server 2016 (13.x) MDS add-in for Excel from

Master Data Services Add-in

for Microsoft Excel

.

By default, the files are installed at

, where

represents the SQL Server version. For example, SQL Server 2017

(14.x) is

, and SQL Server 2019 (15.x) is

.

）

Important

Master Data Services (MDS) is

in SQL Server 2025 (17.x) Preview. We continue to

support MDS in SQL Server 2022 (16.x) and earlier versions.

```cmd
<drive>:\Program Files\Microsoft SQL Server\<nnn>\Master
Data Services
<nnn>
140
150
```
