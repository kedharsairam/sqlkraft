---
title: "Overview"
topic: "migration"
description: |
  SQL Server Replication

  Article

  •

  09/29/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Replication is a set of technologies for copying and distributing data and database objects

  from o
tags:
  - "migration"
  - "overview-3"
pubDate: 2025-12-01
---

Replication

Article

•

09/29/2024

SQL Server

Azure SQL Managed Instance

Replication is a set of technologies for copying and distributing data and database objects

from one database to another and then synchronizing between databases to maintain

consistency. Use replication to distribute data to different locations and to remote or mobile

users over local and wide area networks, dial-up connections, wireless connections, and the

Internet.

Transactional replication is typically used in server-to-server scenarios that require high

throughput, including: improving scalability and availability; data warehousing and reporting;

integrating data from multiple sites; integrating heterogeneous data; and offloading batch

processing. Merge replication is primarily designed for mobile applications or distributed

server applications that have possible data conflicts. Common scenarios include: exchanging

data with mobile users; consumer point of sale (POS) applications; and integration of data from

multiple sites. Snapshot replication is used to provide the initial data set for transactional and

merge replication; it can also be used when complete refreshes of data are appropriate. With

these three types of replication, SQL Server provides a powerful and flexible system for

synchronizing data across your enterprise. Replication to SQLCE 3.5 and SQLCE 4.0 is supported

on both Windows Server 2012 and Windows 8.

2022 hasn't introduced significant new features to SQL Server replication.

2019 hasn't introduced significant new features to SQL Server replication.

2017 hasn't introduced significant new features to SQL Server replication.

2016 hasn't introduced significant new features to SQL Server replication.

For backward compatibility information see,

Replication Backward Compatibility

View and Modify Replication Security Settings

Manage Logins in the Publication Access List

Configure Publishing and Distribution

View and Modify Publication Properties
