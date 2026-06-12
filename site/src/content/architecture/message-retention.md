---
title: "Message Retention"
topic: "service-broker"
description: "09/11/2025 When a queue specifies message retention, Service Broker doesn't delete messages from the queue until the conversation ends. Further,"
tags: ["service-broker","message-retention"]
pubDate: 2025-12-01
---

When a queue specifies message retention, Service Broker doesn't delete messages from the

queue until the conversation ends. Further, Service Broker also copies outgoing messages to

the queue. This allows the service to maintain a precise record of the incoming and outgoing

messages.

Message retention allows you to maintain an exact record of a conversation for a queue while

the conversation is active. For applications that require detailed auditing, or that must perform

compensating transactions when the conversation fails, this can be more convenient than

copying each message to a state table while the conversation is in progress.

Message retention increases the number of messages in the queue for active conversations

and increases the amount of work that SQL Server performs when sending a message.

Therefore, message retention reduces performance. The exact performance impact depends on

the communication patterns for the services that use the queue. In general, you should use

message retention any time that message retention is required for an application to operate

correctly. If the application doesn't require an exact record of all sent and received messages

while the conversation is active, maintaining state in a state table might improve performance.

Also remember that when the conversation ends, the retained messages are removed from the

queue, so if you're using retention for auditing purposes, you must be sure to copy the

messages to permanent storage before ending the conversation.

７

Note

Using message retention can reduce performance. You should only use this setting if the

application service-level agreement requires that the application retain the exact

messages sent and received. Messages in a queue that are ready to be received have a

status of 1. The

statement returns messages that show a status of 1. After the

statement returns a message, it sets the status to 0 and leaves the message in the

queue if message retention is on. If message retention is off, the

statement

deletes the message from the queue. Any service that uses the queue saves both

incoming and outgoing messages. In this case, the

command copies messages to

the queue for the service (with a

of

) as well as adding the message to the

transmission queue. When the conversation ends, the queue deletes all of the messages

for the conversation.

```sql
RECEIVE
RECEIVE
RECEIVE
SEND status
3
```
