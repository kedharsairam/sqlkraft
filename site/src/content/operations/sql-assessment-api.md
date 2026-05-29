---
title: "SQL Assessment API"
topic: "linux-operations"
description: |
  SQL Assessment API
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  The SQL Assessment API provides a mechanism to evaluate the configuration of your SQL
  
  Server for best practices. The API is de
tags:
  - "linux-operations"
  - "sql-assessment-api"
pubDate: 2025-12-01
---

SQL Assessment API

Applies to:

SQL Server

Azure SQL Managed Instance

The SQL Assessment API provides a mechanism to evaluate the configuration of your SQL

Server for best practices. The API is delivered with a ruleset containing best practice rules

suggested by the SQL Server team. This ruleset is enhanced with the release of new versions,

but at the same time, the API is built to give a highly customizable and extensible solution.

Users can tune the default rules and create their own.

The SQL Assessment API is useful when you want to make sure your SQL Server configuration

is in line with recommended best practices. After an initial assessment, configuration stability

can be tracked by regularly scheduled assessments.

The API can be used to assess:

SQL Server on Azure Virtual Machines

Azure SQL Managed Instance

SQL Server 2012 and higher

SQL Server on

Linux-based systems and containers

Rules (sometimes referred to as checks) are defined in JSON formatted files. The ruleset format

requires a ruleset name and version to be specified. When you use custom rulesets, you can

easily know which recommendations from what ruleset come.

The Microsoft's shipped ruleset is available on GitHub. You can view the

entire ruleset

in the

samples repository

.

７

Note

The SQL Assessment API provides assessment on a variety of areas, but it doesn't go

deeply into security. Use the

to proactively

improve your database security.

SQL Assessment cmdlets and associated extensions