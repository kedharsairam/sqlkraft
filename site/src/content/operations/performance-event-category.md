---
title: "Performance Event Category"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  Use the

  event category to monitor

  event classes and event classes that

  are produced from t
tags:
  - "event-classes"
  - "performance-event-category"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Use the

event category to monitor

event classes and event classes that

are produced from the execution of SQL data manipulation language (DML) operators.

Description

Auto Stats Event Class

Indicates that an automatic updating of index and column statistics has

occurred.

Degree of Parallelism (7.0

Insert) Event Class

Indicates that SQL Server has executed a SELECT, INSERT, UPDATE, or

DELETE statement using either a serial or parallel plan. The number of CPUs

used to perform the operation is also reported.

Performance Statistics

Event Class

Monitors performance of the queries that are being executed.

Showplan All Event Class

Identifies

operators within a SQL statement.

Showplan All for Query

Compile Event Class

Displays compile time data for

operators.

Showplan Statistics Profile

Event Class

Displays the estimated cost of a query.

Showplan XML Event Class

Identifies the

operators in a SQL statement. The event class

stores each event as a well defined XML document.

Showplan XML for Query

Compile Event Class

Displays compile time data for

operators in XML format.

Showplan XML Statistics

Profile Event Class

Identifies the

operators associated with a SQL statement. The

output is an XML document.

SQL:FullTextQuery Event

Class

Indicates that SQL Server has executed a full-text query.

Plan Guide Successful

Event Class

Indicates that SQL Server successfully produced an execution plan for a

query or batch that contained a plan guide.

Plan Guide Unsuccessful

Event Class

Indicates that SQL Server could not produce an execution plan for a query

or batch that contained a plan guide.

ﾉ

Expand table
