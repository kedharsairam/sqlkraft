---
title: "Service Broker Communication Protocols"
topic: "service-broker"
description: |
  09/03/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Service Broker uses a broker-specific protocol to communicate with remote brokers. The broker
  
  manages connections separately from the 
tags:
  - "service-broker"
  - "service-broker-communication-protocols"
pubDate: 2025-12-01
---

09/03/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker uses a broker-specific protocol to communicate with remote brokers. The broker

manages connections separately from the normal pool of client connections. In order for two

SQL Server instances to exchange Service Broker messages, each instance must be able to send

TCP/IP traffic to the port that the other instance uses for Service Broker communications. By

convention, Service Broker often uses port 4022 for broker-to-broker communication.

However, the exact port is specified when the endpoint is created.

Service Broker takes a layered approach to communication. Each layer builds on the underlying

layer to help ensure reliable delivery. This approach allows an application to operate without

knowledge of the location of the remote service or the physical transport that the broker uses

to communicate. In most cases, these protocols are transparent to an application. However,

understanding the role each protocol layer plays might help in troubleshooting problems with

an application.

The highest-level protocol that the broker uses is the dialog protocol. The dialog protocol layer

handles reliable, sequenced message transmission. The dialog protocol layer generates

sequence numbers for messages, generates acknowledgment messages, delivers messages to

the proper queues, and fragments and reassembles messages. The dialog protocol handles

authentication and encryption for a dialog.

The dialog protocol uses the adjacent broker protocol to transmit message fragments. The

adjacent broker protocol handles the network transmissions exchanged between two broker

instances.

The adjacent broker protocol uses a transport protocol, such as TCP/IP, to move messages

from broker to broker.

The dialog protocol manages the exactly-once-in-order (EOIO) delivery pattern for messages

on a conversation. This protocol doesn't describe the format that Service Broker messages use

on the network. Instead, the protocol specifies the logical steps required for a reliable

conversation. The dialog protocol handles the tasks required for reliable delivery, including

generating and processing acknowledgment messages.