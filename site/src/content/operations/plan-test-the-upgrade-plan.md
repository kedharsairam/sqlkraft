---
title: "Plan & test the upgrade plan"
topic: "upgrade"
description: "06/16/2025 - Windows only To perform a successful SQL Server upgrade, regardless of approach, appropriate planning is required."
tags: ["upgrade","plan-test-the-upgrade-plan"]
pubDate: "2025-12-01"
---

- Windows only

To perform a successful SQL Server upgrade, regardless of approach, appropriate planning is

required.

Before upgrading the Database Engine, review:

2022 release notes

2019 release notes

2017 release notes

2016 release notes

Discontinued Database Engine functionality in SQL Server

article.

Before upgrading the Database Engine, review the following checklist and the associated

articles. These articles apply to all upgrades, regardless of upgrade method and help you

determine the most appropriate upgrade method: Rolling upgrade, new installation upgrade,

or in-place upgrade. For example, you might not be able to perform an upgrade in-place or a

rolling upgrade, if you upgrade the operating system, upgrading from SQL Server 2005 (9.x), or

upgrading from a 32-bit version of SQL Server. For a decision tree, see

Choose a Database

Engine upgrade method.

Review the hardware and software requirements

to for installing SQL Server. These requirements can be found at:

Hardware and software

requirements for SQL Server 2016 and SQL Server 2017. A part of any upgrade planning

cycle is to consider upgrading hardware and the operating system. Newer hardware is

faster, and can reduce licensing either due to fewer processors or due to database and

server consolidation. These types of hardware and software changes affect the type of

upgrade method you choose.

Research your current environment to understand the SQL Server

components that are being used and the clients that connect to your environment.
