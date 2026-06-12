---
title: "Conversation Group Locks"
topic: "service-broker"
description: ""
tags: ["service-broker","conversation-group-locks"]
pubDate: 2025-12-01
---

Service Broker uses conversation group locks to guarantee that only one queue reader can

work with a related set of messages at any given time. Service Broker uses conversation group

locks to guarantee that messages are processed exactly once, in order.

All conversations belong to a conversation group. By default, each conversation belongs to a

different conversation group, and so it has a different conversation group identifier. The

statement changes the conversation group for a conversation. The

statement contains options for associating a new conversation with an existing

conversation group. For more information on conversation groups, see

Conversation groups.

A conversation group lock is, in effect, an exclusive lock on a set of messages that share the

same conversation group identifier. Conversation group locks are designed for simplicity,

efficiency, and correctness. There's no explicit command or hint for acquiring or releasing a

conversation group lock. Instead, every Service Broker command that affects a dialog or

conversation group acquires the appropriate conversation group lock automatically. For

example, a

statement locks the conversation group that the new dialog belongs

to, whereas a

statement locks the conversation group that the received messages

belong to.

A session holds a conversation group lock for the duration of the transaction within which the

session acquired the lock. A session can't hold a conversation group lock across transactions;

when a transaction ends, all conversation group locks acquired during the transaction are

released.

Locking occurs for the conversation group rather than for the conversation ID. Therefore, the

lock only applies to one side of the conversation, even when both the initiator and the target

are in the same database. A lock acquired by the target service doesn't block the initiating

service, and vice versa. Further, the Database Engine doesn't enforce locking when adding

incoming messages to a queue. The Database Engine adds messages to the queue even when

an application has a conversation group lock on the conversation group to which the messages

belong.

In practical terms, this means that an application that uses only identifiers retrieved from

Service Broker doesn't need to wait to acquire locks on Service Broker resources. Most Service

Broker applications are designed to take advantage of the locking provided by Service Broker;

that is, most Service Broker applications only use conversation group identifiers and

```sql
MOVE
CONVERSATION
BEGIN DIALOG
CONVERSATION
BEGIN DIALOG
RECEIVE
```
