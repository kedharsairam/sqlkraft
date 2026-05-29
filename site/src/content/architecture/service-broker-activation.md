---
title: "Service Broker Activation"
topic: "service-broker"
description: |
  09/11/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Service Broker activation helps applications to scale dynamically to match the message traffic.
  
  In general, an application uses activa
tags:
  - "service-broker"
  - "service-broker-activation"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker activation helps applications to scale dynamically to match the message traffic.

In general, an application uses activation if traffic to the service varies unpredictably or if the

service must dynamically scale to match the traffic the service receives.

Activation uses Service Broker to start an application when there's work for the program to do.

There are two distinct types of activation: internal activation and external activation. Internal

activation works with SQL Server stored procedures. In this case, Service Broker directly

activates the stored procedure. External activation works with programs that run independently

of SQL Server. For external activation, Service Broker produces a SQL Server event indicating

that the external program should start another queue reader.

Not all Service Broker applications use activation. If an application requires substantial

resources during startup, or if response time for infrequent messages is paramount, the

application might be better designed to start when SQL Server starts and remain running. For

tasks that are better performed at certain times, it might be better to design the application to

run as a scheduled job. For more information about choosing a strategy to start an application

that uses Service Broker, see

Choose a startup strategy

.

Description

Understand when activation

occurs

Describes the two steps of the Service Broker activation process.

Internal activation context

Describes the execution context for a stored procedure that is started by

internal activation.

Event-based activation

Describes the event and strategies for receiving and responding to the

event.

sys.dm_broker_activated_tasks (Transact-SQL)

ﾉ

Expand table