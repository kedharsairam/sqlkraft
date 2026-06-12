---
title: "Dialog Conversations"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  All messages sent by Service Broker are part of a conversation. A dialog is a conversation

  between two services. A dialog is a reliabl
tags:
  - "service-broker"
  - "dialog-conversations"
pubDate: 2025-12-01
---

08/29/2025

SQL Server

Azure SQL Managed Instance

All messages sent by Service Broker are part of a conversation. A dialog is a conversation

between two services. A dialog is a reliable, persistent bidirectional stream of messages

between two services.

Dialogs provide exactly-once-in-order (EOIO) message delivery. Dialogs use the conversation

identifier and sequence numbers that are contained in each message to identify related

messages and deliver messages in the correct order. A dialog is a reliable, persistent stream of

messages between two services.

A dialog conversation has two participants. The initiator starts the conversation. The target

accepts a conversation begun by the initiator. Whether a participant starts the conversation

determines the messages that the participant can send, as specified in the contract for the

conversation. The following diagram shows the message flow of a dialog:

Applications exchange messages as part of the dialog. When SQL Server receives a message for

a dialog, SQL Server puts the message in the queue for the dialog. The application receives the

message from the queue and processes the message as necessary. As part of the processing,

the application might send messages to the other participant in the dialog.

Dialogs incorporate automatic message-receipt acknowledgments to ensure reliable delivery.

Service Broker saves each outgoing message in the transmission queue until the message is

acknowledged by the remote service. These automatic acknowledgments save time and

resources by making it unnecessary for an application to explicitly acknowledge each message.
