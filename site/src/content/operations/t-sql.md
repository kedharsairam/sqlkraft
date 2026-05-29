---
title: "T-SQL"
topic: "high-availability"
description: |
  Article
  
  •
  
  02/05/2024
  
  Applies to:
  
  SQL Server
  
  This topic describes how to use Transact-SQL to create and configure an availability group on
  
  instances of SQL Server on which the Always On availabil
tags:
  - "high-availability"
  - "t-sql"
pubDate: 2025-12-01
---

Article

•

02/05/2024

Applies to:

SQL Server

This topic describes how to use Transact-SQL to create and configure an availability group on

instances of SQL Server on which the Always On availability groups feature is enabled. An

availability group

defines a set of user databases that will fail over as a single unit and a set of

failover partners, known as

availability replicas

, that support failover.

Before creating an availability group, verify that the instances of SQL Server that host

availability replicas reside on different Windows Server Failover Clustering (WSFC) node

within the same WSFC failover cluster. Also, verify that each of the server instance meets

all other Always On availability groups prerequisites. For more information, we strongly

recommend that you read

Prerequisites, Restrictions, and Recommendations for Always

On Availability Groups (SQL Server)

.

Requires membership in the

fixed server role and either CREATE AVAILABILITY

GROUP server permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL SERVER

permission.

７

Note

For an introduction to availability groups, see

.

７

Note

As an alternative to using Transact-SQL, you can use the Create Availability Group wizard

or SQL Server PowerShell cmdlets. For more information, see

,

, or

.

Prerequisites, Restrictions, and Recommendations