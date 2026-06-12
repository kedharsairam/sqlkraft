---
title: "What is an Always On availability group?"
topic: "high-availability"
description: ""
tags: ["high-availability","what-is-an-always-on-availability-group"]
pubDate: 2025-12-01
---

This article introduces the Always On availability groups concepts that are central for

configuring and managing one or more availability groups in the Enterprise edition of SQL

Server. For the Standard edition, review

Basic Always On availability groups for a single

database.

The Always On availability groups feature is a high-availability and disaster-recovery solution

that provides an enterprise-level alternative to database mirroring. Always On availability

groups maximizes the availability of a set of user databases for an enterprise. An

availability

group

supports a failover environment for a discrete set of user databases, known as

availability databases

, that fail over together. An availability group supports a set of read-write

primary databases and one to eight sets of corresponding secondary databases. Optionally,

secondary databases can be made available for read-only access and/or some backup

operations.

With

enabled by Azure Arc

, you can

view availability groups

in Azure portal.

An

availability group

supports a replicated environment for a discrete set of user databases,

known as

availability databases. You can create an availability group for high availability (HA) or

for read-scale. An HA availability group is a group of databases that fail over together. A read-

scale availability group is a group of databases that are copied to other instances of SQL Server

for read-only workload. An availability group supports one set of primary databases and one to

eight sets of corresponding secondary databases. Secondary databases

aren't

backups.

Continue to back up your databases and their transaction logs regularly.

Each set of availability databases is hosted by an

availability replica. Two types of availability

replicas exist: a single

primary replica

, which hosts the primary databases, and one to eight

secondary replicas

, each of which hosts a set of secondary databases and serves as potential

failover targets for the availability group. An availability group fails over at the level of an

availability replica. An availability replica provides redundancy only at the database level for the



Tip

You can create any type of backup of a primary database. Alternatively, you can create log

backups and copy-only full backups of secondary databases. For more information, see.
