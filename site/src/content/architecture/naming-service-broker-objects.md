---
title: "Naming Service Broker Objects"
topic: "service-broker"
description: |
  09/11/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  This article describes considerations for naming service broker objects. The conventions differ
  
  slightly for public interface objects,
tags:
  - "service-broker"
  - "naming-service-broker-objects"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes considerations for naming service broker objects. The conventions differ

slightly for public interface objects, network and security configuration objects, and queues.

Contracts, services, and message types form the public interface of a Service Broker

application. Because the names of these objects are contained in messages, naming

conventions for these objects often follow Universal Resource Identifier (URI) naming

conventions. This helps to ensure unique names for the objects.

Services names can also use the conventions to specify a network address in a route. In this

case, the name of the service can be used in a transport route. For more information on

routing, see

Service Broker routing

.

When sending and receiving messages, Service Broker uses binary matching for the names of

these objects. Therefore, characters that have more than one binary representation require

special care when public interface objects are named.

The names for routes and remote service bindings are never included in a message. For

convenience, these names can use the name of the service that the object configures.

These objects can't be temporary objects. Therefore, the number sign (#) isn't considered

significant in names for these objects. An object with a name that begins with # is a permanent

object rather than a temporary object.

Queue names can be used for many of the statements that accept table names. Therefore,

queues names follow standard SQL Server identifier conventions, with one exception. Because

queues can't be temporary objects, the name of a queue can't start with the number sign (#).

Queues are schema-owned objects, so queue names can include a schema name and database

name.