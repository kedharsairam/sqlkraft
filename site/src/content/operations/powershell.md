---
title: "PowerShell"
topic: "high-availability"
description: |
  Article

  •

  09/04/2024

  Applies to:

  SQL Server

  This topic describes how to use PowerShell cmdlets to create and configure an Always On

  availability group by using PowerShell in SQL Server. An

  avai
tags:
  - "high-availability"
  - "powershell"
pubDate: 2025-12-01
---

Article

•

09/04/2024

SQL Server

This topic describes how to use PowerShell cmdlets to create and configure an Always On

availability group by using PowerShell in SQL Server. An

availability group

defines a set of user

databases that will fail over as a single unit and a set of failover partners, known as

availability

replicas

, which support failover.

Before creating an availability group, verify that the host instances of SQL Server each

resides on a different Windows Server Failover Clustering (WSFC) node of a single WSFC

failover cluster. Also, verify that your server instances met the other server-instance

prerequisites and that all of the other Always On availability groups requirements are

meet and that you are aware of the recommendations. For more information, we strongly

recommend that you read

Prerequisites, Restrictions, and Recommendations for Always

On Availability Groups (SQL Server).

Requires membership in the

fixed server role and either CREATE AVAILABILITY

GROUP server permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL SERVER

７

Note

For an introduction to availability groups, see.

７

Note

As an alternative to using PowerShell cmdlets, you can use the Create Availability Group

wizard or Transact-SQL. For more information, see

or.

Prerequisites, Restrictions, and Recommendations
