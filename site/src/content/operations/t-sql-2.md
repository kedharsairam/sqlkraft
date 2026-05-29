---
title: "T-SQL"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/27/2023
  
  Applies to:
  
  SQL Server
  
  For monitoring availability groups and replicas and the associated databases by using Transact-
  
  SQL, Always On availability groups provides a set of c
tags:
  - "high-availability"
  - "t-sql-2"
pubDate: 2025-12-01
---

Article

•

09/27/2023

Applies to:

SQL Server

For monitoring availability groups and replicas and the associated databases by using Transact-

SQL, Always On availability groups provides a set of catalog and dynamic management views

and server properties. Using Transact-SQL SELECT statements, you can use the views to

monitor availability groups and their replicas and databases. The information returned for a

given availability group depends on whether you are connected to the instance of SQL Server

that is hosting the primary replica or a secondary replica.

Always On availability groups catalog views require VIEW ANY DEFINITION permission on the

server instance. Always On availability groups dynamic management views require VIEW

SERVER STATE permission on the server.

To monitor the Always On availability groups feature on a server instance, use the following

built-in function:

SERVERPROPERTY

function

Returns server property information about whether Always On availability groups is enabled

and, if so, whether it has started on the server instance.

IsHadrEnabled, HadrManagerStatus



Tip

Many of these views can be joined using their ID columns to return information from

multiple views in a single query.