---
title: "Completing a Conversation in a Single Database"
topic: "service-broker"
description: |
  09/04/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This tutorial is intended for users who are new to Service Broker, but are familiar with database

  concepts and Transact-SQL statements
tags:
  - "service-broker"
  - "completing-a-conversation-in-a-single-database"
pubDate: 2025-12-01
---

09/04/2025

SQL Server

Azure SQL Managed Instance

This tutorial is intended for users who are new to Service Broker, but are familiar with database

concepts and Transact-SQL statements. It helps new users get started by showing them how to

build and run a simple conversation in a single database.

This tutorial shows you how to create the database objects that are required to support a

simple request-reply Service Broker conversation. You then start a conversation and use it to

transmit messages.

Each Service Broker conversation has two ends: the conversation initiator and target. You

perform the following tasks:

Create a service and queue for the target and a service and queue for the initiator.

Create a request message type and a reply message type.

Create a contract that specifies request messages go from the initiator to the target, and

that reply messages go from the target to the initiator.

Perform a simple conversation:

Start the conversation.

Send a request from the initiator to the target.

Receive the request at the target and send a reply to the initiator.

Receive the reply at the initiator.

End the conversation.

Messages aren't transmitted across a network for conversations that have both ends in the

same instance of the Database Engine. Database Engine security and permissions restricts

access to authorized principles. Network encryption isn't needed for this scenario.

This tutorial is divided into three lessons:
