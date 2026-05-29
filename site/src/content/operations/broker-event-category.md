---
title: "Broker Event Category"
topic: "event-classes"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  The

  event category contains general Service Broker events.

  Description

  Broker:Activation Event Class

  An event generated
tags:
  - "event-classes"
  - "broker-event-category"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Managed Instance

The

event category contains general Service Broker events.

Description

Broker:Activation Event Class

An event generated when a queue monitor starts an activation stored

procedure.

Broker:Connection Event Class

An event generated to report the status of a transport connection

managed by Service Broker.

Broker:Conversation Event Class

An event generated to report the progress of a conversation.

Broker:Conversation Group

Event Class

An event generated when the database creates or drops a

conversation group.

Broker:Corrupted Message

Event Class

An event generated to report that the database has received a corrupt

message.

Broker:Forwarded Message

Dropped Event Class

An event generated when SQL Server drops a Service Broker message

that was to have been forwarded.

Broker:Forwarded Message Sent

Event Class

An event generated when SQL Server forwards a Service Broker

message.

Broker:Message Classify Event

Class

An event generated when Service Broker determines the routing for a

message.

Broker:Message Drop Event

Class

An event generated when Service Broker is unable to retain a received

message that should have been delivered to a service in this instance

Broker:Remote Message Ack

Event Class

An event generated when Service Broker sends or receives a message

acknowledgement.

Two security audit events are also provided for Service Broker. For more information on those

events, see

Audit Broker Login Event Class

and

Audit Broker Conversation Event Class

.

ﾉ

Expand table
