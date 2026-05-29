---
title: "Messages"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Messages are the information exchanged between applications that use Service Broker.

  Each message is part of a conversation. A message
tags:
  - "service-broker"
  - "messages"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Messages are the information exchanged between applications that use Service Broker.

Each message is part of a conversation. A message has a specific type, which is determined by

the application that sends the message. Each message has a unique conversation identity, as

well as a sequence number within the conversation. When receiving messages, Service Broker

uses the conversation identity and the sequence number of the message to enforce message

ordering.

The content of the message is determined by the application. When a message is received,

Service Broker validates the content of the message to ensure that the content is valid for the

message type. Regardless of the message type, SQL Server stores the content of the message

as type varbinary(max). Therefore, a message can contain any data that can be converted to

varbinary(max).

An application typically processes the content of a message based on the contract and the

message type.

Message types

Build applications with Service Broker
