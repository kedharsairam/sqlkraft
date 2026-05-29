---
title: "Planned manual failover"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/04/2024
  
  Applies to:
  
  SQL Server
  
  This topic describes how to perform a manual failover without data loss (a
  
  planned manual
  
  failover
  
  ) on an Always On availability group by using SQL
tags:
  - "high-availability"
  - "planned-manual-failover"
pubDate: 2025-12-01
---

Article

•

09/04/2024

Applies to:

SQL Server

This topic describes how to perform a manual failover without data loss (a

planned manual

failover

) on an Always On availability group by using SQL Server Management Studio, Transact-

SQL, or PowerShell in SQL Server. An availability group fails over at the level of an availability

replica. A planned manual failover, like any Always On availability group failover, transitions a

secondary replica to primary role. Concurrently, the failover transitions the former primary

replica to the secondary role.

A planned manual failover is supported only when the primary replica and the target secondary

replica are running in synchronous-commit mode and are currently synchronized. A planned

manual failover preserves all the data in the secondary databases that are joined to the

availability group on the target secondary replica. After the former primary replica transitions

to the secondary role, its databases become secondary databases. Then they begin to

synchronize with the new primary databases. After they all transition into the SYNCHRONIZED

state, the new secondary replica becomes eligible to serve as the target of a future planned

manual failover.

７

Note

If the secondary and primary replicas are both configured for automatic failover mode,

after the secondary replica is synchronized, it also can serve as the target for an automatic

failover. For more information, see

.

）

Important

There are specific procedures to fail over a read-scale availability group with no cluster

manager. When an availability group has CLUSTER_TYPE = NONE, follow the procedures

under

.