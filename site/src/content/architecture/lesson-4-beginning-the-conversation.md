---
title: "Lesson 4: Beginning the Conversation"
topic: "service-broker"
description: ""
tags: ["service-broker","lesson-4-beginning-the-conversation"]
pubDate: "2025-12-01"
---

In this lesson, you learn to start a conversation that spans two instances of the Database Engine

and send a request message from the initiator instance to the target instance. Run these steps

from a copy of Management Studio running on the same computer as the initiator instance.

Copy and paste the following code into a Query Editor window. Then, run it to switch

context to the

database where you initiate the conversation.

Copy and paste the following code into a Query Editor window, then run it to begin a

conversation and send a request message to the

in the. The code must be run in one block because a variable is used to pass a dialog

handle from

to the

statement.

The batch runs the

statement to begin the conversation, and then builds a

request message. Then, it uses the dialog handle in a

statement to send the request

message on that conversation. The last

statement just displays the text of the message

that was sent.

```sql
BEGIN DIALOG
SEND
BEGIN DIALOG
SEND
SELECT
USE
InstInitiatorDB;
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
FROM
SERVICE [//InstDB/2InstSample/InitiatorService]
```
