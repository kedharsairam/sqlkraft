---
title: "Lock:Timeout (timeout > 0) Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  Azure SQL Database
  
  Azure
  
  SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The
  
  event class indicates that a request for a lock on a res
tags:
  - "event-classes"
  - "locktimeout-timeout-0-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

The

event class indicates that a request for a lock on a resource,

such as a page, has timed out because another transaction is holding a blocking lock on the

required resource. This event class behaves the same as the

event class, except it

does not include any events where the timeout value is 0.

Include the

event class in traces where you are using lock probes

or other processes that have timeout values of zero. This allows you to see where actual time-

outs are occurring without seeing time-out values of zero.

Description

ApplicationName

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

BinaryData

Lock resource identifier.

2

Yes

ClientProcessID

ID assigned by the host computer to the process

where the client application is running. This data

column is populated if the client provides the

client process ID.

9

Yes

DatabaseID

ID of the database in which the timeout

occurred. SQL Server Profiler displays the name

of the database if the

data column

is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

DatabaseName

Name of the database in which the time-out

occurred.

35

Yes

ﾉ

Expand table