---
title: "Configure for distributed transactions"
topic: "high-availability"
description: "2017 (14.x) and later versions support all distributed transactions including databases in an availability group."
tags: ["high-availability","configure-for-distributed-transactions"]
pubDate: "2025-12-01"
---

2017 (14.x) and later versions support all distributed transactions including

databases in an availability group. This article explains how to configure an availability group

for distributed transactions

In order to guarantee distributed transactions, the availability group must be configured to

register databases as distributed transaction resource managers.

In a distributed transaction, client applications work with Microsoft Distributed Transaction

Coordinator (MSDTC or DTC) to guarantee transactional consistency across multiple data

sources. DTC is a service available on supported Windows Server-based operating systems. For

a distributed transaction, DTC is the

transaction coordinator. Normally, a SQL Server instance is

the

resource manager. When a database is in an availability group, each database needs to be

its own resource manager.

doesn't prevent distributed transactions for databases in an availability group -

even when the availability group isn't configured for distributed transactions. However when an

availability group isn't configured for distributed transactions, failover might not succeed in

some situations. Specifically the new primary replica SQL Server instance might not be able to

get the transaction outcome from DTC. To enable the SQL Server instance to get the outcome

of in-doubt transactions from the DTC after failover, configure the availability group for

distributed transactions.

DTC isn't involved in availability group processing unless a database is also a member of a

Failover Cluster. Within an availability group, the consistency between replicas is maintained by

７

Note

2016 (13.x) Service Pack 2 and later versions provide full support for

distributed transactions in availability groups. In SQL Server 2016 (13.x) Service Pack 1 and

earlier versions, cross-database distributed transactions (that is, transaction using

databases on the same SQL Server instance) involving a database in an availability group

aren't supported. SQL Server 2017 (14.x) doesn't have this limitation.

In SQL Server 2016 (13.x), the configuration steps are the same as in SQL Server 2017

(14.x).
