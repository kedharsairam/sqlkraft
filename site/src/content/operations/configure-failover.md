---
title: "Configure failover"
topic: "linux-operations"
description: |
  Applies to:
  
  SQL Server
  
  on Linux
  
  Within the context of an availability group (AG), the primary role and secondary role of
  
  availability replicas are typically interchangeable, in a process known as 
tags:
  - "linux-operations"
  - "configure-failover"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

Within the context of an availability group (AG), the primary role and secondary role of

availability replicas are typically interchangeable, in a process known as failover. Three forms of

failover exist: automatic failover (without data loss), planned manual failover (without data

loss), and forced manual failover (with possible data loss), typically called

forced failover

.

Automatic and planned manual failovers preserve all your data. An AG fails over at the

availability-replica level. That is, an AG fails over to one of its secondary replicas (the current

failover target).

For background information about failover, see

Failover and Failover Modes (Always On

Availability Groups)

.

Use the cluster management tools to fail over an AG managed by an external cluster manager.

For example, if a solution uses Pacemaker to manage a Linux cluster, use

to perform

manual failovers on Red Hat Enterprise Linux (RHEL) or Ubuntu. On SUSE Linux Enterprise

Server (SLES), use

. (Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES)

isn't supported.)

To fail over, the secondary replica that will become the primary replica must be synchronous. If

a secondary replica is asynchronous,

change the availability mode

.

Manually fail over in two steps.

）

Important

Under normal operations, don't fail over with Transact-SQL or SQL Server management

tools like SSMS or PowerShell. When

, the only acceptable value

for

is

. With these settings, all manual or automatic failover

actions are executed by the external cluster manager. For instructions to force failover

with potential data loss, see

.

```cmd
pcs
crm
CLUSTER_TYPE = EXTERNAL
FAILOVER_MODE
EXTERNAL
```