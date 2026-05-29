---
title: "Logical Architecture [Service Broker]"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Service Broker applications consist of Service Broker database objects and one or more

  applications that use those objects. This secti
tags:
  - "service-broker"
  - "logical-architecture-service-broker"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker applications consist of Service Broker database objects and one or more

applications that use those objects. This section describes each of the objects that are used in a

Service Broker application.

There are three types of Service Broker components:

: The runtime structure of the conversation. Applications

exchange messages as part of a conversation.

: These are design-time components that specify the basic

design of the application. These components define the message types for the

application, the conversation flow for the application, and the database storage for the

application.

: These components define the infrastructure for

exchanging messages between databases and instances of the Database Engine.

This section also presents short overview of building applications by using Service Broker.

Description

Conversation

architecture

Describes conversations, conversation groups, and messages. These are the

Service Broker objects that are created and managed at runtime in application

code.

Service architecture

Describes the design-time objects that are created in databases as part of the

Service Broker infrastructure.

Networking and

remote security

Describes objects that control how Service Broker communicates between

databases and instances of the Database Engine.

Benefits of programming with Service Broker

ﾉ

Expand table
