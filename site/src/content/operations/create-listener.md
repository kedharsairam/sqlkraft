---
title: "Create listener"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/29/2024
  
  Applies to:
  
  SQL Server
  
  This article describes how to create or configure a single
  
  availability group listener
  
  for an
  
  Always On availability group
  
  by using SQL Server Mana
tags:
  - "high-availability"
  - "create-listener"
pubDate: 2025-12-01
---

Article

•

09/29/2024

Applies to:

SQL Server

This article describes how to create or configure a single

availability group listener

for an

Always On availability group

by using SQL Server Management Studio, Transact-SQL, or

PowerShell in SQL Server.

View availability group Listener Properties

You can create only one listener per availability group through SQL Server. Typically, each

availability group requires only one listener. However, some customer scenarios require

multiple listeners for one availability group. After creating a listener through SQL Server,

you can use Windows PowerShell for failover clusters or the WSFC Failover Cluster

Manager to create additional listeners. For more information, see

create an additional

listener for an availability group

, later in this article.

）

Important

To create the first availability group listener of an availability group, we strongly

recommend that you use SQL Server Management Studio, Transact-SQL, or SQL Server

PowerShell. Avoid creating a listener directly in the WSFC cluster except when necessary,

for example, to create an additional listener.

７

Note

If a listener already exists and you want to create an additional listener, see

, later in this article.