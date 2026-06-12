---
title: "Lesson 3: Beginning a Conversation and Transmitting Messages"
topic: "service-broker"
description: ""
tags: ["service-broker","lesson-3-beginning-a-conversation-and-transmitting-messages"]
pubDate: 2025-12-01
---

In this lesson, you learn to complete a basic request-reply message cycle in a system

configured with an internal activation stored procedure.

Copy and paste the following code into a Query Editor window, then run it to switch context to

the

database.

Copy and paste the following code into a Query Editor window, then run it to start a

conversation and send a request message to the. The code

must be run in one block, because a variable is used to pass a dialog handle from

to the

statement. The batch runs the

statement to start the

conversation. It builds a request message, then uses the dialog handle in a

statement to

send the request message on that conversation. The last

statement displays the text of

the message that was sent.

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
AdventureWorks2022
BEGIN
DIALOG
SEND
BEGIN DIALOG
SEND
SELECT
AdventureWorks2022
USE
AdventureWorks2022;
GO
```
