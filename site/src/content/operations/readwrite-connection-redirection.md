---
title: "Read/write connection redirection"
topic: "high-availability"
description: ""
tags: ["high-availability","readwrite-connection-redirection"]
pubDate: 2025-12-01
---

2019 (15.x) and later

2019 (15.x) introduces

secondary to primary replica read/write connection redirection

for Always On availability groups. Read/write connection redirection is available on any

operating system platform. It allows client application connections to be directed to the

primary replica regardless of the target server specified in the connections string.

For example, the connection string can target a secondary replica. Depending on the

configuration of the availability group (AG) replica and the settings in the connection string,

the connection can be automatically redirected to the primary replica.

Prior to SQL Server 2019 (15.x), the AG listener and the corresponding cluster resource redirect

user traffic to the primary replica to ensure reconnection after failover. SQL Server 2019 (15.x)

continues to support the AG listener functionality and adds replica connection redirection for

scenarios that cannot include a listener. For example:

The cluster technology that SQL Server availability groups integrates with does not offer a

listener like capability

A multi-subnet configuration like in the cloud or multi-subnet floating IP with Pacemaker

where configurations become complex, prone to errors, and difficult to troubleshoot due

to multiple components involved

Read scale-out, or disaster recovery and cluster type is

, because there is no

straightforward mechanism to ensure transparent reconnection upon manual failover

In order for a secondary replica to redirect read/write connection requests:

The secondary replica must be online.

The replica spec

must include.

The connection string must be

either by defining

as

or by not setting

and letting the default (

) take

effect.

```cmd
NONE
PRIMARY_ROLE
READ_WRITE_ROUTING_URL
ReadWrite
ApplicationIntent
```
