---
name: 'sys.events'
title: 'sys.events'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Contains a row for each event for which a trigger or event notification fires. These events

represent the event types that are specified when the trigger or event notification is created by

using

CREATE TRIGGER

or

CREATE EVENT NOTIFICATION

.


## Description
ID of the trigger or event notification. This value, together with

, uniquely identifies the row.

Event that causes the trigger to fire.


## Description of the event that causes the trigger to fire.
1 = Trigger event.

0 = Notification event.

Event group on which the trigger or event notification is

created, or null if not created on an event group.


## Description of the event group on which the trigger or event
notification is created, or null if not created on an event group.

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Last updated on 11/18/2025

ﾉ

Expand table

See Also
