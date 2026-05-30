---
title: "SQL Server features"
topic: "monitor"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  WideWorldImporters use of SQL Server features and capabilities in the OLTP database.

  WideWorldImporters is designed to showcase ma
tags:
  - "monitor"
  - "sql-server-features"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

WideWorldImporters use of SQL Server features and capabilities in the OLTP database.

WideWorldImporters is designed to showcase many of the key features of SQL Server,

including the latest features introduced in SQL Server 2016. The following table lists the

features and capabilities of SQL Server. Each row also provides a description of how the

features are used in WideWorldImporters.

SQL Server

Temporal tables

There are many temporal tables, including all look-up style reference tables and main

entities such as StockItems, Customers, and Suppliers. Using temporal tables allows to

conveniently keep track of the history of these entities.

AJAX calls for

JSON

The application frequently uses AJAX calls to query these tables: Persons, Customers,

Suppliers, and StockItems. The calls return the data in JSON format. For example, see

the stored procedure

.

JSON

property/value

bags

A number of tables have columns that hold JSON data to extend the relational data in

the table. For example,

has a column for application

settings and

has a column to record user preferences. These

tables use an

column to record the JSON data, along with a CHECK

constraint using the built-in function

to ensure the column values are valid

JSON.

Row-level

security (RLS)

Row Level Security (RLS) is used to limit access to the Customers table, based on role

membership. Each sales territory has a role and a user. To see an RLS access limit in

action, use the corresponding script in sample-script.zip, which is part of the

release of

the sample

.

Real-time

Operational

Analytics

(Full version of the database) The core transactional tables

and

both have a nonclustered columnstore index to support efficient

execution of analytical queries in the transactional database with minimal impact on

the operational workload. Running transactions and analytics in the same database is

also referred to as

Hybrid Transactional/Analytical Processing (HTAP)

. To see this in

action, use the corresponding script in sample-script.zip, which is part of the

release of

the sample

.

ﾉ

Expand table

```cmd
Website.SearchForCustomers
Application.SystemParameters
Application.People nvarchar(max)
ISJSON
```
