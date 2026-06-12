---
title: "Add replica - wizard"
topic: "high-availability"
description: "Use the to help you add a new secondary replica to an existing Always On availability group."
tags: ["high-availability","add-replica-wizard"]
pubDate: "2025-12-01"
---

Use the

to help you add a new secondary replica to

an existing Always On availability group.

If you have never added any availability replica to an availability group, see the "Server

instances" and "Availability groups and replicas" sections in

Prerequisites, restrictions, and

recommendations for Always On availability groups.

You must be connected to the server instance that hosts the current primary replica.

Before adding a secondary replica, verify that the host instance of SQL Server is in the

same Windows Server Failover Cluster (WSFC) as the existing replicas but resides on a

different cluster node. Also, verify that this server instance meets all other Always On

availability groups prerequisites. For more information, see

Prerequisites, restrictions, and

recommendations for Always On availability groups.

If a server instance that you select to host an availability replica is running under a

domain user account and doesn't yet have a database mirroring endpoint, the wizard can

create the endpoint and grant CONNECT permission to the server instance service

account. However, if the SQL Server service is running as a built-in account, such as Local

System, Local Service, or Network Service, or a nondomain account, you must use

certificates for endpoint authentication, and the wizard will be unable to create a

database mirroring endpoint on the server instance. In this case, we recommend that you

create the database mirroring endpoints manually before you launch the Add Replica to

Availability Group Wizard.

CREATE ENDPOINT

７

Note

For information about using Transact-SQL or PowerShell to add a secondary replica to an

availability group, see.
