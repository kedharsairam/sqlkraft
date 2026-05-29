---
title: "SQL Server error log"
topic: "high-availability"
description: |
  SQL Server error log (Always On
  
  Article
  
  •
  
  02/01/2024
  
  Applies to:
  
  SQL Server
  
  The SQL Server error log reports events affecting Always On Availability Groups, such as:
  
  Communication with the Wind
tags:
  - "high-availability"
  - "sql-server-error-log"
pubDate: 2025-12-01
---

SQL Server error log (Always On

Article

•

02/01/2024

Applies to:

SQL Server

The SQL Server error log reports events affecting Always On Availability Groups, such as:

Communication with the Windows Server Failover Clustering (WSFC) cluster

State transitions of availability replicas

State transitions of availability databases

Connectivity state of availability databases between primary and secondary replicas

Statuses of the availability group endpoints

Statuses of the availability group listeners

Lease status between the SQL Server resource DLL (running in the WSFC cluster) and the

SQL Server instance (for more information, see

How It Works: SQL Server Always On lease

timeout

)

Error events in the availability group

The following symptoms should lead to review of the SQL Server error log:

Cannot access availability databases

Unexpected availability group failover

Availability group in the Resolving state unexpectedly

Availability group in an indeterminate state

For more information, see

View the SQL Server error log (SQL Server Management Studio)

.