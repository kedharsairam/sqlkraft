---
title: "Lesson 2: Creating the Target Conversation Objects"
topic: "service-broker"
description: "09/04/2025 In this lesson, you learn to build all the objects that enable a database to be the target of a conversation from another database. C"
tags: ["service-broker","lesson-2-creating-the-target-conversation-objects"]
pubDate: "2025-12-01"
---

In this lesson, you learn to build all the objects that enable a database to be the target of a

conversation from another database.

Copy and paste the following code into a Query Editor window, then run it to switch

context to the

database.

Copy and paste the following code into a Query Editor window, then run it to create the

message types for the conversation. The message type names and properties that you

specify must be identical to the ones that you create in the

in the next

lesson.

```sql
TargetDB
InitiatorDB
USE
TargetDB;
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
