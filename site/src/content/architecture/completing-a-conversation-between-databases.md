---
title: "Completing a Conversation Between Databases"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This tutorial is intended for users who are new to Service Broker, but are familiar with database

  concepts and Transact-SQL statements
tags:
  - "service-broker"
  - "completing-a-conversation-between-databases"
pubDate: 2025-12-01
---

09/11/2025

SQL Server

Azure SQL Managed Instance

This tutorial is intended for users who are new to Service Broker, but are familiar with database

concepts and Transact-SQL statements. It will help new users get started by showing them how

to build and run a basic conversation between two databases on the same instance of the

Database Engine.

This tutorial builds on the tasks that you learned in the tutorial

Complete a conversation in a

single database. In this tutorial, you learn how to configure the conversation so that it runs

between two databases on the same instance of the Database Engine.

The steps that you follow in Lesson 2 are the same as those you followed in Lesson 1, with

these exceptions:

Create two databases:

and. You need to create all the initiator

service and queue in the

and the target service and queue in the.

Create two copies of the message types and contracts, one in the

and the

other in. Both sides of the conversation must have access to message type and

contract definitions that are identical.

Set the

database property to

in the. This is the simplest

mechanism for enabling conversations between two databases when they are on the

same instance of the Database Engine.

Learn which statements must be run in each database to complete a conversation, and

the sequence in which they must be run.

Messages aren't transmitted across a network for conversations that have both ends in the

same instance of the Database Engine. Database Engine security and permissions restricts

access to authorized principles. Network encryption isn't needed for this scenario.

This tutorial is divided into four lessons:

ﾉ

Expand table

```sql
InitiatorDB
TargetDB
InitiatorDB
TargetDB
InitiatorDB
TargetDB
TRUSTWORTHY
ON
InitiatorDB
```
