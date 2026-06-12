---
title: "Contracts"
topic: "service-broker"
description: "08/29/2025 A contract defines which message types an application uses to accomplish a particular task."
tags: ["service-broker","contracts"]
pubDate: "2025-12-01"
---

A contract defines which message types an application uses to accomplish a particular task. A

contract is an agreement between two services about which messages each service sends to

accomplish a particular task. Contract definitions persist in the database where the type is

created.

You create an identical contract in each database that participates in a conversation. For

example, if a human resources application wants to verify an employee ID, the service that

requests the verification must know which types of messages the other service expects. The

requesting service also must know which types of messages it can expect to receive so that it's

prepared to process them.

The contract specifies which message types can be used to accomplish the desired work. The

contract also specifies which participant in the conversation can use each message type. Some

message types can be sent by either participant; other message types are restricted to be sent

only by the initiator or only by the target. A contract must contain a message type sent by the

initiator or a message type sent by either participant; otherwise, there's no way for the initiator

to begin a conversation that uses the contract.

Service Broker also includes a built-in contract named. The

contract contains

only the message type. If no contract is specified in the

statement,

Service Broker uses the

contract.

For example, a contract can have message types

,

, and. Only the initiating endpoint can use

, and only the target

endpoint can send

Either participant in the conversation can send the

message type. The

message type lets the participant either see

where the target is in its processing, or check with the initiator on the status of any parallel

processing relating to this request.

CREATE CONTRACT (Transact-SQL)

DROP CONTRACT (Transact-SQL)

Message Types

Create Service Broker contracts

```sql
DEFAULT
DEFAULT
SENT BY ANY
BEGIN DIALOG
DEFAULT
```
