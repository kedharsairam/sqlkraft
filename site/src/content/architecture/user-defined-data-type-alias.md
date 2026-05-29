---
title: "User defined data type alias"
topic: "collation"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  This topic describes how to create a new user-defined data type alias in SQL Server by using
  
tags:
  - "collation"
  - "user-defined-data-type-alias"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This topic describes how to create a new user-defined data type alias in SQL Server by using

SQL Server Management Studio or Transact-SQL.

Limitations and Restrictions

Security

SQL Server Management Studio

Transact-SQL

The name of a user-defined data type alias must comply with the rules for identifiers.

Requires CREATE TYPE permission in the current database and ALTER permission on

schema_name

. If

schema_name

is not specified, the default name resolution rules for

determining the schema for the current user apply.

1. In Object Explorer, expand

, expand a database, expand

,

expand

, right-click

, and then click