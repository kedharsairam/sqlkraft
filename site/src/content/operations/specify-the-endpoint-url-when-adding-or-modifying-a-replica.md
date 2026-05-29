---
title: "Specify the endpoint URL when adding or modifying a replica"
topic: "high-availability"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  To host an availability replica for an availability group, a server instance must possess a
  
  database mirroring endpoint. The server instance uses this
tags:
  - "high-availability"
  - "specify-the-endpoint-url-when-adding-or-modifying-a-replica"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

To host an availability replica for an availability group, a server instance must possess a

database mirroring endpoint. The server instance uses this endpoint to listen for Always On

availability groups messages from availability replicas hosted by other server instances. To

define an availability replica for an availability group, you must specify the endpoint URL of the

server instance that will host the replica. The

endpoint URL

identifies the transport protocol of

the database mirroring endpoint-TCP, the system address of the server instance, and the port

number associated with the endpoint.

The syntax for an endpoint URL is of the form:

TCP

<system-address>

<port>

where

<system-address>

is a string that unambiguously identifies the target computer system.

Typically, the server address is a system name (if the systems are in the same domain), a

fully qualified domain name, or an IP address:

Because the nodes of Windows Server Failover Clustering (WSFC) cluster are the same

domain, you can use the name of the computer system; for example,

.

To use an IP address, it must be unique in your environment. We recommend that you

use an IP address only if it is static. The IP address can be IP Version 4 (IPv4) or IP

Version 6 (IPv6). An IPv6 address must be enclosed within square brackets, for

example:

<IPv6_address>

.

To learn the IP address of a system, at the Windows command prompt, enter the

command.

７

Note

The term "endpoint URL" is synonymous with the term "server network address" used by

the database mirroring user interface and documentation.

```cmd
SYSTEM46
```