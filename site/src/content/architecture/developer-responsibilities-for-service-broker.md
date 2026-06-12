---
title: "Developer Responsibilities for Service Broker"
topic: "service-broker"
description: "08/29/2025 The application developer is responsible for designing the Service Broker application and creating elements that require programming."
tags: ["service-broker","developer-responsibilities-for-service-broker"]
pubDate: "2025-12-01"
---

The application developer is responsible for designing the Service Broker application and

creating elements that require programming. The system administrator is responsible for

configuring and managing Service Broker. Developers and administrators need to work

together when planning the system, to ensure that it's developed and managed optimally for

their particular environment and business purposes.

The tasks involved in creating an individual application depend on the needs of the application.

The following tasks are a common sequence for developing a Service Broker application:

1. Plan the application. Create an outline of the tasks that the application must accomplish.

Describe the conversations that take place during each task. Which endpoint needs to

provide what information, in what order? What processing must take place? What

priorities should be assigned to the conversations? All subsequent information depends

on this outline.

2. Determine the format and structure of each message in each conversation. Plan the

expected sequence of exchange for the messages, and how each participant in the

conversation should respond to errors and messages that are sent in an unexpected

order.

3. If the conversation uses XML messages, create a schema for each XML message. You use

schemas during development, testing, and troubleshooting. When your service is in

production, you might decide to remove schema validation from your message types, to

improve performance.

4. Create a message type for each message in each conversation.

5. Create a contract for each conversation. The contract identifies the message types that

each endpoint can use in the conversation.

6. Create a queue to store the messages that the application will receive.

7. Create a service to expose the functionality defined by the contract and implemented by

the stored procedure that you created. When creating a service, you associate it with the

queue you created in the previous step. This step tells Service Broker that all messages

that arrive addressed to that service are to be placed in the identified queue.
