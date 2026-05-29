---
title: "View & Modify properties"
topic: "migration"
description: |
  Article
  
  •
  
  12/17/2024
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  This topic describes how to view and modify Distributor and Publisher properties in SQL Server
  
  by using SQL Server Managem
tags:
  - "migration"
  - "view-modify-properties"
pubDate: 2025-12-01
---

Article

•

12/17/2024

Applies to:

SQL Server

Azure SQL Managed Instance

This topic describes how to view and modify Distributor and Publisher properties in SQL Server

by using SQL Server Management Studio, Transact-SQL, or Replication Management Objects

(RMO).

Recommendations

Security

SQL Server Management Studio

Transact-SQL

Replication Management Objects (RMO)

For Publishers running versions prior to Microsoft SQL Server 2005 (9.x), a user in the

fixed server role can register Subscribers on the

page. Beginning

with SQL Server 2005 (9.x), it is no longer necessary to explicitly register Subscribers for

replication.

When possible, prompt users to enter security credentials at runtime.