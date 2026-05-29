---
title: "Extended Security Updates"
topic: "azure-synapse"
description: |
  SQL Server Extended Security Updates
  
  Applies to:
  
  SQL Server 2014 (12.x)
  
  This article explains how to manage a SQL Server subscription to Extended Security Updates
  
  enabled by Azure Arc. For more in
tags:
  - "azure-synapse"
  - "extended-security-updates"
pubDate: 2025-12-01
---

SQL Server Extended Security Updates

Applies to:

SQL Server 2014 (12.x)

This article explains how to manage a SQL Server subscription to Extended Security Updates

enabled by Azure Arc. For more information about the program, see

What are Extended Security

Updates for SQL Server?

After SQL Server reaches the end of its support lifecycle, you can sign up for an Extended Security

Update (ESU) subscription for your servers and remain protected for up to three years. When you

upgrade to a newer version of SQL Server, you can terminate your ESU subscription and stop

paying for it. When you

migrate to Azure SQL

, the ESU charges automatically stop but you

continue to have access to the security updates.

You can use one of the following three options to subscribe to ESUs in a production environment.

The links in the list take you to sections in this article that provide more details.

The diagrams in the list use normalized cores (NCs) to illustrate the cost implications of the

licensing options. One core license for the Standard edition is equivalent to one NC. One core

license for the Enterprise edition is equivalent to four NCs. For more information, see

How

licenses apply to Azure resources

.

License by virtual cores

Use an Enterprise or Standard ESU subscription for the vCPUs (v-cores) of the virtual

machine (VM) that runs one or multiple instances of SQL Server. Each virtual machine is

billed individually for the v-cores allocated to it.

７

Note

Price structure for Extended Security Updates (ESUs) is changing for SQL Server 2016 on

Azure VMs. For more information, see the

.