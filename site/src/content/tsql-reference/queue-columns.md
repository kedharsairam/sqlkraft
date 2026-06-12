---
name: "Queue Columns"
title: "Queue Columns"
category: "statements"
description: "When the WAITFOR clause is specified, the statement waits for the specified time out, or until a"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

When the WAITFOR clause is specified, the statement waits for the specified time out, or until a

result set is available. If the queue is dropped or the status of the queue is set to OFF while the

statement is waiting, the statement immediately returns an error. If the RECEIVE statement

specifies a conversation group or conversation handle and the service for that conversation is

dropped or moved to another queue, the RECEIVE statement reports a Transact-SQL error.

RECEIVE is not valid in a user-defined function.

The RECEIVE statement has no priority starvation prevention. If a single RECEIVE statement

locks a conversation group and retrieves a lot of messages from low priority conversations, no

messages can be received from high priority conversations in the group. To prevent this, when

you are retrieving messages from low priority conversations, use the TOP clause to limit the

number of messages retrieved by each RECEIVE statement.

The following table lists the columns in a queue:

## Description

Status of the message.

RECEIVE command, the status is always.

queue can contain one of the following values:

=Ready

=Received message

=Not yet complete

=Retained sent message

message.

Message order number in the queue.

Identifier for the conversation group that this message

belongs to.

Handle for the conversation that this message is part of.

Sequence number of the message in the conversation.

conversation is to.

#### nvarchar(128)

#### nvarchar(128)

#### varbinary(MAX)

`queuing_order`

`conversation_group_id`

`conversation_handle`

`message_sequence_number`
