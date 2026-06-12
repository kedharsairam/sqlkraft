---
title: "How to: Work with CLR Database Objects"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
    In addition to the Transact-SQL programming language, you can use .NET Framework
  
    languages to create database objects that retrieve and update data. Database objects that are
  
    written in
tags: ["ssb-diagnose","how-to-work-with-clr-database-objects"]
pubDate: "2025-12-01"
---

In addition to the Transact-SQL programming language, you can use.NET Framework

languages to create database objects that retrieve and update data. Database objects that are

written in managed code are called SQL Server Common Language Run (CLR) database objects.

For an explanation of the advantages of using CLR database objects hosted in SQL Server, and

how to choose between Transact-SQL and CLR, see

CLR integration overview

and

Advantages

of Using Managed Code to Create Database Objects.

To create a CLR database object using SQL Server Data Tools, you create a database project

and then add a CLR database object to it. Unlike in previous versions of Visual Studio, you

don't need to create a separate CLR project and then add a reference to it from the database

project. When you build and publish the database project, you automatically publish the CLR

objects in the project at the same time. After you publish these CLR objects, they can be called

and executed like any other database objects.

The CLR and CLR Build property pages contain many settings for using CLR database objects in

your project. Specifically, the CLR property page has a permission level setting to set

permissions on the CLR assembly. It also has the "Generate DDL" setting to control whether

DDL for the CLR database objects added to the project is generated. The CLR Build property

page contains all the compiler options that you can set to configure the compilation of CLR

code in the project. These property pages can be accessed by right-clicking your project in

and select.

To enable debugging of CLR database objects, open

Object Explorer. Right-click

the server containing the CLR database artifacts you want to debug, and choose

SQL/CLR Debugging. A message box appears with the warning:

Output

When you're debugging CLR database objects, breaking execution breaks all threads on the

server, affecting other users. For this reason, you shouldn't debug applications for CLR

database objects on a production server. You should also note that once you have started

debugging, it's too late to change settings in

Object Explorer. Changes made in

Object Explorer

don't take effect until the start of the next debugging session.

For more information on the requirements of building CLR database objects, see

Build

database objects with common language runtime (CLR) integration.

```cmd
During debugging, all managed threads on this server stop. Do you wish to enable
SQL CLR debugging on this server?
```
