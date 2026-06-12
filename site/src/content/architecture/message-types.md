---
title: "Message Types"
topic: "service-broker"
description: "09/11/2025 Applications that use Service Broker communicate by sending messages to each other as part of a conversation."
tags: ["service-broker","message-types"]
pubDate: 2025-12-01
---

Applications that use Service Broker communicate by sending messages to each other as part

of a conversation. The participants in a conversation must agree on the name and content of

each message. A message type object defines a name for a message type and defines the type

of data that the message contains. Message types persist in the database where the message

type is created. You create an identical message type in each database that participates in a

conversation.

Each message type specifies the validation that SQL Server performs for messages of that type.

can validate that the message contains valid XML, that the message contains XML

that conforms to a particular schema, or that the message contains no data at all. For arbitrary

or binary data, the message type can specify that SQL Server doesn't validate the content of

the message.

Validation is performed when the destination service receives the message. If the content of

the message doesn't match the validation specified, Service Broker returns an error message to

the service that sent the message.

For an empty message type, the body of the message must not contain data. For a message

type that specifies well-formed XML, the body of the message must be well-formed XML. For a

message type that specifies XML conforming to a particular schema collection, the message

must contain well-formed XML that's valid for one of the schemas in the collection. For a

message type that specifies no validation, SQL Server accepts any message content. This

includes binary data, XML, or empty messages.

Service Broker offers a built-in message type named. If the message type isn't

specified in a Service Broker

command, the system uses the

message type.

Service Broker includes system messages types that are used to report errors and the status of

dialogs. For more information, see

Broker system messages.

）

Important

Regardless of the validation specified, an application must verify that the content of a

message is appropriate for the application before the program uses the data.

```sql
DEFAULT
SEND
DEFAULT
```
