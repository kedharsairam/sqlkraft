---
title: "Creating Service Broker Contracts"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Contracts define the name of a specific business task and list the message types used in that

  task. Service Broker contracts define tw
tags:
  - "service-broker"
  - "creating-service-broker-contracts"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Contracts define the name of a specific business task and list the message types used in that

task. Service Broker contracts define two different service roles: the initiator and the target. The

initiator of a conversation begins the conversation by sending a message to the target. The

contract that the conversation uses defines which service role can send messages of a given

message type.

For each task that the service performs, create a contract that includes the message types for

each step in the task. For each message type, specify whether the message type is sent from

the initiator to the target, from the target to the initiator, or in both directions.

A contract doesn't specify message ordering or the number of messages of a particular type

that can be sent. Service Broker requires that the initiator send the first message in a dialog

conversation. After the first message, there are no ordering requirements.

More than one contract can use the same message types. For example, a message that consists

of an XML document that contains a part number and quantity might be useful in a task that

accepts an order from a customer, a task that manages inventory, and a task that requests

shipping. Each task corresponds to a distinct contract, but all three contracts can use the same

message type.

The network format for a message includes the name of the contract. Therefore, contract

names are often chosen to avoid collation issues and naming conflicts. For more information

on naming, see

Naming Service Broker Objects

.

CREATE CONTRACT (Transact-SQL)

Conversation architecture

Contracts
