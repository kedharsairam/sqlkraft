---
title: "Start from an existing database"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL

  database in Microsoft Fabric

  SQL projects contain declarative (

  statement) files for all the objects in a database, such
tags:
  - "ssms"
  - "start-from-an-existing-database"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

database in Microsoft Fabric

SQL projects contain declarative (

statement) files for all the objects in a database, such as

tables, views, and stored procedures. You can use these files to create new databases, update

existing databases, or track the database in source control. Often, you start with a SQL project

when you have an existing database and want to create objects in the SQL project that match the

database with minimal effort.

Some SQL project tools include a single step for creating a new SQL project from an existing

database. Other tools require a few steps to create a new SQL project and then import objects

from an existing database. Except for the Visual Studio (SQL Server Data Tools) instructions, this

guide focuses on SDK-style SQL projects.

With

option 1

in this tutorial, you:

Create a new SQL project from an existing database

Build the SQL project

With

option 2

in this tutorial, you:

Create a new empty SQL project

Import objects from an existing database

Build the SQL project.NET 8 SDK

Visual Studio 2022 Community, Professional, or Enterprise

Install SQL Server Data Tools (SSDT) for Visual Studio

７

Note

To complete the tutorial, you need access to an Azure SQL or SQL Server instance. You can

develop locally for free with

developer edition

on Windows or in.

```cmd
CREATE
```
