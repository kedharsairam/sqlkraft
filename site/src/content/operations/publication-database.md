---
title: "Publication database"
topic: "high-availability"
description: "This topic discusses special considerations for maintaining a publication database when you use Always On availability groups. Maintaining an Always"
tags: ["high-availability","publication-database"]
pubDate: "2025-12-01"
---

This topic discusses special considerations for maintaining a publication database when you

use Always On availability groups.

Maintaining an Always On publication database is basically the same as maintaining a standard

publication database, with the following considerations:

Administration must occur at the primary replica host. In SQL Server Management Studio,

publications appear under the

folder for the primary replica host and

also for readable secondary replicas. After failover, you might have to manually refresh

Management Studio for the change to be reflected if the secondary that was promoted to

primary was not readable.

Replication Monitor always displays publication information under the original publisher.

However, this information can be viewed in Replication Monitor from any replica by

adding the original publisher as a server.

When using stored procedures or Replication Management Objects (RMO) to administer

replication at the current primary, for cases in which you specify the Publisher name, you

must specify the name of the instance on which the database was enabled for replication

(the original publisher). To determine the appropriate name, use the

function. When a publishing database joins an availability

group, the replication metadata stored in the secondary database replicas is identical to

that at the primary. Consequently, for publication databases enabled for replication at the

primary, the publisher instance name stored in system tables at the secondary is the

name of the primary, not the secondary. This affects replication configuration and

maintenance if the publication database fails over to a secondary. For example, if you are

configuring replication with stored procedures at a secondary after failover, and you want

a pull subscription to a publication database that was enabled at a different replica, you

must specify the name of the original publisher instead of the current publisher as the

@publisher

parameter of

or.

However, if you enable a publication database after failover, the publisher instance name
