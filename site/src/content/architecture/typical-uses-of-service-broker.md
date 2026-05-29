---
title: "Typical Uses of Service Broker"
topic: "service-broker"
description: |
  09/11/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Service Broker can be useful for any application that needs to perform processing
  
  asynchronously, or that needs to distribute processi
tags:
  - "service-broker"
  - "typical-uses-of-service-broker"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker can be useful for any application that needs to perform processing

asynchronously, or that needs to distribute processing across a number of computers. Typical

uses of Service Broker include:

Asynchronous triggers

Reliable query processing

Reliable data collection

Distributed server-side processing for client applications

Data consolidation for client applications

Large-scale batch processing

Many applications that use triggers, such as online transaction processing (OLTP) systems, can

benefit from Service Broker. A trigger queues a message that requests work from a Service

Broker service. The trigger doesn't actually perform the requested work. Instead, the trigger

creates a message that contains information about the work to be done and sends this

message to a service that performs the work. The trigger then returns.

When the original transaction commits, Service Broker delivers the message to the destination

service. The program that implements the service performs the work in a separate transaction.

By performing this work in a separate transaction, the original transaction can commit

immediately. The application avoids system slowdowns that result from keeping the original

transaction open while performing the work.

Some applications must reliably process queries without regard to computer failures, power

outages, or similar problems. An application that needs reliable query processing can submit

queries by sending messages to a Service Broker service. The application that implements the

service reads the message, runs the query, and returns the results. All three of these operations

take place in the same transaction. If a failure occurs before the transaction commits, the entire

transaction rolls back and the message returns to the queue. When the computer recovers, the

application restarts and processes the message again.