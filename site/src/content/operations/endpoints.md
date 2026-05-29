---
title: "Endpoints"
topic: "high-availability"
description: |
  08/29/2025
  
  Applies to:
  
  SQL Server
  
  - Windows only
  
  Azure SQL Managed Instance
  
  To participate in Always On availability groups or database mirroring a server instance requires
  
  its own, dedicated
  
  d
tags:
  - "high-availability"
  - "endpoints"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

- Windows only

Azure SQL Managed Instance

To participate in Always On availability groups or database mirroring a server instance requires

its own, dedicated

database mirroring endpoint

. This endpoint is a special-purpose endpoint

that is used exclusively to receive connections from other server instances. On a given server

instance, every Always On availability groups or database mirroring connection to any other

server instance uses a single database mirroring endpoint.

Database mirroring endpoints use Transmission Control Protocol (TCP) to send and receive

messages between the server instances participating database mirroring sessions or hosting

availability replicas. The database mirroring endpoint listens on a unique TCP port number.

Client connections to a principal server or primary replica don't use the database mirroring

endpoint.

The network address of a server instance (its

server network address

or

Endpoint URL

) contains

the port number of its endpoint, as well as the system and domain name of its host computer.

The port number uniquely identifies a specific server instance.

The following figure illustrates how two server instances on the same server are uniquely

identified. The server network addresses of both server instances contain the same system

name,

, and domain name,

. To enable the system to

route connections to a server instance, a server network address includes the port number

associated with the mirroring endpoint of a particular server instance.

７

Note

The database mirroring feature will be removed in a future version of Microsoft SQL

Server. Avoid using this feature in new development work, and plan to modify applications

that currently use database mirroring to use Always On availability groups instead.

```cmd
MYSYSTEM
Adventure-Works.MyDomain.com
```