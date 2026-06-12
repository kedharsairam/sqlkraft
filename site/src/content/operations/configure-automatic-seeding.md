---
title: "Configure automatic seeding"
topic: "high-availability"
description: "2016 introduced automatic seeding of availability groups. When you create an availability group with automatic seeding, SQL Server automati"
tags: ["high-availability","configure-automatic-seeding"]
pubDate: 2025-12-01
---

2016 introduced automatic seeding of availability groups. When you create an

availability group with automatic seeding, SQL Server automatically creates the secondary

replicas for every database in the group. You no longer have to manually back up and restore

secondary replicas. To enable automatic seeding, create the availability group with T-SQL or

use the latest version of SQL Server Management Studio.

For background information, see

Automatic seeding for secondary replicas.

In SQL Server 2016, automatic seeding requires that the data and log file path is the same on

every SQL Server instance participating in the availability group. In SQL Server 2017, you can

use different paths, however Microsoft recommends using the same paths when all replicas are

hosted on the same platform (for example either Windows or Linux). Cross-platform availability

groups have different paths for the replicas. For details, see

Disk layout.

Availability group seeding communicates over the database mirroring endpoint. Open inbound

firewall rules to the mirroring endpoint port on each server.

Databases in an availability group must be in full recovery model. The database needs to have

a current full backup and transaction log backup. These backup files are not used for automatic

seeding, but they are required before including the database in an availability group.

To create an availability group with automatic seeding, set.

The following example creates an availability group on a two-node Windows Server failover

cluster. Before running the scripts, update the values for your environment.

1. Create the endpoints. Each server needs an endpoint. The following script creates an

endpoint that uses TCP port 5022 for the listener. Set

and

to match your environment and run the script on both servers:

```cmd
SEEDING_MODE=AUTOMATIC
<endpoint_name>
LISTENER_PORT
```
