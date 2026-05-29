---
title: "Lesson 3: Creating the Initiator Conversation Objects"
topic: "service-broker"
description: |
  09/11/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  In this lesson, you learn to build all the objects that enable a database to initiate a conversation
  
  with another database.
  
  Copy and 
tags:
  - "service-broker"
  - "lesson-3-creating-the-initiator-conversation-objects"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

In this lesson, you learn to build all the objects that enable a database to initiate a conversation

with another database.

Copy and paste the following code into a Query Editor window, then run it to switch

context to the

database.

SQL

Copy and paste the following code into a Query Editor window, then run it to create the

message types for the conversation. The message type names and properties that are

specified here must be identical to the ones that were created in the

in the

previous lesson.

SQL

```sql
USE
InitiatorDB;
GO
CREATE
MESSAGE
TYPE
[//BothDB/2DBSample/RequestMessage]
VALIDATION
= WELL_FORMED_XML;
CREATE
MESSAGE
TYPE
[//BothDB/2DBSample/ReplyMessage]
VALIDATION
= WELL_FORMED_XML;
GO
```