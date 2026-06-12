---
title: "Optimized locking and deadlocks"
topic: "locking"
description: ""
tags: ["locking","architecture"]
pubDate: "2026-05-29"
---

## Session A

## Session B

## Session A

## Session B

## Session A

## Session B

## Session A

## Session B

## Session A

The second update statement in

is blocked by

on the.

and

are now mutually blocking one another. Neither transaction can

proceed, as they each need a resource that is locked by the other.

After a few seconds, the deadlock monitor identifies that the transactions in

and

are mutually blocking one another, and that neither can make progress. You see a

deadlock occur, with

chosen as the deadlock victim.

completes

successfully. An error message appears in the query window of

with text similar to

the following example:

Output

If a deadlock isn't raised, verify that

is enabled in your sample

database. Deadlocks can occur in any database configuration, but this example requires that

is enabled.

You can view the details of the deadlock in the

target of the

event

session, which is enabled and active by default in SQL Server and Azure SQL Managed Instance.

Consider the following query:

You can view the XML in the

column inside SSMS, by selecting the cell that

appears as a hyperlink. Save this output as a

file, close, then reopen the

file in SSMS

for visual deadlock graph. The deadlock graph should look something like the following image.

With

optimized locking

, page and row locks aren't held until the end of transaction. They are

released as soon as a row is updated. Additionally, if

is enabled,

update (

) locks aren't used. As a result, the likelihood of deadlocks is reduced.

The previous example doesn't cause a deadlock when optimized locking is enabled because it

relies on the update (

) locks.

The following example can be used to cause a deadlock on a database that has optimized

locking enabled.

First, create an example table and add data.



The following T-SQL batches, executed in sequence in two separate sessions, create a

deadlock.

In session 1:

In session 2:

In session 1:

In session 2:

In this case, each session holds an exclusive (

) lock on its own transaction ID (TID) resource,

and is waiting on the shared (

) lock on the other TID, resulting in a deadlock.

The following abbreviated deadlock report contains elements and attributes specific to

optimized locking. Under each resource in the deadlock report

, each

element reports the underlying resources and TID lock information of each

member of a deadlock.

XML

Extended Events overview

sys.dm_tran_locks (Transact-SQL)

Deadlock Graph Event Class

Deadlocks with Read Repeatable Isolation Level

Lock:Deadlock Chain Event Class

Lock:Deadlock Event Class

SET DEADLOCK_PRIORITY (Transact-SQL)

Analyze and prevent deadlocks in Azure SQL Database and SQL database in Fabric

Open, view, and print a deadlock file in SQL Server Management Studio (SSMS)
