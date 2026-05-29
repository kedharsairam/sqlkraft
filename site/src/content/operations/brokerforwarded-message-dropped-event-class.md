---
title: "Broker:Forwarded Message Dropped Event Class"
topic: "event-classes"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  SQL Server generates a Broker:Forwarded Message Dropped event when Service Broker drops
  
  a message that was intended to be 
tags:
  - "event-classes"
  - "brokerforwarded-message-dropped-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server generates a Broker:Forwarded Message Dropped event when Service Broker drops

a message that was intended to be forwarded.

Description

ApplicationName

The name of the client application that

created the connection to an instance of

SQL Server. This column is populated with

the values passed by the application

rather than the displayed name of the

program.

10

Yes

BigintData1

Message sequence number.

52

No

ClientProcessID

The ID assigned by the host computer to

the process where the client application is

running. This data column is populated if

the client process ID is provided by the

client.

9

Yes

DatabaseID

The ID of the database specified by the

USE

database

statement, or the ID of the

default database if no USE

database

statement has been issued for a

given instance. SQL Server Profiler

displays the name of the database if the

Server Name data column is captured in

the trace and the server is available.

Determine the value for a database by

using the DB_ID function.

3

Yes

DatabaseName

The name of the database in which the

user statement is running.

35

Yes

ﾉ

Expand table