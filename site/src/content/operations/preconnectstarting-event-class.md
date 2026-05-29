---
title: "PreConnect:Starting Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The PreConnect:Starting event class indicates when a LOGON trigger or the Resource Governor
  
  
tags:
  - "event-classes"
  - "preconnectstarting-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The PreConnect:Starting event class indicates when a LOGON trigger or the Resource Governor

classifier function starts execution.

Description

EventClass

215

27

No

SPID

The ID of server process that fires this event.

12

Yes

EventSubClass

1 for the user-defined classifier function.

21

Yes

StartTime

The time when the user-defined classifier

function starts.

14

Yes

ObjectID

The ID of the user-defined classifier object.

22

Yes

ObjectName

The two-part name of the classifier user-

defined function. For example, dbo.classifier.

34

Yes

Extended Events

PreConnect:Completed Event Class

Resource Governor

Last updated on 11/18/2025

ﾉ

Expand table