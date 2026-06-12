---
title: "Lesson 2: Beginning a Conversation and Transmitting Messages"
topic: "service-broker"
description: "09/04/2025 In this lesson, you learn to start a conversation, complete a simple request-reply message cycle, and then end the conversation. Copy"
tags: ["service-broker","lesson-2-beginning-a-conversation-and-transmitting-messages"]
pubDate: 2025-12-01
---

In this lesson, you learn to start a conversation, complete a simple request-reply message cycle,

and then end the conversation.

Copy and paste the following code into a Query Editor window, then run it to switch

context to the AdventureWorks2008R2 database.

Copy and paste the following code into a Query Editor window, then run it to start a

conversation and send a request message to the. You

must run the code in one block because a variable is used to pass a dialog handle from

to the

statement. The batch runs the

statement to start

the conversation. It builds a request message, and then uses the dialog handle in a

statement to send the request message on that conversation. The last

statement

displays the text of the message that was sent.

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
BEGIN DIALOG
SEND
BEGIN DIALOG
SEND
SELECT
AdventureWorks2022
USE
AdventureWorks2008R2;
GO
```
