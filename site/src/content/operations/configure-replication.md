---
title: "Configure replication"
topic: "high-availability"
description: |
  Article
  
  •
  
  01/08/2025
  
  Applies to:
  
  SQL Server
  
  - Windows only
  
  Configuring SQL Server replication and Always On availability groups involves seven steps.
  
  Each step is described in more detail in th
tags:
  - "high-availability"
  - "configure-replication"
pubDate: 2025-12-01
---

Article

•

01/08/2025

Applies to:

SQL Server

- Windows only

Configuring SQL Server replication and Always On availability groups involves seven steps.

Each step is described in more detail in the following sections.

The distribution database can't be placed in an availability group with SQL Server 2012 and

SQL Server 2014. Placing the distribution database into an availability group is supported with

SQL 2016 and greater, except for distribution databases used in merge, bidirectional, or peer-

to-peer replication topologies. For more information, see

Set up replication distribution

database in Always On availability group

.

1. Configure distribution at the distributor. If stored procedures are being used for

configuration, run

Use the

@password

parameter to identify the

password that will be used when a remote publisher connects to the distributor. The

password will also be needed at each remote publisher when the remote distributor is set

up.

SQL

2. Create the distribution database at the distributor. If stored procedures are being used for

configuration, run

SQL

```cmd
sp_adddistributor
sp_adddistributiondb
USE
master
;
GO
EXECUTE
sys.sp_adddistributor
@distributor =
'MyDistributor'
,
@
password
=
'**Strong password for distributor**'
;
USE
master
;
GO
```