---
title: "Distributed transactions"
topic: "high-availability"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  This article describes cross-database and distributed transactions support for Always On
  
  availability groups and database mirroring.
  
  SQL Server 2017 
tags:
  - "high-availability"
  - "distributed-transactions"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

This article describes cross-database and distributed transactions support for Always On

availability groups and database mirroring.

SQL Server 2017 supports distributed transactions for databases in availability groups. This

support includes databases on the same instance of SQL Server or databases on different

instances of SQL Server. Distributed transactions are not supported for databases configured

for database mirroring.

To configure an availability group for distributed transactions, see

Configure Availability Group

for Distributed Transactions

.

See more information at:

DTC Administration Guide

DTC Developers Guide

DTC Programmers Reference

７

Note

SQL Server 2016 (13.x) Service Pack 2 and later provides full support for distributed

transactions in availability groups.

In SQL Server 2016 (13.x) versions prior to Service Pack 2, cross-database distributed

transactions (i.e. transaction using databases on the same SQL Server instance) involving a

database in an availability group are not supported.

SQL Server 2016 SP1 and before: Support for cross-