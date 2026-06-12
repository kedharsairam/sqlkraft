---
title: "Lesson 4: Beginning a Conversation and Transmitting Messages"
topic: "service-broker"
description: |
  09/04/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  In this lesson, you learn to start a conversation that spans two databases in the same instance

  of the Database Engine. You also learn
tags:
  - "service-broker"
  - "lesson-4-beginning-a-conversation-and-transmitting-messages"
pubDate: 2025-12-01
---

09/04/2025

SQL Server

Azure SQL Managed Instance

In this lesson, you learn to start a conversation that spans two databases in the same instance

of the Database Engine. You also learn how to complete a simple request-reply message cycle,

and then end the conversation.

Copy and paste the following code into a Query Editor window. Then, run it to switch

context to the

database where you initiate the conversation.

Copy and paste the following code into a Query Editor window. Then, run it to start a

conversation and send a request message to the

in

the. The code must be run in one block because a variable is used to pass a

dialog handle from

to the

statement. The batch runs the

statement to begin the conversation and build a request message. Then, it uses

the dialog handle in a

statement to send the request message on that conversation.

The last

statement displays the text of the message that was sent.

```sql
InitiatorDB
TargetDB
BEGIN DIALOG
SEND
BEGIN
DIALOG
SEND
SELECT
USE
InitiatorDB;
GO
DECLARE
@InitDlgHandle
AS
UNIQUEIDENTIFIER;
DECLARE
@RequestMsg
AS
NVARCHAR (100);
BEGIN
TRANSACTION
;
BEGIN
DIALOG @InitDlgHandle
```
