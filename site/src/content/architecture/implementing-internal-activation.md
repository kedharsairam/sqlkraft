---
title: "Implementing Internal Activation"
topic: "service-broker"
description: "09/03/2025 This tutorial is intended for users who are new to Service Broker, but are familiar with database concepts and Transact-SQL statements"
tags: ["service-broker","implementing-internal-activation"]
pubDate: 2025-12-01
---

This tutorial is intended for users who are new to Service Broker, but are familiar with database

concepts and Transact-SQL statements. It helps new users get started by showing them how to

implement an internal activation stored procedure to process Service Broker messages.

This tutorial shows you how to create the database objects that are required to support a basic

request-reply Service Broker conversation using an internal activation stored procedure. You

then start a conversation and use it to transmit messages.

Each Service Broker conversation has two ends: the conversation initiator and target. In a

request-reply conversation, a request message us sent from the initiator to the target, which

returns a reply message. Service Broker internal activation can be used to run a stored

procedure whenever there are messages to process. Service Broker can run multiple copies of

the stored procedure if there are many messages being transmitted. This tutorial shows you

how to create a stored procedure that receives the request messages at the target, and how to

configure the target to use internal activation to run the stored procedure.

This lesson guides you to perform the following tasks:

Create a service and queue for the target and a service and queue for the initiator.

Create a request message type and a reply message type.

Create a contract that specifies request messages go from the initiator to the target, and

that reply messages go from the target to the initiator.

Create a stored procedure that receives request messages from the target queue and

sends reply messages to the initiator.

Alter the target queue to enable internal activation of the stored procedure.

You then perform a basic conversation:

Start the conversation.

Send a request from the initiator to the target.
