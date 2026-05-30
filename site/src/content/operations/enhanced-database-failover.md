---
title: "Enhanced Database Failover"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  In SQL Server 2012 and 2014, if a database participating in an availability group on the primary

  replica loses the ability to write transactions, it w
tags:
  - "high-availability"
  - "enhanced-database-failover"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

In SQL Server 2012 and 2014, if a database participating in an availability group on the primary

replica loses the ability to write transactions, it will not trigger a failover even if the replicas are

synchronized and configured for automatic failover.

SQL Server 2016 introduces a new optional behavior named

enhanced database failover

that

can be set either by the Wizard or by using Transact-SQL. If this option is enabled and

automatic failover is configured, when one database participating in an availability group is no

longer able to write transactions, this will trigger a failover to a synchronized secondary replica.

An availability group is configured between Instance A and Instance B, containing a single

database named DB1. DB1's data file is on Drive E and its transaction log file is on Drive F. The

availability mode is set to synchronous commit with automatic failover. The new enhanced

database failover option is configured on the availability group. The two replicas are currently

in a synchronized state. A problem causes Drive E to fail. This scenario will not cause an

enhanced database failover, as Drive E does not contain the transaction log.

In the above scenario, if error 823 is reported 4 consecutive times while database failover

option is set to on, SQL Server will inform Windows Failover Cluster to take appropriate action

based on AG Role failover policy, this can be configured to perform a failover, or perform a

resource restart.

This has the same availability group configuration as Scenario 1. Rather than Drive E failing, this

time the transaction log drive, Drive F, fails. This will trigger a failover, as it meets the condition

covered by enhanced database failover: the transaction log is not reachable, which means the

database cannot write transactions.

An availability group is configured between Instance A and Instance B containing two

databases: DB1 and DB2. The availability mode is set to synchronous commit with a failover

mode of automatic, and enhanced database failover is enabled. Access to the disk containing

DB2's data and transaction log files is lost. When the problem is detected, the availability group

will automatically fail over to Instance B.
