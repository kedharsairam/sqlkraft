---
title: "Building Applications with Service Broker"
topic: "service-broker"
description: "08/29/2025 Any program that can run Transact-SQL statements can use Service Broker. A Service Broker application can be implemented as a program"
tags: ["service-broker","building-applications-with-service-broker"]
pubDate: 2025-12-01
---

Any program that can run Transact-SQL statements can use Service Broker. A Service Broker

application can be implemented as a program running outside of SQL Server, or as a stored

procedure written in Transact-SQL or a.NET language.

A program that uses Service Broker is typically composed of a number of components working

together to accomplish a task. A program that initiates a conversation creates and sends a

message to another service. That program might wait for a response, or exit immediately and

rely on another program to process the response. For a service that is the target of a

conversation, the program receives an incoming message from the queue for the service, reads

the message data, does any necessary processing, and then creates and sends a response

message if appropriate.

Service Broker extends Transact-SQL. An application doesn't need a special object model or

library to work with Service Broker. Instead, programs send Transact-SQL commands to SQL

Server and process the results of those commands. An application can be activated by Service

Broker, can run as a background service, can run as a scheduled job, or can be started in

response to an event. For more information on strategies for starting an application that uses

Service Broker, see

Choose a startup strategy.

For information on creating applications with Service Broker, see

Benefits of programming with

Service Broker.

The following illustration shows the interaction in an application that uses Service Broker:
