---
title: "Service Broker Application Outline"
topic: "service-broker"
description: |
  09/11/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Most Service Broker applications follow the same basic steps to receive and process messages:
  
  1. The application begins a transaction.
tags:
  - "service-broker"
  - "service-broker-application-outline"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Most Service Broker applications follow the same basic steps to receive and process messages:

1. The application begins a transaction.

2. If the application maintains state, the application gets a conversation group identifier. The

application uses this identifier to restore state from a state table. If there's no

conversation group with has messages that are ready to be received, the application rolls

back the transaction and exits.

3. The application receives one or more messages from the queue. If the application has a

conversation group identifier, the application uses the conversation group identifier to

receive messages for that conversation group. If no more messages are available to be

received, the application commits the transaction and returns to Step 1.

4. The application validates the content of the messages based on the message type name.

5. The application processes the messages based on the message type name and the

content of the message.

6. The application sends any messages that result from the processing.

7. If the application maintains state, the application updates the state table, using the

conversation group identifier as the primary key for the table.

8. The application returns to Step 3 to check whether more messages are available.

The precise structure of the application depends on the requirements of the application, the

communication style of the application, whether the application is a target service or an

initiating service, and whether Service Broker activates the application or not.

For example, an initiating application sends a message before it starts the processing loop

outlined in the preceding steps. The initiating service might send a message from another

program or stored procedure, then use an activation stored procedure for the initiating service

queue. For example, an order-entry application can include an external application that initiates

the conversation to enter the order. After the order is entered, the external application need

not remain running. An activation stored procedure for the initiating service sends the order

confirmation when a response returns from the order service. The activation stored procedure

also processes any Service Broker error messages that are returned by the target service and

sends notifications that the order couldn't be confirmed.