---
title: "Rename a failover cluster"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  When a SQL Server instance is part of a failover cluster, the process of renaming the virtual

  server differs from that of renaming a stand-alone insta
tags:
  - "high-availability"
  - "rename-a-failover-cluster"
pubDate: 2025-12-01
---

Article

•

03/03/2023

SQL Server

When a SQL Server instance is part of a failover cluster, the process of renaming the virtual

server differs from that of renaming a stand-alone instance. For more information, see

Rename

a Computer that Hosts a Stand-Alone Instance of SQL Server.

The name of the virtual server is always the same as the name of the SQL Network Name (the

SQL Virtual Server Network Name). Although you can change the name of the virtual server,

you cannot change the instance name. For example, you can change a virtual server named

VS1\instance1 to some other name, such as SQL35\instance1, but the instance portion of the

name, instance1, will remain unchanged.

Before you begin the renaming process, review the items below.

does not support renaming servers involved in replication, except in the case

of using log shipping with replication. The secondary server in log shipping can be

renamed if the primary server is permanently lost. For more information, see

Log

Shipping and Replication (SQL Server).

When renaming a virtual server that is configured to use database mirroring, you must

turn off database mirroring before the renaming operation, and then re-establish

database mirroring with the new virtual server name. Metadata for database mirroring will

not be updated automatically to reflect the new virtual server name.

1. Using Cluster Administrator, change the SQL Network Name to the new name.

2. Take the network name resource offline. This takes the SQL Server resource and other

dependent resources offline as well.

3. Bring the SQL Server resource back online.

After a virtual server has been renamed, any connections that used the old name must now

connect using the new name.
