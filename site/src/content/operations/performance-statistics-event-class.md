---
title: "Performance Statistics Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The Performance Statistics event class can be used to monitor the performance of queries,
  
  st
tags:
  - "event-classes"
  - "performance-statistics-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The Performance Statistics event class can be used to monitor the performance of queries,

stored procedures, and triggers that are executing. Each of the six event subclasses indicates an

event in the lifetime of queries, stored procedures, and triggers within the system. Using the

combination of these event subclasses and the associated sys.dm_exec_query_stats,

sys.dm_exec_procedure_stats and sys.dm_exec_trigger_stats dynamic management views, you

can reconstitute the performance history of any given query, stored procedure, or trigger.

The following tables describe the event class data columns associated with each of the

following event subclasses: EventSubClass 0, EventSubClass 1,EventSubClass 2,EventSubClass 3,

EventSubClass 4, and EventSubClass 5.

Description

BigintData1

NULL

52

Yes

BinaryData

NULL

2

Yes

DatabaseID

ID of the database specified by the USE

database

statement or the default database if no

USE

database

statement has been issued for a

given instance. SQL Server Profiler displays the

name of the database if the ServerName data

column is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

EventSequence

Sequence of a given event within the request.

51

No

EventSubClass

Type of event subclass.

0 = New batch SQL text that is not currently

present in the cache.

21

Yes

ﾉ

Expand table