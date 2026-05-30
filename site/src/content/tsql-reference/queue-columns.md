---
name: "Queue Columns"
title: "Queue Columns"
category: "statements"
description: "When the WAITFOR clause is specified, the statement waits for the specified time out, or until a"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
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

Status of the message. For messages returned by the

RECEIVE command, the status is always

. Messages in the

queue can contain one of the following values:

=Ready

=Received message

=Not yet complete

=Retained sent message

The conversation priority level that is applied to the

message.

Message order number in the queue.

Identifier for the conversation group that this message

belongs to.

Handle for the conversation that this message is part of.

Sequence number of the message in the conversation.

Name of the service that the conversation is to.

SQL Server object identifier of the service that the

conversation is to.

Expand table

#### Column name

#### Data type

#### nvarchar(128)

#### nvarchar(128)

#### nchar(2)

#### varbinary(MAX)

`status`

```sql
0
```

```sql
0
```

```sql
1
```

```sql
2
```

```sql
3
```

`priority`

`queuing_order`

`conversation_group_id`

`conversation_handle`

`message_sequence_number`

`service_name`

`service_id`
