---
title: "Backward compatibility"
topic: "migration"
description: |
  Article
  
  •
  
  02/26/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Backward compatibility is important to understand if you are upgrading, or if you have more
  
  than one version of SQL Server
tags:
  - "migration"
  - "backward-compatibility"
pubDate: 2025-12-01
---

Article

•

02/26/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Backward compatibility is important to understand if you are upgrading, or if you have more

than one version of SQL Server in a replication topology.

The general rules are:

A Distributor can be any version as long as it is greater than or equal to the Publisher

version (in many cases the Distributor is the same instance as the Publisher).

A Publisher can be any version as long as it less than or equal to the Distributor version.

The Publisher and Distributor are always the same product:

If the Publisher is SQL Server, the Distributor is SQL Server.

If the Publisher is

Azure SQL Managed Instance

, the Distributor is Azure SQL Managed

Instance.

Subscriber version depends on the type of publication:

A Subscriber to a transactional publication can be any version within two versions of

the Publisher version. For example: a SQL Server 2012 (11.x) Publisher can have SQL

Server 2014 (12.x) and SQL Server 2016 (13.x) Subscribers; and a SQL Server 2016 (13.x)

Publisher can have SQL Server 2014 (12.x) and SQL Server 2012 (11.x) Subscribers.

A Subscriber to a merge publication can be any version equal to or lower than the

Publisher version, which is supported as per the versions life cycle support cycle.

The Subscriber can be either SQL Server or Azure SQL Managed Instance, regardless of

what product the Distributor is, as long as it's within two versions of the Publisher -

except configuring Azure SQL Managed Instance as a pull Subscriber to a SQL Server

Distributor isn't supported.

Azure SQL Managed

Instance

Azure SQL Managed

Instance

Azure SQL Database

Azure SQL Managed

Instance

Azure SQL Managed Instance

ﾉ

Expand table

AUTD

AUTD

AUTD

2022