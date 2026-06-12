---
title: "Client connection types"
topic: "high-availability"
description: "In an Always On availability group, you can configure one or more availability replicas to allow read-only connections when running under the secondar"
tags: ["high-availability","client-connection-types"]
pubDate: "2025-12-01"
---

In an Always On availability group, you can configure one or more availability replicas to allow

read-only connections when running under the secondary role (that is, when running as a

secondary replica). You can also configure each availability replica to allow or exclude read-only

connections when running under the primary role (that is, when running as the primary

replica).

To facilitate client access to primary or secondary databases of a given availability group, you

should define an availability group listener. By default, the availability group listener directs

incoming connections to the primary replica. However, you can configure an availability group

to support read-only routing, which enables its availability group listener to redirect the

connection requests of read-intent applications to a readable secondary replica. For more

information, see

Configure Read-Only Routing for an Availability Group (SQL Server).

During a failover, a secondary replica transitions to the primary role and the former primary

replica transitions to the secondary role. During the failover process, all client connections to

both the primary replica and secondary replicas are terminated. After the failover, when a client

reconnects to the availability group listener, the listener reconnects the client to the new

primary replica, except for a read-intent connect request. If read-only routing is configured on

the client and on the server instances that hosts the new primary replica and on at least one

readable secondary replica, read-intent connection requests are re-routed to a secondary

replica that supports the type of connection access that the client requires. To ensure a graceful

client experience after a failover, it is important to configure connection access for both the

secondary and primary roles of every availability replica.

The secondary role supports three alternatives for client connections, as follows:

７

Note

For information about the availability group listener, which handles client connection

requests, see.
