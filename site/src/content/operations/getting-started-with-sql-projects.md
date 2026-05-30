---
title: "Getting started with SQL projects"
topic: "ssms"
description: |
  Applies to:

  SQL Server 2022 (16.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  A SQL database project is a local representation of SQL objec
tags:
  - "ssms"
  - "getting-started-with-sql-projects"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2022 (16.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

A SQL database project is a local representation of SQL objects that comprise the schema for a

single database, such as tables, stored procedures, or functions. The development cycle of a

SQL database project enables database development to be integrated into a continuous

integration and continuous deployment (CI/CD) workflows familiar as a development best

practice.

This article steps through creating a new SQL project, adding objects to the project, and

building and deploying the project. Except for the Visual Studio (SQL Server Data Tools)

instructions, the guide focuses on SDK-style SQL projects.

1.

Create a new project

2.

Add objects to the project

3.

Build the project

4.

Deploy the project

.NET SDK

Visual Studio 2022 Community, Professional, or Enterprise

Install SQL Server Data Tools (SSDT) for Visual Studio

We start our project by creating a new SQL database project before manually adding objects to

it. There are other ways to create a project that enable immediately populating the project with

objects from an existing database, such as using the

schema comparison tools

.

Select

,

, then

.

７

Note

To complete the deployment of a SQL database project, you need access to an Azure SQL

or SQL Server instance. You can develop locally for free with

SQL Server developer

on Windows or in

.
