---
title: "Service Broker Dialog Security"
topic: "service-broker"
description: "09/03/2025 Dialog security provides encryption, remote authentication, and remote authorization for a specific conversation. When a conversation"
tags: ["service-broker","service-broker-dialog-security"]
pubDate: 2025-12-01
---

Dialog security provides encryption, remote authentication, and remote authorization for a

specific conversation. When a conversation uses dialog security, Service Broker encrypts all

messages sent outside a SQL Server instance. Service Broker conversations use dialog security

by default.

Service Broker dialog security lets your application use authentication, authorization, or

encryption for an individual dialog conversation (or dialog). By default, all dialog conversations

use dialog security. When you begin a dialog, you can explicitly allow a dialog to proceed

without dialog security by including the

clause on the

statement. However, if a remote service binding exists for the service that the

conversation targets, the dialog uses security even when.

For a dialog that uses security, Service Broker encrypts all messages sent outside a SQL Server

instance. Messages that remain within a SQL Server instance are never encrypted. In dialog

security, only the database that hosts the initiating service and the database that hosts the

target service need to have access to the certificates used for security. That is, an instance that

performs message forwarding isn't required to have the capability to decrypt the messages

that the instance forward.

Service Broker provides two types of dialog security, full security and anonymous security. For

conversations that use dialog security, Service Broker provides remote authorization to map

the remote side of the conversation to a local user.

Messages are encrypted on the network when the conversation uses either full security or

anonymous security. However, the effective rights in the target database and the strategy used

for message encryption differ slightly between the two approaches.

Whether the conversation uses full security or anonymous security, the message body is

encrypted with a symmetric session key that is generated for the specific conversation. Only

the keys are encrypted with private key encryption using the certificate supplied for Dialog

Security. Service Broker also performs a message integrity check to help detect message

corruption or tampering.

creates a session key for a conversation that uses dialog security. To protect the

session key while it's stored in the database, Service Broker encrypts the session key with the

```sql
ENCRYPTION = OFF
BEGIN DIALOG
CONVERSATION
ENCRYPTION = OFF
```
