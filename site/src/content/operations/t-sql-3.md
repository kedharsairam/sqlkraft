---
title: "T-SQL"
topic: "high-availability"
description: |
  Article
  
  •
  
  02/01/2024
  
  Applies to:
  
  SQL Server
  
  This topic introduces the Transact-SQL statements that support deploying Always On
  
  availability groups and creating and managing an given availability
tags:
  - "high-availability"
  - "t-sql-3"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

This topic introduces the Transact-SQL statements that support deploying Always On

availability groups and creating and managing an given availability group, availability replica

and availability database.

CREATE ENDPOINT ... FOR DATABASE_MIRRORING

creates a database mirroring endpoint, if

none exists on the server instance. Every server instance on which you intend to deploy Always

On availability groups or database mirroring requires a database mirroring endpoint.

Execute this statement on the server instance on which you are creating the endpoint. You can

create only one database mirroring endpoint on a given server instance. For more information,

see

The Database Mirroring Endpoint (SQL Server)

.

CREATE AVAILABILITY GROUP

creates a new availability group and optionally an availability

group listener. Minimally, you must specify your local server instance, which will become the

initial primary replica. Optionally, you can also specify up to four secondary replicas.

Execute CREATE AVAILABILITY GROUP on the instance of SQL Server that you want to host the

initial primary replica of your new availability group. This server instance must reside on a node

of a Windows Server Failover Cluster (WSFC) (for more information, see

Prerequisites,

Restrictions, and Recommendations for Always On Availability Groups (SQL Server)

.

ALTER AVAILABILITY GROUP

supports changing an existing availability group or availability

group listener and for failing over an availability group.

Execute ALTER AVAILABILITY GROUP on the instance of SQL Server that hosts the current

primary replica.