---
title: "Overview"
topic: "upgrade"
description: "06/04/2025 The articles in this section help you upgrade the SQL Server Database Engine from a prior release of SQL Server to SQL Server 2022 (16.x). 1. Choose a Database"
tags: ["upgrade","overview-2"]
pubDate: "2025-12-01"
---

The articles in this section help you upgrade the SQL Server Database Engine from a prior

release of SQL Server to SQL Server 2022 (16.x).

1.

Choose a Database Engine upgrade method. Before beginning an upgrade, you need to

understand the various upgrade methods. This article discusses the upgrade methods and

the steps involved with each upgrade method.

2.

Plan and test the Database Engine upgrade plan. After reviewing the upgrade methods,

you're ready to develop the appropriate upgrade method for your environment and then

test the upgrade method before upgrading the existing environment. This article

discusses developing an upgrade plan and testing it.

3.

Complete the Database Engine upgrade. After your database engine has been upgraded

and databases are online, there are additional steps you need to take, including taking a

new backup, upgrading the databases functionality to enable new features, and

repopulating full-text catalogs. This article discusses these steps.

4. Upgrade the

Database Compatibility Level.

, Azure SQL Database, and Azure SQL Managed Instance

One of the steps to take after your databases are online in the new version of SQL Server

or Azure SQL Database, might be to upgrade the databases functionality mode to enable

new features, by changing the database compatibility level. This can be done manually or

through the Query Tuning Assistant.

Change the database compatibility level and use the Query Store. After manually

changing the database compatibility level, use the Query Store to monitor

performance and identify possible regressions. This article discusses the

recommended process and provides a recommended workflow.

Upgrade databases using the Query Tuning Assistant. Alternatively to a manual

change, use the

to be guided through the

recommended process of changing the database compatibility level. This article

discusses this process and provides instructions on the QTA workflow.

For more information about new features and improved behaviors available after

changing a database compatibility level, see

Differences between Compatibility Levels.
