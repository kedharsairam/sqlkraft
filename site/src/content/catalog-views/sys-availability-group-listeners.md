---
name: 'sys.availability_group_listeners'
title: 'sys.availability_group_listeners (Transact-'
category: 'objects'
description: 'statement. In addition, if an IP configuration'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Permissions


## Description
statement. In addition, if an IP configuration

that was created outside of SQL Server, for

example by using the WSFC Failover Cluster

Manager, but can be modified by the ALTER

AVAILABILITY GROUP tsql statement, the IP

configuration qualifies as conformant.

0 = Listener is nonconformant. Typically, this

indicates an IP address that couldn't be

configured by using SQL Server commands

and, instead, was defined directly in the WSFC

cluster.

Cluster IP configuration strings, if any, for this

listener. NULL = Listener has no virtual IP

addresses. For example:

IPv4 address:

.

IPv6 address:

: SQL Server 2019 (15.x) CU8 and

later, SQL Server 2017 (14.x) CU25 and later,

SQL Server 2016 (13.x) SP3 and later

This column indicates the listener is a

distributed network name (DNN) listener if

value set to 1. For more information, see

Configure a DNN listener for an availability

group

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.


## Permissions for SQL Server 2022 and later
Always On Availability Groups Dynamic Management Views and Functions (Transact-SQL)

Always On Availability Groups Catalog Views (Transact-SQL)

Monitor Availability Groups (Transact-SQL)

Always On Availability Groups (SQL Server)

Last updated on 03/03/2026

Related content

```sql
65.55.39.10
```

```sql
2001::4898:23:1002:20f:1fff:feff:b3a3
```
