---
title: "Audit Server Starts & Stops Event Class"
topic: "event-classes"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  The

  event class occurs when the Microsoft SQL Server service

  state is modified.

  Description

  Name of
tags:
  - "event-classes"
  - "audit-server-starts-stops-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The

event class occurs when the Microsoft SQL Server service

state is modified.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

Type of event = 18.

27

No

Sequence of a given event within the request.

51

No

Type of event subclass.

1=Shutdown

2=Started

3=Paused

4=Continue

21

Yes

Name of the computer on which the client is

running. This data column is populated if the

client provides the host name. To determine the

host name, use the HOST_NAME function.

8

Yes

ﾉ

Expand table
