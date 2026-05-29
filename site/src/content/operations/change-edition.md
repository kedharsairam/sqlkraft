---
title: "Change edition"
topic: "upgrade"
description: |
  08/22/2025

  Applies to:

  SQL Server

  - Windows only

  SQL Server Setup supports edition upgrade among various editions of SQL Server. For

  information about supported edition upgrade paths, see

  Suppor
tags:
  - "upgrade"
  - "change-edition"
pubDate: 2025-12-01
---

08/22/2025

Applies to:

SQL Server

- Windows only

SQL Server Setup supports edition upgrade among various editions of SQL Server. For

information about supported edition upgrade paths, see

Supported version and edition

upgrades (SQL Server 2022)

.

For a list of features supported by the editions of SQL Server on Windows, see:

Editions and supported features of SQL Server 2025 Preview

Editions and supported features of SQL Server 2022

Editions and supported features of SQL Server 2019

Editions and supported features of SQL Server 2017

Editions and supported features of SQL Server 2016

This article also provides steps on how you can do an edition downgrade. For example, if you

need to downgrade from Enterprise edition to Standard edition of SQL Server, follow the steps

outlined in this article.

Before you initiate the edition upgrade of an instance of SQL Server, review the following

articles:

Compute capacity limits by edition of SQL Server

Hardware and software requirements for SQL Server 2022

For SQL Server on a failover cluster instance (FCI), running edition upgrade on one of the FCI

nodes is sufficient. This node can be either active or passive, and the Database Engine doesn't

bring the resources offline during the edition upgrade. After the edition upgrade, you must

either restart the SQL Server instance, or fail over to a different node.

For local installations, you must run Setup as an administrator. If you install SQL Server from a

remote share, you must use a domain account that has read permissions on the remote share.
