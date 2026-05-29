---
title: "Data Quality Services"
topic: "upgrade"
description: |
  06/04/2025
  
  Applies to:
  
  SQL Server
  
  - Windows only
  
  This article provides information on how to upgrade your existing installation of SQL Server Data
  
  Quality Services (DQS). As part of upgrading you
tags:
  - "upgrade"
  - "data-quality-services"
pubDate: 2025-12-01
---

06/04/2025

Applies to:

SQL Server

- Windows only

This article provides information on how to upgrade your existing installation of SQL Server Data

Quality Services (DQS). As part of upgrading your SQL Server Data Quality Server, you must also

upgrade the DQS databases schema.

You must back up your DQS databases before upgrading DQS to prevent any accidental data loss

during the schema upgrade. For information about backing up DQS databases, see

Backing Up

and Restoring DQS Databases

.

You can connect to SQL Server Data Quality Server by using the current or an earlier version of

Data Quality Client or the

DQS Cleansing Transformation

in Integration Services to perform your

data quality tasks.

After upgrading Data Quality Services (DQS) and Master Data Services (MDS), any earlier version

of the MDS add-in for Excel no longer works. You can download the SQL Server version of MDS

add-in for Excel from

Master Data Services Installation and Configuration

.

You must be logged on as a member of the Administrators group on the Data Quality Server

computer.

Your Windows user account must be a member of the

fixed server role in the SQL

Server instance where Data Quality Server is installed.

To upgrade DQS:

）

Important

Data Quality Services (DQS) is

in SQL Server 2025 (17.x) Preview. We continue to

support DQS in SQL Server 2022 (16.x) and earlier versions.