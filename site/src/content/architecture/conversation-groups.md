---
title: "Conversation Groups"
topic: "service-broker"
description: "08/29/2025 A conversation group identifies a group of related conversations."
tags: ["service-broker","conversation-groups"]
pubDate: "2025-12-01"
---

A conversation group identifies a group of related conversations. A conversation group allows

an application to easily coordinate conversations involved in a specific business task.

Every conversation belongs to one conversation group. Every conversation group is associated

with a specific service, and all conversations in the group are conversations to or from that

service. A conversation group can contain any number of conversations.

uses conversation groups to provide exactly-once-in-order (EOIO) access to

messages that are related to a specific business task. When an application sends or receives a

message, SQL Server locks the conversation group to which the message belongs. Thus, only

one session at a time can receive messages for the conversation group. The conversation

group lock guarantees that an application can process messages on each conversation exactly

once in order (EOIO). Because a conversation group can contain more than one conversation,

an application can use conversation groups to identify messages related to the same business

task, and process those messages together.

A conversation group isn't shared between participants in a conversation. Therefore, each

participant in a conversation is free to group that conversation as appropriate. An application

can manage complex interactions among services without requiring any special support from

the services.

A human resources application might have a

service that combines

information from a payroll service and information from a benefits service. The

service begins a conversation with each service, and relates one

conversation to the other in the same conversation group. Service Broker adds the

conversation group identifier to each incoming message on these two conversations,

regardless of whether the message arrives from the payroll service or the benefits service.

Because the conversations are in the same conversation group, Service Broker provides all the

information necessary for the

service to match the benefits

information to the payroll information, regardless of how many requests are in progress in the

service.

The messages to the payroll service and the messages to the benefits service don't contain

conversation group information for the conversation group created by

```sql
GetEmployeeInformation
GetEmployeeInformation
GetEmployeeInformation
GetEmployeeInformation
```
