---
title: "Transactions Event Category"
topic: "event-classes"
description: "The event classes can be used to monitor the status of transactions."
tags: ["event-classes","transactions-event-category"]
pubDate: 2025-12-01
---

The

event classes can be used to monitor the status of transactions. The event

class names that are prefixed with

are used to track the transaction-related operations that

are sent through the transaction management interface.

Description

DTCTransaction Event

Class

Tracks transactions coordinated by the Microsoft Distributed Transaction

Coordinator (MS DTC). These are transactions distributed between two or more

databases or instances of the SQL Server Database Engine.

SQLTransaction Event

Class

Tracks Transact-SQL BEGIN TRAN, COMMIT TRAN, SAVE TRAN, and ROLLBACK

TRAN statements.

TM: Begin Tran

Completed Event Class

Indicates that a BEGIN TRANSACTION request has completed.

TM: Begin Tran Starting

Event Class

Indicates that a BEGIN TRANSACTION request is starting.

TM: Commit Tran

Completed Event Class

Indicates that a COMMIT TRANSACTION request has completed.

TM: Commit Tran

Starting Event Class

Indicates that a COMMIT TRANSACTION request is starting.

TM: Promote Tran

Completed Event Class

Indicates that a PROMOTE TRANSACTION request has completed.

TM: Promote Tran

Starting Event Class

Indicates that a PROMOTE TRANSACTION request is starting.

TM: Rollback Tran

Completed Event Class

Indicates that a ROLLBACK TRANSACTION request has completed.

TM: Rollback Tran

Starting Event Class

Indicates that a ROLLBACK TRANSACTION request is starting.

TM: Save Tran

Completed Event Class

Indicates that a SAVE TRANSACTION request has completed.

ﾉ

Expand table
