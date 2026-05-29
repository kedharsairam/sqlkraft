---
title: "Service Broker Routing"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes the details of how Service Broker routes messages. For an overview, see

  Routes

  .

  For most applications, a sim
tags:
  - "service-broker"
  - "service-broker-routing"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes the details of how Service Broker routes messages. For an overview, see

Routes

.

For most applications, a simple approach to Service Broker routing works well. In each

database that contains a service, specify a route for the external services that the service

communicates with. However, Service Broker provides a sophisticated routing system for

handling cases where an application needs more complex behavior. For examples that illustrate

the routing process, see

Service Broker routing examples

.

SQL Server maintains two distinct levels of routing information. Each database contains a local

routing table,

, for conversations begun in that database. For conversations that

originate in the instance of SQL Server, SQL Server searches the routing table in the database

that created the conversation. For conversations that arrive from outside the instance, SQL

Server searches

.

The basic matching process is identical whether the conversation originates in the instance or

outside the instance. The process ignores routes that have expired. The routing process

consists of three distinct steps:

1.

: Service Broker finds a set of possible routes by matching the

service name and the Service Broker identifier.

2.

: Service Broker chooses a route from among the set of possible routes.

3.

: When the route chosen specifies

as the network

address, Service Broker locates the service in the instance. If the service doesn't exist in

the instance, Service Broker might return to Step 2 and choose another route.

When a message has been sent from the initiator to the target and the initiator receives an

acknowledgment message from the target, the initiator uses the Service Broker identifier in the

acknowledgment messages to route subsequent messages to the same target. Service Broker

handles acknowledgment messages; the process is transparent to an application that uses

Service Broker. For more information about acknowledgment messages, see

Service Broker

communication protocols

.

```sql
sys.routes
msdb.sys.routes
'LOCAL'
```
