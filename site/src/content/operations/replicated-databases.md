---
title: "Replicated databases"
topic: "upgrade"
description: "- Windows only SQL Server supports upgrading replicated databases from previous versions of SQL Server; it isn't required to stop activity at other n"
tags: ["upgrade","replicated-databases"]
pubDate: "2025-12-01"
---

- Windows only

supports upgrading replicated databases from previous versions of SQL Server; it

isn't required to stop activity at other nodes while a node is being upgraded.

Ensure that you adhere to the rules regarding which versions are supported in a topology:

A Distributor can be any version as long as it's greater than or equal to the Publisher

version (in many cases the Distributor is the same instance as the Publisher).

A Publisher can be any version as long as it less than or equal to the Distributor version.

The Publisher and Distributor must be the same product. Either both are SQL Server, or

both are Azure SQL Managed Instance.

Subscriber version depends on the type of publication:

A Subscriber to a transactional publication can be any version within two versions of

the Publisher version. For example: a SQL Server 2012 (11.x) Publisher can have SQL

Server 2014 (12.x) and SQL Server 2016 (13.x) Subscribers; and a SQL Server 2016 (13.x)

Publisher can have SQL Server 2014 (12.x) and SQL Server 2012 (11.x) Subscribers.

A Subscriber to a merge publication can be all versions equal to or lower than the

Publisher version, whichever is supported as per the versions life cycle support cycle.

The upgrade path to SQL Server is different depending on the deployment pattern. SQL Server

offers two upgrade paths in general:

Side-by-side: Deploy a parallel environment and move databases along with the

associated instance level objects, such as logins, jobs, etc. to the new environment.

In-place upgrade: Allow the SQL Server installation media to upgrade the existing SQL

Server installation by replacing the SQL Server bits, and upgrading the database objects.

For environments running availability groups (AGs) or failover cluster instances (FCIs), an

in-place upgrade is combined with a

rolling upgrade

to minimize downtime.
