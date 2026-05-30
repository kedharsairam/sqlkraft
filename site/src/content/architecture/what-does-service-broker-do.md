---
title: "What does service broker do?"
topic: "service-broker"
description: |
  09/10/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Service Broker helps developers build asynchronous, loosely coupled applications in which

  independent components work together to acco
tags:
  - "service-broker"
  - "what-does-service-broker-do"
pubDate: 2025-12-01
---

09/10/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker helps developers build asynchronous, loosely coupled applications in which

independent components work together to accomplish a task. These application components

exchange messages that contain the information required to complete the task. This topic

describes the following aspects of Service Broker:

Conversations

Message ordering and coordination

Transactional asynchronous programming

Support for loosely coupled applications

Service Broker components

Service Broker is designed around the basic functions of sending and receiving messages. Each

message forms part of a conversation. Each conversation is a reliable, persistent

communication channel. Each message and conversation has a specific type that Service Broker

enforces to help developers write reliable applications.

New Transact-SQL statements let applications reliably send and receive these messages. An

application sends messages to a service, which is a name for a set of related tasks. An

application receives messages from a queue, which is a view of an internal table.

Messages for the same task are part of the same conversation. Within each conversation,

Service Broker guarantees that an application receives each message exactly once, in the order

in which the message was sent. The program that implements a service can associate related

conversations for the same service in a conversation group.

Certificate-based security helps you protect sensitive messages and control access to services.

You can think of Service Broker being like a postal service: to hold a conversation with a distant

colleague, you can communicate by sending letters through the postal service. The postal

service sorts and delivers the letters. You and your colleague then retrieve the letters from your

mailboxes, read them, write responses, and send new letters until the conversation has ended.

Letter delivery occurs asynchronously while you and your colleague handle other tasks.
