---
title: "Lesson 6: Receiving the Reply and Ending the Conversation"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  In this lesson, you learn to receive the reply message from the target service and end the

  conversation. Open SQL Server Management St
tags:
  - "service-broker"
  - "lesson-6-receiving-the-reply-and-ending-the-conversation"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

In this lesson, you learn to receive the reply message from the target service and end the

conversation. Open SQL Server Management Studio (SSMS) and connect to the SQL Server

which has the Service Broker initiator, then run these steps from the query window in SSMS.

Copy and paste the following code into a Query Editor window, then run it to switch

context back to the

database where you receive the reply message and

end the conversation.

SQL

Copy and paste the following code into a Query Editor window, then run it to receive the

reply message and end the conversation. The

statement retrieves the reply

message from the

. The

statement ends the initiator

side of the conversation. The last

statement displays the text of the reply message

so you can confirm it's the same as what was sent in the last step.

SQL

```sql
RECEIVE
END CONVERSATION
SELECT
USE
InstInitiatorDB;
GO
DECLARE
@RecvReplyMsg
AS
NVARCHAR
(100);
DECLARE
@RecvReplyDlgHandle
AS
UNIQUEIDENTIFIER;
BEGIN
TRANSACTION
;
WAITFOR (RECEIVE TOP (1) @RecvReplyDlgHandle = conversation_handle,
@RecvReplyMsg = message_body FROM InstInitiatorQueue),
TIMEOUT 1000;
```
