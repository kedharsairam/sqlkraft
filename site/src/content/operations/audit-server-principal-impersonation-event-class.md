---
title: "Audit Server Principal Impersonation Event Class"
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
  
  event class occurs when there is an impersonation
  
  within server scope, such as EXECUTE AS <
  
  logi
tags:
  - "event-classes"
  - "audit-server-principal-impersonation-event-class"
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

event class occurs when there is an impersonation

within server scope, such as EXECUTE AS <

login

>.

Description

Name of the client application that created the

connection to an instance of Microsoft SQL

Server. This column is populated with the values

passed by the application rather than the

displayed name of the program.

10

Yes

ID of the database specified by the USE

database

statement or the default database if

no USE

database

statement has been issued for

a given instance. SQL Server Profiler displays

the name of the database if the

data column is captured in the trace and the

server is available. Determine the value for a

database by using the DB_ID function.

3

Yes

Name of the database in which the user

statement is running.

35

Yes

SQL Server user name of the client.

40

Yes

Sequence of a given event within the request.

51

No

Type of event subclass.

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