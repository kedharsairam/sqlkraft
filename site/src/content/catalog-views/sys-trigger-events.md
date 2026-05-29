---
name: 'sys.trigger_events'
title: 'sys.trigger_events'
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

Contains a row per event for which a trigger fires.


## Description
Not

applicable

Inherits the

,

,

columns from

sys.events

.

Trigger is marked to be the first to fire for this event.

Trigger is marked to be the last to fire for this event.

Event group on which the trigger is created, or null if

not created on an event group.


## Description of the event group on which the trigger is
created, or null if not created on an event group.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Catalog Views (Transact-SQL)

Object Catalog Views (Transact-SQL)

Last updated on 11/18/2025

７

Note

does not apply to event notifications.

ﾉ

Expand table

See Also
