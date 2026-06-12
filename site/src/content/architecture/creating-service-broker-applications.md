---
title: "Creating Service Broker Applications"
topic: "service-broker"
description: "08/29/2025 This section provides a general overview of the structure of a Service Broker application, discusses some of the most common strategie"
tags: ["service-broker","creating-service-broker-applications"]
pubDate: 2025-12-01
---

This section provides a general overview of the structure of a Service Broker application,

discusses some of the most common strategies for starting an application that uses Service

Broker, and describes the basic steps to receive and process messages.

The application for an initiating service uses the

statement to specify information

about the services at each endpoint and the service contract that the application will use to

communicate. The application uses the

statement to send the first message of the

conversation to the target service. The application must be prepared to receive and process

messages from Service Broker, even if the contract doesn't allow the target service to return

messages. The initiating application is often implemented as two separate components. One

component begins the conversation; the other component processes messages that arrive in

the queue.

The application for a target service receives and processes messages from the initiating service.

The application must also be prepared to receive and process messages from Service Broker.

Depending on the needs of the service, the part of the application that processes the queue

can be started in several different ways. For more information about starting an application

that uses Service Broker, see

Choose a startup strategy.

However the application starts, the application begins a transaction and uses the

statement to dequeue a message. The application extracts the data from the messages and

does any necessary processing. If necessary, the application uses the

statement to send

messages to the other side of the conversation. The application then commits the transaction.

For efficiency, the application might process multiple messages within the same transaction.

Services that maintain state often use the

statement to lock a

conversation group, retrieve state for the conversation group, and then process multiple

messages for the conversation group.

The conversation continues, using

and

statements to transmit messages

between the endpoints. At any time, if necessary, either participant in the conversation can use

to start a conversation with another service to get additional information. For

example, an application that is processing an event notification might initiate another

conversation with a service that provides personnel information in order to retrieve current

contact information before sending out an alert.

```sql
BEGIN DIALOG
SEND
RECEIVE
SEND
GET CONVERSATION GROUP
SEND
RECEIVE
BEGIN DIALOG
```
